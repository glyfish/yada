from __future__ import annotations

import asyncio
import os
import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any

from sqlalchemy import MetaData, Table, create_engine, select, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from lib.logger import get_logger

logger = get_logger("YADA")
_DEFAULT_CACHE_TTL_DAYS = 30
_SOURCE_TTL_DAYS: dict[str, int] = {
    "fred": 30,
    "alpaca": 1,
}
_SOURCE_FREQUENCY_TTL_DAYS: dict[tuple[str, str], int] = {
    ("alpaca", "1Min"): 1,
    ("alpaca", "5Min"): 1,
    ("alpaca", "15Min"): 1,
    ("alpaca", "1Hour"): 1,
    ("alpaca", "1Day"): 3,
}

class SeriesCache:
    """
    Singleton cache for time series data backed by PostgreSQL.
    Initialized once at app startup via SeriesCache.initialize().
    """

    _engine: Engine | None = None
    _table: Table | None = None


    @classmethod
    def initialize(cls, url: str | None = None) -> None:
        db_url = url or os.getenv("YADA_DB_URL", "postgresql://yada@localhost/yada")
        cls._engine = create_engine(db_url, pool_pre_ping=True)
        with cls._engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        metadata = MetaData()
        metadata.reflect(bind=cls._engine, only=["time_series_cache"])
        cls._table = metadata.tables["time_series_cache"]
        logger.info(f"SeriesCache initialized: {db_url}")


    @classmethod
    def _engine_or_raise(cls) -> Engine:
        if cls._engine is None:
            raise RuntimeError("SeriesCache not initialized — call SeriesCache.initialize() at startup")
        return cls._engine


    @classmethod
    def _table_or_raise(cls) -> Table:
        if cls._table is None:
            raise RuntimeError("SeriesCache not initialized — call SeriesCache.initialize() at startup")
        return cls._table


    @classmethod
    def _get_by_cache_id_sync(cls, cache_id: str) -> dict | None:
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.native_id == uuid.UUID(cache_id)
        )
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        entry = dict(row)
        if entry["expires_at"] < datetime.now(tz=timezone.utc):
            logger.debug(f"SeriesCache: cache_id {cache_id} expired")
            return None
        return entry


    @classmethod
    def _get_by_native_id_sync(cls, source: str, external_id: str) -> dict | None:
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.source == source,
            cls._table_or_raise().c.external_id == external_id,
        )
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        entry = dict(row)
        if entry["expires_at"] < datetime.now(tz=timezone.utc):
            logger.debug(f"SeriesCache: {source}:{external_id} expired")
            return None
        return entry


    @classmethod
    def _put_sync(
        cls,
        source: str,
        external_id: str,
        data: Any,
        observation_start: str,
        observation_end: str,
        observation_count: int,
        frequency: str | None = None,
        units: str | None = None,
        title: str | None = None,
        ttl_days: int | None = None,
    ) -> str:
        engine = cls._engine_or_raise()
        now = datetime.now(tz=timezone.utc)
        row_frequency = frequency or "unknown"
        row_title = title or external_id
        effective_ttl_days = cls._effective_ttl_days(source, row_frequency, ttl_days)
        expires_at = now + timedelta(days=effective_ttl_days)

        def _as_date(v: str | None) -> date | None:
            if not v:
                return None
            return date.fromisoformat(v[:10])

        metadata: dict[str, Any] = {"observation_count": observation_count}
        if units is not None:
            metadata["units"] = units

        stmt = (
            insert(cls._table_or_raise())
            .values(
                native_id=uuid.uuid4(),
                source=source,
                external_id=external_id,
                title=row_title,
                frequency=row_frequency,
                metadata=metadata,
                observations=data,
                observation_start=_as_date(observation_start),
                observation_end=_as_date(observation_end),
                created_at=now,
                updated_at=now,
                expires_at=expires_at,
            )
            .on_conflict_do_update(
                constraint="uq_tsc_source_external_frequency",
                set_=dict(
                    title=row_title,
                    metadata=metadata,
                    observations=data,
                    observation_start=_as_date(observation_start),
                    observation_end=_as_date(observation_end),
                    updated_at=now,
                    expires_at=expires_at,
                ),
            )
            .returning(cls._table_or_raise().c.native_id)
        )

        with engine.begin() as conn:
            result = conn.execute(stmt)
            cache_id = str(result.scalar())

        logger.debug(f"SeriesCache: stored {source}:{external_id} → {cache_id}")
        return cache_id


    @classmethod
    def _effective_ttl_days(
        cls,
        source: str,
        frequency: str,
        ttl_days: int | None = None,
    ) -> int:
        if ttl_days is not None:
            return ttl_days
        if (source, frequency) in _SOURCE_FREQUENCY_TTL_DAYS:
            return _SOURCE_FREQUENCY_TTL_DAYS[(source, frequency)]
        if source in _SOURCE_TTL_DAYS:
            return _SOURCE_TTL_DAYS[source]
        return _DEFAULT_CACHE_TTL_DAYS


    @classmethod
    async def get_by_cache_id(cls, cache_id: str) -> dict | None:
        return await asyncio.to_thread(cls._get_by_cache_id_sync, cache_id)


    @classmethod
    async def get_by_native_id(cls, source: str, native_id: str) -> dict | None:
        return await asyncio.to_thread(cls._get_by_native_id_sync, source, native_id)


    @classmethod
    async def put(
        cls,
        source: str,
        native_id: str,
        data: Any,
        observation_start: str,
        observation_end: str,
        observation_count: int,
        frequency: str | None = None,
        units: str | None = None,
        title: str | None = None,
        ttl_days: int | None = None,
    ) -> str:
        return await asyncio.to_thread(
            cls._put_sync,
            source,
            native_id,
            data,
            observation_start,
            observation_end,
            observation_count,
            frequency,
            units,
            title,
            ttl_days,
        )
