from __future__ import annotations

import json
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr

from apps.agentic.core.agents.caching_data_tool import CachingDataTool
from lib.logger import get_logger

logger = get_logger("YADA")

#: Observations per request to meida.
#:
#: meida relays FRED's reply as one JSON-RPC response, and the legacy SSE transport
#: carries a whole response in a SINGLE SSE event, which the client caps at 1 MiB.
#: That cap cannot be raised from here: `mcp.client.sse.sse_client` calls
#: `sse_within_origin(client, url)` with no `max_event_size` (mcp/client/sse.py:70), so
#: it takes the 1 MiB default in mcp/shared/_httpx_utils.py, and fastmcp's
#: `SSETransport` exposes no knob for it either. Only streamable-http threads one
#: through, and meida serves SSE only.
#:
#: Measured on this path: ~75 bytes per observation in the reply, ~1.4x that once
#: escaped into the event, so one request for 10,000 observations of DCOILWTICO
#: overflows while 8,000 does not. 5,000 keeps ~30% headroom for series whose values
#: are wider than oil prices.
_PAGE = 5000

#: Backstop so a server that ignored `offset` cannot spin here forever. 60 pages is
#: 300,000 observations -- an order of magnitude past FRED's longest daily series.
_MAX_PAGES = 60


class _Input(BaseModel):
    series_id: str = Field(..., description="FRED series ID, e.g. UNRATE")
    limit: int | None = Field(
        None,
        description="Cap on observations returned. Omit for the whole series.",
    )


class CachingFredTool(CachingDataTool):
    """Caching wrapper for the MCP fred_series_observations tool.

    Pages the fetch. The previous single request for `limit=10000` had two faults, and
    the cap above is only the louder one: DCOILWTICO has 10,669 observations and DGS10
    has 16,931, so a flat 10,000 also TRUNCATED them -- silently, and from the recent
    end, because FRED returns observations ascending by date. The result was a chart
    that looked right and stopped years short. meida already reports the true total as
    `count` and already accepts `offset`; this reads both.
    """

    source: str = "fred"
    name: str = "fred_series_observations"
    description: str = (
        "Fetch observations for a FRED series. Returns a SeriesRef JSON object "
        "identifying where the data is cached. Use series_id to specify the series; "
        "the whole series is fetched unless limit caps it."
    )

    _wrapped: BaseTool = PrivateAttr()
    _info_tool: BaseTool | None = PrivateAttr(default=None)

    def __init__(self, wrapped: BaseTool, info_tool: BaseTool | None = None, **kwargs: Any):
        super().__init__(args_schema=_Input, **kwargs)
        self._wrapped = wrapped
        self._info_tool = info_tool

    def _native_id(self, **kwargs: Any) -> str:
        return kwargs["series_id"]

    async def _fetch_raw(self, **kwargs: Any) -> dict:
        """Fetch every observation, in `_PAGE`-sized requests.

        `limit` is a cap on the total, not a page size: a caller asking for 200 gets one
        request, and a caller asking for nothing gets the series however many requests
        that takes.
        """
        series_id = kwargs["series_id"]
        cap = kwargs.get("limit")
        observations: list[dict] = []
        total: int | None = None
        pages = 0

        while pages < _MAX_PAGES:
            want = _PAGE if cap is None else min(_PAGE, cap - len(observations))
            if want <= 0:
                break
            page = self._parse_mcp_json(await self._wrapped.ainvoke({
                "series_id": series_id,
                "limit": want,
                "offset": len(observations),
            }))
            pages += 1
            rows = page.get("observations") or []
            if total is None:
                total = page.get("count")
            if not rows:
                break
            observations.extend(rows)
            # A short page is the last page. Checked on the row count rather than on
            # `total` alone so the loop still ends if `count` is missing.
            if len(rows) < want:
                break
            if total is not None and len(observations) >= total:
                break

        if pages >= _MAX_PAGES:
            logger.warning(
                f"{self.name}: stopped paging {series_id} at {_MAX_PAGES} pages with "
                f"{len(observations)} of {total} observations. The cached series is "
                f"incomplete.")
        elif total is not None and cap is None and len(observations) < total:
            # Never silent: this is the failure the flat limit used to hide.
            logger.warning(
                f"{self.name}: {series_id} returned {len(observations)} of {total} "
                f"observations. The cached series is incomplete.")

        if pages > 1:
            logger.debug(f"{self.name}: {series_id} fetched in {pages} pages, "
                         f"{len(observations)} observations")

        return {"observations": observations,
                "count": total if total is not None else len(observations)}

    def _obs_range(self, data: dict) -> tuple[str, str, int]:
        observations = data.get("observations", [])
        obs_start = observations[0]["date"] if observations else ""
        obs_end = observations[-1]["date"] if observations else ""
        return obs_start, obs_end, len(observations)

    async def _fetch_metadata(self, native_id: str) -> dict:
        if self._info_tool is None:
            return {}
        raw = await self._info_tool.ainvoke({"series_id": native_id})
        info = self._parse_mcp_json(raw)
        # meida's fred_series_info normalises FRED's "seriess" to "series". Read
        # either: the raw REST key still reaches the collection path (fred_catalogue,
        # fred_discovery), while this tool is fed by MCP. Reading only "seriess" here
        # returned {} and silently dropped title/frequency/units from the cache.
        series_list = info.get("series") or info.get("seriess") or []
        if not series_list:
            return {}
        s = series_list[0]
        return {
            "title": s.get("title"),
            "frequency": s.get("frequency_short"),
            "units": s.get("units_short") or s.get("units"),
        }
