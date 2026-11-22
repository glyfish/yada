"""
The two FRED catalogue tools: search and describe, over Postgres.

Same two verbs as the document stores, and deliberately so -- but nothing underneath is
shared. ``search_code`` embeds a query and ranks by cosine distance in Chroma. This ranks
by FRED's own popularity score in SQL, because that is what the data has and it is better
than anything a similarity score would produce: asked for the most popular housing series
it returns Housing Starts, Permits and Median Sales Price, while the 2,128-per-leaf metro
listing series that dominate the category by count sink out of sight on their own.

Why no embeddings, for now
--------------------------
There are none to use: the subcategory build embedded all 854,318 titles, clustered, and
kept only the 58,227 node centroids. Full-text matching is therefore literal -- "jobless"
scores zero against 29,927 series titled "Unemployment ...". That gap is closed in the
tool DESCRIPTION rather than in the retrieval, by telling the model to prefer FRED's own
name for a measure, because the client is itself an LLM and already knows that inflation
is measured by the CPI. If that proves insufficient the centroids are the next step; they
are a coarse index over the series, which is what makes them worth keeping.

Why a category filter means the subtree
---------------------------------------
Measured: `category_id = 97` ("Housing") alone misses MSPUS, HOUST, ASPUS and PERMIT,
because those sit in CHILD categories. 177 categories hold series *and* have children, so
"the category" and "everything under the category" are routinely different sets and only
the second is ever what was meant.

See sefer/planning/yada-document-mcp-design.md 2.1a for the naming, and
sefer/planning/yada-todo.md for why search over this catalogue is yada's rather than
meida's.
"""

from __future__ import annotations

import logging
from contextvars import ContextVar
from time import perf_counter
from typing import Any, Callable

import sqlalchemy as sa
from sqlalchemy.engine import Engine

from apps.core.environment import db_url
from mcp_server.fred_models import (
    FredCategories, FredCategory, FredHits, FredSeries,
)

from lib.logger import get_logger

logger = get_logger("YADA")

#: How many categories describe_fred returns before truncating.
DESCRIBE_LIMIT = 25

#: Normalised frequency values, published in the tool description. Small and closed, so
#: they are embedded rather than pointed at -- unlike the 46 raw `frequency` spellings.
FREQUENCY_CLASSES = ("annual", "monthly", "quarterly", "daily",
                     "weekly", "semiannual", "biweekly", "other")

_engine: Engine | None = None
_current_tool: ContextVar[str | None] = ContextVar("fred_current_tool", default=None)


def _conn():
    global _engine
    if _engine is None:
        _engine = sa.create_engine(db_url(), pool_pre_ping=True)
    return _engine.connect()


class _EndpointFilter(logging.Filter):
    """Prefix records logged during a tool call with the endpoint name."""

    def filter(self, record: logging.LogRecord) -> bool:
        tool = _current_tool.get()
        if tool and not getattr(record, "_endpoint_tagged", False):
            record.msg = f"[{tool}] {record.msg}"
            record._endpoint_tagged = True
        return True


def _tool_call(tool: str, arguments: dict, run: Callable[[], Any]) -> Any:
    """Run one tool call, logging what was asked and what came back.

    Local rather than imported from document_tools: that one reads `filters_resolved`,
    `hits` and `chunks`, none of which exist here.
    """
    shown = " ".join(f"{k}={v!r}" for k, v in arguments.items() if v is not None)
    logger.info(f"{tool} <- {shown or '(no arguments)'}")

    token = _current_tool.set(tool)
    started = perf_counter()
    try:
        result = run()
    finally:
        _current_tool.reset(token)

    parts = [f"{tool} -> {result.status} in {perf_counter() - started:.2f}s"]
    if result.filters_applied:
        parts.append(f"applied={result.filters_applied}")
    rows = getattr(result, "series", None)
    if rows is None:
        rows = getattr(result, "categories", [])
    parts.append(f"{len(rows)} of {result.total:,}")
    if result.detail:
        parts.append(result.detail)
    logger.info(" | ".join(parts))
    return result


# ------------------------------------------------------------------ category resolution

#: Every resolution step, tried in order. A category is named three ways in practice --
#: by its own name ("Housing"), by its full path, or by a fragment of one -- and the model
#: picks whichever the previous reply showed it.
_RESOLVERS = (
    ("exact name", "lower(category_name) = lower(:v)"),
    ("exact path", "lower(category_path) = lower(:v)"),
    ("path contains", "category_path ILIKE '%' || :v || '%'"),
)


