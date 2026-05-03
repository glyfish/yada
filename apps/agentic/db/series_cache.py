from __future__ import annotations

import asyncio
import os
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from sqlalchemy import MetaData, Table, create_engine, select, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from lib.logger import get_logger

logger = get_logger("YADA")
_CACHE_TTL_DAYS = 30

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
            cls._table_or_raise().c.cache_id == uuid.UUID(cache_id)
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
    def _get_by_native_id_sync(cls, source: str, native_id: str) -> dict | None:
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.source == source,
            cls._table_or_raise().c.native_id == native_id,
        )
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        entry = dict(row)
        if entry["expires_at"] < datetime.now(tz=timezone.utc):
            logger.debug(f"SeriesCache: {source}:{native_id} expired")
            return None
        return entry


    @classmethod
    def _put_sync(
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
    ) -> str:
        engine = cls._engine_or_raise()
        now = datetime.now(tz=timezone.utc)
        expires_at = now + timedelta(days=_CACHE_TTL_DAYS)

        stmt = (
            insert(cls._table_or_raise())
            .values(
                cache_id=uuid.uuid4(),
                source=source,
                native_id=native_id,
                cached_at=now,
                expires_at=expires_at,
                observation_start=observation_start,
                observation_end=observation_end,
                observation_count=observation_count,
                frequency=frequency,
                units=units,
                title=title,
                data=data,
            )
            .on_conflict_do_update(
                constraint="uq_source_native_id",
                set_=dict(
                    cached_at=now,
                    expires_at=expires_at,
                    observation_start=observation_start,
                    observation_end=observation_end,
                    observation_count=observation_count,
                    frequency=frequency,
                    units=units,
                    title=title,
                    data=data,
                ),
            )
            .returning(cls._table_or_raise().c.cache_id)
        )

        with engine.begin() as conn:
            result = conn.execute(stmt)
            cache_id = str(result.scalar())

        logger.debug(f"SeriesCache: stored {source}:{native_id} → {cache_id}")
        return cache_id


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
        )
