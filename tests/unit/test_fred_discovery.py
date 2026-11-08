"""
Tests for FRED API discovery.

The pagination loop is the whole point of the module, and it is pure given a stub
client, so it is tested without a database or a network. What is deliberately *not*
covered here is the database reconciliation in `fetch_category` and the surplus query in
`surplus_categories`, both of which need Postgres; they are exercised by running
`discover` and `fred_metadata.py status` against dev.

The page cap and the exclusion table used to be tested here too. Both were removed on
2026-11-08 along with the mechanisms, so what is asserted now is their absence: every
page FRED reports is read, and no argument can shorten that.

`surplus_categories` was verified that way on 2026-11-07: it returns exactly one row
across 5,201 categories (34111, holding 2,398 against FRED's 1,398), which is the case
that prompted writing it.
"""

import pytest

from apps.agentic.db import fred_discovery
from apps.agentic.db.fred_discovery import (
    PAGE,
    FredApi,
    FredApiError,
    iter_category_series,
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


# ------------------------------------------------------------- no partial fetch

@pytest.mark.parametrize("total", [0, 1, 999, 1000, 1001, 2790, 2917, 9932])
def test_every_page_fred_reports_is_read(total):
    """
    The invariant that replaced `page_limit`: there is no way to ask for less than the
    whole category. A short read can therefore only mean something went wrong, which is
    what lets `fetch_category` treat any shortfall as a defect.
    """
    api = StubApi(total=total)
    pages = list(iter_category_series(api, 1))
    assert sum(len(page) for page, _ in pages) == total


def test_iter_category_series_takes_no_limiting_argument():
    """
    Guards the decision rather than the code. Reinstating a cap means reintroducing data
    that is missing on purpose and unreadably -- the failure this module exists to undo
    -- so the signature is asserted, not just the behaviour.
    """
    import inspect

    parameters = inspect.signature(iter_category_series).parameters
    assert list(parameters) == ["api", "category_id"]


def test_the_true_count_is_reported_on_every_page():
    """`api_series_count` is what the reconciliation compares against, so every page
    must carry FRED's own total rather than the size of the page."""
    api = StubApi(total=9932)
    counts = {count for _, count in iter_category_series(api, 33735)}
    assert counts == {9932}


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
