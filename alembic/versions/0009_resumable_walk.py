"""Record which categories the tree walk has visited

The series fetch is resumable: `fred_category_scan` stores a row per category, so a run
that dies resumes from what is not yet `ok`. **The walk is not.** It records the
categories it *found* but not the ones it *visited*, and those differ — a category is
found by asking its parent for children, and visited by asking it for its own.

That cost nothing while the walk was 1,030 requests. It costs about 45 minutes of a
2-hour regional run, because re-walking the 4,130 regional categories already discovered
means asking each one for children it has already told us about. There is also no way to
tell a genuine leaf from a node the walk never reached, which is exactly the ambiguity
that made the original export's gaps invisible.

`walked_at` resolves both. A resuming walk skips what it has visited; a category with
`walked_at IS NULL` is either new or unreached, and either way is work to do.

**The semantics matter.** Skipping a visited category means not noticing children FRED has
added since. That is right for resuming an interrupted run and wrong for a refresh, so the
caller chooses: resume skips, refresh revisits. Defaulting to skip would silently make
every later run a no-op; defaulting to revisit would make resume pointless. Neither is
safe as an implicit choice, so `walk_categories` takes it as an argument.

Revision ID: 0009
Revises: 0008
Create Date: 2026-11-07
"""

import sqlalchemy as sa
from alembic import op

revision = "0009"
down_revision = "0008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "fred_category", sa.Column("walked_at", sa.DateTime(timezone=True))
    )
    # Partial index on the unwalked set: that is what a resuming walk queries, and it
    # shrinks to nothing as the walk completes.
    op.create_index(
        "ix_fred_category_unwalked",
        "fred_category",
        ["category_id"],
        postgresql_where=sa.text("walked_at IS NULL"),
    )

    # The 1,058 fetchable categories were walked to completion on 2026-11-01 -- the walk
    # finished and reported 0 unreachable -- so backfill them rather than making the next
    # run redo verified work. Regional is deliberately left NULL: its walk was stopped
    # part way, and marking it walked would record a completeness we do not have.
    op.execute(
        """
        UPDATE fred_category
           SET walked_at = now()
         WHERE excluded_reason IS NULL
           AND category_path IS NOT NULL
        """
    )


def downgrade() -> None:
    op.drop_index("ix_fred_category_unwalked", table_name="fred_category")
    op.drop_column("fred_category", "walked_at")
