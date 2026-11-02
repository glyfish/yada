"""
Discover FRED's catalogue from the API and write it straight to Postgres.

This replaces reading `clients/fred/**.yaml`. The export those files came from had three
faults and reported none of them -- series lists truncated at one page of 1,000, a tree
rooted a level too low, and `Production & Business Activity` missing entirely. A file
cannot report a short fetch: it has no transaction and nothing to reconcile against, so
one page of nine looks like completion. See `0006_fred_api_discovery.py`.

So the reconciliation is the point of this module, not a nicety on the side. Every
category fetch records FRED's own `count` beside the number of series actually written,
and disagreement is stored as `status='incomplete'` rather than logged and forgotten. A
run that fetches 60% of the catalogue says so in a query.

Two things follow from that and are deliberate:

- **Nothing here deletes.** `build()` in `fred_catalogue` truncates and rewrites, which
  is safe when the source is a local file read in one pass. Here the source is 1,100-odd
  paced HTTP requests over about fifteen minutes, any of which can fail. Upsert means a
  partial run leaves the catalogue larger and more correct than it was, never emptier.
  Pruning series FRED has genuinely dropped is a separate pass that must read a
  *complete* scan to be safe, and is not implemented.
- **Resume is driven by the scan table**, not by position in a loop. A category is
  skipped only when its stored status is `ok`, so an interrupted run resumes, and a
  category that came back short is retried rather than inherited.

Rate limit: FRED documents 120 requests/minute. Probing at ~480/min returned 429s, so
`MIN_INTERVAL` paces to ~100/min. Be gentle here; this walks the whole catalogue.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from datetime import datetime, timezone
from typing import Any, Iterator

from sqlalchemy import MetaData, Table, text
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.engine import Engine

from apps.agentic.db.fred_catalogue import (
    PERIOD_DAYS,
    _date,
    _engine,
    _int,
    _timestamp,
    currency_cutoffs,
    frequency_class,
)
from lib.logger import get_logger

logger = get_logger("YADA")

BASE_URL = "https://api.stlouisfed.org/fred"

#: FRED's maximum page size for `category/series`. The export used this as if it were a
#: count, which is the defect this module exists to undo.
PAGE = 1000

#: Seconds between requests: ~100/min against a documented ceiling of 120.
MIN_INTERVAL = 0.6

#: FRED's root. Its children are the eight real top-level categories.
ROOT_CATEGORY = 0

#: A guard on the tree walk, not a limit on FRED. A parent/child cycle would otherwise
#: spin forever, and a silent infinite loop in a paced fetch looks like slow progress.
MAX_DEPTH = 12

#: Subtrees recorded but deliberately not fetched, with the reason stored in
#: `fred_category.excluded_reason`. These are decisions, not gaps: state and county data
#: was left out of the original export on purpose because of its volume, and nothing
#: recorded that, so this session mistook it for a defect. Deferral, not rejection --
#: the categories are walked and kept, so lifting one is a fetch, never a re-walk.
VOLUME_EXCLUDED: dict[int, str] = {
    3008: (
        "U.S. Regional Data: excluded by volume (decision 2026-11-01). "
        "States alone is 53 categories holding ~80,000 series before county and metro "
        "nodes, which make up 4,160 of the 5,186 categories in FRED's tree. "
        "Fetchable later without re-walking."
    ),
}

#: Deliberate page ceilings, matched against `category_path` by prefix. Countries stay at
#: one page for the same volume reason the branch above is out. Recorded per category in
#: `fred_category_scan.page_limit` so a capped fetch reads as a choice rather than as the
#: truncation this module exists to undo.
PAGE_LIMITS: tuple[tuple[str, int], ...] = (
    ("International Data > Countries", 1),
)


def page_limit_for(category_path: str | None) -> int | None:
    """The deliberate page ceiling for this category, or None to fetch everything."""
    if not category_path:
        return None
    for prefix, limit in PAGE_LIMITS:
        if category_path.startswith(prefix):
            return limit
    return None


class FredApiError(RuntimeError):
    """A request failed in a way retrying will not fix."""


class FredApi:
    """
    A paced, retrying FRED client.

    Deliberately not the client in `meida/clients/fred.py`: that one is async and lives
    in the repo that will eventually own this. Duplicating ~40 lines of paced GET is the
    cheaper side of that bet than coupling the two repos before the ownership question
    in `yada-todo.md` section 5 is settled.
    """

    def __init__(self, api_key: str | None = None, min_interval: float = MIN_INTERVAL):
        key = api_key or os.environ.get("FRED_API_KEY")
        if not key:
            raise FredApiError(
                "FRED_API_KEY is not set. Discovery cannot run without it."
            )
        self._key = key
        self._min_interval = min_interval
        self._last = 0.0
        self.requests = 0

    def get(self, path: str, **params: Any) -> dict:
        """One paced GET, retrying 429 and 5xx with increasing backoff."""
        params.update(api_key=self._key, file_type="json")
        url = f"{BASE_URL}/{path}?" + urllib.parse.urlencode(params)
        for attempt in range(6):
            wait = self._min_interval - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            try:
                self.requests += 1
                with urllib.request.urlopen(url, timeout=60) as response:
                    return json.load(response)
            except urllib.error.HTTPError as error:
                body = error.read().decode(errors="replace")[:200]
                # 400 with this message means the key is wrong, not rate-limited. Fail
                # loudly: yada's stored key was unregistered and nothing noticed,
                # because nothing in yada called the API.
                if error.code == 400 and "api_key" in body:
                    raise FredApiError(f"FRED rejected the API key: {body}") from error
                if error.code == 429 or error.code >= 500:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise FredApiError(f"{path} -> HTTP {error.code}: {body}") from error
            except (urllib.error.URLError, TimeoutError) as error:
                time.sleep(5 * (attempt + 1))
                last_error = error
        raise FredApiError(f"{path} failed after retries: {locals().get('last_error')}")


def _table(engine: Engine, name: str) -> Table:
    return Table(name, MetaData(), autoload_with=engine)


def _now() -> datetime:
    return datetime.now(timezone.utc)


# --------------------------------------------------------------------------- tree


def walk_categories(
    engine: Engine, api: FredApi, excluded: dict[int, str] | None = None
) -> dict[str, int]:
    """
    Breadth-first from FRED's root, writing `(category_id, category_name, parent_id)`.

    The parent is taken from FRED's own response rather than inferred from a path
    string, which is what went wrong before: `category_path` was the only record of
    parentage, so a subtree fetched from its own id -- as `Countries` was -- lost the
    levels above it with nothing to detect the loss.

    An excluded category is **recorded and not descended into**. It stays in the tree
    carrying its reason, so the branch is visible as a decision rather than a gap, and
    the walk costs one request for it instead of several thousand.
    """
    excluded = VOLUME_EXCLUDED if excluded is None else excluded
    categories = _table(engine, "fred_category")
    seen: set[int] = set()
    queue: deque[tuple[int, int]] = deque([(ROOT_CATEGORY, 0)])
    written = 0
    stopped: list[int] = []

    while queue:
        category_id, depth = queue.popleft()
        if category_id in seen or depth > MAX_DEPTH:
            continue
        seen.add(category_id)

        if category_id in excluded:
            # Recorded by mark_exclusions, which also covers anything already walked
            # beneath it from an earlier, unscoped run.
            stopped.append(category_id)
            continue

        children = api.get("category/children", category_id=category_id).get(
            "categories", []
        )
        rows = []
        for child in children:
            child_id = _int(child.get("id"))
            if child_id is None:
                continue
            parent = _int(child.get("parent_id"))
            rows.append(
                {
                    "category_id": child_id,
                    "category_name": child.get("name") or f"Category {child_id}",
                    # FRED reports 0 for a top-level category; NULL is what makes the
                    # recursive path query terminate.
                    "parent_id": None if parent in (None, ROOT_CATEGORY) else parent,
                }
            )
            queue.append((child_id, depth + 1))

        if rows:
            statement = pg_insert(categories).values(rows)
            statement = statement.on_conflict_do_update(
                index_elements=["category_id"],
                set_={
                    "category_name": statement.excluded.category_name,
                    "parent_id": statement.excluded.parent_id,
                },
            )
            with engine.begin() as connection:
                connection.execute(statement)
            written += len(rows)

        if len(seen) % 100 == 0:
            logger.info(f"FRED tree walk: {len(seen)} categories visited")

    logger.info(
        f"FRED tree walk complete: {written} categories written, "
        f"{len(stopped)} excluded subtrees not descended into"
    )
    return {"visited": len(seen), "written": written, "excluded_roots": len(stopped)}


def mark_exclusions(engine: Engine, excluded: dict[int, str] | None = None) -> dict[str, int]:
    """
    Stamp `excluded_reason` on each excluded subtree.

    Applied to descendants too, because an earlier unscoped walk already wrote 4,160
    regional categories. Those are kept -- they cost nothing, they record that the
    branch exists, and keeping them means a later decision to include regional data is
    a fetch rather than another hour of walking.

    A descendant that already holds series is left unmarked: `Census Regions`, `BEA
    Regions` and `BLS Regions` came through the original export with data, so calling
    them excluded would contradict the rows sitting under them.
    """
    excluded = VOLUME_EXCLUDED if excluded is None else excluded
    marked = 0
    with engine.begin() as connection:
        for root_id, reason in excluded.items():
            marked += connection.execute(
                text(
                    """
                    WITH RECURSIVE subtree AS (
                        SELECT category_id, 1 AS depth FROM fred_category
                         WHERE category_id = :root
                        UNION ALL
                        SELECT child.category_id, subtree.depth + 1
                          FROM fred_category AS child
                          JOIN subtree ON child.parent_id = subtree.category_id
                         WHERE subtree.depth < :max_depth
                    )
                    UPDATE fred_category AS target
                       SET excluded_reason = :reason
                     WHERE target.category_id IN (SELECT category_id FROM subtree)
                       AND NOT EXISTS (
                           SELECT 1 FROM fred_series_category sc
                            WHERE sc.category_id = target.category_id
                       )
                       AND target.excluded_reason IS DISTINCT FROM :reason
                    """
                ),
                {"root": root_id, "reason": reason, "max_depth": MAX_DEPTH},
            ).rowcount
    if marked:
        logger.info(f"marked {marked} categories as deliberately excluded")
    return {"marked": marked}


def rebuild_paths(engine: Engine) -> dict[str, int]:
    """
    Derive `category_path` from `parent_id`.

    The path is a convenience for display and prefix search; `parent_id` is the truth.
    Deriving it means the two cannot disagree, which they did before.

    Reports categories that no path reaches. Those are rows FRED's tree does not
    contain -- left over from the YAML export, which fetched subtrees by id. They are
    *not* pruned here: deleting catalogue rows on the strength of one walk is how a
    transient failure becomes data loss.
    """
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                WITH RECURSIVE tree AS (
                    SELECT category_id, category_name::text AS path, 1 AS depth
                      FROM fred_category
                     WHERE parent_id IS NULL
                    UNION ALL
                    SELECT child.category_id,
                           tree.path || ' > ' || child.category_name,
                           tree.depth + 1
                      FROM fred_category AS child
                      JOIN tree ON child.parent_id = tree.category_id
                     WHERE tree.depth < :max_depth
                )
                UPDATE fred_category AS target
                   SET category_path = tree.path
                  FROM tree
                 WHERE target.category_id = tree.category_id
                   AND target.category_path IS DISTINCT FROM tree.path
                """
            ),
            {"max_depth": MAX_DEPTH},
        )

    with engine.connect() as connection:
        total = connection.execute(
            text("SELECT count(*) FROM fred_category")
        ).scalar_one()
        unreachable = connection.execute(
            text(
                """
                WITH RECURSIVE tree AS (
                    SELECT category_id, 1 AS depth FROM fred_category
                     WHERE parent_id IS NULL
                    UNION ALL
                    SELECT child.category_id, tree.depth + 1
                      FROM fred_category AS child
                      JOIN tree ON child.parent_id = tree.category_id
                     WHERE tree.depth < :max_depth
                )
                SELECT count(*) FROM fred_category
                 WHERE category_id NOT IN (SELECT category_id FROM tree)
                """
            ),
            {"max_depth": MAX_DEPTH},
        ).scalar_one()

    if unreachable:
        logger.warning(
            f"{unreachable} of {total} FRED categories are not reachable from the root; "
            f"their category_path is stale. Left in place deliberately -- see "
            f"rebuild_paths docstring."
        )
    return {"categories": total, "unreachable": unreachable}


