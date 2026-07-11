"""add ttl_days to time_series_cache

Records the per-series time-to-live (in days) used to compute expires_at. Derived
from the series' update frequency on first fetch and preserved across re-fetches, so
it can be inspected and overridden per series. Nullable: existing rows are populated
on their next fetch, and reads rely on expires_at, not ttl_days.

Revision ID: 0003
Revises: 0002
Create Date: 2026-07-05
"""

from alembic import op
import sqlalchemy as sa

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("time_series_cache", sa.Column("ttl_days", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("time_series_cache", "ttl_days")
