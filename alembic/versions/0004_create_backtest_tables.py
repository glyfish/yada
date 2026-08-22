"""create backtest schema and tables

Moves the backtrader persistence tables into the yada database, in their own
`backtest` schema (they previously lived in a separate `backtest` database managed
from alef). Column definitions mirror the ORM models in
apps/backtrader/db/backtest_db.py, which are the source of truth for what the
backtest code writes.

Revision ID: 0004
Revises: 0003
Create Date: 2026-08-22
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None

SCHEMA = "backtest"


def upgrade() -> None:
    op.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

    op.create_table(
        "backtests",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("time_stamp", sa.DateTime(), nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("strategy", sa.String(length=256), primary_key=True, nullable=False),
        schema=SCHEMA,
    )
    op.create_table(
        "broker",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("time_stamp", sa.DateTime(), nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("strategy", sa.String(length=256), nullable=False),
        sa.Column("cash", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        schema=SCHEMA,
    )
    op.create_table(
        "positions",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("adjbase", sa.Float(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("price_orig", sa.Float(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("upclosed", sa.Float(), nullable=False),
        sa.Column("upopened", sa.Float(), nullable=False),
        sa.Column("updt", sa.Date(), nullable=False),
        schema=SCHEMA,
    )
    op.create_table(
        "trades",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("ref", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("status", sa.String(length=256), nullable=False),
        sa.Column("trade_id", sa.Integer(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("commission", sa.Float(), nullable=False),
        sa.Column("pnl", sa.Float(), nullable=False),
        sa.Column("pnlcomm", sa.Float(), nullable=False),
        sa.Column("dtclose", sa.Date(), nullable=False),
        sa.Column("dtopen", sa.Date(), nullable=False),
        sa.Column("baropen", sa.Integer(), nullable=False),
        sa.Column("barclose", sa.Integer(), nullable=False),
        sa.Column("barlen", sa.Integer(), nullable=False),
        sa.Column("is_long", sa.Boolean(), nullable=False),
        schema=SCHEMA,
    )
    op.create_table(
        "orders",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("order_status", sa.String(length=256), nullable=False),
        sa.Column("order_type", sa.String(length=256), nullable=False),
        sa.Column("trade_id", sa.Integer(), nullable=True),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("commission", sa.Float(), nullable=False),
        sa.Column("pnl", sa.Float(), nullable=False),
        sa.Column("exec_type", sa.String(length=256), nullable=False),
        schema=SCHEMA,
    )
    op.create_table(
        "analyzers",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("analyzer", sa.String(length=256), nullable=False),
        sa.Column("value", JSONB, nullable=False),
        sa.Column("parameters", JSONB, nullable=True),
        schema=SCHEMA,
    )
    op.create_table(
        "indicators",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("indicator", sa.String(length=256), nullable=False),
        sa.Column("value", JSONB, nullable=False),
        sa.Column("params", JSONB, nullable=True),
        schema=SCHEMA,
    )
    op.create_table(
        "asset_prices",
        sa.Column("run_id", sa.String(length=256), primary_key=True, nullable=False),
        sa.Column("date", sa.Date(), primary_key=True, nullable=False),
        sa.Column("ensemble_id", sa.String(length=256), nullable=False),
        sa.Column("ticker", sa.String(length=256), nullable=False),
        sa.Column("open_price", sa.Float(), nullable=False),
        sa.Column("high_price", sa.Float(), nullable=False),
        sa.Column("low_price", sa.Float(), nullable=False),
        sa.Column("close_price", sa.Float(), nullable=False),
        schema=SCHEMA,
    )
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
        schema=SCHEMA,
    )


def downgrade() -> None:
    for table in ("price_series", "asset_prices", "indicators", "analyzers",
                  "orders", "trades", "positions", "broker", "backtests"):
        op.drop_table(table, schema=SCHEMA)
    op.execute(f"DROP SCHEMA IF EXISTS {SCHEMA}")