# --------------------------------------------------------------------------- series


def _series_row(raw: dict) -> dict:
    frequency = raw.get("frequency")
    return {
        "series_id": str(raw["id"]),
        "series_title": raw.get("title") or "Unknown Series",
        "units": raw.get("units"),
        "frequency": frequency,
        "frequency_class": frequency_class(frequency),
        "seasonal_adjustment": raw.get("seasonal_adjustment"),
        "observation_start": _date(raw.get("observation_start")),
        "observation_end": _date(raw.get("observation_end")),
        "last_updated": _timestamp(raw.get("last_updated")),
        "popularity": _int(raw.get("popularity")),
        "notes": raw.get("notes"),
        # Recomputed for the whole table once the fetch is complete; a per-class cutoff
        # cannot be known from one category's worth of series.
        "currently_relevant": False,
    }


def iter_category_series(
    api: FredApi, category_id: int, page_limit: int | None = None
) -> Iterator[tuple[list[dict], int]]:
    """
    Yield `(page_of_series, api_count)` until the reported count is covered.

    Pagination is the whole fix. `offset` advances by the page FRED actually returned,
    not by `PAGE`, so a short page cannot cause an infinite loop or a skipped window.

    `page_limit` stops early on purpose. It is the mechanism behind the country cap, and
    the caller records it so the short result is attributable.
    """
    offset = 0
    pages = 0
    while True:
        payload = api.get(
            "category/series", category_id=category_id, limit=PAGE, offset=offset
        )
        count = _int(payload.get("count")) or 0
        page = payload.get("seriess") or []
        yield page, count
        if not page:
            return
        pages += 1
        if page_limit is not None and pages >= page_limit:
            return
        offset += len(page)
        if offset >= count:
            return


