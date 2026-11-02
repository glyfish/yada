"""
Derive browsable subcategories under each FRED category, and name them.

FRED's taxonomy bottoms out above browsable size -- every category holding 500+ series
has zero children, and the largest holds 53,187 -- so the nodes between a category and
its series do not exist upstream and have to be built. See `0008_fred_subcategories.py`.

The pipeline, per category:

1. **Embed** each distinct member title once (cached across categories; 69.1% of titles
   are distinct, and a series in several categories would otherwise be embedded twice).
2. **Split recursively** until every leaf holds at most `LEAF_CAP` series. Not one k-means
   at `k = n/LEAF_CAP`: measured, that leaves 37% of leaves over the cap holding 56% of
   the titles. A mean of 25 is not a maximum of 25.
3. **Name** each node from its members with an LLM, producing a short name and a set of
   search `concepts` that deliberately includes synonyms absent from the titles.

Step 3 is why this works at all. The names and concepts become a ~31,000-row full-text
index that answers conceptual queries the 424,634 titles cannot: measured on a sample,
"steel making capacity", "heavy industry plant buildout" and "coal and coke production"
all reached **first place** for a topic whose titles contain none of those words, while
lexical search over the titles returned zero rows for all three.

Because the names are model output rather than source data, `PROMPT_VERSION` is stored on
every row. A changed prompt gives different names for identical input, and a half-rebuilt
tree must not be mistakable for a consistent one.

Clustering happens **within** a category, never globally. It is cheaper, the naming is
sharper because the input is already homogeneous, and it keeps FRED's own curation as the
spine rather than replacing it with 27,000 derived nodes and no human structure above
them.
"""

from __future__ import annotations

import json
import math
import os
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, Sequence

from sqlalchemy import MetaData, Table, text
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.engine import Engine

from apps.agentic.db.fred_catalogue import _engine
from lib.logger import get_logger

logger = get_logger("YADA")

#: The requirement: a leaf holds at most this many series, so it can be read by eye.
#: A ceiling, asserted by `leaf_cap_violations`, not a target.
LEAF_CAP = 25

#: Branching ceiling for interior nodes. The same argument applies upward: a node with
#: 243 children is no more evaluable than a leaf with 1,000 series.
BRANCH_CAP = 25

EMBED_MODEL = "text-embedding-3-small"
#: 256 of 1,536 dimensions. Measured sufficient for this task and 6x smaller; 293,210
#: titles at 1,536 dims would be 1.7 GB of centroids and member vectors.
EMBED_DIMS = 256
EMBED_BATCH = 1000

NAMING_MODEL = "claude-haiku-5-5"
#: Members shown to the namer. Enough to characterise a cluster, few enough to keep the
#: call cheap: measured at $0.000156 per name with 18.
NAMING_SAMPLE = 18
#: Generous on purpose. `claude-haiku-5-5` uses adaptive thinking, and it judges well --
#: a six-title leaf came back with no thinking block at all and 80 output tokens, while
#: an interior node summarising 18 child names spent 355. At 400 the latter truncated
#: mid-JSON with `stop_reason='max_tokens'`, which parsed as a failure for 6 of 75 names
#: including a category's root node. Thinking is not the cost here: measured at $0.000088
#: per leaf name either way, so it is left enabled.
NAMING_MAX_TOKENS = 1500

#: Per 1M tokens for NAMING_MODEL, for the cost recorded per category.
NAMING_INPUT_RATE = 0.10
NAMING_OUTPUT_RATE = 0.50