def _resolve_category(conn, proposed: str) -> tuple[list[int], str, list[FredCategory]]:
    """
    Resolve a category string to ids.

    Returns (ids, how, candidates). `ids` is empty when nothing matched or when several
    did -- ambiguity is REPORTED, never resolved by picking. "Housing" names four
    categories, one of which is housing inflation under Prices > CPI with 51 series and
    another of which is housing activity with 53,187. Choosing the larger is right for
    "housing starts" and wrong for "housing prices", and the tool cannot tell which was
    meant, so it hands the choice back with the counts attached.
    """
    if proposed.strip().isdigit():
        cid = int(proposed.strip())
        found = conn.execute(sa.text(
            "SELECT category_id FROM fred_category WHERE category_id = :i"), {"i": cid}).all()
        return ([cid], "category_id", []) if found else ([], "no match", [])

    for how, clause in _RESOLVERS:
        rows = conn.execute(sa.text(
            f"SELECT category_id FROM fred_category WHERE {clause} ORDER BY category_id"
        ), {"v": proposed}).all()
        if len(rows) == 1:
            return [rows[0][0]], how, []
        if len(rows) > 1:
            return [], f"{how}, {len(rows)} matches", _categories_for(
                conn, [r[0] for r in rows], limit=DESCRIBE_LIMIT)
    return [], "no match", []


def _subtree_ids(conn, ids: list[int]) -> list[int]:
    """Every category at or beneath `ids`. See the module docstring for why."""
    rows = conn.execute(sa.text("""
        WITH RECURSIVE sub AS (
            SELECT category_id FROM fred_category WHERE category_id = ANY(:ids)
          UNION
            SELECT c.category_id FROM fred_category c JOIN sub ON c.parent_id = sub.category_id
        ) SELECT category_id FROM sub"""), {"ids": ids}).all()
    return [r[0] for r in rows]


def _categories_for(conn, ids: list[int], limit: int) -> list[FredCategory]:
    rows = conn.execute(sa.text("""
        SELECT c.category_id, c.category_path,
               (SELECT count(*) FROM fred_category k WHERE k.parent_id = c.category_id),
               (SELECT count(*) FROM fred_series_category s WHERE s.category_id = c.category_id)
          FROM fred_category c
         WHERE c.category_id = ANY(:ids)
         ORDER BY 4 DESC, 2
         LIMIT :lim"""), {"ids": ids, "lim": limit}).all()

    out: list[FredCategory] = []
    for cid, path, kids, here in rows:
        subtree = conn.execute(sa.text("""
            WITH RECURSIVE sub AS (
                SELECT category_id FROM fred_category WHERE category_id = :i
              UNION
                SELECT c.category_id FROM fred_category c JOIN sub ON c.parent_id = sub.category_id)
            SELECT count(DISTINCT s.series_id) FROM fred_series_category s
             WHERE s.category_id IN (SELECT category_id FROM sub)"""), {"i": cid}).scalar()
        out.append(FredCategory(category_id=cid, category_path=path, children=kids,
                                series_here=here, series_in_subtree=subtree or 0))
    return out


# ----------------------------------------------------------------------------- the tools

