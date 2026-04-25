"""create time_series_cache table

Revision ID: 0001
Revises:
Create Date: 2026-04-25
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "time_series_cache",
        sa.Column(
            "cache_id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("source", sa.Text(), nullable=False),
        sa.Column("native_id", sa.Text(), nullable=False),
        sa.Column(
            "cached_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("observation_start", sa.Date(), nullable=False),
        sa.Column("observation_end", sa.Date(), nullable=False),
        sa.Column("observation_count", sa.Integer(), nullable=False),
        sa.Column("frequency", sa.Text(), nullable=True),
        sa.Column("units", sa.Text(), nullable=True),
        sa.Column("title", sa.Text(), nullable=True),
        sa.Column("data", JSONB(), nullable=False),
        sa.UniqueConstraint("source", "native_id", name="uq_source_native_id"),
    )

    op.create_index(
        "idx_tsc_source_native_id",
        "time_series_cache",
        ["source", "native_id"],
    )
    op.create_index(
        "idx_tsc_expires_at",
        "time_series_cache",
        ["expires_at"],
    )


def downgrade() -> None:
    op.drop_index("idx_tsc_expires_at", table_name="time_series_cache")
    op.drop_index("idx_tsc_source_native_id", table_name="time_series_cache")
    op.drop_table("time_series_cache")