def fetch_category(
    engine: Engine, api: FredApi, category_id: int, page_limit: int | None = None
) -> dict[str, Any]:
    """
    Fetch the pages for one category, write series and memberships, record the scan.

    The scan row is written even when the fetch raises, because the failure is the thing
    worth keeping: an absent row is indistinguishable from a category nobody tried.

    `status` answers "did we write what we asked for", not "did we write everything FRED
    has". With a `page_limit` those differ on purpose, and conflating them would make
    every capped country look broken and be retried on every resume.
    """
    series_table = _table(engine, "fred_series")
    membership = _table(engine, "fred_series_category")
    scan = _table(engine, "fred_category_scan")

    started = _now()
    _record_scan(
        engine, scan, category_id, status="pending", started_at=started,
        page_limit=page_limit,
    )

    fetched: set[str] = set()
    api_count = 0
    pages = 0
    try:
        for page, count in iter_category_series(api, category_id, page_limit):
            api_count = count
            if not page:
                break
            pages += 1
            rows = [_series_row(raw) for raw in page if raw.get("id")]
            if not rows:
                continue
            with engine.begin() as connection:
                statement = pg_insert(series_table).values(rows)
                connection.execute(
                    statement.on_conflict_do_update(
                        index_elements=["series_id"],
                        set_={
                            column: statement.excluded[column]
                            for column in (
                                "series_title", "units", "frequency", "frequency_class",
                                "seasonal_adjustment", "observation_start",
                                "observation_end", "last_updated", "popularity", "notes",
                            )
                        },
                    )
                )
                link = pg_insert(membership).values(
                    [
                        {"series_id": row["series_id"], "category_id": category_id}
                        for row in rows
                    ]
                )
                connection.execute(link.on_conflict_do_nothing())
            fetched.update(row["series_id"] for row in rows)
    except Exception as error:  # noqa: BLE001 -- recorded, then re-raised by the caller
        _record_scan(
            engine, scan, category_id, status="error", started_at=started,
            finished_at=_now(), api_series_count=api_count or None,
            fetched_series_count=len(fetched), pages=pages, error=str(error)[:2000],
            page_limit=page_limit,
        )
        raise

    # The reconciliation this whole module exists for. `requested` is what we set out to
    # write: everything FRED has, unless a cap says otherwise.
    requested = api_count if page_limit is None else min(api_count, page_limit * PAGE)
    status = "ok" if len(fetched) >= requested else "incomplete"
    _record_scan(
        engine, scan, category_id, status=status, started_at=started,
        finished_at=_now(), api_series_count=api_count,
        fetched_series_count=len(fetched), pages=pages, error=None,
        page_limit=page_limit,
    )
    if status == "incomplete":
        logger.warning(
            f"category {category_id}: asked for {requested} series, wrote "
            f"{len(fetched)} over {pages} pages (FRED reports {api_count})"
        )
    return {
        "category_id": category_id, "api_series_count": api_count,
        "fetched_series_count": len(fetched), "pages": pages, "status": status,
        "page_limit": page_limit, "capped": page_limit is not None and api_count > requested,
    }


