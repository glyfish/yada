"""initial schema

Rolled-up initial schema for the yada database (replaces the earlier 0001-0004 chain).

public                  time_series_cache, time_series_reports (the analysis cache) and
                        price_series (reference prices)
trading                 strategy_configs -- the unit promoted through backtest -> paper ->
                        live -- and promotions, the audit log of stage changes
backtest, paper, live   identical run-output table sets, one schema per trading mode
trading.*_all           UNION ALL views across the three modes, with a `mode` column

The trading and mode table definitions mirror apps/backtrader/db/trading_db.py, which is
the source of truth; alembic's compare_metadata is used to keep the two in step.

Revision ID: 0001
Revises:
Create Date: 2026-08-22
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None

TRADING = "trading"
MODES = ("backtest", "paper", "live")
MODE_TABLES = ("runs", "orders", "trades", "positions", "broker", "analyzers", "indicators", "asset_prices")


def _create_public_tables() -> None:
    op.create_table(
        "time_series_cache",
        sa.Column("cache_id", UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("source", sa.Text(), nullable=False),
        sa.Column("native_id", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("frequency", sa.Text(), nullable=False),
        sa.Column("metadata", JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("observations", JSONB(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("observation_start", sa.Date(), nullable=True),
        sa.Column("observation_end", sa.Date(), nullable=True),
        # Per-series time-to-live (days) used to compute expires_at; nullable, reads rely
        # on expires_at.
        sa.Column("ttl_days", sa.Integer(), nullable=True),
        sa.UniqueConstraint("source", "native_id", "frequency", name="uq_tsc_source_native_frequency"),
    )
    op.create_index("idx_tsc_source", "time_series_cache", ["source"])
    op.create_index("idx_tsc_native_id", "time_series_cache", ["native_id"])
    op.create_index("idx_tsc_frequency", "time_series_cache", ["frequency"])
    op.create_index("idx_tsc_metadata_gin", "time_series_cache", ["metadata"], postgresql_using="gin")
    op.create_index("idx_tsc_expires_at", "time_series_cache", ["expires_at"])

    op.create_table(
        "time_series_reports",
        sa.Column("report_id", UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("report_title", sa.Text(), nullable=False),
        sa.Column("report_description", sa.Text(), nullable=False, server_default=""),
        sa.Column("time_series_info", JSONB(), nullable=False, server_default=sa.text("'[]'::jsonb")),
        # Source-keyed catalog metadata merged across the report's series, e.g.
        # {"tiingo": {"family": [...], "category_group": [...]}} -- auto-derived, used
        # for filtering reports by reusing the document-search filter extractors.
        sa.Column("metadata", JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("time_range_from", sa.Date(), nullable=False),
        sa.Column("time_range_to", sa.Date(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_tsr_report_title", "time_series_reports", ["report_title"])
    op.create_index("idx_tsr_time_series_info_gin", "time_series_reports", ["time_series_info"], postgresql_using="gin")
    op.create_index("idx_tsr_metadata_gin", "time_series_reports", ["metadata"], postgresql_using="gin")

    op.create_table(
        "price_series",
        sa.Column("ticker", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("open_price", sa.Float(), nullable=False),
        sa.Column("high_price", sa.Float(), nullable=False),
        sa.Column("low_price", sa.Float(), nullable=False),
        sa.Column("close_price", sa.Float(), nullable=False),
        sa.Column("adj_close_price", sa.Float(), nullable=False),
        sa.Column("volume", sa.Float(), nullable=False),
        sa.Column("open_interest", sa.Float(), nullable=False),
    )


def _create_trading_tables() -> None:
    op.create_table(
        "strategy_configs",
        sa.Column("config_id", sa.String(length=32), primary_key=True, nullable=False),
        sa.Column("strategy", sa.String(length=256), nullable=False),
        sa.Column("params", JSONB(), nullable=False),
        sa.Column("universe", JSONB(), nullable=False),
        sa.Column("stage", sa.String(length=32), nullable=False, server_default="exploratory"),
        sa.Column("description", sa.String(length=1024), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        schema=TRADING,
    )
    op.create_table(
        "promotions",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column("config_id", sa.String(length=32), sa.ForeignKey(f"{TRADING}.strategy_configs.config_id"), nullable=False),
        sa.Column("from_stage", sa.String(length=32), nullable=False),
        sa.Column("to_stage", sa.String(length=32), nullable=False),
        sa.Column("evidence_mode", sa.String(length=32), nullable=True),
        sa.Column("evidence_run_id", sa.String(length=256), nullable=True),
        sa.Column("promoted_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("notes", sa.String(length=4096), nullable=True),
        schema=TRADING,
    )
    op.create_index("ix_trading_promotions_config", "promotions", ["config_id"], schema=TRADING)


def _create_mode_tables(mode: str) -> None:
    def run_fk(**kwargs):
        return sa.Column("run_id", sa.String(length=256), sa.ForeignKey(f"{mode}.runs.run_id", ondelete="CASCADE"), **kwargs)

    op.create_table(
        "runs",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("config_id", sa.String(length=32), sa.ForeignKey(f"{TRADING}.strategy_configs.config_id"), nullable=False),
        sa.Column("tier", sa.String(length=32), nullable=False, server_default="exploratory"),
        sa.Column("ensemble_id", sa.String(length=256), nullable=True),
        sa.Column("status", sa.String(length=32), nullable=False, server_default="running"),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ended_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("broker_account", sa.String(length=256), nullable=True),
        sa.Column("notes", sa.String(length=4096), nullable=True),
        schema=mode,
    )
    op.create_index(f"ix_{mode}_runs_config", "runs", ["config_id"], schema=mode)

    op.create_table(
        "broker",
        run_fk(primary_key=True, nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), primary_key=True, nullable=False),
        sa.Column("cash", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        schema=mode,
    )
    op.create_table(
        "positions",
        run_fk(primary_key=True, nullable=False),
        sa.Column("ticker", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), primary_key=True, nullable=False),
        sa.Column("adjbase", sa.Float(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("price_orig", sa.Float(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("upclosed", sa.Float(), nullable=False),
        sa.Column("upopened", sa.Float(), nullable=False),
        sa.Column("updt", sa.DateTime(timezone=True), nullable=True),
        schema=mode,
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True, nullable=False),
        run_fk(nullable=False),
        sa.Column("ref", sa.Integer(), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("order_status", sa.String(length=256), nullable=False),
        sa.Column("order_type", sa.String(length=256), nullable=False),
        sa.Column("exec_type", sa.String(length=256), nullable=False),
        sa.Column("trade_id", sa.BigInteger(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("commission", sa.Float(), nullable=False),
        sa.Column("pnl", sa.Float(), nullable=False),
        schema=mode,
    )
    op.create_index(f"ix_{mode}_orders_run_ref", "orders", ["run_id", "ref"], schema=mode)
    op.create_index(f"ix_{mode}_orders_run_ts", "orders", ["run_id", "ts"], schema=mode)

    op.create_table(
        "trades",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True, nullable=False),
        run_fk(nullable=False),
        sa.Column("ref", sa.Integer(), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(length=256), nullable=False),
        sa.Column("trade_id", sa.BigInteger(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("commission", sa.Float(), nullable=False),
        sa.Column("pnl", sa.Float(), nullable=False),
        sa.Column("pnlcomm", sa.Float(), nullable=False),
        sa.Column("dtopen", sa.DateTime(timezone=True), nullable=True),
        sa.Column("dtclose", sa.DateTime(timezone=True), nullable=True),
        sa.Column("baropen", sa.Integer(), nullable=False),
        sa.Column("barclose", sa.Integer(), nullable=False),
        sa.Column("barlen", sa.Integer(), nullable=False),
        sa.Column("is_long", sa.Boolean(), nullable=False),
        schema=mode,
    )
    op.create_index(f"ix_{mode}_trades_run_ref", "trades", ["run_id", "ref"], schema=mode)
    op.create_index(f"ix_{mode}_trades_run_ts", "trades", ["run_id", "ts"], schema=mode)

    op.create_table(
        "analyzers",
        run_fk(primary_key=True, nullable=False),
        sa.Column("analyzer", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("value", JSONB(), nullable=False),
        sa.Column("parameters", JSONB(), nullable=True),
        schema=mode,
    )
    op.create_table(
        "indicators",
        run_fk(primary_key=True, nullable=False),
        sa.Column("ticker", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("indicator", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), primary_key=True, nullable=False),
        sa.Column("value", JSONB(), nullable=False),
        sa.Column("params", JSONB(), nullable=True),
        schema=mode,
    )
    op.create_table(
        "asset_prices",
        run_fk(primary_key=True, nullable=False),
        sa.Column("ticker", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("ts", sa.DateTime(timezone=True), primary_key=True, nullable=False),
        sa.Column("open_price", sa.Float(), nullable=False),
        sa.Column("high_price", sa.Float(), nullable=False),
        sa.Column("low_price", sa.Float(), nullable=False),
        sa.Column("close_price", sa.Float(), nullable=False),
        schema=mode,
    )


def _create_views() -> None:
    for table in MODE_TABLES:
        union = " UNION ALL ".join(f"SELECT '{mode}'::text AS mode, * FROM {mode}.{table}" for mode in MODES)
        op.execute(f"CREATE VIEW {TRADING}.{table}_all AS {union}")


def upgrade() -> None:
    for schema in (TRADING, *MODES):
        op.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
    _create_public_tables()
    _create_trading_tables()
    for mode in MODES:
        _create_mode_tables(mode)
    _create_views()


def downgrade() -> None:
    for table in MODE_TABLES:
        op.execute(f"DROP VIEW IF EXISTS {TRADING}.{table}_all")
    for mode in MODES:
        for table in reversed(MODE_TABLES):
            op.drop_table(table, schema=mode)
    op.drop_table("promotions", schema=TRADING)
    op.drop_table("strategy_configs", schema=TRADING)
    op.drop_table("price_series")
    op.drop_table("time_series_reports")
    op.drop_table("time_series_cache")
    for schema in (*MODES, TRADING):
        op.execute(f"DROP SCHEMA IF EXISTS {schema}")
