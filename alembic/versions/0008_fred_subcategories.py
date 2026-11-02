"""Derived subcategories, because FRED's taxonomy bottoms out too high

FRED curates 1,058 fetchable categories and then stops. Every one of the 134 categories
holding 500 or more series returns **zero children** from `category/children` -- checked
individually, no exceptions -- and the largest holds 53,187. So for most of the catalogue
there is no finer node upstream to fetch; subcategories have to be derived or they do not
exist.

The requirement they are built to: **a leaf holds at most 25 series**, so its contents can
be read and judged by eye. A ceiling, not an average, and the distinction is load-bearing
-- flat k-means at `k = n/25` put 37% of leaves over the cap holding 56% of the titles. The
cap is reached by recursive splitting instead, measured at 1.58x the leaf floor, which is
why `parent_subcategory_id` and `depth` exist: the tree's shape is data-dependent, 1 to 5
levels, not a fixed two.

Three columns carry the weight:

- **`concepts`** -- search terms generated alongside the name, deliberately including
  synonyms *absent* from the member titles. This is the vocabulary bridge, and it is what
  makes the whole structure findable with ordinary full-text search: measured on a sample,
  it took "steel making capacity", "heavy industry plant buildout" and "coal and coke
  production" to **first place** for a topic whose titles share no word with any of them.
  Lexical search over 424,634 titles returns nothing for all three.

- **`centroid`** -- the mean embedding of the leaf's members, as `real[]` because pgvector
  is not installed here. Stored so a resync can place a newly discovered series by nearest
  centroid without re-clustering or spending an LLM call. Without it every resync is a
  full rebuild.

- **`prompt_version`** / **`embed_model`** -- the name and concepts are model output, not
  source data. A changed prompt produces different names for identical input, so the
  version travels with the row; otherwise a half-rebuilt tree is indistinguishable from a
  consistent one. Same argument as `fred_category_scan.page_limit`, one layer up.

`fred_subcategory_build` records cost per category. The full run is ~31,000 LLM calls, and
a build that cannot say what it spent cannot be reasoned about before it is repeated.

Nothing is deleted on rebuild. A subcategory id may be referenced from outside this
schema, and an emptied leaf is marked, not dropped.

Design: sefer/planning/yada-fred-etf-postgres-design.md section 9
Procedure: sefer/planning/yada-fred-subcategory-procedure.md

Revision ID: 0008
Revises: 0007
Create Date: 2026-11-01
"""

import sqlalchemy as sa
from alembic import op

revision = "0008"
down_revision = "0007"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fred_subcategory",
        sa.Column("subcategory_id", sa.BigInteger(), primary_key=True,
                  autoincrement=True),
        sa.Column("category_id", sa.Integer(), nullable=False),
        # NULL means the node sits directly under the FRED category.
        sa.Column("parent_subcategory_id", sa.BigInteger()),
        # 1 is the first derived level. Varies by subtree by design.
        sa.Column("depth", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("concepts", sa.Text()),
        sa.Column("series_count", sa.Integer(), nullable=False,
                  server_default=sa.text("0")),
        sa.Column("is_leaf", sa.Boolean(), nullable=False,
                  server_default=sa.text("true")),
        # Mean unit-normalised embedding of the members. 256 dims.
        sa.Column("centroid", sa.ARRAY(sa.REAL())),
        sa.Column("prompt_version", sa.Text(), nullable=False),
        sa.Column("embed_model", sa.Text(), nullable=False),
        sa.Column("built_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("now()")),
        # An emptied leaf is marked, never dropped: the id may be referenced elsewhere.
        sa.Column("emptied_at", sa.DateTime(timezone=True)),
        sa.ForeignKeyConstraint(["category_id"], ["fred_category.category_id"],
                                ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["parent_subcategory_id"],
                                ["fred_subcategory.subcategory_id"],
                                ondelete="CASCADE"),
        sa.CheckConstraint("depth >= 1", name="ck_fred_subcategory_depth"),
    )
    op.create_index("ix_fred_subcategory_category", "fred_subcategory", ["category_id"])
    op.create_index("ix_fred_subcategory_parent", "fred_subcategory",
                    ["parent_subcategory_id"])
    # The leaf-size invariant is asserted against this, so it has to be cheap to scan.
    op.create_index("ix_fred_subcategory_leaf", "fred_subcategory",
                    ["category_id", "series_count"],
                    postgresql_where=sa.text("is_leaf AND emptied_at IS NULL"))

    # name + concepts is the search surface. Searching ~31,000 of these beats searching
    # 424,634 titles, which is the point of the whole layer.
    op.execute(
        """
        ALTER TABLE fred_subcategory
          ADD COLUMN name_tsv tsvector
          GENERATED ALWAYS AS (
              to_tsvector('english', name || ' ' || coalesce(concepts, ''))
          ) STORED
        """
    )
    op.create_index("ix_fred_subcategory_tsv", "fred_subcategory", ["name_tsv"],
                    postgresql_using="gin")

    op.create_table(
        "fred_series_subcategory",
        sa.Column("series_id", sa.Text(), nullable=False),
        sa.Column("subcategory_id", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("series_id", "subcategory_id"),
        sa.ForeignKeyConstraint(["series_id"], ["fred_series.series_id"],
                                ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["subcategory_id"],
                                ["fred_subcategory.subcategory_id"],
                                ondelete="CASCADE"),
    )
    op.create_index("ix_fred_series_subcategory_sub", "fred_series_subcategory",
                    ["subcategory_id"])

    op.create_table(
        "fred_subcategory_build",
        sa.Column("category_id", sa.Integer(), primary_key=True),
        sa.Column("status", sa.Text(), nullable=False,
                  server_default=sa.text("'pending'")),
        sa.Column("series_count", sa.Integer()),
        sa.Column("leaves", sa.Integer()),
        sa.Column("nodes", sa.Integer()),
        sa.Column("max_leaf_size", sa.Integer()),
        sa.Column("prompt_version", sa.Text()),
        sa.Column("embed_model", sa.Text()),
        sa.Column("llm_calls", sa.Integer()),
        # Recorded per category: the full run spends real money and a build that cannot
        # report its cost cannot be judged before being repeated.
        sa.Column("cost_usd", sa.Numeric(10, 5)),
        sa.Column("error", sa.Text()),
        sa.Column("started_at", sa.DateTime(timezone=True)),
        sa.Column("finished_at", sa.DateTime(timezone=True)),
        sa.ForeignKeyConstraint(["category_id"], ["fred_category.category_id"],
                                ondelete="CASCADE"),
        sa.CheckConstraint(
            "status IN ('pending', 'ok', 'over_cap', 'error', 'skipped')",
            name="ck_fred_subcategory_build_status",
        ),
    )
    op.create_index("ix_fred_subcategory_build_status", "fred_subcategory_build",
                    ["status"])


def downgrade() -> None:
    op.drop_table("fred_subcategory_build")
    op.drop_table("fred_series_subcategory")
    op.drop_index("ix_fred_subcategory_tsv", table_name="fred_subcategory")
    op.drop_index("ix_fred_subcategory_leaf", table_name="fred_subcategory")
    op.drop_index("ix_fred_subcategory_parent", table_name="fred_subcategory")
    op.drop_index("ix_fred_subcategory_category", table_name="fred_subcategory")
    op.drop_table("fred_subcategory")
