from __future__ import annotations

from sqlalchemy import and_, cast, func
from sqlalchemy.dialects.postgresql import JSONB, array

# Catalog string fields stored per source in the metadata JSONB (must match
# series_metadata._CATALOG). Filtered by list containment.
_CATALOG_FIELDS = {
    "tiingo": {"family", "category_group", "category", "exchange"},
    "fred": {"category_name", "category_path", "seasonal_adjustment", "frequency"},
}

# Numeric YYYYMMDD fields recorded in the metadata at fetch (any source); filtered by
# range against the stored (current) observation dates — one consistent source of truth.
_RANGE_FIELDS = {"observation_start_int", "observation_end_int"}
_RANGE_OPS = {"$gte": ">=", "$lte": "<=", "$gt": ">", "$lt": "<"}


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
        if field in fields:
            # Catalog string field: list containment (? for exact, ?| for $in).
            arr = cast(metadata_col[source][field], JSONB)
            if isinstance(spec, dict):
                values = [str(v) for v in (spec.get("$in") or [])]
                if values:
                    clauses.append(arr.has_any(array(values)))
            elif spec is not None:
                clauses.append(arr.has_key(str(spec)))
        elif field in _RANGE_FIELDS and isinstance(spec, dict):
            # Numeric int array: any stored value satisfies the comparison. The int
            # values are safe to inline (from _iso_to_yyyymmdd); the field is fixed.
            for op, sqlop in _RANGE_OPS.items():
                if op in spec:
                    val = int(spec[op])
                    path = f'$."{field}"[*] ? (@ {sqlop} {val})'
                    clauses.append(func.jsonb_path_exists(cast(metadata_col[source], JSONB), path))
    return and_(*clauses) if clauses else None
