from __future__ import annotations

import asyncio
import os
import uuid
from datetime import date
from typing import Any, Mapping, Sequence

from sqlalchemy import MetaData, Table, create_engine, delete, select, text, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from lib.logger import get_logger

logger = get_logger("YADA")


class ReportCache:
    """
    Singleton store for time series reports backed by PostgreSQL.
    Initialized once at app startup via ReportCache.initialize().
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
        metadata.reflect(bind=cls._engine, only=["time_series_reports"])
        cls._table = metadata.tables["time_series_reports"]
        logger.info(f"ReportCache initialized: {db_url}")


    @classmethod
    def _engine_or_raise(cls) -> Engine:
        if cls._engine is None:
            raise RuntimeError("ReportCache not initialized — call ReportCache.initialize() at startup")
        return cls._engine


    @classmethod
    def _table_or_raise(cls) -> Table:
        if cls._table is None:
            raise RuntimeError("ReportCache not initialized — call ReportCache.initialize() at startup")
        return cls._table


    @classmethod
    def _put_sync(
        cls,
        report_title: str,
        report_description: str,
        time_series_info: Sequence[Mapping[str, Any]],
        time_range_from: str,
        time_range_to: str | None = None,
        tags: list[str] | None = None,
    ) -> str:
        engine = cls._engine_or_raise()
        report_id = uuid.uuid4()

        def _as_date(v: str | None) -> date | None:
            if not v:
                return None
            return date.fromisoformat(v[:10])

        stmt = (
            insert(cls._table_or_raise())
            .values(
                report_id=report_id,
                report_title=report_title,
                report_description=report_description,
                time_series_info=list(time_series_info),
                tags=tags or [],
                time_range_from=_as_date(time_range_from),
                time_range_to=_as_date(time_range_to),
            )
            .returning(cls._table_or_raise().c.report_id)
        )
        with engine.begin() as conn:
            result = conn.execute(stmt)
            returned_id = str(result.scalar())
        logger.debug(f"ReportCache: stored report '{report_title}' → {returned_id}")
        return returned_id


    @classmethod
    def _get_by_report_id_sync(cls, report_id: str) -> dict | None:
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.report_id == uuid.UUID(report_id)
        )
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        return dict(row)


    @classmethod
    def _list_reports_sync(cls) -> list[dict[str, Any]]:
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        stmt = select(
            t.c.report_id,
            t.c.report_title,
            t.c.report_description,
            t.c.tags,
            t.c.time_range_from,
            t.c.time_range_to,
        ).order_by(t.c.report_title)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [
            {
                "report_id": str(r["report_id"]),
                "report_title": r["report_title"],
                "report_description": r["report_description"] or "",
                "tags": list(r["tags"] or []),
                "time_range_from": str(r["time_range_from"] or ""),
                "time_range_to": str(r["time_range_to"] or ""),
            }
            for r in rows
        ]


    @classmethod
    def _search_by_title_sync(cls, title_fragment: str) -> list[dict[str, Any]]:
        engine = cls._engine_or_raise()
        stmt = select(
            cls._table_or_raise().c.report_id,
            cls._table_or_raise().c.report_title,
        ).where(
            cls._table_or_raise().c.report_title.ilike(f"%{title_fragment}%")
        ).order_by(cls._table_or_raise().c.report_title)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [{"report_id": str(r["report_id"]), "report_title": r["report_title"]} for r in rows]


    @classmethod
    async def put(
        cls,
        report_title: str,
        report_description: str,
        time_series_info: Sequence[Mapping[str, Any]],
        time_range_from: str,
        time_range_to: str | None = None,
        tags: list[str] | None = None,
    ) -> str:
        return await asyncio.to_thread(
            cls._put_sync, report_title, report_description, time_series_info, time_range_from, time_range_to, tags
        )


    @classmethod
    def _update_report_sync(
        cls,
        report_id: str,
        report_title: str,
        report_description: str,
        time_series_info: Sequence[Mapping[str, Any]],
        time_range_from: str,
        time_range_to: str | None = None,
        tags: list[str] | None = None,
    ) -> dict | None:
        engine = cls._engine_or_raise()

        def _as_date(v: str | None) -> date | None:
            if not v:
                return None
            return date.fromisoformat(v[:10])

        t = cls._table_or_raise()
        stmt = (
            update(t)
            .where(t.c.report_id == uuid.UUID(report_id))
            .values(
                report_title=report_title,
                report_description=report_description,
                time_series_info=list(time_series_info),
                tags=tags or [],
                time_range_from=_as_date(time_range_from),
                time_range_to=_as_date(time_range_to),
            )
        )
        with engine.begin() as conn:
            conn.execute(stmt)
        logger.debug(f"ReportCache: updated report {report_id} → '{report_title}'")
        return cls._get_by_report_id_sync(report_id)


    @classmethod
    async def get_by_report_id(cls, report_id: str) -> dict | None:
        return await asyncio.to_thread(cls._get_by_report_id_sync, report_id)


    @classmethod
    async def update_report(
        cls,
        report_id: str,
        report_title: str,
        report_description: str,
        time_series_info: Sequence[Mapping[str, Any]],
        time_range_from: str,
        time_range_to: str | None = None,
        tags: list[str] | None = None,
    ) -> dict | None:
        return await asyncio.to_thread(
            cls._update_report_sync,
            report_id, report_title, report_description,
            time_series_info, time_range_from, time_range_to, tags,
        )


    @classmethod
    def _delete_report_sync(cls, report_id: str) -> bool:
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        stmt = delete(t).where(t.c.report_id == uuid.UUID(report_id))
        with engine.begin() as conn:
            result = conn.execute(stmt)
        deleted = result.rowcount > 0
        if deleted:
            logger.debug(f"ReportCache: deleted report {report_id}")
        return deleted


    @classmethod
    async def delete_report(cls, report_id: str) -> bool:
        return await asyncio.to_thread(cls._delete_report_sync, report_id)


    @classmethod
    async def list_reports(cls) -> list[dict[str, Any]]:
        return await asyncio.to_thread(cls._list_reports_sync)


    @classmethod
    async def search_by_title(cls, title_fragment: str) -> list[dict[str, Any]]:
        return await asyncio.to_thread(cls._search_by_title_sync, title_fragment)
