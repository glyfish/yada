"""
Derive browsable subcategories under each FRED category, and name them.

FRED's taxonomy bottoms out above browsable size: 206 categories hold 500 or more series
attached directly to them, the largest holds 53,187, and descending does not help --
`Production & Business Activity > Housing` holds 53,187 series while its 7 children hold
254 between them. So the nodes between a category and its series do not exist upstream and
have to be built. See `0008_fred_subcategories.py`.

**Corrected 2026-11-07.** This said "every category holding 500+ series has zero
children", measured against a partially walked tree. 64 of the 206 do have children. The
argument is unaffected and better supported: it does not rest on an absence of children
but on where the series are attached.

The pipeline, per category:

1. **Embed** each distinct member title once (cached across categories; 69.1% of titles
   are distinct, and a series in several categories would otherwise be embedded twice).
2. **Split recursively** until every leaf holds at most `LEAF_CAP` series. Not one k-means
   at `k = n/LEAF_CAP`: measured, that leaves 37% of leaves over the cap holding 56% of
   the titles. A mean of 25 is not a maximum of 25.
3. **Name** each node from its members with an LLM, producing a short name and a set of
   search `concepts` that deliberately includes synonyms absent from the titles.

Step 3 is why this works at all. The names and concepts become a full-text index --
27,385 rows for the non-regional half -- that answers conceptual queries the 846,628
titles cannot: measured on a sample,
"steel making capacity", "heavy industry plant buildout" and "coal and coke production"
all reached **first place** for a topic whose titles contain none of those words, while
lexical search over the titles returned zero rows for all three.

Because both the names and the shape are derived rather than source data, every row
stores `PROMPT_VERSION` and `SPLIT_VERSION`. A changed prompt gives different names for
identical input and a changed splitter gives a different tree, and a half-rebuilt
catalogue must not be mistakable for a consistent one.

Clustering happens **within** a category, never globally. It is cheaper, the naming is
sharper because the input is already homogeneous, and it keeps FRED's own curation as the
spine rather than replacing it with tens of thousands of derived nodes and no human
structure above them.

**Scope.** `SCOPES` splits the catalogue, and `pending_builds` defaults to
`non-regional`. Regional data is 4,173 of 5,201 categories and the semantic scheme does
not fit it -- see `SCOPES` for why, and section 4.4 of
`sefer/planning/yada-fred-subcategory-procedure.md` for what it would need instead.
"""

from __future__ import annotations

import json
import math
import os
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from threading import Lock
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
#:
#: Enforced in `recursive_split` and asserted by `branch_cap_violations`. It was
#: previously only *documented*: the k ceiling read `branch ** 2`, so a node could take
#: 625 children, and 130 of the 723 non-regional categories were over the threshold that
#: triggers it. Measured 2026-11-08 before fixing it: enforcing 25 costs ~$1.02 more in
#: naming and does NOT make the tree deeper to browse -- total depth (FRED path +
#: derived levels) stays at a median of 4 non-regional and 6 regional either way,
#: because the categories with the most series sit shallowest in FRED's own tree.
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

#: Naming calls in flight at once, within one level of one category's tree.
#:
#: Cost was never the constraint here; wall-clock was. Measured sequentially at 1.37 s
#: per call (34 calls in 44.0 s and 43 in 62.6 s on the two probe categories), which puts
#: the non-regional half at ~13.6 hours of nothing but waiting on HTTP. Siblings are
#: independent, so the only ordering the tree requires is child-before-parent.
NAMING_CONCURRENCY = 8

#: Attempts at getting a *parsable* reply for one node, across all failure kinds. This is
#: not the SDK's retry below -- that one covers transport (429, 5xx) and never sees a reply
#: that arrived intact and simply was not JSON.
#:
#: Raised from an effective 2 on 2026-11-08. The loop retried a truncated reply and
#: returned immediately on an unparsable one, so a single bad draw degraded a node
#: permanently. Measured: 50 of 29,661 calls (0.17%) across two runs, with 0 truncations --
#: so every observed failure was in the branch that had no retry. It is a formatting miss
#: rather than a property of the input: rebuilding 38 countries cleared 12 failures and
#: produced 24 new ones in different places, which is a dice roll, not a hard case. At
#: 0.17% a second draw should take 50 to well under 1.
NAMING_ATTEMPTS = 3

