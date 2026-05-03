from __future__ import annotations

import asyncio
import os
import uuid
from typing import Any

from sqlalchemy import MetaData, Table, create_engine, select, text
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
        time_series_ids: list[str],
    ) -> str:
        engine = cls._engine_or_raise()
        report_id = uuid.uuid4()
        stmt = (
            insert(cls._table_or_raise())
            .values(
                report_id=report_id,
                report_title=report_title,
                report_description=report_description,
                time_series_ids=time_series_ids,
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
        stmt = select(
            cls._table_or_raise().c.report_id,
            cls._table_or_raise().c.report_title,
        ).order_by(cls._table_or_raise().c.report_title)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [{"report_id": str(r["report_id"]), "report_title": r["report_title"]} for r in rows]


    @classmethod
    async def put(
        cls,
        report_title: str,
        report_description: str,
        time_series_ids: list[str],
    ) -> str:
        return await asyncio.to_thread(cls._put_sync, report_title, report_description, time_series_ids)


    @classmethod
    async def get_by_report_id(cls, report_id: str) -> dict | None:
        return await asyncio.to_thread(cls._get_by_report_id_sync, report_id)


    @classmethod
    async def list_reports(cls) -> list[dict[str, Any]]:
        return await asyncio.to_thread(cls._list_reports_sync)
