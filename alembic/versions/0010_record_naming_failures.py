"""Record how many nodes a category's build could not name

`parse_naming_reply` degrades a bad model reply to `UNNAMED (naming failed)` rather than
aborting. That is the right behaviour — one unparseable reply must not kill a build of
~36,000 nodes — but it means a failure is written into a browsable tree *as a name*,
beside a `fred_subcategory_build` row whose status says `ok`. The only record of it was a
counter in a process that then exited.

At ~36,000 calls for the non-regional half, even a 0.5% failure rate is ~180 nodes
labelled `UNNAMED` in the user-facing layer. `naming_failures` makes the per-category
count durable, so the categories worth rebuilding are a query rather than a log search.
`unnamed_nodes()` finds the offending rows themselves.

No index here. The two that looked missing — children-of-a-node and leaves-of-a-series —
are already covered: `ix_fred_subcategory_parent` exists, and `series_id` leads the
`fred_series_subcategory` primary key, so an index on it alone would be redundant.

Revision ID: 0010
Revises: 0009
Create Date: 2026-11-08
"""

import sqlalchemy as sa
from alembic import op

revision = "0010"
down_revision = "0009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "fred_subcategory_build",
        sa.Column("naming_failures", sa.Integer(), server_default="0"),
    )
    # Nothing to backfill: the two probe categories recorded 0 naming failures each,
    # which is what the server default already says. Writing a value we did not measure
    # would be worse than the column not existing.


def downgrade() -> None:
    op.drop_column("fred_subcategory_build", "naming_failures")
