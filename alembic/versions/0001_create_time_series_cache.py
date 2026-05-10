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
            "native_id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("source", sa.Text(), nullable=False),
        sa.Column("external_id", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("frequency", sa.Text(), nullable=False),
        sa.Column("metadata", JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("observations", JSONB(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("observation_start", sa.Date(), nullable=True),
        sa.Column("observation_end", sa.Date(), nullable=True),
        sa.UniqueConstraint("source", "external_id", "frequency", name="uq_tsc_source_external_frequency"),
    )

    op.create_index(
        "idx_tsc_source",
        "time_series_cache",
        ["source"],
    )
    op.create_index(
        "idx_tsc_external_id",
        "time_series_cache",
        ["external_id"],
    )
    op.create_index("idx_tsc_frequency", "time_series_cache", ["frequency"])
    op.create_index(
        "idx_tsc_metadata_gin",
        "time_series_cache",
        ["metadata"],
        postgresql_using="gin",
    )
    op.create_index("idx_tsc_expires_at", "time_series_cache", ["expires_at"])


def downgrade() -> None:
    op.drop_index("idx_tsc_expires_at", table_name="time_series_cache")
    op.drop_index("idx_tsc_metadata_gin", table_name="time_series_cache")
    op.drop_index("idx_tsc_frequency", table_name="time_series_cache")
    op.drop_index("idx_tsc_external_id", table_name="time_series_cache")
    op.drop_index("idx_tsc_source", table_name="time_series_cache")
    op.drop_table("time_series_cache")
