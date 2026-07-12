"""Unit tests for the metadata JSONB filter translator.

metadata_where turns a Chroma-style where-dict (as emitted by the document-search
filter extractors) into a SQLAlchemy condition over a source-keyed JSONB column.
We compile the returned expression to a Postgres dialect string + bind params and
assert on those, so no database connection is needed.
"""

import pytest
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import JSONB

from apps.agentic.db.metadata_filter import _flatten, metadata_where

_COL = Table("r", MetaData(), Column("metadata", JSONB)).c.metadata


def _compile(source, where):
    """Return (sql_string, params) for a metadata_where clause, or (None, None)."""
    clause = metadata_where(_COL, source, where)
    if clause is None:
        return None, None
    compiled = clause.compile(dialect=postgresql.dialect())
    return str(compiled), dict(compiled.params)


# ---------- _flatten ----------

def test_flatten_flat_dict():
    assert _flatten({"family": "X", "category": "Y"}) == [("family", "X"), ("category", "Y")]


def test_flatten_unwraps_and():
    assert _flatten({"$and": [{"a": 1}, {"b": 2}]}) == [("a", 1), ("b", 2)]


def test_flatten_nested_and():
    assert _flatten({"$and": [{"a": 1}, {"$and": [{"b": 2}, {"c": 3}]}]}) == [
        ("a", 1), ("b", 2), ("c", 3),
    ]


def test_flatten_skips_or_and_operators():
    assert _flatten({"$or": [{"a": 1}]}) == []


def test_flatten_empty_and_none():
    assert _flatten(None) == []
    assert _flatten({}) == []


# ---------- metadata_where: catalog string fields ----------

def test_exact_match_uses_has_key():
    sql, params = _compile("tiingo", {"family": "VanEck Asset Management"})
    assert ") ? " in sql          # JSONB has_key operator, not has_any
    assert "?|" not in sql
    assert "VanEck Asset Management" in params.values()
    assert "tiingo" in params.values() and "family" in params.values()


def test_in_match_uses_has_any():
    sql, params = _compile("tiingo", {"category": {"$in": ["Government Bonds", "High Yield Bonds"]}})
    assert "?|" in sql            # has_any
    assert "ARRAY[" in sql
    assert "Government Bonds" in params.values()
    assert "High Yield Bonds" in params.values()


def test_empty_in_list_produces_no_clause():
    clause = metadata_where(_COL, "tiingo", {"category": {"$in": []}})
    assert clause is None


# ---------- metadata_where: numeric range fields ----------

def test_range_uses_jsonb_path_exists():
    sql, params = _compile("fred", {"observation_end_int": {"$gte": 20250101}})
    assert "jsonb_path_exists" in sql
    path = next(v for v in params.values() if isinstance(v, str) and "observation_end_int" in v)
    assert "@ >= 20250101" in path


@pytest.mark.parametrize("op,sqlop", [("$gte", ">="), ("$lte", "<="), ("$gt", ">"), ("$lt", "<")])
def test_range_operator_mapping(op, sqlop):
    _, params = _compile("fred", {"observation_start_int": {op: 20200101}})
    path = next(v for v in params.values() if isinstance(v, str) and "observation_start_int" in v)
    assert f"@ {sqlop} 20200101" in path


# ---------- metadata_where: composition + no-op cases ----------

def test_and_produces_two_conjoined_clauses():
    sql, params = _compile(
        "tiingo",
        {"$and": [{"family": "VanEck Asset Management"}, {"category_group": "Fixed Income"}]},
    )
    assert " AND " in sql
    assert sql.count(") ? ") == 2
    assert "VanEck Asset Management" in params.values()
    assert "Fixed Income" in params.values()


def test_empty_where_returns_none():
    assert metadata_where(_COL, "tiingo", {}) is None
    assert metadata_where(_COL, "tiingo", None) is None


def test_unknown_field_ignored_returns_none():
    assert metadata_where(_COL, "tiingo", {"bogus": "x"}) is None


def test_field_not_in_source_vocab_ignored():
    # 'frequency' is a fred field; under tiingo it is neither catalog nor range → ignored.
    assert metadata_where(_COL, "tiingo", {"frequency": "Monthly"}) is None


def test_source_case_insensitive():
    assert metadata_where(_COL, "TIINGO", {"family": "VanEck Asset Management"}) is not None
