"""Remove the partial-fetch mechanisms, and fetch the catalogue whole

`0007` added two columns so a deliberate omission could be told apart from a failed
fetch: `fred_category.excluded_reason` for a subtree not fetched at all, and
`fred_category_scan.page_limit` for one fetched only partly. That was the right answer to
the question it was asked. This migration removes the question.

Both columns existed to carry volume decisions inherited from the YAML export -- skip
state and county, keep one page per country -- made when the catalogue was collected by
hand, where "volume" meant somebody's afternoon. Collection is now paced, resumable and
idempotent, so the cost is wall-clock nobody waits on. Measured: the regional branch was
~10,400 requests and two hours, and was included on 2026-11-07. The country cap, the only
`page_limit` ever set, withheld 51,753 memberships and 7,690 series that exist nowhere
else in the catalogue -- for a saving of **69 requests**, about 41 seconds.

The cap was also arbitrary in a way nothing recorded. No `order_by` is sent, so FRED's
default applies and what survived was an alphabetical prefix of the series id: Germany
kept everything up to `DEURGDPH` and nothing after, and because ids are concept-prefixed
that is a systematic cut by concept rather than a sample. `DEU*` series were kept and
`LFU*`, `NGDP*`, `PRC*` were dropped whole. No reader would choose that slice; it is
where page one happened to end.

What replaces the pair is a stronger invariant, because it has no exceptions:
**`fetched_series_count` below `api_series_count` is a defect.** `status = 'ok'` now
means every series FRED reports was written, and no setting can make a short write
acceptable. The pair's distinction -- a choice versus a fault -- cost a configurable way
for data to be absent on purpose, discoverable only by whoever later debugged the gap and
traced it to a flag nobody set. For a pre-production catalogue with dependents still to
be written, that trade is not worth 41 seconds.

Lossless in practice: both columns are being dropped while every value in them is NULL.
`excluded_reason` was cleared across all 5,201 rows by the regional reversal, and
`page_limit` is reset to NULL by the re-fetch this migration accompanies.

Revision ID: 0012
Revises: 0011
Create Date: 2026-11-08
"""

import sqlalchemy as sa
from alembic import op

revision = "0012"
down_revision = "0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # `ok` used to mean "we wrote what we asked for". It now means "we wrote everything
    # FRED reports", and 38 rows hold the old `ok` because a cap lowered the bar. The
    # column that explained them is going away, so relabel them against the new rule --
    # otherwise they keep a verdict granted under a definition nothing records any more,
    # and `pending_categories` never offers them to a fetch.
    op.execute(
        sa.text(
            "UPDATE fred_category_scan SET status = 'incomplete' "
            " WHERE status = 'ok' AND fetched_series_count < api_series_count"
        )
    )

    op.drop_column("fred_category_scan", "page_limit")
    op.drop_index("ix_fred_category_excluded", table_name="fred_category")
    op.drop_column("fred_category", "excluded_reason")


def downgrade() -> None:
    # Restores the columns, not the decisions: every value was NULL when they were
    # dropped, so there is nothing to put back.
    op.add_column("fred_category", sa.Column("excluded_reason", sa.Text()))
    op.create_index(
        "ix_fred_category_excluded",
        "fred_category",
        ["excluded_reason"],
        postgresql_where=sa.text("excluded_reason IS NOT NULL"),
    )
    op.add_column("fred_category_scan", sa.Column("page_limit", sa.Integer()))