def _search(query: str | None, category: str | None,
            frequency: str | None, limit: int) -> FredHits:
    requested = {k: v for k, v in
                 (("query", query), ("category", category), ("frequency", frequency))
                 if v}
    shown = " ".join(f"{k}={v!r}" for k, v in requested.items())

    if not query and not category:
        # The one guard document-mcp-design 2.3 insists on, in the form FRED needs. An
        # optional query that silently means "everything" is the failure it names; a
        # category with no query is a real request ("most popular series in Housing").
        # So: either, not neither.
        return FredHits(status="empty_request", request=shown or "(no arguments)", limit=limit,
                        detail="Give query, category, or both. An unqualified call would "
                               "return the catalogue's 10 most popular series, which is "
                               "never what was meant.")

    with _conn() as conn:
        ids: list[int] = []
        applied: dict[str, str] = {}

        if category:
            resolved, how, candidates = _resolve_category(conn, category)
            if candidates:
                return FredHits(
                    status="ambiguous_filter", request=shown, filters_requested=requested,
                    limit=limit, total=len(candidates),
                    available={"category": [c.category_path for c in candidates]},
                    detail=f"'{category}' matches {len(candidates)} categories ({how}); "
                           f"no search was run. Call again with one of the paths in "
                           f"`available`, or describe_fred to compare them.")
            if not resolved:
                roots = [r[0] for r in conn.execute(sa.text(
                    "SELECT category_name FROM fred_category WHERE parent_id IS NULL ORDER BY 1"))]
                return FredHits(
                    status="unresolvable_filter", request=shown, filters_requested=requested,
                    limit=limit, available={"category (top level)": roots},
                    detail=f"No category matches '{category}'; no search was run. "
                           f"Call describe_fred to find the right name.")
            ids = _subtree_ids(conn, resolved)
            applied["category"] = f"{how} -> {len(ids)} categories in subtree"

        if frequency:
            applied["frequency"] = f"frequency_class = {frequency.lower()}"
        if query:
            applied["query"] = "title full-text"

        where = ["TRUE"]
        params: dict[str, Any] = {"lim": limit}
        if ids:
            where.append("sc.category_id = ANY(:ids)")
            params["ids"] = ids
        if query:
            where.append("s.title_tsv @@ plainto_tsquery('english', :q)")
            params["q"] = query
        if frequency:
            where.append("s.frequency_class = :f")
            params["f"] = frequency.lower()
        clause = " AND ".join(where)

        # DISTINCT ON collapses the many-to-many: a series in three categories of the
        # searched subtree is one row, keeping its shallowest path as provenance.
        base = f"""
            SELECT DISTINCT ON (s.series_id)
                   s.series_id, s.series_title, s.frequency, s.frequency_class, s.units,
                   s.observation_start, s.observation_end, s.seasonal_adjustment,
                   s.popularity, s.currently_relevant, c.category_path
              FROM fred_series s
              JOIN fred_series_category sc USING (series_id)
              JOIN fred_category c ON c.category_id = sc.category_id
             WHERE {clause}
             ORDER BY s.series_id, length(c.category_path)"""

        total = conn.execute(sa.text(
            f"SELECT count(*) FROM ({base}) t"), params).scalar() or 0
        rows = conn.execute(sa.text(
            f"SELECT * FROM ({base}) t ORDER BY popularity DESC NULLS LAST, series_id "
            f"LIMIT :lim"), params).all()

    series = [
        FredSeries(
            rank=i, series_id=r[0], title=r[1], frequency=r[2], frequency_class=r[3],
            units=r[4], observation_start=r[5], observation_end=r[6],
            seasonal_adjustment=r[7], popularity=r[8], currently_relevant=r[9],
            category_path=r[10])
        for i, r in enumerate(rows, 1)
    ]
    detail = None
    if total > limit:
        # No silent caps: the top 10 of 53,187 reads exactly like the top 10 of 10.
        detail = (f"Showing the {limit} most popular of {total:,} matches. "
                  f"Narrow with category or frequency, or raise limit.")
    return FredHits(
        status="ok" if series else "no_match", request=shown, filters_requested=requested,
        filters_applied=applied, series=series, total=total, limit=limit,
        detail=detail or (None if series else "Nothing matched. FRED titles use formal "
                          "names -- try the measure's published name, e.g. 'consumer "
                          "price index' rather than 'inflation'."))


def _series_total(conn) -> int:
    return conn.execute(sa.text("SELECT count(*) FROM fred_series")).scalar() or 0


def _describe(category: str | None, limit: int) -> FredCategories:
    shown = f"category={category!r}" if category else "(no arguments)"
    with _conn() as conn:
        total_series = _series_total(conn)
        if not category:
            ids = [r[0] for r in conn.execute(sa.text(
                "SELECT category_id FROM fred_category WHERE parent_id IS NULL"))]
            cats = _categories_for(conn, ids, limit)
            return FredCategories(
                status="ok", request=shown, categories=cats, total=len(ids), limit=limit,
                series_total=total_series,
                detail=f"The {len(ids)} top-level categories, of {total_series:,} series "
                       f"in the catalogue. Do not add series_in_subtree across rows -- "
                       f"subtrees overlap and the sum overcounts by about 11%.")

        resolved, how, candidates = _resolve_category(conn, category)
        if candidates:
            return FredCategories(
                status="ok", request=shown, categories=candidates, limit=limit,
                total=len(candidates), filters_applied={"category": how},
                series_total=total_series,
                detail=f"'{category}' matches {len(candidates)} categories. Use the "
                       f"category_path of the one you want.")
        if not resolved:
            roots = [r[0] for r in conn.execute(sa.text(
                "SELECT category_name FROM fred_category WHERE parent_id IS NULL ORDER BY 1"))]
            return FredCategories(
                status="unresolvable_filter", request=shown, limit=limit,
                series_total=total_series,
                available={"category (top level)": roots},
                detail=f"No category matches '{category}'.")

        kids = [r[0] for r in conn.execute(sa.text(
            "SELECT category_id FROM fred_category WHERE parent_id = ANY(:ids)"),
            {"ids": resolved}).all()]
        shown_ids = kids or resolved
        cats = _categories_for(conn, shown_ids, limit)
        note = (f"{len(kids)} categories beneath '{category}'."
                if kids else f"'{category}' has no child categories.")
        return FredCategories(status="ok", request=shown, categories=cats,
                              total=len(shown_ids), limit=limit, series_total=total_series,
                              filters_applied={"category": how}, detail=note)