def _record_scan(engine: Engine, scan: Table, category_id: int, **fields: Any) -> None:
    values = {"category_id": category_id, **fields}
    statement = pg_insert(scan).values(values)
    with engine.begin() as connection:
        connection.execute(
            statement.on_conflict_do_update(
                index_elements=["category_id"],
                set_={key: statement.excluded[key] for key in fields},
            )
        )


# --------------------------------------------------------------------------- derived


def refresh_derived(engine: Engine) -> dict[str, Any]:
    """
    Recompute `frequency_class` cutoffs and `currently_relevant` across the table.

    Must run after the fetch, never during it: the cutoff for a class is the p95 of its
    observation_end, so it is only correct once every series in that class is present.
    Computing it per category would give each one its own definition of current.
    """
    with engine.connect() as connection:
        rows = connection.execute(
            text(
                "SELECT series_id, frequency_class, observation_end FROM fred_series"
            )
        ).fetchall()

    series = {
        row[0]: {"frequency_class": row[1] or "other", "observation_end": row[2]}
        for row in rows
    }
    cutoffs = currency_cutoffs(series)

    classes = _table(engine, "fred_frequency_class")
    built = _now()
    with engine.begin() as connection:
        for klass in cutoffs.values():
            payload = {**klass, "built_at": built}
            statement = pg_insert(classes).values(payload)
            connection.execute(
                statement.on_conflict_do_update(
                    index_elements=["frequency_class"],
                    set_={
                        key: statement.excluded[key]
                        for key in payload
                        if key != "frequency_class"
                    },
                )
            )
        # One statement, so no series is briefly current under the old rule and stale
        # under the new one.
        updated = connection.execute(
            text(
                """
                UPDATE fred_series AS s
                   SET currently_relevant = (
                           c.currency_cutoff IS NOT NULL
                           AND s.observation_end >= c.currency_cutoff
                       )
                  FROM fred_frequency_class AS c
                 WHERE c.frequency_class = s.frequency_class
                """
            )
        ).rowcount

    relevant = 0
    with engine.connect() as connection:
        relevant = connection.execute(
            text("SELECT count(*) FROM fred_series WHERE currently_relevant")
        ).scalar_one()
    return {
        "classes": len(cutoffs),
        "series_updated": updated,
        "currently_relevant": relevant,
        "period_days_known": len(PERIOD_DAYS),
    }


