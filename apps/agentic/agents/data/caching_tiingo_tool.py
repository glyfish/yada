from __future__ import annotations

import json
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr

from apps.agentic.core.agents.caching_data_tool import CachingDataTool


class _Input(BaseModel):
    ticker: str = Field(..., description="Ticker symbol, e.g. SPY or VFIAX")


class CachingTiingoTool(CachingDataTool):
    """Caching wrapper for the MCP tiingo_price_series tool.

    Normalizes Tiingo's EOD payload into the same observation shape the FRED path
    produces — ``{"observations": [{"date": "YYYY-MM-DD", "value": <adj close>, ...}]}`` —
    so the cache and all downstream plotting code treat Tiingo and FRED series identically.
    """

    source: str = "tiingo"
    name: str = "tiingo_price_series"
    description: str = (
        "Fetch the end-of-day price history for an ETF, mutual fund, or stock ticker "
        "from Tiingo. Returns a SeriesRef JSON object identifying where the data is "
        "cached. Provide the ticker symbol, e.g. SPY."
    )

    _wrapped: BaseTool = PrivateAttr()
    _info_tool: BaseTool | None = PrivateAttr(default=None)

    def __init__(self, wrapped: BaseTool, info_tool: BaseTool | None = None, **kwargs: Any):
        super().__init__(args_schema=_Input, **kwargs)
        self._wrapped = wrapped
        self._info_tool = info_tool

    def _native_id(self, **kwargs: Any) -> str:
        return kwargs["ticker"].upper()

    async def _fetch_raw(self, **kwargs: Any) -> dict:
        raw = await self._wrapped.ainvoke({
            "ticker": self._native_id(**kwargs),
            "start_date": "1900-01-01",  # far-past start → full available history
        })
        payload = json.loads(raw)
        observations = [
            {
                "date": p["date"][:10],          # ISO timestamp → YYYY-MM-DD for the plotter
                "value": str(p["adj_close"]),    # adjusted close is the series value
                "open": p["open"],
                "high": p["high"],
                "low": p["low"],
                "close": p["close"],
                "volume": p["volume"],
                "adj_open": p["adj_open"],
                "adj_high": p["adj_high"],
                "adj_low": p["adj_low"],
                "adj_close": p["adj_close"],
                "adj_volume": p["adj_volume"],
                "div_cash": p["div_cash"],
                "split_factor": p["split_factor"],
            }
            for p in payload.get("prices", [])
        ]
        return {"observations": observations}

    def _obs_range(self, data: dict) -> tuple[str, str, int]:
        observations = data.get("observations", [])
        obs_start = observations[0]["date"] if observations else ""
        obs_end = observations[-1]["date"] if observations else ""
        return obs_start, obs_end, len(observations)

    async def _fetch_metadata(self, native_id: str) -> dict:
        if self._info_tool is None:
            return {}
        raw = await self._info_tool.ainvoke({"ticker": native_id})
        info = json.loads(raw)
        return {
            "title": info.get("name"),
            "frequency": "daily",
            "units": "USD",
        }
