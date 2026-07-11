from __future__ import annotations

import asyncio
import os
import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any

from sqlalchemy import MetaData, Table, and_, create_engine, select, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from apps.agentic.db.metadata_filter import metadata_where
from lib.logger import get_logger

logger = get_logger("YADA")
_DEFAULT_CACHE_TTL_DAYS = 30
_SOURCE_TTL_DAYS: dict[str, int] = {
    "fred": 30,
    "alpaca": 1,
    "tiingo": 1,
}
_SOURCE_FREQUENCY_TTL_DAYS: dict[tuple[str, str], int] = {
    ("alpaca", "1Min"): 1,
    ("alpaca", "5Min"): 1,
    ("alpaca", "15Min"): 1,
    ("alpaca", "1Hour"): 1,
    ("alpaca", "1Day"): 3,
}
# TTL keyed off a series' update cadence — the refresh interval should track how often
# the source publishes new observations. Keys are normalized (upper-cased) frequency
# labels: FRED stores short codes (D/W/BW/M/Q/SA/A), other sources long names.
_FREQUENCY_TTL_DAYS: dict[str, int] = {
    "D": 1, "DAILY": 1,
    "W": 7, "BW": 7, "WEEKLY": 7, "BIWEEKLY": 7,
    "M": 30, "MONTHLY": 30,
    "Q": 90, "QUARTERLY": 90,
    "SA": 180, "SEMIANNUAL": 180,
    "A": 365, "ANNUAL": 365,
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
    def _get_by_cache_id_sync(cls, cache_id: str, include_expired: bool = False) -> dict | None:
        # include_expired=True returns the persisted observations even past the TTL.
        # Rows are never deleted (expiry only forces a re-fetch for freshness), so a
        # saved report can always load its historical snapshot even if the entry has
        # aged out — the report references a durable series, not a live fetch.
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.cache_id == uuid.UUID(cache_id)
        )
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        entry = dict(row)
        if not include_expired and entry["expires_at"] < datetime.now(tz=timezone.utc):
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
    def _get_obs_ranges_by_source_sync(cls, source: str, native_ids: list[str]) -> dict[str, dict]:
        """
        Bulk lookup of (observation_start, observation_end) for a set of native_ids
        under one source, for cache entries that have not expired. Returns a dict
        keyed by native_id. Used to backfill obs-date columns in search results for
        series that have already been fetched into the cache.
        """
        if not native_ids:
            return {}
        t = cls._table_or_raise()
        stmt = select(
            t.c.native_id, t.c.observation_start, t.c.observation_end, t.c.expires_at
        ).where(t.c.source == source, t.c.native_id.in_(native_ids))
        now = datetime.now(tz=timezone.utc)
        result: dict[str, dict] = {}
        with cls._engine_or_raise().connect() as conn:
            for row in conn.execute(stmt).mappings():
                if row["expires_at"] < now:
                    continue
                result[row["native_id"]] = {
                    "observation_start": row["observation_start"],
                    "observation_end": row["observation_end"],
                }
        return result


    @classmethod
    def _existing_ttl_days_sync(cls, source: str, native_id: str, frequency: str) -> int | None:
        """
        Return the ttl_days currently stored for a series (by its unique key), or None
        if there is no row or the column is unset. Ignores expiry — used to preserve a
        per-series TTL override across re-fetches.
        """
        t = cls._table_or_raise()
        stmt = select(t.c.ttl_days).where(
            t.c.source == source,
            t.c.native_id == native_id,
            t.c.frequency == frequency,
        )
        with cls._engine_or_raise().connect() as conn:
            row = conn.execute(stmt).first()
        return row[0] if row and row[0] is not None else None


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
        ttl_days: int | None = None,
        catalog: dict | None = None,
    ) -> str:
        engine = cls._engine_or_raise()
        now = datetime.now(tz=timezone.utc)
        row_frequency = frequency or "unknown"
        row_title = title or native_id
        if ttl_days is not None:
            effective_ttl_days = ttl_days
        else:
            # Honor a per-series override already persisted on the row; otherwise
            # derive the interval from the series' update cadence (frequency).
            existing_ttl = cls._existing_ttl_days_sync(source, native_id, row_frequency)
            effective_ttl_days = (
                existing_ttl if existing_ttl is not None
                else cls._effective_ttl_days(source, row_frequency)
            )
        expires_at = now + timedelta(days=effective_ttl_days)

        def _as_date(v: str | None) -> date | None:
            if not v:
                return None
            return date.fromisoformat(v[:10])

        metadata: dict[str, Any] = {"observation_count": observation_count}
        if units is not None:
            metadata["units"] = units
        # Source-keyed catalog metadata ({"tiingo": {"family": [...], ...}}) lives
        # alongside the flat keys so the series can be filtered by reusing the
        # document-search extractors' where-dict against metadata[source].
        if catalog:
            metadata.update(catalog)

        stmt = (
            insert(cls._table_or_raise())
            .values(
                cache_id=uuid.uuid4(),
                source=source,
                native_id=native_id,
                title=row_title,
                frequency=row_frequency,
                metadata=metadata,
                observations=data,
                observation_start=_as_date(observation_start),
                observation_end=_as_date(observation_end),
                created_at=now,
                updated_at=now,
                expires_at=expires_at,
                ttl_days=effective_ttl_days,
            )
            .on_conflict_do_update(
                constraint="uq_tsc_source_native_frequency",
                # effective_ttl_days already preserved any existing override (via the
                # pre-SELECT) and filled in NULLs from cadence, so write it back here —
                # this keeps overrides and backfills pre-existing rows on re-fetch.
                set_=dict(
                    title=row_title,
                    metadata=metadata,
                    observations=data,
                    observation_start=_as_date(observation_start),
                    observation_end=_as_date(observation_end),
                    updated_at=now,
                    expires_at=expires_at,
                    ttl_days=effective_ttl_days,
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
    def _effective_ttl_days(
        cls,
        source: str,
        frequency: str,
        ttl_days: int | None = None,
    ) -> int:
        # Precedence: explicit override -> source+frequency special case (alpaca
        # intraday) -> generic frequency cadence -> source default -> global default.
        if ttl_days is not None:
            return ttl_days
        if (source, frequency) in _SOURCE_FREQUENCY_TTL_DAYS:
            return _SOURCE_FREQUENCY_TTL_DAYS[(source, frequency)]
        freq_key = (frequency or "").strip().upper()
        if freq_key in _FREQUENCY_TTL_DAYS:
            return _FREQUENCY_TTL_DAYS[freq_key]
        if source in _SOURCE_TTL_DAYS:
            return _SOURCE_TTL_DAYS[source]
        return _DEFAULT_CACHE_TTL_DAYS


    @classmethod
    def _list_series_sync(cls, source: str | None = None, where: dict | None = None) -> list[dict]:
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        stmt = select(
            t.c.cache_id,
            t.c.title,
            t.c.native_id,
            t.c.source,
            t.c.frequency,
            t.c.observation_start,
            t.c.observation_end,
            t.c.metadata,
        )
        # source scopes the rows; where filters by catalog metadata (reusing the
        # document-search extractors' where-dict against metadata[source]).
        conds = []
        if source:
            conds.append(t.c.source == source)
            mw = metadata_where(t.c.metadata, source, where)
            if mw is not None:
                conds.append(mw)
        if conds:
            stmt = stmt.where(and_(*conds))
        stmt = stmt.order_by(t.c.source, t.c.title)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [
            {
                "cache_id": str(r["cache_id"]),
                "title": r["title"],
                "native_id": r["native_id"],
                "source": r["source"],
                "frequency": r["frequency"],
                "observation_start": str(r["observation_start"] or ""),
                "observation_end": str(r["observation_end"] or ""),
                "metadata": r["metadata"],
            }
            for r in rows
        ]


    @classmethod
    def _get_details_by_id_sync(cls, id_str: str) -> list[dict]:
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        cols = [
            t.c.cache_id,
            t.c.source,
            t.c.native_id,
            t.c.title,
            t.c.frequency,
            t.c.observation_start,
            t.c.observation_end,
            t.c.metadata,
            t.c.created_at,
            t.c.updated_at,
            t.c.expires_at,
        ]
        try:
            uid = uuid.UUID(id_str)
            stmt = select(*cols).where(t.c.cache_id == uid)
        except ValueError:
            stmt = select(*cols).where(t.c.native_id == id_str)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [
            {
                "cache_id": str(r["cache_id"]),
                "source": r["source"],
                "native_id": r["native_id"],
                "title": r["title"],
                "frequency": r["frequency"],
                "observation_start": str(r["observation_start"] or ""),
                "observation_end": str(r["observation_end"] or ""),
                "metadata": r["metadata"],
                "created_at": str(r["created_at"]),
                "updated_at": str(r["updated_at"]),
                "expires_at": str(r["expires_at"]),
            }
            for r in rows
        ]


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
        catalog: dict | None = None,
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
            catalog,
        )