#: Attempts the SDK makes for 429 and 5xx before raising. The default of 2 is thin for a
#: run of tens of thousands of calls: one unretried overload marks a whole category
#: `error`, and a retry re-spends every name already generated for it. Measured over the
#: 26,922 calls of the non-regional run: 0 categories failed.
NAMING_MAX_RETRIES = 8

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

#: The clustering that produced a tree, stored on every row beside `PROMPT_VERSION`.
#:
#: Same argument as the prompt version, for the same reason: the names are not the only
#: model output here, the *shape* is derived too, and a tree half-built under one splitter
#: is no more comparable than one half-built under two prompts. Bump this on any change
#: to `recursive_split` or the clustering it defaults to.
#:
#: `2026-11-08.balanced` replaced plain k-means with a size-balanced assignment. Plain
#: k-means returns clusters of wildly uneven size, and since the recursion continues until
#: every leaf is under the cap, one fat cluster drags a whole branch down several further
#: levels. Measured: a 9,932-series category reached **depth 8** with 1,105 nodes and 9
#: leaves holding a single series; balanced, the same category is depth 3 with 426 nodes
#: and no singletons. It is shallower, 61% cheaper to name, and costs 2 points of leaf
#: cohesion (0.953 -> 0.931 mean cosine to the leaf centroid).
SPLIT_VERSION = "2026-11-08.balanced"

#: Which half of the catalogue a build covers, as a `category_path` predicate.
#:
#: The split is not cosmetic. The semantic scheme clusters series by title text, which
#: works where titles differ by WHAT is measured and fails where they differ by WHERE:
#: county titles are one measure with a place name substituted, so clustering groups
#: Alabama's counties together instead of grouping unemployment measures together.
#: Regional data is 4,173 of 5,201 categories, it already sits 5 levels deep in FRED's
#: own tree (3,078 of those are `States > * > Counties > *`), and building a semantic
#: tree under it would reach 8 levels to browse data whose natural shape is two facets.
#: See `sefer/planning/yada-fred-subcategory-procedure.md` section 4.4. Until that is
#: settled, `non-regional` is the only scope with a measured basis, so there is no
#: default: a caller states which half it is paying for.
SCOPES = {
    "all": "",
    "non-regional": "AND c.category_path NOT LIKE 'U.S. Regional Data%'",
    "regional": "AND c.category_path LIKE 'U.S. Regional Data%'",
}

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
        #: float32 rows, not `list[float]`. The cache spans a whole build so duplicate
        #: titles are embedded once, and the non-regional half holds 289,744 distinct
        #: titles: as Python float objects at 256 dims that is ~2.4 GB, as float32 rows
        #: ~0.30 GB. The callers already coerce to float32, so nothing downstream changes.
        self._cache: dict[str, Any] = {}
        self.embedded = 0

    def _ensure_client(self) -> Any:
        if self._client is None:
            from openai import OpenAI

            self._client = OpenAI()
        return self._client

    def embed(self, titles: Iterable[str]) -> dict[str, Any]:
        import numpy as np

        wanted = [t for t in dict.fromkeys(titles) if t not in self._cache]
        for start in range(0, len(wanted), EMBED_BATCH):
            batch = wanted[start:start + EMBED_BATCH]
            response = self._ensure_client().embeddings.create(
                model=self._model, input=batch, dimensions=self._dims
            )
            for title, item in zip(batch, response.data):
                self._cache[title] = np.asarray(item.embedding, dtype="float32")
            self.embedded += len(batch)
        return self._cache


# --------------------------------------------------------------------------- naming


