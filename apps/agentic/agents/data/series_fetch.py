from __future__ import annotations

import json

from apps.agentic.agents.data.caching_tiingo_tool import CachingTiingoTool
from apps.agentic.agents.data.caching_fred_tool import CachingFredTool
from apps.agentic.core.mcp_tool_registry import MCPToolRegistry
from apps.agentic.db.series_cache import SeriesCache
from lib.logger import get_logger

logger = get_logger("YADA")

# Maps a data source to its (observations tool, info tool, caching wrapper, id kwarg).
# The caching wrapper fetches the full series into SeriesCache (or returns the cached
# entry when still fresh) and preserves the cache_id across refreshes.
SERIES_SOURCE_SPECS = {
    "tiingo": ("tiingo_price_series", "tiingo_series_info", CachingTiingoTool, "ticker"),
    "fred": ("fred_series_observations", "fred_series_info", CachingFredTool, "series_id"),
}


async def fetch_series_into_cache(source: str, native_id: str) -> dict | None:
    """
    Ensure (source, native_id) is fresh in SeriesCache and return the cache entry.

    Delegates to the caching tool, which re-fetches only when the entry is missing or
    past its TTL — a still-fresh entry is a cache hit with no network call. The upsert
    preserves the cache_id, so a saved report's references stay valid across refreshes.

    Returns None when the source is unknown or its MCP tool is unavailable; raises on
    an actual fetch failure.
    """
    spec = SERIES_SOURCE_SPECS.get(source.strip().lower())
    if spec is None:
        return None
    obs_tool_name, info_tool_name, tool_cls, id_kwarg = spec

    wrapped = MCPToolRegistry.get(obs_tool_name)
    if wrapped is None:
        logger.warning(f"fetch_series_into_cache: MCP tool '{obs_tool_name}' unavailable")
        return None

    tool = tool_cls(wrapped=wrapped, info_tool=MCPToolRegistry.get(info_tool_name))
    ref = json.loads(await tool._arun(**{id_kwarg: native_id}))
    return await SeriesCache.get_by_cache_id(ref["cache_id"])