# ---------------------------------------------------------------------------
# The classification prompt.
#
# Versioned and stored on every row it produces. Bump PROMPT_VERSION on ANY edit below,
# including whitespace: the version is the only way to tell a tree built under one prompt
# from a tree built under another, and names are not reproducible across prompts.
#
# Design notes, so the next edit is deliberate:
#
# * **JSON only, no prose.** The reply is parsed, and a model that explains itself first
#   costs output tokens on every one of ~31,000 calls.
# * **`concepts` must include words NOT in the titles.** This is the whole point of the
#   field and it is stated twice, because a model given a list of titles will otherwise
#   echo their vocabulary back and the bridge does not get built. Without it the layer is
#   a prettier index over the same words.
# * **The name is a noun phrase, not a sentence.** It is rendered in a tree, beside
#   siblings, and has to read as a label.
# * **Interior nodes are named from their children's names**, never from series titles.
#   A node two levels up whose name was generated from 18 sampled series describes a
#   sample, not the subtree -- and reads authoritative either way.
# * **No invented specifics.** The namer sees a sample; a geography or date range it adds
#   from that sample will be wrong for the rest. This is the one instruction that guards
#   against a plausible, confident, false label, which is the failure mode this whole
#   migration keeps meeting.
# ---------------------------------------------------------------------------

PROMPT_VERSION = "2026-11-01.1"

LEAF_SYSTEM_PROMPT = """\
You name groups of statistical data series in a catalogue, for a browsable tree.

Reply with JSON only, no other text:
{"name": "<4-8 word noun phrase>", "concepts": "<6-12 comma-separated search terms>"}

Rules:
- "name" is a label shown in a tree beside sibling labels. A noun phrase, not a sentence,
  and no trailing punctuation.
- "concepts" are terms a researcher might search for. At least half MUST be words that do
  NOT appear in the titles shown: synonyms, the field of study, the economic concept, the
  industry, common abbreviations. Terms already present in the titles add nothing.
- Describe only what every title shown has in common. Do NOT add a country, region, date
  range or units unless it is in all of them -- you are shown a sample, and a specific
  that fits the sample will be wrong for the rest of the group.
- If the titles have little in common, say so plainly in the name (for example
  "Assorted regional labour indicators") rather than inventing a theme.\
"""

INTERIOR_SYSTEM_PROMPT = """\
You name a parent group in a statistical data catalogue, given the names of its children.

Reply with JSON only, no other text:
{"name": "<4-8 word noun phrase>", "concepts": "<6-12 comma-separated search terms>"}

Rules:
- "name" must cover ALL the child groups listed, at one level of generality above them.
  A noun phrase, not a sentence, and no trailing punctuation.
- "concepts" are search terms for the whole group. At least half MUST be words that do NOT
  appear in the child names: broader field terms, synonyms, common abbreviations.
- Do NOT name the group after one child, and do NOT add a country, region or date range
  unless every child carries it.\
"""


def leaf_user_prompt(titles: Sequence[str]) -> str:
    return "Series titles in this group:\n" + "\n".join(f"- {t}" for t in titles)


def interior_user_prompt(child_names: Sequence[str]) -> str:
    return "Child group names:\n" + "\n".join(f"- {n}" for n in child_names)


# --------------------------------------------------------------------------- helpers


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _table(engine: Engine, name: str) -> Table:
    return Table(name, MetaData(), autoload_with=engine)


def split_sizes(n: int, cap: int = LEAF_CAP, branch: int = BRANCH_CAP) -> int:
    """How many derived levels `n` series need to reach leaves of at most `cap`."""
    depth = 0
    while n > cap:
        n = math.ceil(n / branch)
        depth += 1
    return depth


def parse_naming_reply(raw: str) -> dict[str, str]:
    """
    Pull `{name, concepts}` out of a model reply.

    Tolerant by design: a naming failure must degrade to a usable label, never abort a
    build of ~31,000 nodes. An unparsed reply is recorded as such so it can be found and
    rebuilt, rather than silently becoming a plausible-looking name.
    """
    text_body = (raw or "").strip()
    if text_body.startswith("```"):
        text_body = text_body.strip("`")
        if text_body.lower().startswith("json"):
            text_body = text_body[4:]
    text_body = text_body.strip()
    try:
        parsed = json.loads(text_body)
        name = str(parsed.get("name") or "").strip()
        concepts = str(parsed.get("concepts") or "").strip()
        if name:
            return {"name": name[:200], "concepts": concepts[:1000]}
    except (json.JSONDecodeError, AttributeError, TypeError):
        pass
    return {"name": "UNNAMED (naming failed)", "concepts": ""}


