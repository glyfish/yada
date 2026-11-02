"""FRED discovery from the API, with the tree it actually has

`0005` built the catalogue from the YAML export under `clients/fred/`. Measuring that
export against the API found three faults, none of which announces itself:

**The series lists are truncated at 1,000.** Eighty categories hold exactly 1,000
series, which is a page size, not a count. Their true totals sum to 225,192 against
80,000 stored -- **145,192 missing memberships, 64.5% of those categories**. `Poverty`
holds 1,000 of 9,932; `Stock Market Indexes` 1,000 of 9,707. The export took the first
page and stopped.

**The tree is rooted one level too low.** FRED's root has eight categories. The export
stored twelve "top-level" names because seven of them are second-level: `Countries`,
`Geography`, `Indicators` and `Institutions` are children of `International Data`, and
`Census Regions`, `BEA Regions` and `BLS Regions` are children of `U.S. Regional Data`.
Every path under them is missing its real prefix, so the hierarchy is wrong at the top
-- and `category_path` was the only record of parentage. Hence `parent_id`: the edge
belongs in a column, with the path derived from it rather than the reverse.

**A whole branch is absent.** `Production & Business Activity` (category 1) was never
downloaded: 3,274 series directly plus sixteen children, among them `Construction` and
`Housing`. `U.S. Regional Data` is missing `States`, `Federal Reserve Districts` and
`Freddie Mac Regions`.

A file hand-off cannot report any of this. It has no transaction, no row count and no
reconciliation, so a pass that fetched one page of nine looks exactly like one that
fetched everything. `fred_category_scan` is the fix in schema form: it stores what FRED
said the count was next to what we actually wrote, so an incomplete fetch is a row that
says so rather than an absence nobody can see.

`notes` arrives here too. 93.8% of series carry it, mean 509 characters, and it was the
only substantive source field `0005` dropped. It is the input the derived subcategory
names are generated from -- the titles alone are too thin, and the category is too
coarse.

Design: sefer/planning/yada-fred-etf-postgres-design.md
Discovery policy: sefer/planning/yada-todo.md section 5

Revision ID: 0006
Revises: 0005
Create Date: 2026-11-01
"""

import sqlalchemy as sa
from alembic import op

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # The tree edge. Nullable because FRED's eight roots have no parent, and because a
    # category reached before its parent during a walk is written parentless and fixed
    # on the next pass rather than failing the run.
    op.add_column("fred_category", sa.Column("parent_id", sa.Integer()))
    op.create_index("ix_fred_category_parent", "fred_category", ["parent_id"])

    # The source field 0005 dropped. No index: it is naming input, not a filter, and
    # the measurement that matters is that only 28.8% of notes are distinct -- 19,332
    # series share one identical sentence -- so it must not become a search column.
    op.add_column("fred_series", sa.Column("notes", sa.Text()))

    # What FRED said, beside what we wrote. The point of the table is the pair.
    op.create_table(
        "fred_category_scan",
        sa.Column("category_id", sa.Integer(), primary_key=True),
        # FRED's own `count` for this category, from the first page of the fetch.
        sa.Column("api_series_count", sa.Integer()),
        # Distinct series actually written for it. Equal to api_series_count on a
        # complete fetch; anything else is the truncation 0005 could not detect.
        sa.Column("fetched_series_count", sa.Integer()),
        sa.Column("pages", sa.Integer(), nullable=False, server_default=sa.text("0")),
        # 'ok' when the two counts agree, 'incomplete' when they do not, 'error' when
        # the fetch raised. Only 'ok' is skipped on resume.
        sa.Column("status", sa.Text(), nullable=False, server_default=sa.text("'pending'")),
        sa.Column("error", sa.Text()),
        sa.Column("started_at", sa.DateTime(timezone=True)),
        sa.Column("finished_at", sa.DateTime(timezone=True)),
        sa.CheckConstraint(
            "status IN ('pending', 'ok', 'incomplete', 'error')",
            name="ck_fred_category_scan_status",
        ),
    )
    # Resume reads this: everything not yet 'ok'.
    op.create_index(
        "ix_fred_category_scan_status", "fred_category_scan", ["status"]
    )


def downgrade() -> None:
    op.drop_index("ix_fred_category_scan_status", table_name="fred_category_scan")
    op.drop_table("fred_category_scan")
    op.drop_column("fred_series", "notes")
    op.drop_index("ix_fred_category_parent", table_name="fred_category")
    op.drop_column("fred_category", "parent_id")
