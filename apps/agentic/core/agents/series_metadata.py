from __future__ import annotations

import sqlalchemy as sa

from apps.agentic.core.document_loaders.etf.finance_database_loader import FinanceDatabaseLoader
from apps.core.environment import db_url
from lib.logger import get_logger

logger = get_logger("YADA")

# Per cache source: the catalog document store, the metadata key to match a series by,
# and the catalog fields to lift into the series' metadata. These are the same fields
# the document-search filter extractors (extract_etf_filters / extract_fred_filters)
# filter on, so a cached series can be filtered by reusing those extractors.
_CATALOG = {
    "tiingo": {
        "loader": FinanceDatabaseLoader,
        "key": "ticker",
        "fields": ("family", "category_group", "category", "exchange"),
    },
}

#: FRED is read from Postgres, not from a document store. It used to go through
#: FREDChromaDocumentLoader, which is built from the YAML dump in clients/fred/ --
#: meida's superseded catalogue, which deliberately skipped States, Federal Reserve
#: Districts and Freddie Mac Regions. Measured over a 120-series sample before this
#: changed: 42% of non-regional series enriched, 0% of regional ones, 15% overall. The
#: other 85% got {}, which is a legal return, so nothing ever reported it.
_FRED_FIELDS = ("category_name", "category_path", "seasonal_adjustment", "frequency")

_engine = None


def _fred_engine():
    global _engine
    if _engine is None:
        _engine = sa.create_engine(db_url(), pool_pre_ping=True)
    return _engine


def _fred_catalog(series_id: str) -> dict:
    """The shallowest category a series belongs to, plus its own frequency and adjustment.

    Shallowest because a series sits in every category it belongs to and the shortest
    path is the most general -- the same tie-break search_fred uses for provenance.
    """
    with _fred_engine().connect() as conn:
        row = conn.execute(sa.text("""
            SELECT c.category_name, c.category_path,
                   s.seasonal_adjustment, s.frequency
              FROM fred_series s
              JOIN fred_series_category sc USING (series_id)
              JOIN fred_category c ON c.category_id = sc.category_id
             WHERE s.series_id = :sid
             ORDER BY length(c.category_path)
             LIMIT 1"""), {"sid": series_id}).fetchone()
    if row is None:
        return {}
    return {f: [str(v)] for f, v in zip(_FRED_FIELDS, row)
            if v not in (None, "", "N/A")}

_loaders: dict = {}


def _loader(source: str):
    if source not in _loaders:
        _loaders[source] = _CATALOG[source]["loader"]()
    return _loaders[source]


def catalog_metadata(source: str, native_id: str) -> dict:
    """
    Look up a series' catalog metadata in the ETF/FRED document store and return it as a
    source-keyed dict of field -> [value] lists, e.g.
        {"tiingo": {"family": ["VanEck"], "category_group": ["Fixed Income"], ...}}

    Single-element lists so it merges uniformly with a report's aggregated metadata
    (see merge_source_metadata). Returns {} when the source is unknown or no catalog row
    matches — enrichment is best-effort.
    """
    source = source.strip().lower()
    if source == "fred":
        try:
            fields = _fred_catalog(native_id)
        except Exception as exc:
            logger.warning(f"catalog_metadata: FRED lookup failed for {native_id}: {exc}")
            return {}
        return {"fred": fields} if fields else {}

    spec = _CATALOG.get(source)
    if spec is None:
        return {}
    try:
        got = _loader(source).vectorstore.get(where={spec["key"]: {"$eq": native_id}})
    except Exception as exc:
        logger.warning(f"catalog_metadata: lookup failed for {source}:{native_id}: {exc}")
        return {}
    metas = got.get("metadatas") or []
    if not metas:
        return {}
    m = metas[0] or {}
    fields = {}
    for f in spec["fields"]:
        v = m.get(f)
        if v not in (None, "", "N/A"):
            fields[f] = [str(v)]
    return {source: fields} if fields else {}


def merge_source_metadata(dicts: list[dict]) -> dict:
    """
    Merge several source-keyed metadata dicts into one, unioning each field's value list
    (deduped, order preserved). Used to aggregate a report's series metadata so the report
    can be filtered by the same source-keyed containment as a single cached series.
    """
    merged: dict = {}
    for d in dicts:
        for source, fields in (d or {}).items():
            dst = merged.setdefault(source, {})
            for field, values in (fields or {}).items():
                bucket = dst.setdefault(field, [])
                for v in values:
                    if v not in bucket:
                        bucket.append(v)
    return merged


def report_metadata_from_series(time_series_info) -> dict:
    """
    Build a report's merged, source-keyed catalog metadata from its series. Each
    time_series_info entry carries the series' cache metadata ({units, observation_count,
    <source>: {catalog fields}}); this lifts each series' source-keyed catalog subset and
    unions them, so a report is filterable by the same containment as a single series.
    """
    parts: list[dict] = []
    for entry in time_series_info or []:
        src = str(entry.get("source") or "").strip().lower()
        md = entry.get("metadata")
        if src and isinstance(md, dict) and isinstance(md.get(src), dict):
            parts.append({src: md[src]})
    return merge_source_metadata(parts)
