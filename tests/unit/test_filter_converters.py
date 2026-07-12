"""Unit tests for the pure filter-object -> Chroma where-dict converters.

These operate on already-parsed ETFFilters / FredFilters objects, so no LLM is
involved — we construct the filter objects directly and assert the where-dict.
"""

from apps.agentic.core.agents.llm_filter_extractor import (
    ETFFilters,
    FredFilters,
    etf_filters_to_where,
    fred_filters_to_where,
)


def _etf(**kw):
    kw.setdefault("cleaned_query", "q")
    return ETFFilters(**kw)


def _fred(**kw):
    kw.setdefault("cleaned_query", "q")
    return FredFilters(**kw)


# ---------- etf_filters_to_where ----------

def test_etf_single_field_single_value():
    where = etf_filters_to_where(_etf(family=["VanEck Asset Management"]))
    assert where == {"family": "VanEck Asset Management"}


def test_etf_single_field_multi_value_is_in():
    where = etf_filters_to_where(_etf(category=["Government Bonds", "High Yield Bonds"]))
    assert where == {"category": {"$in": ["Government Bonds", "High Yield Bonds"]}}


def test_etf_multiple_fields_are_anded():
    where = etf_filters_to_where(_etf(family=["VanEck Asset Management"], category_group=["Fixed Income"]))
    assert where == {"$and": [{"family": "VanEck Asset Management"}, {"category_group": "Fixed Income"}]}


def test_etf_no_fields_returns_none():
    assert etf_filters_to_where(_etf()) is None


def test_etf_empty_list_treated_as_absent():
    assert etf_filters_to_where(_etf(family=[])) is None


# ---------- fred_filters_to_where ----------

def test_fred_frequency():
    assert fred_filters_to_where(_fred(frequency="Monthly")) == {"frequency": "Monthly"}


def test_fred_category_and_seasonal():
    where = fred_filters_to_where(_fred(category_name="Interest Rates", seasonal_adjustment="Seasonally Adjusted"))
    assert where == {"category_name": "Interest Rates", "seasonal_adjustment": "Seasonally Adjusted"}


def test_fred_observation_end_defaults_to_gte():
    # Missing operator defaults to $gte, and the ISO date becomes a YYYYMMDD int.
    where = fred_filters_to_where(_fred(observation_end="2025-01-01"))
    assert where == {"observation_end_int": {"$gte": 20250101}}


def test_fred_observation_end_explicit_lte():
    where = fred_filters_to_where(_fred(observation_end="2020-06-30", observation_end_op="$lte"))
    assert where == {"observation_end_int": {"$lte": 20200630}}


def test_fred_popularity_requires_op_and_value():
    assert fred_filters_to_where(_fred(popularity_op="$gte", popularity_value=50)) == {
        "popularity": {"$gte": 50}
    }
    # op without value contributes nothing
    assert fred_filters_to_where(_fred(popularity_op="$gte")) is None


def test_fred_no_fields_returns_none():
    assert fred_filters_to_where(_fred()) is None
