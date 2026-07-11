from __future__ import annotations

from abc import abstractmethod
from typing import Any

from langchain_core.tools import BaseTool

from apps.agentic.db.series_cache import SeriesCache
from apps.agentic.db.series_ref import SeriesRef
from apps.agentic.core.agents.series_metadata import catalog_metadata
from lib.logger import get_logger

logger = get_logger("YADA")


class CachingDataTool(BaseTool):
    """
    Abstract base for data source tools that cache full series in SeriesCache
    and return a compact SeriesRef JSON string instead of raw observations.

    Subclasses implement:
        source       — data source name used as the cache namespace (e.g. "fred")
        _native_id   — extract the series identifier from tool call kwargs
        _fetch_raw   — call the underlying API and return parsed JSON
        _obs_range   — extract (obs_start, obs_end, obs_count) from the parsed data
    """

    source: str

    def _run(self, *args: Any, **kwargs: Any) -> str:
        raise NotImplementedError("Use async")

    async def _arun(self, **kwargs: Any) -> str:
        native_id = self._native_id(**kwargs)

        entry = await SeriesCache.get_by_native_id(self.source, native_id)
        if entry:
            logger.debug(f"{self.name}: cache hit for {self.source}:{native_id}")
            return SeriesRef(
                source=self.source,
                native_id=native_id,
                cache_id=str(entry["cache_id"]),
            ).to_json()

        logger.debug(f"{self.name}: cache miss for {self.source}:{native_id} — fetching")
        data = await self._fetch_raw(**kwargs)
        obs_start, obs_end, obs_count = self._obs_range(data)

        meta = await self._fetch_metadata(native_id)
        # Enrich with catalog metadata (family/category/exchange or FRED category) from
        # the document store, as a source-keyed dict, so the cached series is filterable
        # by reusing the document-search filter extractors. Best-effort — {} when the
        # series isn't in the catalog store.
        catalog = catalog_metadata(self.source, native_id)
        cache_id = await SeriesCache.put(
            source=self.source,
            native_id=native_id,
            data=data,
            observation_start=obs_start,
            observation_end=obs_end,
            observation_count=obs_count,
            frequency=meta.get("frequency"),
            units=meta.get("units"),
            title=meta.get("title"),
            catalog=catalog,
        )

        ref = SeriesRef(source=self.source, native_id=native_id, cache_id=cache_id)
        logger.debug(f"{self.name}: cached {self.source}:{native_id} → {cache_id}")
        return ref.to_json()

    @abstractmethod
    def _native_id(self, **kwargs: Any) -> str: ...

    @abstractmethod
    async def _fetch_raw(self, **kwargs: Any) -> dict: ...

    @abstractmethod
    def _obs_range(self, data: dict) -> tuple[str, str, int]: ...

    async def _fetch_metadata(self, native_id: str) -> dict:  # noqa: ARG002
        return {}