# ----------------------------------------------------------- generated descriptions

def _counts() -> str:
    """Live counts for the description. Generated, never written: a hand-kept figure is
    wrong the first time the catalogue is rebuilt, and wrong silently."""
    try:
        with _conn() as conn:
            series = conn.execute(sa.text("SELECT count(*) FROM fred_series")).scalar()
            cats = conn.execute(sa.text("SELECT count(*) FROM fred_category")).scalar()
        return f"{series:,} series in {cats:,} categories"
    except Exception as exc:
        logger.warning(f"fred_tools: could not read catalogue counts: {exc}")
        return "the FRED catalogue"


def _roots() -> list[str]:
    """The top-level category names, as a LIST.

    Returned unjoined because three of the eight contain commas -- "Money, Banking, &
    Finance" -- so a comma-joined string both miscounts when split and reads as three
    categories to whoever receives it. They are quoted individually in the description.
    """
    try:
        with _conn() as conn:
            return [r[0] for r in conn.execute(sa.text(
                "SELECT category_name FROM fred_category WHERE parent_id IS NULL ORDER BY 1"))]
    except Exception as exc:
        logger.warning(f"fred_tools: could not read top-level categories: {exc}")
        return []


def register(server) -> None:
    """
    Register search_fred and describe_fred.

    add_tool rather than the decorator, for the same reason document_tools gives: the
    descriptions carry live counts and the real top-level category names, and a decorator
    takes a literal.
    """
    if not any(isinstance(f, _EndpointFilter) for f in logger.filters):
        logger.addFilter(_EndpointFilter())

    def search_fred(query: str | None = None, category: str | None = None,
                    frequency: str | None = None, limit: int = 10) -> FredHits:
        return _tool_call("search_fred",
                          {"query": query, "category": category,
                           "frequency": frequency, "limit": limit},
                          lambda: _search(query, category, frequency, limit))

    def describe_fred(category: str | None = None,
                      limit: int = DESCRIBE_LIMIT) -> FredCategories:
        return _tool_call("describe_fred", {"category": category, "limit": limit},
                          lambda: _describe(category, limit))

    roots = _roots()
    root_line = (f" The {len(roots)} top-level categories are "
                 + ", ".join(f"'{r}'" for r in roots) + ".") if roots else ""

    server.add_tool(
        search_fred, name="search_fred",
        description=(
            f"Search the FRED catalogue of US and international economic time series "
            f"({_counts()}) and return ranked series with the metadata needed to choose "
            f"one. Returns descriptions only — use fred_series_observations to fetch the "
            f"data once a series_id is chosen.\n"
            "- query: what to look for, matched against series titles. FRED titles use "
            "formal published names, so prefer the measure's real name over the "
            "colloquial one — 'consumer price index' rather than 'inflation', "
            "'unemployment rate' rather than 'jobless claims'. Matching is literal: a "
            "word that does not appear in the title does not match.\n"
            "- category: a category name or path as describe_fred reports it. Includes "
            "everything beneath it, which is usually what is meant — the most popular "
            "housing series sit in children of 'Housing', not on it."
            f"{root_line} A name matching several categories is reported with the "
            "candidates and no search is run; 'Housing' is four different categories, "
            "one of them housing inflation.\n"
            f"- frequency: one of {', '.join(FREQUENCY_CLASSES)}.\n"
            "- limit: how many series to return (default 10).\n"
            "Ranked by FRED's own popularity score, highest first, which surfaces the "
            "headline series ahead of the thousands of metro-level variants. Give query, "
            "category, or both — neither is an error. Discontinued series are included; "
            "`currently_relevant` says which, and popularity already ranks them low."),
    )

    server.add_tool(
        describe_fred, name="describe_fred",
        description=(
            "What the FRED catalogue contains: categories, their paths, and how many "
            "series sit in each. No series titles, no observations.\n"
            "- category: omit to list the top-level categories; give one to list what is "
            "directly beneath it. A name matching several returns all of them with their "
            "counts, which is how an ambiguous name is resolved before searching.\n"
            "`series_here` counts series attached to that category itself and "
            "`series_in_subtree` counts everything beneath it. The two differ sharply and "
            "both matter: 177 categories hold series AND have children, so a category is "
            "often both a folder and a file.\n"
            "Do NOT sum series_in_subtree across rows to get a catalogue total. Subtrees "
            "overlap — a Pennsylvania housing series is filed under both Housing and "
            "U.S. Regional Data — so the sum overcounts by about 11%. The true total is "
            "published as `series_total`. Call this before search_fred whenever a "
            "category name is uncertain."),
    )

    logger.info("FRED tools registered: search_fred, describe_fred")
