from __future__ import annotations

from apps.agentic.core.document_loaders.etf.finance_database_loader import FinanceDatabaseLoader
from apps.agentic.core.document_loaders.fred_document_loader import FREDChromaDocumentLoader
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
    "fred": {
        "loader": FREDChromaDocumentLoader,
        "key": "series_id",
        "fields": ("category_name", "category_path", "seasonal_adjustment", "frequency"),
    },
}

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