def extract_text(message: Any) -> str:
    """
    First text block of an Anthropic reply.

    `content[0]` is wrong: haiku-5-5 uses adaptive thinking, so block zero is a
    ThinkingBlock with no `.text` and indexing it raises. Cost this a run already.
    """
    for block in getattr(message, "content", []) or []:
        if getattr(block, "type", None) == "text":
            return block.text
    return ""


# --------------------------------------------------------------------------- embedding


class TitleEmbedder:
    """Embeds distinct titles once and remembers them for the rest of the build."""

    def __init__(self, client: Any = None, model: str = EMBED_MODEL,
                 dims: int = EMBED_DIMS):
        self._client = client
        self._model = model
        self._dims = dims
        self._cache: dict[str, list[float]] = {}
        self.embedded = 0

    def _ensure_client(self) -> Any:
        if self._client is None:
            from openai import OpenAI

            self._client = OpenAI()
        return self._client

    def embed(self, titles: Iterable[str]) -> dict[str, list[float]]:
        wanted = [t for t in dict.fromkeys(titles) if t not in self._cache]
        for start in range(0, len(wanted), EMBED_BATCH):
            batch = wanted[start:start + EMBED_BATCH]
            response = self._ensure_client().embeddings.create(
                model=self._model, input=batch, dimensions=self._dims
            )
            for title, item in zip(batch, response.data):
                self._cache[title] = item.embedding
            self.embedded += len(batch)
        return self._cache


# --------------------------------------------------------------------------- naming


