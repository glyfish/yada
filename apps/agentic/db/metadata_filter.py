from __future__ import annotations

from sqlalchemy import and_, cast
from sqlalchemy.dialects.postgresql import JSONB, array

# Catalog fields stored per source in the metadata JSONB (must match
# series_metadata._CATALOG). Only these are filtered here — other where-dict keys
# ($gte date ranges, popularity, series_id) are handled elsewhere or ignored.
_CATALOG_FIELDS = {
    "tiingo": {"family", "category_group", "category", "exchange"},
    "fred": {"category_name", "category_path", "seasonal_adjustment", "frequency"},
}


def _flatten(where: dict | None) -> list[tuple[str, object]]:
    """
    Flatten a Chroma-style where-dict (flat, or $and-wrapped by _normalize_chroma_filter)
    into (field, spec) pairs. $or and other top-level operators are skipped.
    """
    if not where:
        return []
    out: list[tuple[str, object]] = []
    if "$and" in where:
        for sub in where["$and"]:
            out.extend(_flatten(sub))
        return out
    for k, v in where.items():
        if not k.startswith("$"):
            out.append((k, v))
    return out


def metadata_where(metadata_col, source: str, where: dict | None):
    """
    Translate a document-search where-dict (from extract_etf_filters / extract_fred_filters)
    into a SQLAlchemy condition over a source-keyed metadata JSONB column, e.g.
        metadata = {"tiingo": {"family": ["VanEck..."], "exchange": ["PCX"]}}

    Catalog values are stored as JSONB lists, so an exact match tests array membership
    (?), and $in tests any-of (?|). The same condition works for a cached series and a
    report (its metadata column is the merged catalog). Returns None when nothing applies.
    """
    source = (source or "").strip().lower()
    fields = _CATALOG_FIELDS.get(source, set())
    clauses = []
    for field, spec in _flatten(where):
        if field not in fields:
            continue
        arr = cast(metadata_col[source][field], JSONB)
        if isinstance(spec, dict):
            values = [str(v) for v in (spec.get("$in") or [])]
            if values:
                clauses.append(arr.has_any(array(values)))
        elif spec is not None:
            clauses.append(arr.has_key(str(spec)))
    return and_(*clauses) if clauses else None