class Namer:
    """
    Names nodes, counting tokens so the build can report what it spent.

    Safe to call from several threads: `_name_tree` names a whole level at once, so the
    counters are mutated concurrently and an unguarded `+=` would under-report the spend
    on the one run where the number matters.
    """

    def __init__(self, client: Any = None, model: str = NAMING_MODEL,
                 max_retries: int = NAMING_MAX_RETRIES):
        self._client = client
        self._model = model
        self._max_retries = max_retries
        self._lock = Lock()
        self._client_lock = Lock()
        self.calls = 0
        self.input_tokens = 0
        self.output_tokens = 0
        #: Nodes that could not be named within `NAMING_ATTEMPTS`, not bad replies. A
        #: single bad draw is now retried, so this counts only exhaustion -- which is what
        #: makes a non-zero value worth investigating rather than absorbing.
        self.failures = 0
        #: Replies discarded for hitting the token ceiling. Counted separately from
        #: `failures` because a rising count means the budget is wrong, not the model.
        self.truncated = 0

    def _ensure_client(self) -> Any:
        # Double-checked under a lock: without it, concurrent first calls each build a
        # client and all but one are discarded along with their connection pools.
        if self._client is None:
            with self._client_lock:
                if self._client is None:
                    from anthropic import Anthropic

                    self._client = Anthropic(max_retries=self._max_retries)
        return self._client

    @property
    def cost_usd(self) -> float:
        return (
            self.input_tokens / 1e6 * NAMING_INPUT_RATE
            + self.output_tokens / 1e6 * NAMING_OUTPUT_RATE
        )

    def _call(self, system: str, user: str) -> dict[str, str]:
        """
        One naming call, retried up to `NAMING_ATTEMPTS` times on either failure kind.

        `stop_reason == 'max_tokens'` is checked *before* parsing, and the reply is
        discarded rather than parsed. A JSON object cut off mid-string can still yield a
        name that reads perfectly while its concepts are silently half-missing -- a
        plausible wrong answer, which is worse than a visible failure.

        An unparsable-but-complete reply is retried too. It was not until 2026-11-08, and
        since truncations measured zero over two runs, that branch was the only one any
        observed failure took.
        """
        budget = NAMING_MAX_TOKENS
        outcome = "naming failed"
        for _ in range(NAMING_ATTEMPTS):
            message = self._ensure_client().messages.create(
                model=self._model,
                max_tokens=budget,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            usage = getattr(message, "usage", None)
            with self._lock:
                self.calls += 1
                if usage is not None:
                    self.input_tokens += getattr(usage, "input_tokens", 0) or 0
                    self.output_tokens += getattr(usage, "output_tokens", 0) or 0
            if getattr(message, "stop_reason", None) == "max_tokens":
                with self._lock:
                    self.truncated += 1
                budget *= 2
                outcome = "reply truncated"
                continue
            named = parse_naming_reply(extract_text(message))
            if not named["name"].startswith("UNNAMED"):
                return named
            # An intact reply that is not the JSON asked for. Retried rather than
            # returned, which is the 2026-11-08 fix: see NAMING_ATTEMPTS for why this is
            # worth another draw and truncation is not the same thing.
            outcome = "naming failed"
        with self._lock:
            self.failures += 1
        return {"name": f"UNNAMED ({outcome})", "concepts": ""}

    def name_leaf(self, titles: Sequence[str]) -> dict[str, str]:
        return self._call(LEAF_SYSTEM_PROMPT, leaf_user_prompt(titles[:NAMING_SAMPLE]))

    def name_interior(self, child_names: Sequence[str]) -> dict[str, str]:
        return self._call(
            INTERIOR_SYSTEM_PROMPT, interior_user_prompt(child_names[:NAMING_SAMPLE])
        )


# --------------------------------------------------------------------------- clustering


def balanced_clusters(vectors: Any, k: int) -> Any:
    """
    k-means centroids, then assignment capped at `ceil(n / k)` per cluster.

    Plain k-means optimises cohesion and says nothing about size, which is the wrong
    objective for a tree whose requirement is a *size* ceiling: the recursion keeps
    splitting until every leaf is under the cap, so an uneven split does not get
    absorbed, it gets amplified into depth. See `SPLIT_VERSION` for the measurement.

    Points are placed most-confident-first -- ordered by distance to their nearest
    centroid -- so the points with a clear home get it, and the ones paying for the
    balance are the ones that were ambiguous anyway. Deterministic: `random_state` is
    fixed and the sorts are stable, so a rebuild reproduces the tree.
    """
    import numpy as np
    from sklearn.cluster import KMeans

    kmeans = KMeans(n_clusters=k, n_init=3, random_state=0).fit(vectors)
    capacity = math.ceil(len(vectors) / k)
    distance = np.stack(
        [((vectors - centre) ** 2).sum(1) for centre in kmeans.cluster_centers_], axis=1
    )
    # Precomputed once: per-point argsort inside the loop is the same work n times over.
    preference = np.argsort(distance, axis=1, kind="stable")
    order = np.argsort(distance.min(axis=1), kind="stable")

    counts = np.zeros(k, dtype=int)
    labels = np.full(len(vectors), -1, dtype=int)
    for point in order:
        for choice in preference[point]:
            if counts[choice] < capacity:
                labels[point] = choice
                counts[choice] += 1
                break
    return labels


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

    `k` is capped at `branch`, not `branch ** 2`. The squared form was here first and it
    let the 53,187-series category give its root 625 children -- a node no more readable
    than the pile it was built to break up, which is the whole requirement. See
    `BRANCH_CAP` for what enforcing it costs, and for the measurement showing it does not
    make the tree deeper.

    Clustering defaults to `balanced_clusters`, not plain k-means: the recursion turns an
    uneven split into depth rather than absorbing it. `cluster` stays injectable so the
    shape can be tested without a model or a network.
    """
    import numpy as np

    indices = list(indices)
    if len(indices) <= cap:
        return {"members": indices, "children": [], "depth": depth}

    k = min(max(2, math.ceil(len(indices) / cap)), len(indices), branch)
    labels = (cluster or balanced_clusters)(vectors[indices], k)

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


def modelled_nodes(size: int, cap: int = LEAF_CAP, branch: int = BRANCH_CAP) -> int:
    """
    How many nodes `recursive_split` will produce for a category of `size` series.

    Exact, not an estimate, because `balanced_clusters` divides each node evenly: it
    predicted 20 / 151 / 426 nodes for the 454 / 2,790 / 9,932-series categories and the
    real splitter produced 20 / 151 / 426. Under plain k-means nothing like this was
    possible -- an uneven split recursed further, and the same three categories came out
    at 43 / 259 / 1,105.

    Every node is one naming call, so this is what a run costs. It lives here rather than
    in the CLI that reports it because a cost model that drifts from the splitter is how
    a plan ends up quoting a number nobody can reproduce.
    """
    total = 0
    frontier = [size]
    while frontier:
        following = []
        for node in frontier:
            total += 1
            if node <= cap:
                continue
            k = min(max(2, math.ceil(node / cap)), node, branch)
            base, extra = divmod(node, k)
            following.extend([base + 1] * extra + [base] * (k - extra))
        frontier = following
    return total


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


def branch_cap_violations(
    engine: Engine, cap: int = BRANCH_CAP
) -> list[tuple[int, int, int]]:
    """
    Interior nodes with more than `cap` children, as `(subcategory_id, category_id, n)`.

    The upward half of the invariant, and the reason it exists: `BRANCH_CAP` was stated,
    documented and argued for, and the splitter quietly allowed 25x it for a year because
    nothing asserted it. `leaf_cap_violations` covers the downward half; a tree can
    satisfy that one completely and still be unbrowsable at the top.
    """
    with engine.connect() as connection:
        return [
            (row[0], row[1], row[2])
            for row in connection.execute(
                text(
                    """
                    SELECT parent_subcategory_id, category_id, count(*) AS children
                      FROM fred_subcategory
                     WHERE parent_subcategory_id IS NOT NULL
                     GROUP BY parent_subcategory_id, category_id
                    HAVING count(*) > :cap
                     ORDER BY children DESC
                    """
                ),
                {"cap": cap},
            )
        ]


def unnamed_nodes(engine: Engine) -> list[tuple[int, int, str]]:
    """
    Nodes whose name is a naming failure, as `(subcategory_id, category_id, name)`.

    `parse_naming_reply` degrades to `UNNAMED (...)` on purpose -- one bad reply must not
    abort a build of ~36,000 nodes -- but a degraded name is written to a browsable tree
    beside a build row that says `ok`. Without this query the only record of a failure is
    a counter in a process that has since exited.
    """
    with engine.connect() as connection:
        return [
            (row[0], row[1], row[2])
            for row in connection.execute(
                text(
                    """
                    SELECT subcategory_id, category_id, name
                      FROM fred_subcategory
                     WHERE name LIKE 'UNNAMED%'
                     ORDER BY category_id, subcategory_id
                    """
                )
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


def _name_tree(
    node: dict, titles: Sequence[str], namer: Namer,
    workers: int = NAMING_CONCURRENCY,
) -> None:
    """
    Name every node bottom-up, in place: concurrent within a level, ordered between them.

    Bottom-up because an interior node is named from its children's names. Naming it
    from a sample of its series would describe the sample and read as describing the
    subtree -- confidently, and wrongly.

    That dependency is the *only* ordering the tree needs. Siblings do not see each other
    (`§4.4 sibling-blind naming`), so a level can be named all at once, and the recursive
    one-at-a-time version this replaces spent the entire run waiting on HTTP: 1.37 s per
    call measured, which was 10.4 hours for the non-regional half alone. Measured again on
    the completed run: 27,385 names in 1 h 57 m at 8 concurrent, a 5.3x speedup.

    Names do not depend on the order within a level, so the tree this produces is the
    same tree the sequential version produced -- a concurrent build is reproducible for
    the same reason a sequential one is.
    """
    levels: dict[int, list[dict]] = defaultdict(list)
    stack = [node]
    while stack:
        current = stack.pop()
        levels[current["depth"]].append(current)
        stack.extend(current["children"])

    for depth in sorted(levels, reverse=True):
        jobs = [
            (
                target,
                namer.name_interior if target["children"] else namer.name_leaf,
                [child["name"] for child in target["children"]] if target["children"]
                else [titles[index] for index in target["members"]],
            )
            for target in levels[depth]
        ]
        if workers <= 1 or len(jobs) == 1:
            for target, name_it, argument in jobs:
                target.update(name_it(argument))
            continue
        with ThreadPoolExecutor(max_workers=min(workers, len(jobs))) as pool:
            futures = {
                pool.submit(name_it, argument): target
                for target, name_it, argument in jobs
            }
            for future in as_completed(futures):
                # Raises if the call failed after the SDK's retries. Deliberate: it
                # aborts this category and `build_category` records the error, rather
                # than writing a tree with a silently unnamed branch in it.
                futures[future].update(future.result())


def _write_tree(
    engine: Engine, category_id: int, node: dict, series_ids: Sequence[str],
    vectors: Any, parent_id: int | None = None,
) -> tuple[int, int]:
    """
    Insert a category's whole tree. Returns `(nodes, leaves)`.

    Reflects the two tables once and writes in one transaction, both per category rather
    than per node. The recursive version did `Table(..., autoload_with=engine)` twice and
    opened a transaction on every node it visited, which for the non-regional half is
    ~72,000 schema round-trips and ~36,000 transactions to write 36,000 rows.

    One transaction also makes a crash mid-write atomic. It was already *recoverable* --
    `clear_category` runs before the next attempt -- but recoverable and atomic are not
    the same promise, and the weaker one leaves a partial tree readable in the meantime.
    """
    tables = (
        _table(engine, "fred_subcategory"),
        _table(engine, "fred_series_subcategory"),
    )
    with engine.begin() as connection:
        return _write_node(
            connection, tables, category_id, node, series_ids, vectors, parent_id
        )


def _write_node(
    connection: Any, tables: tuple[Table, Table], category_id: int, node: dict,
    series_ids: Sequence[str], vectors: Any, parent_id: int | None,
) -> tuple[int, int]:
    """
    Insert this node and its descendants top-down. Returns `(nodes, leaves)`.

    Top-down because a child needs its parent's generated id. Memberships are written
    for leaves only: an interior node's members are reachable through its children, and
    duplicating them would make `series_count` ambiguous.
    """
    subcategories, memberships = tables
    is_leaf = not node["children"]

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
            split_version=SPLIT_VERSION,
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
        child_nodes, child_leaves = _write_node(
            connection, tables, category_id, child, series_ids, vectors, subcategory_id
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
    cap: int = LEAF_CAP, workers: int = NAMING_CONCURRENCY,
) -> dict[str, Any]:
    """Derive, name and store the subcategory tree for one FRED category."""
    import numpy as np

    started = _now()
    rows = category_series(engine, category_id)
    _record_build(
        engine, category_id, status="pending", started_at=started,
        series_count=len(rows), prompt_version=PROMPT_VERSION,
        split_version=SPLIT_VERSION, embed_model=EMBED_MODEL,
    )

    if len(rows) <= cap:
        # Already browsable. Recorded as skipped rather than left absent, so "no subtree"
        # is distinguishable from "never attempted".
        _record_build(
            engine, category_id, status="skipped", finished_at=_now(),
            leaves=0, nodes=0, max_leaf_size=len(rows), llm_calls=0, cost_usd=0,
            naming_failures=0, error=None,
        )
        return {"category_id": category_id, "status": "skipped", "series": len(rows)}

    before_calls, before_cost = namer.calls, namer.cost_usd
    before_failures = namer.failures
    try:
        series_ids = [r[0] for r in rows]
        titles = [r[1] for r in rows]
        cache = embedder.embed(titles)
        vectors = np.asarray([cache[t] for t in titles], dtype="float32")
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        vectors = vectors / np.where(norms == 0, 1, norms)

        tree = recursive_split(range(len(rows)), vectors, cap=cap)
        _name_tree(tree, titles, namer, workers=workers)
        clear_category(engine, category_id)
        nodes, leaves = _write_tree(engine, category_id, tree, series_ids, vectors)
    except Exception as error:  # noqa: BLE001 -- recorded, then re-raised
        _record_build(
            engine, category_id, status="error", finished_at=_now(),
            error=str(error)[:2000], llm_calls=namer.calls - before_calls,
            naming_failures=namer.failures - before_failures,
            cost_usd=round(namer.cost_usd - before_cost, 5),
        )
        raise

    violations = [v for v in leaf_cap_violations(engine, cap) if v[1] == category_id]
    max_leaf = max((v[2] for v in violations), default=cap)
    failures = namer.failures - before_failures
    _record_build(
        engine, category_id, status="over_cap" if violations else "ok",
        finished_at=_now(), leaves=leaves, nodes=nodes, max_leaf_size=max_leaf,
        llm_calls=namer.calls - before_calls, naming_failures=failures,
        cost_usd=round(namer.cost_usd - before_cost, 5), error=None,
    )
    if violations:
        logger.warning(
            f"category {category_id}: {len(violations)} leaves over the cap of {cap}, "
            f"largest {max_leaf}"
        )
    if failures:
        # Stored as well as logged. A degraded name is written to a browsable tree beside
        # a row that says `ok`, and a counter in an exited process is not a record.
        logger.warning(f"category {category_id}: {failures} nodes could not be named")
    return {
        "category_id": category_id, "status": "over_cap" if violations else "ok",
        "series": len(rows), "nodes": nodes, "leaves": leaves,
        "llm_calls": namer.calls - before_calls, "naming_failures": failures,
        "cost_usd": round(namer.cost_usd - before_cost, 5),
    }


def pending_builds(
    engine: Engine, scope: str = "non-regional",
    prompt_version: str = PROMPT_VERSION, split_version: str = SPLIT_VERSION,
) -> list[int]:
    """
    Categories needing a subcategory build, largest last so a bounded run proves the
    cheap ones first.

    A build under a different `prompt_version` or `split_version` counts as pending:
    neither the names nor the shape are comparable across versions, so a tree half-built
    under each is not a tree. Both are checked, because either one alone would let a
    stale tree read as finished.

    **So does a changed series count.** `series_count` records how many series the build
    actually saw, and FRED keeps adding them, so a tree built before a fetch describes a
    catalogue that no longer exists. Without this the drift is permanent and silent: the
    build row says `ok` forever while the category grows underneath it. Found on
    2026-11-08, when lifting the country page cap added series to 38 categories and
    nothing re-queued them.

    `scope` bounds which half of the catalogue is considered; see `SCOPES`. It defaults
    to `non-regional` because that is the half the cost and quality were measured on --
    the unfiltered version this replaces returned all 4,606 over-cap categories, so
    `build()` with no argument would have spent the regional budget by accident.
    """
    if scope not in SCOPES:
        raise ValueError(f"unknown scope {scope!r}; expected one of {sorted(SCOPES)}")
    with engine.connect() as connection:
        return [
            row[0]
            for row in connection.execute(
                text(
                    f"""
                    SELECT c.category_id
                      FROM fred_category AS c
                      JOIN fred_series_category AS sc USING (category_id)
                      LEFT JOIN fred_subcategory_build AS b USING (category_id)
                     WHERE TRUE
                       {SCOPES[scope]}
                     GROUP BY c.category_id, b.status, b.prompt_version,
                              b.split_version, b.series_count
                    HAVING b.status IS NULL
                        OR b.status NOT IN ('ok', 'skipped')
                        OR b.prompt_version IS DISTINCT FROM :version
                        OR b.split_version IS DISTINCT FROM :split
                        OR b.series_count IS DISTINCT FROM count(DISTINCT sc.series_id)
                     ORDER BY count(DISTINCT sc.series_id)
                    """
                ),
                {"version": prompt_version, "split": split_version},
            )
        ]


def build(
    url: str | None = None, scope: str = "non-regional", limit: int | None = None,
    cap: int = LEAF_CAP, max_series: int | None = None,
    workers: int = NAMING_CONCURRENCY,
) -> dict[str, Any]:
    """
    Build subcategories for every pending category in `scope`.

    `limit` and `max_series` bound a run: the full job is ~36,000 LLM calls, and proving
    the mechanism on small categories before committing to that is worth more than a
    single unattended pass.

    Resumable, because `pending_builds` skips what is already `ok` or `skipped` -- so an
    interrupted run is continued by invoking it again with the same arguments, and a
    completed one is a no-op that makes no calls and spends nothing.
    """
    engine = _engine(url)
    embedder, namer = TitleEmbedder(), Namer()
    pending = pending_builds(engine, scope=scope)
    if max_series is not None:
        sizes = dict(_category_sizes(engine))
        pending = [c for c in pending if sizes.get(c, 0) <= max_series]
    if limit is not None:
        pending = pending[:limit]

    started = time.monotonic()
    logger.info(f"subcategory build: {len(pending)} {scope} categories pending")
    outcome = {"attempted": len(pending), "ok": 0, "skipped": 0, "over_cap": 0, "failed": 0}
    for index, category_id in enumerate(pending, 1):
        try:
            result = build_category(engine, category_id, embedder, namer, cap, workers)
        except Exception as error:  # noqa: BLE001
            outcome["failed"] += 1
            logger.warning(f"category {category_id} failed: {error}")
            continue
        outcome[result["status"]] = outcome.get(result["status"], 0) + 1
        if index % 20 == 0:
            elapsed = max(time.monotonic() - started, 1)
            logger.info(
                f"subcategory build: {index}/{len(pending)} categories, "
                f"{namer.calls} names, ${namer.cost_usd:.4f}, "
                f"{namer.calls / elapsed * 60:.0f} names/min"
            )
    outcome.update(
        scope=scope, llm_calls=namer.calls, naming_failures=namer.failures,
        truncated_replies=namer.truncated, titles_embedded=embedder.embedded,
        input_tokens=namer.input_tokens, output_tokens=namer.output_tokens,
        cost_usd=round(namer.cost_usd, 5), prompt_version=PROMPT_VERSION,
        split_version=SPLIT_VERSION, elapsed_s=round(time.monotonic() - started, 1),
    )
    # Both halves of the invariant, read back from the database rather than inferred from
    # what the build thought it wrote.
    outcome["leaf_cap_violations"] = len(leaf_cap_violations(engine, cap))
    outcome["branch_cap_violations"] = len(branch_cap_violations(engine))
    outcome["unnamed_nodes"] = len(unnamed_nodes(engine))
    return outcome


def _scoped_categories(engine: Engine, scope: str) -> list[int]:
    """Every category id inside `scope`, regardless of build state."""
    if scope not in SCOPES:
        raise ValueError(f"unknown scope {scope!r}; expected one of {sorted(SCOPES)}")
    with engine.connect() as connection:
        return [
            row[0]
            for row in connection.execute(
                text(
                    f"""
                    SELECT c.category_id FROM fred_category AS c
                     WHERE TRUE
                       {SCOPES[scope]}
                    """
                )
            )
        ]


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


def resync(
    url: str | None = None, split_over_cap: bool = False,
    scope: str = "non-regional", workers: int = NAMING_CONCURRENCY,
) -> dict[str, Any]:
    """
    Bring the derived tree back in step with the catalogue after a FRED discovery run.

    The cheap half runs always: place new series on existing leaves by centroid, recount,
    and mark leaves that emptied. No model call, so it is safe to run on a schedule.

    The expensive half is opt-in. `split_over_cap` rebuilds the categories whose leaves
    the cheap half pushed past the ceiling, which costs names. Left off, the debt is
    reported and not paid -- visible either way, which is the point.

    `scope` bounds the rebuild, not the assignment. Placing a new series on an existing
    leaf is free and must happen wherever a tree exists, or the series is unbrowsable;
    paying to rebuild is a budget decision, and it inherits the same default as `build`.
    """
    engine = _engine(url)
    embedder, namer = TitleEmbedder(), Namer()

    result: dict[str, Any] = {"assignment": assign_to_nearest_leaf(engine, embedder)}
    result["counts"] = refresh_counts(engine)

    over = leaf_cap_violations(engine)
    result["over_cap_leaves"] = len(over)
    result["over_cap_categories"] = sorted({v[1] for v in over})

    result["branch_cap_violations"] = len(branch_cap_violations(engine))
    result["unnamed_nodes"] = len(unnamed_nodes(engine))

    if split_over_cap and over:
        in_scope = set(_scoped_categories(engine, scope))
        rebuilt = []
        for category_id in result["over_cap_categories"]:
            if category_id not in in_scope:
                continue
            try:
                rebuilt.append(
                    build_category(engine, category_id, embedder, namer,
                                   workers=workers)
                )
            except Exception as error:  # noqa: BLE001
                logger.warning(f"resync rebuild of {category_id} failed: {error}")
        result["rebuilt"] = rebuilt
        result["rebuild_scope"] = scope
        result["cost_usd"] = round(namer.cost_usd, 5)
        result["over_cap_leaves_after"] = len(leaf_cap_violations(engine))
        result["branch_cap_violations_after"] = len(branch_cap_violations(engine))
    return result
