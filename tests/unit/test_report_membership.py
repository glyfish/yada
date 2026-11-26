"""Unit tests for adding and removing a report's series (no DB, no LLM).

The rule worth pinning is the date range. A report's `time_range_from`/`time_range_to`
are not decoration: `render_report_plot` hands them to every series it loads, so they
CLIP. Adding a series that begins before the window and leaving the window alone draws
it with its early years missing, on a chart that looks entirely correct -- the same
failure shape as the truncated daily series and the misaligned twinx. `add_report_series`
therefore widens by default, and only ever widens.

The store and the cache projection are stubbed, so these assert the merge, dedupe, range
and refusal rules rather than Postgres.
"""

import pytest

import apps.agentic.agents.data.reports as reports
from apps.agentic.agents.data.reports import add_report_series, remove_report_series


def _entry(native_id, start, end="2026-01-01", cache_id=None):
    return {"cache_id": cache_id or f"cache-{native_id}", "title": native_id,
            "source": "fred", "native_id": native_id, "frequency": "M",
            "observation_start": start, "observation_end": end, "metadata": {}}


@pytest.fixture
def store(monkeypatch):
    """A report in a dict, with the two store calls the service makes stubbed out."""
    state = {
        "report": {
            "report_id": "r-1",
            "report_title": "Probe",
            "report_description": "desc",
            "time_series_info": [_entry("UNRATE", "1948-01-01")],
            "time_range_from": "2000-01-01",
            "time_range_to": None,
        },
        "writes": [],
    }
    # Every cache_id the tests reference, as the cache would project it.
    catalogue = {
        "cache-CPIAUCSL": _entry("CPIAUCSL", "1947-01-01"),
        "cache-GDP": _entry("GDP", "2010-01-01", end="2030-06-01"),
        "cache-UNRATE": _entry("UNRATE", "1948-01-01"),
    }

    monkeypatch.setattr(reports, "current_user_id", lambda: "owner-1")
    monkeypatch.setattr(reports, "resolve_report_or_raise",
                        lambda ref, owner=None, action="plot": state["report"])

    def _resolve(cache_ids):
        missing = [c for c in cache_ids if c not in catalogue]
        if missing:
            raise ValueError("Report creation aborted. Missing cache IDs: "
                             + ", ".join(missing))
        return [catalogue[c] for c in cache_ids]

    monkeypatch.setattr(reports, "resolve_series_entries", _resolve)

    def _update(**kwargs):
        state["writes"].append(kwargs)
        state["report"] = {**state["report"],
                           "time_series_info": list(kwargs["time_series_info"]),
                           "time_range_from": kwargs["time_range_from"],
                           "time_range_to": kwargs["time_range_to"]}
        return state["report"]

    monkeypatch.setattr(reports.ReportCache, "_update_report_sync",
                        staticmethod(lambda **kw: _update(**kw)))
    monkeypatch.setattr(reports, "report_metadata_from_series", lambda info: {})
    return state


def _labels(record):
    return [e["native_id"] for e in record["time_series_info"]]


# ---------- add ----------

def test_add_appends_and_keeps_the_existing_series(store):
    change = add_report_series("Probe", ["cache-CPIAUCSL"])
    assert change.changed == ["CPIAUCSL"]
    assert _labels(change.record) == ["UNRATE", "CPIAUCSL"]


def test_add_widens_the_range_to_cover_the_new_series(store):
    """CPIAUCSL starts 1947; the window started 2000. Without this it plots clipped."""
    change = add_report_series("Probe", ["cache-CPIAUCSL"])
    assert change.record["time_range_from"] == "1947-01-01"
    assert change.range_extended is True


def test_add_leaves_the_range_alone_when_the_series_fits(store):
    """GDP starts 2010, inside the 2000 window: nothing to widen."""
    change = add_report_series("Probe", ["cache-GDP"])
    assert change.record["time_range_from"] == "2000-01-01"
    assert change.range_extended is False


def test_add_never_pins_an_open_ended_range(store):
    """time_range_to None means 'track the latest'; setting it would freeze the report."""
    change = add_report_series("Probe", ["cache-GDP"])
    assert change.record["time_range_to"] is None


