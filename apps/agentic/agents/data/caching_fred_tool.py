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

    def __init__(self, wrapped: BaseTool, **kwargs: Any):
        super().__init__(args_schema=_Input, **kwargs)
        self._wrapped = wrapped

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
