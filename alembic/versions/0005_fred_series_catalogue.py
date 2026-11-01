"""FRED series discovery in Postgres

The `fred` Chroma store moves here. It is a relational table wearing a vector store,
and the vector store was hiding two defects in it.

**Titles do not identify series.** 19,441 titles are shared by 54,111 series -- 44% of
the store -- and they are identical, not similar. What separates them is never in the
text: observation_start (63.5% of collisions), observation_end (62.2%), popularity
(60.0%), frequency (54.8%), seasonal_adjustment (41.3%), units (33.9%). Eighteen series
share the title "International Merchandise Trade Statistics: Exports: Commodi...",
differing only by units and seasonal adjustment. An embedding of those eighteen is the
same vector -- not hard to rank, nothing to rank with. So for nearly half the store,
selection is a filter problem by construction, and `units` and `seasonal_adjustment`
are indexed here because they are filters rather than columns that happen to be stored.

**series_id is not unique in the source.** 145,679 rows for 123,119 series, because a
series appears once per category it belongs to. Hence the membership table: a search
that does not collapse those returns the same series up to six times.

Two derived columns, both computed at load because neither can be reconstructed from a
query:

- `frequency_class` -- the source spells 41 variants of about eight frequencies.
  `frequency = 'Quarterly'` silently drops the 1,109 series spelled
  "Quarterly, End of Quarter" or "Quarterly, End of Period".
- `currently_relevant` -- two-thirds of the store is discontinued, so this is the
  highest-value filter available, and a flat date cutoff gets it catastrophically
  wrong. Annual is the largest class (56,170 series) and only 176 of them end in 2025
  or later; `observation_end >= '2025-01-01'` would mark 22,200 perfectly current
  annual series as dead. Currency has to be measured in PERIODS. See
  `fred_frequency_class` for the derived cutoffs, which are stored so the tool can
  state the definition it applied rather than hiding it.

Design: sefer/planning/yada-fred-etf-postgres-design.md

Revision ID: 0005
Revises: 0004
Create Date: 2026-11-01
"""

from alembic import op
import sqlalchemy as sa

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fred_series",
        sa.Column("series_id", sa.Text(), primary_key=True),
        sa.Column("series_title", sa.Text(), nullable=False),
        sa.Column("units", sa.Text()),
        # Raw, all 41 spellings, for display. frequency_class is what filters.
        sa.Column("frequency", sa.Text()),
        sa.Column("frequency_class", sa.Text()),
        sa.Column("seasonal_adjustment", sa.Text()),
        sa.Column("observation_start", sa.Date()),
        sa.Column("observation_end", sa.Date()),
        sa.Column("last_updated", sa.DateTime(timezone=True)),
        sa.Column("popularity", sa.Integer()),
        sa.Column("currently_relevant", sa.Boolean(), nullable=False,
                  server_default=sa.text("false")),
    )

    # Generated rather than maintained: a trigger or an application write could fall out
    # of step with the title, and a stale search index is the failure this whole move is
    # meant to remove.
    op.execute("""
        ALTER TABLE fred_series ADD COLUMN title_tsv tsvector
        GENERATED ALWAYS AS (to_tsvector('english', series_title)) STORED
    """)
    op.execute("CREATE INDEX idx_fred_series_title_tsv ON fred_series USING GIN (title_tsv)")

    op.create_index("idx_fred_series_freq_start", "fred_series",
                    ["frequency_class", "observation_start"])
    op.create_index("idx_fred_series_start", "fred_series", ["observation_start"])
    # Partial: the filter is only ever used in the positive direction.
    op.execute("""
        CREATE INDEX idx_fred_series_current ON fred_series (currently_relevant)
        WHERE currently_relevant
    """)
    # The two that separate identically-titled series.
    op.create_index("idx_fred_series_units", "fred_series", ["units"])
    op.create_index("idx_fred_series_seasonal", "fred_series", ["seasonal_adjustment"])

    op.create_table(
        "fred_category",
        sa.Column("category_id", sa.Integer(), primary_key=True),
        # `leaf_name` is deliberately absent: measured identical to category_name on
        # 0 of 145,679 source rows. Two spellings of one fact is what put 15 wrong
        # rows in a Goose table when `repo` sat beside `account/repo`.
        sa.Column("category_name", sa.Text(), nullable=False),
        # A property of the category, which is why it varies across 100% of series
        # that appear more than once.
        sa.Column("category_path", sa.Text()),
    )

    op.create_table(
        "fred_series_category",
        sa.Column("series_id", sa.Text(),
                  sa.ForeignKey("fred_series.series_id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column("category_id", sa.Integer(),
                  sa.ForeignKey("fred_category.category_id", ondelete="CASCADE"),
                  nullable=False),
        sa.PrimaryKeyConstraint("series_id", "category_id",
                                name="pk_fred_series_category"),
    )
    op.create_index("idx_fsc_category", "fred_series_category", ["category_id"])

    op.create_table(
        "fred_frequency_class",
        # Why this exists: `currently_relevant` is a boolean whose meaning differs per
        # class, so a tool reporting it has to be able to say WHICH cutoff it applied.
        # Without this the definition is invisible to the caller and unauditable later.
        sa.Column("frequency_class", sa.Text(), primary_key=True),
        sa.Column("period_days", sa.Integer(), nullable=False),
        # p95 rather than max: projections push annual's max to 2030-01-01 against a
        # p95 of 2024-01-01, and a max-anchored cutoff would sit at 2028 and match
        # nothing.
        sa.Column("p95_observation_end", sa.Date()),
        sa.Column("currency_cutoff", sa.Date()),
        sa.Column("series_count", sa.Integer(), nullable=False,
                  server_default=sa.text("0")),
        sa.Column("built_at", sa.DateTime(timezone=True),
                  server_default=sa.text("now()"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("fred_frequency_class")
    op.drop_index("idx_fsc_category", table_name="fred_series_category")
    op.drop_table("fred_series_category")
    op.drop_table("fred_category")
    op.drop_index("idx_fred_series_seasonal", table_name="fred_series")
    op.drop_index("idx_fred_series_units", table_name="fred_series")
    op.execute("DROP INDEX IF EXISTS idx_fred_series_current")
    op.drop_index("idx_fred_series_start", table_name="fred_series")
    op.drop_index("idx_fred_series_freq_start", table_name="fred_series")
    op.execute("DROP INDEX IF EXISTS idx_fred_series_title_tsv")
    op.drop_table("fred_series")
