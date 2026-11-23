from __future__ import annotations

import asyncio
import os
import uuid
from datetime import date
from typing import Any, Mapping, Sequence

from sqlalchemy import MetaData, Table, create_engine, delete, select, text, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine

from apps.agentic.db.metadata_filter import metadata_where
from lib.logger import get_logger
from apps.core.environment import db_url as environment_db_url

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
        db_url = url or environment_db_url()
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
        metadata: dict | None = None,
        created_by: str | None = None,
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
                # created_by is None when no users are configured, which is the
                # unauthenticated local case. A model must never supply it -- it comes
                # from the token on the request, or it is NULL.
                created_by=uuid.UUID(created_by) if created_by else None,
                report_id=report_id,
                report_title=report_title,
                report_description=report_description,
                time_series_info=list(time_series_info),
                metadata=metadata or {},
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
    def _owned_by(cls, owner: str | None):
        """A WHERE term scoping rows to `owner`, or None when scoping is off.

        Strict equality: a row whose `created_by` is NULL belongs to nobody, not to
        everybody. Those rows can only predate the first user, and handing them to
        whoever asks first is a worse default than leaving them unreachable until
        someone claims them with an UPDATE. There are none today, so the rule is free
        to settle now and expensive to change later.
        """
        if owner is None:
            return None
        return cls._table_or_raise().c.created_by == uuid.UUID(owner)


    @staticmethod
    def _as_report_id(report_id: str) -> uuid.UUID | None:
        """The id as a UUID, or None when it is not one.

        A malformed id matches no row, so it is a miss -- the same answer this store
        already gives for a report belonging to someone else. Raising instead made a
        title crash the caller: `uuid.UUID("GDP Overview")` is a ValueError, LangGraph's
        default handler re-raises anything that is not a ToolInvocationError, so "delete
        the GDP Overview report" killed the chat turn, and GET /api/reports/<title>
        answered 500 rather than 404. Both tools' own descriptions invite a title.
        """
        try:
            return uuid.UUID(report_id)
        except (ValueError, AttributeError, TypeError):
            return None

    @classmethod
    def _get_by_report_id_sync(cls, report_id: str, owner: str | None = None) -> dict | None:
        uid = cls._as_report_id(report_id)
        if uid is None:
            return None
        engine = cls._engine_or_raise()
        stmt = select(cls._table_or_raise()).where(
            cls._table_or_raise().c.report_id == uid
        )
        scope = cls._owned_by(owner)
        if scope is not None:
            # A report_id is an unguessable UUID, but unguessable is not an access rule
            # -- ids travel in logs, links and transcripts.
            stmt = stmt.where(scope)
        with engine.connect() as conn:
            row = conn.execute(stmt).mappings().first()
        if row is None:
            return None
        return dict(row)


    @classmethod
    def _list_reports_sync(cls, source: str | None = None, where: dict | None = None,
                           owner: str | None = None) -> list[dict[str, Any]]:
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        stmt = select(
            t.c.report_id,
            t.c.report_title,
            t.c.report_description,
            t.c.metadata,
            t.c.time_range_from,
            t.c.time_range_to,
        )
        # A report's metadata column is the merged catalog, so the same containment
        # filter used for a cached series selects reports that contain a matching series.
        if source:
            mw = metadata_where(t.c.metadata, source, where)
            if mw is not None:
                stmt = stmt.where(mw)
        scope = cls._owned_by(owner)
        if scope is not None:
            stmt = stmt.where(scope)
        stmt = stmt.order_by(t.c.report_title)
        with engine.connect() as conn:
            rows = conn.execute(stmt).mappings().all()
        return [
            {
                "report_id": str(r["report_id"]),
                "report_title": r["report_title"],
                "report_description": r["report_description"] or "",
                "metadata": dict(r["metadata"] or {}),
                "time_range_from": str(r["time_range_from"] or ""),
                "time_range_to": str(r["time_range_to"] or ""),
            }
            for r in rows
        ]


    @classmethod
    def _search_by_title_sync(cls, title_fragment: str,
                              owner: str | None = None) -> list[dict[str, Any]]:
        """Reports whose title CONTAINS the fragment, scoped to one owner.

        The scope is not an optimisation. Titles are not unique -- nothing enforces it,
        and the match is a substring, so "GDP" already finds both "GDP Overview" and
        "GDP Deflator" for one user. Unscoped, two owners' identical titles make the
        ambiguity insoluble AND put one person's titles and report ids into the other
        person's disambiguation list, which is a disclosure rather than an annoyance.
        """
        engine = cls._engine_or_raise()
        stmt = select(
            cls._table_or_raise().c.report_id,
            cls._table_or_raise().c.report_title,
        ).where(
            cls._table_or_raise().c.report_title.ilike(f"%{title_fragment}%")
        )
        scope = cls._owned_by(owner)
        if scope is not None:
            stmt = stmt.where(scope)
        stmt = stmt.order_by(cls._table_or_raise().c.report_title)
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
        metadata: dict | None = None,
    ) -> str:
        return await asyncio.to_thread(
            cls._put_sync, report_title, report_description, time_series_info, time_range_from, time_range_to, metadata
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
        metadata: dict | None = None,
        owner: str | None = None,
    ) -> dict | None:
        uid = cls._as_report_id(report_id)
        if uid is None:
            return None
        engine = cls._engine_or_raise()

        def _as_date(v: str | None) -> date | None:
            if not v:
                return None
            return date.fromisoformat(v[:10])

        t = cls._table_or_raise()
        scope = cls._owned_by(owner)
        stmt = (
            update(t)
            .where(t.c.report_id == uid)
            .values(
                report_title=report_title,
                report_description=report_description,
                time_series_info=list(time_series_info),
                metadata=metadata or {},
                time_range_from=_as_date(time_range_from),
                time_range_to=_as_date(time_range_to),
            )
        )
        if scope is not None:
            stmt = stmt.where(scope)
        with engine.begin() as conn:
            conn.execute(stmt)
        logger.debug(f"ReportCache: updated report {report_id} → '{report_title}'")
        return cls._get_by_report_id_sync(report_id, owner=owner)


    @classmethod
    async def get_by_report_id(cls, report_id: str,
                               owner: str | None = None) -> dict | None:
        return await asyncio.to_thread(cls._get_by_report_id_sync, report_id, owner)


    @classmethod
    async def update_report(
        cls,
        report_id: str,
        report_title: str,
        report_description: str,
        time_series_info: Sequence[Mapping[str, Any]],
        time_range_from: str,
        time_range_to: str | None = None,
        metadata: dict | None = None,
        owner: str | None = None,
    ) -> dict | None:
        return await asyncio.to_thread(
            cls._update_report_sync,
            report_id, report_title, report_description,
            time_series_info, time_range_from, time_range_to, metadata, owner,
        )


    @classmethod
    def _delete_report_sync(cls, report_id: str, owner: str | None = None) -> bool:
        uid = cls._as_report_id(report_id)
        if uid is None:
            return False
        engine = cls._engine_or_raise()
        t = cls._table_or_raise()
        stmt = delete(t).where(t.c.report_id == uid)
        scope = cls._owned_by(owner)
        if scope is not None:
            # Returns False rather than raising when the row belongs to someone else,
            # which is the same answer as "no such report" -- deliberately, so a
            # caller cannot probe for the existence of other people's reports.
            stmt = stmt.where(scope)
        with engine.begin() as conn:
            result = conn.execute(stmt)
        deleted = result.rowcount > 0
        if deleted:
            logger.debug(f"ReportCache: deleted report {report_id}")
        return deleted


    @classmethod
    async def delete_report(cls, report_id: str, owner: str | None = None) -> bool:
        return await asyncio.to_thread(cls._delete_report_sync, report_id, owner)


    @classmethod
    async def list_reports(cls, source: str | None = None, where: dict | None = None,
                           owner: str | None = None) -> list[dict[str, Any]]:
        return await asyncio.to_thread(cls._list_reports_sync, source, where, owner)


    @classmethod
    async def search_by_title(cls, title_fragment: str,
                              owner: str | None = None) -> list[dict[str, Any]]:
        return await asyncio.to_thread(cls._search_by_title_sync, title_fragment, owner)
