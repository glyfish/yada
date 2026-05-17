"""create time_series_reports table

Revision ID: 0002
Revises: 0001
Create Date: 2026-05-02
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "time_series_reports",
        sa.Column(
            "report_id",
            UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("report_title", sa.Text(), nullable=False),
        sa.Column("report_description", sa.Text(), nullable=False, server_default=""),
        sa.Column("time_series_info", JSONB(), nullable=False, server_default=sa.text("'[]'::jsonb")),
        sa.Column("time_range_from", sa.Date(), nullable=False),
        sa.Column("time_range_to", sa.Date(), nullable=True),
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
    )

    op.create_index(
        "idx_tsr_report_title",
        "time_series_reports",
        ["report_title"],
    )
    op.create_index(
        "idx_tsr_time_series_info_gin",
        "time_series_reports",
        ["time_series_info"],
        postgresql_using="gin",
    )


def downgrade() -> None:
    op.drop_index("idx_tsr_time_series_info_gin", table_name="time_series_reports")
    op.drop_index("idx_tsr_report_title", table_name="time_series_reports")
    op.drop_table("time_series_reports")
