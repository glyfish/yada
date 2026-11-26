"""Unit tests for CachingFredTool's paged fetch (no network, no cache).

The bug these guard: the tool used to ask meida for `limit=10000` in a single request
and ignore the `count` it came back with. That did two things at once. It overflowed the
legacy SSE transport's 1 MiB per-event cap, which is hardcoded in the client and cannot
be raised from yada -- the loud failure, on DCOILWTICO. And for any series past 10,000
observations it also TRUNCATED, silently, from the recent end, because FRED returns
observations ascending by date. DCOILWTICO has 10,669 and DGS10 has 16,931, so both came
back short and plotted as a chart that looked right and stopped years early.

`_fetch_raw` is exercised directly against a fake wrapped tool, so these assert the
paging arithmetic rather than FRED's current data.
"""

import json

import pytest

from apps.agentic.agents.data.caching_fred_tool import CachingFredTool, _MAX_PAGES, _PAGE


class _FakeTool:
    """Stands in for meida's fred_series_observations.

    Returns the MCP content-block shape `_parse_mcp_json` expects, honours offset/limit
    against a synthetic series of `total` observations, and records every request so a
    test can assert how the fetch was paged.
    """

    def __init__(self, total: int, *, report_count: bool = True, honour_offset: bool = True,
                 claimed_total: int | None = None):
        self.total = total
        self.report_count = report_count
        self.honour_offset = honour_offset
        #: What `count` claims, when that differs from how many rows are actually served.
        self.claimed_total = total if claimed_total is None else claimed_total
        self.calls: list[dict] = []

    async def ainvoke(self, args: dict):
        self.calls.append(dict(args))
        offset = args.get("offset", 0) if self.honour_offset else 0
        limit = args.get("limit")
        rows = [{"date": f"{2000 + i // 365:04d}-01-01", "value": str(i)}
                for i in range(offset, min(offset + limit, self.total))]
        payload = {"series_id": args["series_id"], "observations": rows}
        if self.report_count:
            payload["count"] = self.claimed_total
        return [{"type": "text", "text": json.dumps(payload)}]


def _tool(total: int, **kwargs) -> tuple[CachingFredTool, _FakeTool]:
    fake = _FakeTool(total, **kwargs)
    return CachingFredTool(wrapped=fake), fake


# ---------- the whole series, however many pages it takes ----------

@pytest.mark.parametrize("total,expected_pages", [
    (0, 1),                   # empty series: one request, then stop
    (1, 1),
    (_PAGE - 1, 1),           # short page is the last page
    (_PAGE, 1),               # exactly a page: `count` says it ended, so no second request
    (_PAGE + 1, 2),
    (10669, 3),               # DCOILWTICO
    (16931, 4),               # DGS10
])
@pytest.mark.asyncio
async def test_fetches_every_observation(total, expected_pages):
    tool, fake = _tool(total)
    data = await tool._fetch_raw(series_id="X")
    assert len(data["observations"]) == total
    assert len(fake.calls) == expected_pages


@pytest.mark.asyncio
async def test_pages_are_contiguous_and_in_order():
    """No gap and no overlap: the offsets must walk the series exactly once."""
    tool, fake = _tool(10669)
    data = await tool._fetch_raw(series_id="DCOILWTICO")
    assert [c["offset"] for c in fake.calls] == [0, _PAGE, 2 * _PAGE]
    assert [o["value"] for o in data["observations"]] == [str(i) for i in range(10669)]


@pytest.mark.asyncio
async def test_no_request_exceeds_the_page_size():
    """The page size is what keeps each response under the SSE cap."""
    tool, fake = _tool(16931)
    await tool._fetch_raw(series_id="DGS10")
    assert all(c["limit"] <= _PAGE for c in fake.calls)


# ---------- limit is a cap on the total, not a page size ----------

@pytest.mark.parametrize("cap,expected_obs,expected_pages", [
    (0, 0, 0),                      # nothing asked for, nothing requested
    (200, 200, 1),                  # well inside one page
    (_PAGE, _PAGE, 1),              # exactly one page: no second request
    (_PAGE + 1, _PAGE + 1, 2),
    (7000, 7000, 2),
    (99999, 10669, 3),              # cap above the total yields the total
])
@pytest.mark.asyncio
async def test_limit_caps_the_total(cap, expected_obs, expected_pages):
    tool, fake = _tool(10669)
    data = await tool._fetch_raw(series_id="X", limit=cap)
    assert len(data["observations"]) == expected_obs
    assert len(fake.calls) == expected_pages


# ---------- the count field ----------

@pytest.mark.asyncio
async def test_count_reports_the_series_total_not_what_was_returned():
    """A capped fetch still reports how much the series has, so truncation is visible."""
    tool, _ = _tool(10669)
    data = await tool._fetch_raw(series_id="X", limit=200)
    assert data["count"] == 10669
    assert len(data["observations"]) == 200


@pytest.mark.asyncio
async def test_missing_count_falls_back_to_what_arrived():
    """`count` is optional on the wire; its absence must not stop the paging."""
    tool, fake = _tool(7200, report_count=False)
    data = await tool._fetch_raw(series_id="X")
    assert len(data["observations"]) == 7200
    assert data["count"] == 7200
    assert len(fake.calls) == 2


# ---------- termination ----------

@pytest.mark.asyncio
async def test_a_server_ignoring_offset_cannot_spin_forever():
    """Without `count` AND without honoured offsets, only the page cap ends the loop."""
    tool, fake = _tool(10_000_000, report_count=False, honour_offset=False)
    data = await tool._fetch_raw(series_id="X")
    assert len(fake.calls) == _MAX_PAGES
    assert len(data["observations"]) == _MAX_PAGES * _PAGE


@pytest.mark.asyncio
async def test_short_page_ends_the_loop_when_count_overstates():
    """A `count` larger than the data must not spin, and must not be believed.

    The short page is the authority on where the series ends; `count` only tells the
    loop whether to ask again.
    """
    tool, fake = _tool(6000, claimed_total=999_999)
    data = await tool._fetch_raw(series_id="X")
    assert len(data["observations"]) == 6000
    # Page 2 comes back short (1000 of 5000 asked for), which ends it.
    assert len(fake.calls) == 2