class Namer:
    """Names nodes, counting tokens so the build can report what it spent."""

    def __init__(self, client: Any = None, model: str = NAMING_MODEL):
        self._client = client
        self._model = model
        self.calls = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.failures = 0
        #: Replies discarded for hitting the token ceiling. Counted separately from
        #: `failures` because a rising count means the budget is wrong, not the model.
        self.truncated = 0

    def _ensure_client(self) -> Any:
        if self._client is None:
            from anthropic import Anthropic

            self._client = Anthropic()
        return self._client

    @property
    def cost_usd(self) -> float:
        return (
            self.input_tokens / 1e6 * NAMING_INPUT_RATE
            + self.output_tokens / 1e6 * NAMING_OUTPUT_RATE
        )

    def _call(self, system: str, user: str) -> dict[str, str]:
        """
        One naming call, retried once on a truncated reply.

        `stop_reason == 'max_tokens'` is checked *before* parsing, and the reply is
        discarded rather than parsed. A JSON object cut off mid-string can still yield a
        name that reads perfectly while its concepts are silently half-missing -- a
        plausible wrong answer, which is worse than a visible failure.
        """
        budget = NAMING_MAX_TOKENS
        for attempt in range(2):
            message = self._ensure_client().messages.create(
                model=self._model,
                max_tokens=budget,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            self.calls += 1
            usage = getattr(message, "usage", None)
            if usage is not None:
                self.input_tokens += getattr(usage, "input_tokens", 0) or 0
                self.output_tokens += getattr(usage, "output_tokens", 0) or 0
            if getattr(message, "stop_reason", None) == "max_tokens":
                self.truncated += 1
                budget *= 2
                continue
            named = parse_naming_reply(extract_text(message))
            if named["name"].startswith("UNNAMED"):
                self.failures += 1
            return named
        self.failures += 1
        return {"name": "UNNAMED (reply truncated)", "concepts": ""}

    def name_leaf(self, titles: Sequence[str]) -> dict[str, str]:
        return self._call(LEAF_SYSTEM_PROMPT, leaf_user_prompt(titles[:NAMING_SAMPLE]))

    def name_interior(self, child_names: Sequence[str]) -> dict[str, str]:
        return self._call(
            INTERIOR_SYSTEM_PROMPT, interior_user_prompt(child_names[:NAMING_SAMPLE])
        )


# --------------------------------------------------------------------------- clustering


def recursive_split(
    indices: Sequence[int],
    vectors: Any,
    cap: int = LEAF_CAP,
    branch: int = BRANCH_CAP,
    depth: int = 1,
    cluster: Callable | None = None,
) -> dict:
    """
    Split until every leaf holds at most `cap` members. Returns a nested node dict.

    `{"members": [...], "children": [...], "depth": n}` -- a node with children is
    interior and its `members` is the union of theirs.

    The forced-halving branch matters: k-means can return every point in one cluster,
    and without it the recursion never terminates. Falling back to an arbitrary split is
    worse structure but a finite build, and the alternative is a hang that looks like
    slow progress.
    """
    import numpy as np

    indices = list(indices)
    if len(indices) <= cap:
        return {"members": indices, "children": [], "depth": depth}

    k = min(max(2, math.ceil(len(indices) / cap)), len(indices), branch ** 2)
    if cluster is None:
        from sklearn.cluster import KMeans

        labels = KMeans(n_clusters=k, n_init=3, random_state=0).fit_predict(
            vectors[indices]
        )
    else:
        labels = cluster(vectors[indices], k)

    groups: dict[int, list[int]] = defaultdict(list)
    for position, label in enumerate(labels):
        groups[int(label)].append(indices[position])

    usable = [g for g in groups.values() if g]
    if len(usable) < 2 or max(len(g) for g in usable) == len(indices):
        half = len(indices) // 2
        usable = [indices[:half], indices[half:]]

    children = [
        recursive_split(group, vectors, cap, branch, depth + 1, cluster)
        for group in usable
    ]
    return {"members": indices, "children": children, "depth": depth}


def centroid_of(vectors: Any, indices: Sequence[int]) -> list[float]:
    import numpy as np

    mean = np.asarray(vectors[list(indices)], dtype="float32").mean(axis=0)
    norm = float(np.linalg.norm(mean))
    if norm:
        mean = mean / norm
    return [float(x) for x in mean]


# --------------------------------------------------------------------------- invariant


def leaf_cap_violations(engine: Engine, cap: int = LEAF_CAP) -> list[tuple[int, int, int]]:
    """
    Leaves over the cap, as `(subcategory_id, category_id, series_count)`.

    The requirement is a ceiling, so it is assertable -- and this project has been bitten
    repeatedly by things that were true when built and quietly stopped being true.
    """
    with engine.connect() as connection:
        return [
            (row[0], row[1], row[2])
            for row in connection.execute(
                text(
                    """
                    SELECT subcategory_id, category_id, series_count
                      FROM fred_subcategory
                     WHERE is_leaf AND emptied_at IS NULL AND series_count > :cap
                     ORDER BY series_count DESC
                    """
                ),
                {"cap": cap},
            )
        ]


# --------------------------------------------------------------------------- build


def category_series(engine: Engine, category_id: int) -> list[tuple[str, str]]:
    """`(series_id, series_title)` for one category, ordered so a build is repeatable."""
    with engine.connect() as connection:
        return [
            (row[0], row[1])
            for row in connection.execute(
                text(
                    """
                    SELECT DISTINCT s.series_id, s.series_title
                      FROM fred_series AS s
                      JOIN fred_series_category AS sc USING (series_id)
                     WHERE sc.category_id = :category
                     ORDER BY s.series_id
                    """
                ),
                {"category": category_id},
            )
        ]


def _name_tree(node: dict, titles: Sequence[str], namer: Namer) -> None:
    """
    Name every node bottom-up, in place.

    Bottom-up because an interior node is named from its children's names. Naming it
    from a sample of its series would describe the sample and read as describing the
    subtree -- confidently, and wrongly.
    """
    for child in node["children"]:
        _name_tree(child, titles, namer)
    if node["children"]:
        node.update(namer.name_interior([c["name"] for c in node["children"]]))
    else:
        node.update(namer.name_leaf([titles[i] for i in node["members"]]))


def _write_tree(
    engine: Engine, category_id: int, node: dict, series_ids: Sequence[str],
    vectors: Any, parent_id: int | None = None,
) -> tuple[int, int]:
    """
    Insert this node and its descendants top-down. Returns `(nodes, leaves)`.

    Top-down because a child needs its parent's generated id. Memberships are written
    for leaves only: an interior node's members are reachable through its children, and
    duplicating them would make `series_count` ambiguous.
    """
    subcategories = _table(engine, "fred_subcategory")
    memberships = _table(engine, "fred_series_subcategory")
    is_leaf = not node["children"]

    with engine.begin() as connection:
        subcategory_id = connection.execute(
            subcategories.insert().values(
                category_id=category_id,
                parent_subcategory_id=parent_id,
                depth=node["depth"],
                name=node.get("name") or "UNNAMED",
                concepts=node.get("concepts") or None,
                series_count=len(node["members"]),
                is_leaf=is_leaf,
                centroid=centroid_of(vectors, node["members"]),
                prompt_version=PROMPT_VERSION,
                embed_model=EMBED_MODEL,
                built_at=_now(),
            ).returning(subcategories.c.subcategory_id)
        ).scalar_one()

        if is_leaf and node["members"]:
            connection.execute(
                pg_insert(memberships).values(
                    [
                        {"series_id": series_ids[i], "subcategory_id": subcategory_id}
                        for i in node["members"]
                    ]
                ).on_conflict_do_nothing()
            )

    nodes, leaves = 1, 1 if is_leaf else 0
    for child in node["children"]:
        child_nodes, child_leaves = _write_tree(
            engine, category_id, child, series_ids, vectors, subcategory_id
        )
        nodes += child_nodes
        leaves += child_leaves
    return nodes, leaves


def _record_build(engine: Engine, category_id: int, **fields: Any) -> None:
    build = _table(engine, "fred_subcategory_build")
    statement = pg_insert(build).values({"category_id": category_id, **fields})
    with engine.begin() as connection:
        connection.execute(
            statement.on_conflict_do_update(
                index_elements=["category_id"],
                set_={key: statement.excluded[key] for key in fields},
            )
        )


def clear_category(engine: Engine, category_id: int) -> int:
    """
    Drop a category's derived subtree so it can be rebuilt.

    The only delete in this module, and it is scoped to derived rows for one category --
    never to `fred_series`, and never to another category's nodes. A rebuild that
    appended instead would double every node silently.
    """
    with engine.begin() as connection:
        return connection.execute(
            text("DELETE FROM fred_subcategory WHERE category_id = :category"),
            {"category": category_id},
        ).rowcount


def build_category(
    engine: Engine, category_id: int, embedder: TitleEmbedder, namer: Namer,
    cap: int = LEAF_CAP,
) -> dict[str, Any]:
    """Derive, name and store the subcategory tree for one FRED category."""
    import numpy as np

    started = _now()
    rows = category_series(engine, category_id)
    _record_build(
        engine, category_id, status="pending", started_at=started,
        series_count=len(rows), prompt_version=PROMPT_VERSION, embed_model=EMBED_MODEL,
    )

    if len(rows) <= cap:
        # Already browsable. Recorded as skipped rather than left absent, so "no subtree"
        # is distinguishable from "never attempted".
        _record_build(
            engine, category_id, status="skipped", finished_at=_now(),
            leaves=0, nodes=0, max_leaf_size=len(rows), llm_calls=0, cost_usd=0,
        )
        return {"category_id": category_id, "status": "skipped", "series": len(rows)}

    before_calls, before_cost = namer.calls, namer.cost_usd
    try:
        series_ids = [r[0] for r in rows]
        titles = [r[1] for r in rows]
        cache = embedder.embed(titles)
        vectors = np.asarray([cache[t] for t in titles], dtype="float32")
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        vectors = vectors / np.where(norms == 0, 1, norms)

        tree = recursive_split(range(len(rows)), vectors, cap=cap)
        _name_tree(tree, titles, namer)
        clear_category(engine, category_id)
        nodes, leaves = _write_tree(engine, category_id, tree, series_ids, vectors)
    except Exception as error:  # noqa: BLE001 -- recorded, then re-raised
        _record_build(
            engine, category_id, status="error", finished_at=_now(),
            error=str(error)[:2000], llm_calls=namer.calls - before_calls,
            cost_usd=round(namer.cost_usd - before_cost, 5),
        )
        raise

    violations = [v for v in leaf_cap_violations(engine, cap) if v[1] == category_id]
    max_leaf = max((v[2] for v in violations), default=cap)
    _record_build(
        engine, category_id, status="over_cap" if violations else "ok",
        finished_at=_now(), leaves=leaves, nodes=nodes, max_leaf_size=max_leaf,
        llm_calls=namer.calls - before_calls,
        cost_usd=round(namer.cost_usd - before_cost, 5), error=None,
    )
    if violations:
        logger.warning(
            f"category {category_id}: {len(violations)} leaves over the cap of {cap}, "
            f"largest {max_leaf}"
        )
    return {
        "category_id": category_id, "status": "over_cap" if violations else "ok",
        "series": len(rows), "nodes": nodes, "leaves": leaves,
        "llm_calls": namer.calls - before_calls,
        "cost_usd": round(namer.cost_usd - before_cost, 5),
    }


def pending_builds(engine: Engine, prompt_version: str = PROMPT_VERSION) -> list[int]:
    """
    Categories needing a subcategory build, largest last so a bounded run proves the
    cheap ones first.

    A build under a different `prompt_version` counts as pending: names are not
    comparable across prompts, so a tree half-built under each is not a tree.
    """
    with engine.connect() as connection:
        return [
            row[0]
            for row in connection.execute(
                text(
                    """
                    SELECT c.category_id
                      FROM fred_category AS c
                      JOIN fred_series_category AS sc USING (category_id)
                      LEFT JOIN fred_subcategory_build AS b USING (category_id)
                     WHERE c.excluded_reason IS NULL
                       AND (b.status IS NULL
                            OR b.status NOT IN ('ok', 'skipped')
                            OR b.prompt_version IS DISTINCT FROM :version)
                     GROUP BY c.category_id
                     ORDER BY count(DISTINCT sc.series_id)
                    """
                ),
                {"version": prompt_version},
            )
        ]


def build(
    url: str | None = None, limit: int | None = None, cap: int = LEAF_CAP,
    max_series: int | None = None,
) -> dict[str, Any]:
    """
    Build subcategories for every pending category.

    `limit` and `max_series` bound a run: the full job is ~31,000 LLM calls, and proving
    the mechanism on small categories before committing to that is worth more than a
    single unattended pass.
    """
    engine = _engine(url)
    embedder, namer = TitleEmbedder(), Namer()
    pending = pending_builds(engine)
    if max_series is not None:
        sizes = dict(_category_sizes(engine))
        pending = [c for c in pending if sizes.get(c, 0) <= max_series]
    if limit is not None:
        pending = pending[:limit]

    logger.info(f"subcategory build: {len(pending)} categories pending")
    outcome = {"attempted": len(pending), "ok": 0, "skipped": 0, "over_cap": 0, "failed": 0}
    for index, category_id in enumerate(pending, 1):
        try:
            result = build_category(engine, category_id, embedder, namer, cap)
        except Exception as error:  # noqa: BLE001
            outcome["failed"] += 1
            logger.warning(f"category {category_id} failed: {error}")
            continue
        outcome[result["status"]] = outcome.get(result["status"], 0) + 1
        if index % 20 == 0:
            logger.info(
                f"subcategory build: {index}/{len(pending)} categories, "
                f"{namer.calls} names, ${namer.cost_usd:.4f}"
            )
    outcome.update(
        llm_calls=namer.calls, naming_failures=namer.failures,
        titles_embedded=embedder.embedded, cost_usd=round(namer.cost_usd, 5),
        prompt_version=PROMPT_VERSION,
    )
    return outcome


def _category_sizes(engine: Engine) -> list[tuple[int, int]]:
    with engine.connect() as connection:
        return [
            (row[0], row[1])
            for row in connection.execute(
                text(
                    """
                    SELECT category_id, count(DISTINCT series_id)
                      FROM fred_series_category GROUP BY category_id
                    """
                )
            )
        ]


# --------------------------------------------------------------------------- resync


def unassigned_series(engine: Engine, category_id: int | None = None) -> list[tuple[str, str, int]]:
    """
    `(series_id, series_title, category_id)` for series in a built category that no leaf
    holds.

    These are what a FRED resync produces: a series that appeared after the tree was
    built. They are the normal case, not an error, and they must not be left invisible --
    a series in no leaf is unreachable by browsing even though it is in the catalogue.
    """
    with engine.connect() as connection:
        return [
            (row[0], row[1], row[2])
            for row in connection.execute(
                text(
                    """
                    SELECT s.series_id, s.series_title, sc.category_id
                      FROM fred_series AS s
                      JOIN fred_series_category AS sc USING (series_id)
                      JOIN fred_subcategory_build AS b
                        ON b.category_id = sc.category_id AND b.status = 'ok'
                     WHERE (:category IS NULL OR sc.category_id = :category)
                       AND NOT EXISTS (
                           SELECT 1
                             FROM fred_series_subcategory AS ss
                             JOIN fred_subcategory AS sub USING (subcategory_id)
                            WHERE ss.series_id = s.series_id
                              AND sub.category_id = sc.category_id
                       )
                     ORDER BY sc.category_id, s.series_id
                    """
                ),
                {"category": category_id},
            )
        ]


def assign_to_nearest_leaf(
    engine: Engine, embedder: TitleEmbedder, category_id: int | None = None,
) -> dict[str, Any]:
    """
    Place unassigned series on the nearest existing leaf centroid.

    **No LLM call and no re-clustering.** This is what `centroid` is stored for, and it
    is what makes a resync cheap enough to run often: a few hundred new series cost a few
    embeddings instead of a rebuild and thousands of names.

    A leaf pushed over the cap by this is left over the cap and reported. Splitting it
    needs naming, so it belongs to a build pass -- and `leaf_cap_violations` plus the
    `over_cap` status make the debt visible instead of quietly breaking the invariant.
    """
    import numpy as np

    rows = unassigned_series(engine, category_id)
    if not rows:
        return {"unassigned": 0, "assigned": 0, "categories": 0, "pushed_over_cap": 0}

    cache = embedder.embed([r[1] for r in rows])
    memberships = _table(engine, "fred_series_subcategory")
    by_category: dict[int, list[tuple[str, str]]] = defaultdict(list)
    for series_id, title, cat in rows:
        by_category[cat].append((series_id, title))

    assigned = 0
    for cat, items in by_category.items():
        with engine.connect() as connection:
            leaves = connection.execute(
                text(
                    """
                    SELECT subcategory_id, centroid FROM fred_subcategory
                     WHERE category_id = :category AND is_leaf
                       AND emptied_at IS NULL AND centroid IS NOT NULL
                    """
                ),
                {"category": cat},
            ).fetchall()
        if not leaves:
            continue
        leaf_ids = [row[0] for row in leaves]
        centroids = np.asarray([row[1] for row in leaves], dtype="float32")
        norms = np.linalg.norm(centroids, axis=1, keepdims=True)
        centroids = centroids / np.where(norms == 0, 1, norms)

        vectors = np.asarray([cache[title] for _, title in items], dtype="float32")
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        vectors = vectors / np.where(norms == 0, 1, norms)
        best = (vectors @ centroids.T).argmax(axis=1)

        values = [
            {"series_id": items[i][0], "subcategory_id": leaf_ids[int(best[i])]}
            for i in range(len(items))
        ]
        with engine.begin() as connection:
            connection.execute(
                pg_insert(memberships).values(values).on_conflict_do_nothing()
            )
        assigned += len(values)

    refresh_counts(engine)
    over = leaf_cap_violations(engine)
    return {
        "unassigned": len(rows), "assigned": assigned,
        "categories": len(by_category), "pushed_over_cap": len(over),
    }


def refresh_counts(engine: Engine) -> dict[str, int]:
    """
    Recompute `series_count` for every node and mark emptied leaves.

    An interior node's count is the size of its subtree, so it is summed from
    memberships below it rather than stored at insert time and left to drift.
    """
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                WITH leaf AS (
                    SELECT subcategory_id, count(*) AS n
                      FROM fred_series_subcategory GROUP BY subcategory_id
                )
                UPDATE fred_subcategory AS s
                   SET series_count = COALESCE(leaf.n, 0)
                  FROM leaf
                 WHERE s.subcategory_id = leaf.subcategory_id AND s.is_leaf
                """
            )
        )
        connection.execute(
            text(
                """
                UPDATE fred_subcategory AS s SET series_count = 0
                 WHERE s.is_leaf
                   AND NOT EXISTS (SELECT 1 FROM fred_series_subcategory ss
                                    WHERE ss.subcategory_id = s.subcategory_id)
                """
            )
        )
        # Interior counts, deepest first, so a parent sums children already updated.
        connection.execute(
            text(
                """
                WITH RECURSIVE depths AS (
                    SELECT max(depth) AS d FROM fred_subcategory
                )
                UPDATE fred_subcategory AS parent
                   SET series_count = child.total
                  FROM (SELECT parent_subcategory_id AS pid, sum(series_count) AS total
                          FROM fred_subcategory
                         WHERE parent_subcategory_id IS NOT NULL
                         GROUP BY parent_subcategory_id) AS child
                 WHERE parent.subcategory_id = child.pid AND NOT parent.is_leaf
                """
            )
        )
        emptied = connection.execute(
            text(
                """
                UPDATE fred_subcategory SET emptied_at = now()
                 WHERE is_leaf AND series_count = 0 AND emptied_at IS NULL
                """
            )
        ).rowcount
        revived = connection.execute(
            text(
                """
                UPDATE fred_subcategory SET emptied_at = NULL
                 WHERE is_leaf AND series_count > 0 AND emptied_at IS NOT NULL
                """
            )
        ).rowcount
    return {"emptied": emptied, "revived": revived}


def resync(url: str | None = None, split_over_cap: bool = False) -> dict[str, Any]:
    """
    Bring the derived tree back in step with the catalogue after a FRED discovery run.

    The cheap half runs always: place new series on existing leaves by centroid, recount,
    and mark leaves that emptied. No model call, so it is safe to run on a schedule.

    The expensive half is opt-in. `split_over_cap` rebuilds the categories whose leaves
    the cheap half pushed past the ceiling, which costs names. Left off, the debt is
    reported and not paid -- visible either way, which is the point.
    """
    engine = _engine(url)
    embedder, namer = TitleEmbedder(), Namer()

    result: dict[str, Any] = {"assignment": assign_to_nearest_leaf(engine, embedder)}
    result["counts"] = refresh_counts(engine)

    over = leaf_cap_violations(engine)
    result["over_cap_leaves"] = len(over)
    result["over_cap_categories"] = sorted({v[1] for v in over})

    if split_over_cap and over:
        rebuilt = []
        for category_id in result["over_cap_categories"]:
            try:
                rebuilt.append(build_category(engine, category_id, embedder, namer))
            except Exception as error:  # noqa: BLE001
                logger.warning(f"resync rebuild of {category_id} failed: {error}")
        result["rebuilt"] = rebuilt
        result["cost_usd"] = round(namer.cost_usd, 5)
        result["over_cap_leaves_after"] = len(leaf_cap_violations(engine))
    return result
