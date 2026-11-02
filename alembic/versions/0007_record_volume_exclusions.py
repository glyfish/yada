"""Record what was deliberately not fetched, and why

Measuring the YAML export against the API found the catalogue short in several ways, and
I read all of them as defects. Two were decisions: country data and state data were
limited **on purpose, because of volume**. Nothing recorded that, so a later reader --
this session included -- cannot tell a deliberate omission from a failed fetch. Both
look like absence.

That is the same failure mode as the truncation itself, one level up. A short fetch that
says nothing is indistinguishable from a complete one; a skipped branch that says nothing
is indistinguishable from a bug. So the decision goes in the schema beside the data:

- **`fred_category.excluded_reason`** -- set on a subtree that is deliberately not
  fetched. The categories stay in the tree, so a browse can say "this branch exists and
  was excluded by volume" instead of showing an unexplained gap, and lifting the
  exclusion later needs no re-walk. `U.S. Regional Data > States` alone is 53 categories
  holding roughly 80,000 series before counties and metros, which is why it is out.

- **`fred_category_scan.page_limit`** -- the deliberate page ceiling for one category,
  where that is less than everything FRED has. Countries stay at one page of 1,000.
  Without this column a capped country reads as `status='incomplete'`, which is both
  alarming and wrong: `incomplete` means FRED had more than we managed to write, and
  resume would retry it on every run forever. With it, `status='ok'` means "we wrote
  what we asked for" while `api_series_count` still records what exists, so the gap
  stays visible and stops being a defect.

The distinction the pair buys: `api_series_count > fetched_series_count` with a
`page_limit` is a choice; the same inequality without one is a fault.

Design: sefer/planning/yada-fred-etf-postgres-design.md
Discovery policy: sefer/planning/yada-todo.md section 5

Revision ID: 0007
Revises: 0006
Create Date: 2026-11-01
"""

import sqlalchemy as sa
from alembic import op

revision = "0007"
down_revision = "0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Free text rather than a flag: the reason is the useful part, and a boolean would
    # have to be explained somewhere this table cannot reach.
    op.add_column("fred_category", sa.Column("excluded_reason", sa.Text()))
    op.create_index(
        "ix_fred_category_excluded",
        "fred_category",
        ["excluded_reason"],
        postgresql_where=sa.text("excluded_reason IS NOT NULL"),
    )

    # NULL means "fetch everything FRED reports", which is the default intent.
    op.add_column("fred_category_scan", sa.Column("page_limit", sa.Integer()))


def downgrade() -> None:
    op.drop_column("fred_category_scan", "page_limit")
    op.drop_index("ix_fred_category_excluded", table_name="fred_category")
    op.drop_column("fred_category", "excluded_reason")
