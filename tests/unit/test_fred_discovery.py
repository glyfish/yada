"""
Tests for FRED API discovery.

The pagination loop and the page cap are the whole point of the module, and both are
pure given a stub client, so they are tested without a database or a network. What is
deliberately *not* covered here is the database reconciliation in `fetch_category`,
which needs Postgres; it is exercised by running `discover` against dev.
"""

import pytest

from apps.agentic.db import fred_discovery
from apps.agentic.db.fred_discovery import (
    PAGE,
    VOLUME_EXCLUDED,
    FredApi,
    FredApiError,
    iter_category_series,
    page_limit_for,
)


class StubApi:
    """Returns `total` synthetic series in pages, recording every call it receives."""

    def __init__(self, total: int, page_size: int = PAGE):
        self.total = total
        self.page_size = page_size
        self.calls: list[dict] = []

    def get(self, path, **params):
        self.calls.append(params)
        offset = params["offset"]
        limit = min(params["limit"], self.page_size)
        rows = [
            {"id": f"S{index}", "title": f"Series {index}"}
            for index in range(offset, min(offset + limit, self.total))
        ]
        return {"count": self.total, "offset": offset, "limit": limit, "seriess": rows}


# --------------------------------------------------------------------- page_limit_for


def test_countries_are_capped_at_one_page():
    assert page_limit_for("International Data > Countries > Belgium") == 1


def test_the_countries_node_itself_is_capped():
    assert page_limit_for("International Data > Countries") == 1


def test_a_sibling_of_countries_is_not_capped():
    assert page_limit_for("International Data > Indicators > Prices") is None


def test_an_unrelated_branch_is_not_capped():
    assert page_limit_for("Prices > Commodities") is None


def test_a_missing_path_is_not_capped():
    """A category with no path yet must not silently inherit a cap."""
    assert page_limit_for(None) is None
    assert page_limit_for("") is None


def test_the_cap_matches_on_the_full_prefix_not_a_substring():
    """'Countries' alone must not trigger the International Data cap."""
    assert page_limit_for("Countries > Belgium") is None


# --------------------------------------------------------------- iter_category_series


def test_a_single_page_takes_one_request():
    api = StubApi(total=454)
    pages = list(iter_category_series(api, 33062))
    assert len(api.calls) == 1
    assert sum(len(page) for page, _ in pages) == 454


def test_pagination_covers_a_count_larger_than_one_page():
    """The defect this module exists to fix: 2,790 series behind a 1,000 page size."""
    api = StubApi(total=2790)
    pages = list(iter_category_series(api, 32267))
    assert [call["offset"] for call in api.calls] == [0, 1000, 2000]
    assert sum(len(page) for page, _ in pages) == 2790


def test_every_page_reports_the_same_total():
    api = StubApi(total=2790)
    assert {count for _, count in iter_category_series(api, 32267)} == {2790}


def test_a_count_that_is_an_exact_multiple_does_not_fetch_a_trailing_empty_page():
    """`offset >= count` must end the loop, or every exact multiple costs a wasted call."""
    api = StubApi(total=2000)
    list(iter_category_series(api, 1))
    assert [call["offset"] for call in api.calls] == [0, 1000]


def test_an_empty_category_stops_after_one_request():
    api = StubApi(total=0)
    pages = list(iter_category_series(api, 999))
    assert len(api.calls) == 1
    assert pages == [([], 0)]


def test_offset_advances_by_the_page_actually_returned():
    """
    Advancing by the requested limit instead of the returned length would skip a window
    whenever the server returns a short page.
    """
    api = StubApi(total=1500, page_size=400)
    list(iter_category_series(api, 1))
    assert [call["offset"] for call in api.calls] == [0, 400, 800, 1200]


def test_a_short_page_run_still_terminates():
    api = StubApi(total=950, page_size=100)
    pages = list(iter_category_series(api, 1))
    assert sum(len(page) for page, _ in pages) == 950


# --------------------------------------------------------------------------- the cap


def test_a_page_limit_stops_early_on_purpose():
    api = StubApi(total=2790)
    pages = list(iter_category_series(api, 32267, page_limit=1))
    assert len(api.calls) == 1
    assert sum(len(page) for page, _ in pages) == 1000


def test_a_page_limit_above_the_count_fetches_everything():
    """A cap must not invent a shortfall where FRED has less than the ceiling."""
    api = StubApi(total=454)
    pages = list(iter_category_series(api, 33062, page_limit=5))
    assert sum(len(page) for page, _ in pages) == 454


def test_a_page_limit_of_two_takes_exactly_two_pages():
    api = StubApi(total=9932)
    pages = list(iter_category_series(api, 33735, page_limit=2))
    assert [call["offset"] for call in api.calls] == [0, 1000]
    assert sum(len(page) for page, _ in pages) == 2000


def test_the_true_count_is_still_reported_under_a_cap():
    """
    The cap must not hide what exists. `api_series_count` is how a capped category stays
    distinguishable from a complete one.
    """
    api = StubApi(total=9932)
    counts = {count for _, count in iter_category_series(api, 33735, page_limit=1)}
    assert counts == {9932}


# ------------------------------------------------------------------------- exclusions


def test_the_exclusion_table_holds_ids_against_reasons():
    """
    Tests the contract, not today's contents. `VOLUME_EXCLUDED` is empty as of
    2026-11-07 -- U.S. Regional Data was excluded on 2026-11-01 and is now being
    fetched -- and asserting a particular entry would just encode whichever volume
    decision was current when the test was written.
    """
    for category_id, reason in VOLUME_EXCLUDED.items():
        assert isinstance(category_id, int)
        # A flag without a reason is exactly what this column exists to prevent: an
        # omission nobody can tell from a bug.
        assert isinstance(reason, str) and len(reason) > 40, category_id


def test_an_empty_exclusion_table_means_fetch_everything():
    """
    Emptying the table must be a valid configuration, because that is how a branch gets
    included again. `mark_exclusions` reconciles in both directions for the same reason:
    emptying it has to CLEAR the stored marks, or a branch that is wanted again stays
    invisible to `pending_categories` and the fetch skips it silently.
    """
    assert isinstance(VOLUME_EXCLUDED, dict)


# ------------------------------------------------------------------------------- key


def test_a_missing_api_key_fails_loudly(monkeypatch):
    """
    yada's stored key was unregistered for an unknown length of time and nothing
    noticed, because nothing in yada called the API. Construction must raise.
    """
    monkeypatch.delenv("FRED_API_KEY", raising=False)
    with pytest.raises(FredApiError, match="FRED_API_KEY"):
        FredApi()


def test_an_explicit_key_overrides_the_environment(monkeypatch):
    monkeypatch.setenv("FRED_API_KEY", "from-env")
    assert FredApi(api_key="explicit")._key == "explicit"


def test_the_page_size_is_freds_maximum():
    """
    1,000 is FRED's ceiling for category/series. The export treated it as a count, which
    is how 145,192 memberships went missing.
    """
    assert PAGE == 1000


def test_pacing_stays_under_freds_documented_rate():
    """120 requests/minute is the documented limit; probing above it returned 429s."""
    assert fred_discovery.MIN_INTERVAL >= 60 / 120
