"""Unit tests for source-keyed catalog metadata merging.

merge_source_metadata unions field value-lists per source; report_metadata_from_series
lifts each series' source-keyed catalog subset and merges them so a report is filterable
by the same containment as a single cached series. Both are pure (no Chroma).
"""

from apps.agentic.core.agents.series_metadata import (
    merge_source_metadata,
    report_metadata_from_series,
)


# ---------- merge_source_metadata ----------

def test_merge_single_dict_passthrough():
    d = {"tiingo": {"family": ["VanEck Asset Management"]}}
    assert merge_source_metadata([d]) == {"tiingo": {"family": ["VanEck Asset Management"]}}


def test_merge_unions_and_dedupes_within_source():
    merged = merge_source_metadata([
        {"tiingo": {"category": ["Corporate Bonds"]}},
        {"tiingo": {"category": ["High Yield Bonds", "Corporate Bonds"]}},
    ])
    assert merged == {"tiingo": {"category": ["Corporate Bonds", "High Yield Bonds"]}}


def test_merge_preserves_first_seen_order():
    merged = merge_source_metadata([
        {"tiingo": {"category": ["B", "A"]}},
        {"tiingo": {"category": ["A", "C"]}},
    ])
    assert merged["tiingo"]["category"] == ["B", "A", "C"]


def test_merge_keeps_sources_separate():
    merged = merge_source_metadata([
        {"tiingo": {"family": ["VanEck Asset Management"]}},
        {"fred": {"frequency": ["Monthly"]}},
    ])
    assert merged == {
        "tiingo": {"family": ["VanEck Asset Management"]},
        "fred": {"frequency": ["Monthly"]},
    }


def test_merge_handles_empty_and_none_entries():
    assert merge_source_metadata([]) == {}
    assert merge_source_metadata([None, {}, {"fred": {}}]) == {"fred": {}}


# ---------- report_metadata_from_series ----------

def _entry(source, source_meta):
    return {"source": source, "metadata": {source: source_meta, "units": "USD"}}


def test_report_metadata_merges_two_same_source_series():
    tsi = [
        _entry("tiingo", {"family": ["VanEck Asset Management"], "category": ["Corporate Bonds"]}),
        _entry("tiingo", {"family": ["VanEck Asset Management"], "category": ["Government Bonds"]}),
    ]
    md = report_metadata_from_series(tsi)
    assert md == {"tiingo": {
        "family": ["VanEck Asset Management"],
        "category": ["Corporate Bonds", "Government Bonds"],
    }}


def test_report_metadata_mixed_sources():
    tsi = [
        _entry("tiingo", {"family": ["VanEck Asset Management"]}),
        _entry("fred", {"frequency": ["Monthly"]}),
    ]
    md = report_metadata_from_series(tsi)
    assert set(md) == {"tiingo", "fred"}
    assert md["fred"]["frequency"] == ["Monthly"]


def test_report_metadata_skips_entries_without_source_metadata():
    tsi = [
        {"source": "tiingo", "metadata": {"units": "USD"}},   # no tiingo key
        {"source": "fred"},                                    # no metadata at all
        _entry("tiingo", {"family": ["VanEck Asset Management"]}),
    ]
    md = report_metadata_from_series(tsi)
    assert md == {"tiingo": {"family": ["VanEck Asset Management"]}}


def test_report_metadata_empty_input():
    assert report_metadata_from_series([]) == {}
    assert report_metadata_from_series(None) == {}
