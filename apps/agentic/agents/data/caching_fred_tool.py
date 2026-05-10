from __future__ import annotations

import json
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr

from apps.agentic.core.agents.caching_data_tool import CachingDataTool


class _Input(BaseModel):
    series_id: str = Field(..., description="FRED series ID, e.g. UNRATE")
    limit: int = Field(10000, description="Maximum number of observations to return")


class CachingFredTool(CachingDataTool):
    """Caching wrapper for the MCP fred_series_observations tool."""

    source: str = "fred"
    name: str = "fred_series_observations"
    description: str = (
        "Fetch observations for a FRED series. Returns a SeriesRef JSON object "
        "identifying where the data is cached. Use series_id to specify the series "
        "and limit to cap the number of observations (default 10000)."
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
        raw = await self._wrapped.ainvoke({
            "series_id": kwargs["series_id"],
            "limit": kwargs.get("limit", 10000),
        })
        return json.loads(raw)

    def _obs_range(self, data: dict) -> tuple[str, str, int]:
        observations = data.get("observations", [])
        obs_start = observations[0]["date"] if observations else ""
        obs_end = observations[-1]["date"] if observations else ""
        return obs_start, obs_end, len(observations)

    async def _fetch_metadata(self, native_id: str) -> dict:
        if self._info_tool is None:
            return {}
        raw = await self._info_tool.ainvoke({"series_id": native_id})
        info = json.loads(raw)
        series_list = info.get("seriess", [])  # "seriess" is the FRED API's key
        if not series_list:
            return {}
        s = series_list[0]
        return {
            "title": s.get("title"),
            "frequency": s.get("frequency_short"),
            "units": s.get("units_short") or s.get("units"),
        }
