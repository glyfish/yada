"""Unit tests for the ISO-date -> YYYYMMDD int helper used when stamping cache metadata."""

import pytest

from apps.agentic.db.series_cache import _date_to_int


@pytest.mark.parametrize("value,expected", [
    ("2026-07-10", 20260710),
    ("1947-01-01", 19470101),
    ("2026-07-10T00:00:00", 20260710),   # matches the ISO prefix
    ("  2026-07-10", 20260710),          # leading whitespace tolerated
])
def test_valid_dates(value, expected):
    assert _date_to_int(value) == expected


@pytest.mark.parametrize("value", [
    None,
    "",
    "20260710",       # no separators -> no match
    "2026/07/10",     # wrong separator
    "not-a-date",
    "26-07-10",       # two-digit year
])
def test_invalid_returns_none(value):
    assert _date_to_int(value) is None


def test_non_string_returns_none():
    assert _date_to_int(20260710) is None
    assert _date_to_int(["2026-07-10"]) is None