def test_add_widens_a_closed_range_forwards(store):
    store["report"]["time_range_to"] = "2020-01-01"
    change = add_report_series("Probe", ["cache-GDP"])      # ends 2030-06-01
    assert change.record["time_range_to"] == "2030-06-01"


def test_extend_range_false_keeps_the_window(store):
    change = add_report_series("Probe", ["cache-CPIAUCSL"], extend_range=False)
    assert change.record["time_range_from"] == "2000-01-01"
    assert change.range_extended is False
    assert change.changed == ["CPIAUCSL"]


def test_add_is_idempotent_and_writes_nothing(store):
    """A series already present is reported, not duplicated -- it would draw twice."""
    change = add_report_series("Probe", ["cache-UNRATE"])
    assert change.changed == []
    assert change.skipped == ["cache-UNRATE"]
    assert _labels(change.record) == ["UNRATE"]
    assert store["writes"] == []


def test_add_dedupes_within_one_call(store):
    change = add_report_series("Probe", ["cache-GDP", "cache-GDP"])
    assert change.changed == ["GDP"]
    assert _labels(change.record) == ["UNRATE", "GDP"]


def test_add_matches_an_existing_series_by_native_id_too(store):
    change = add_report_series("Probe", ["unrate"])
    assert change.changed == []
    assert change.skipped == ["unrate"]


def test_a_bad_cache_id_writes_nothing(store):
    with pytest.raises(ValueError, match="Missing cache IDs"):
        add_report_series("Probe", ["cache-GDP", "nope"])
    assert store["writes"] == []
    assert _labels(store["report"]) == ["UNRATE"]


def test_add_requires_at_least_one_id(store):
    with pytest.raises(ValueError, match="No time series cache IDs"):
        add_report_series("Probe", [])


# ---------- remove ----------

def test_remove_by_native_id_case_insensitively(store):
    store["report"]["time_series_info"].append(_entry("GDP", "2010-01-01"))
    change = remove_report_series("Probe", ["unrate"])
    assert change.changed == ["UNRATE"]
    assert _labels(change.record) == ["GDP"]


def test_remove_by_cache_id(store):
    store["report"]["time_series_info"].append(_entry("GDP", "2010-01-01"))
    change = remove_report_series("Probe", ["cache-UNRATE"])
    assert change.changed == ["UNRATE"]
    assert _labels(change.record) == ["GDP"]


def test_remove_reports_a_miss_without_failing_the_call(store):
    store["report"]["time_series_info"].append(_entry("GDP", "2010-01-01"))
    change = remove_report_series("Probe", ["GDP", "NOPE"])
    assert change.changed == ["GDP"]
    assert change.skipped == ["NOPE"]


def test_remove_leaves_the_range_alone(store):
    """Narrowing to what remains would clip the surviving series."""
    store["report"]["time_series_info"].append(_entry("GDP", "2010-01-01"))
    change = remove_report_series("Probe", ["UNRATE"])
    assert change.record["time_range_from"] == "2000-01-01"
    assert change.range_extended is False


def test_removing_the_last_series_is_refused(store):
    with pytest.raises(ValueError, match="cannot be"):
        remove_report_series("Probe", ["UNRATE"])
    assert store["writes"] == []
    assert _labels(store["report"]) == ["UNRATE"]


def test_removing_nothing_that_matches_says_what_the_report_holds(store):
    with pytest.raises(ValueError, match="UNRATE"):
        remove_report_series("Probe", ["ZZZ"])
    assert store["writes"] == []


def test_remove_requires_at_least_one_name(store):
    with pytest.raises(ValueError, match="No series were named"):
        remove_report_series("Probe", [])


# ---------- the whole-row replace ----------

def test_the_reports_text_survives_a_membership_change(store):
    """`_update_report_sync` replaces the whole row, so the title has to be handed back.

    Getting this wrong would blank the title on every add.
    """
    add_report_series("Probe", ["cache-GDP"])
    written = store["writes"][-1]
    assert written["report_title"] == "Probe"
    assert written["report_description"] == "desc"
    assert written["owner"] == "owner-1"