# --------------------------------------------------------------------------- run


def pending_categories(engine: Engine) -> list[tuple[int, int | None]]:
    """
    Categories still needing a fetch, as `(category_id, page_limit)`.

    Excluded by two things: a scan already `ok`, and an `excluded_reason`. The second is
    why the exclusion lives in the table -- the fetch loop reads the decision instead of
    hard-coding it, so changing `VOLUME_EXCLUDED` and re-marking is the whole change.
    """
    with engine.connect() as connection:
        return [
            (row[0], page_limit_for(row[1]))
            for row in connection.execute(
                text(
                    """
                    SELECT c.category_id, c.category_path
                      FROM fred_category AS c
                      LEFT JOIN fred_category_scan AS s USING (category_id)
                     WHERE s.status IS DISTINCT FROM 'ok'
                       AND c.excluded_reason IS NULL
                     ORDER BY c.category_id
                    """
                )
            )
        ]


def discover(
    url: str | None = None,
    api: FredApi | None = None,
    walk: bool = True,
    limit: int | None = None,
) -> dict[str, Any]:
    """
    Walk the tree, then fetch every category that is not already complete.

    `limit` caps how many categories are fetched in this call, so the first run can be
    proved on a handful before committing to ~1,100 requests.
    """
    engine = _engine(url)
    api = api or FredApi()
    result: dict[str, Any] = {}

    if walk:
        result["tree"] = walk_categories(engine, api)
        # Paths before exclusions: marking matches on the subtree, and the path is what
        # page_limit_for reads to decide the country cap.
        result["paths"] = rebuild_paths(engine)
    result["excluded"] = mark_exclusions(engine)

    pending = pending_categories(engine)
    if limit is not None:
        pending = pending[:limit]
    logger.info(f"FRED discovery: {len(pending)} categories to fetch")

    done, incomplete, failed, capped = 0, 0, 0, 0
    for index, (category_id, page_limit) in enumerate(pending, 1):
        try:
            outcome = fetch_category(engine, api, category_id, page_limit)
        except FredApiError:
            raise                      # key or protocol failure: stop, do not grind on
        except Exception as error:     # noqa: BLE001
            failed += 1
            logger.warning(f"category {category_id} failed: {error}")
            continue
        done += 1
        incomplete += outcome["status"] == "incomplete"
        capped += bool(outcome["capped"])
        if index % 25 == 0:
            logger.info(
                f"FRED discovery: {index}/{len(pending)} categories, "
                f"{api.requests} requests"
            )

    result["fetch"] = {
        "attempted": len(pending), "completed": done, "incomplete": incomplete,
        "capped": capped, "failed": failed, "requests": api.requests,
    }
    if done:
        result["derived"] = refresh_derived(engine)
    return result
