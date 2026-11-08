"""Version the clustering, not just the prompt

`fred_subcategory` already stores `prompt_version` and `embed_model`, on the argument
that a name is model output and a tree half-built under two prompts is not a tree. The
same argument applies to the *shape*, and it was missing: the splitter is the other
thing that determines what a row says, and nothing recorded which one produced it.

That became load-bearing on 2026-11-08, when plain k-means was replaced with a
size-balanced assignment. k-means optimises cohesion and says nothing about size, and
because the recursion continues until every leaf is under the cap, one fat cluster is not
absorbed — it is amplified into depth. A 9,932-series category reached depth 8 with 1,105
nodes and 9 leaves holding one series each; balanced, it is depth 3 with 426 nodes and no
singletons.

Without this column, the two categories built under the old splitter would read as `ok`
and be skipped forever, leaving two trees in the catalogue shaped by rules nothing else
follows. With it they fall out of `pending_builds` as work to redo, which costs $0.01.

The backfill is `2026-11-01.kmeans` rather than NULL: we know exactly what built those
rows, and recording it is better than recording an absence.

Revision ID: 0011
Revises: 0010
Create Date: 2026-11-08
"""

import sqlalchemy as sa
from alembic import op

revision = "0011"
down_revision = "0010"
branch_labels = None
depends_on = None

#: What the splitter was before `balanced_clusters`.
PREVIOUS = "2026-11-01.kmeans"


def upgrade() -> None:
    for table in ("fred_subcategory", "fred_subcategory_build"):
        op.add_column(table, sa.Column("split_version", sa.Text()))
        op.execute(
            sa.text(
                f"UPDATE {table} SET split_version = :previous "  # noqa: S608
                "WHERE split_version IS NULL"
            ).bindparams(previous=PREVIOUS)
        )


def downgrade() -> None:
    for table in ("fred_subcategory", "fred_subcategory_build"):
        op.drop_column(table, "split_version")
