"""document store vocabulary

The distinct metadata values held by each Chroma document store, with their chunk
counts. Derived data, rebuilt by the loader -- never edited by hand.

It exists because Chroma cannot answer "what values does this field have?" without a
full scan: 33.5 s over github's 415,006 chunks, and 4.0 s even for a filter matching
384. The values themselves are four orders of magnitude smaller than the chunks --
101 repositories, 190 extensions, 27 authors -- so they are cheap to hold and
microseconds to read.

Four consumers (see sefer/planning/yada-document-mcp-design.md §5): filter resolution,
the generated tool descriptions, the describe_* tools, and the extractor's prompt.

public  document_vocabulary       one row per (store, field, value)
        document_vocabulary_alias one row per (store, field, alias -> value), so a
                                  surname can reach the full names containing it
        document_vocabulary_scan  one row per store: when it was built and against
                                  how many chunks, for the staleness check

Revision ID: 0002
Revises: 0001
Create Date: 2026-10-24
"""

from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "document_vocabulary",
        sa.Column("store", sa.Text(), nullable=False),
        sa.Column("field", sa.Text(), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.Column("chunks", sa.Integer(), nullable=False),
        # Present-on count for the FIELD, repeated per row. A field below the store's
        # chunk total is partial, and a filter on it silently excludes the chunks that
        # lack it -- so the generated description has to say so (design §5).
        sa.Column("field_chunks", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("store", "field", "value"),
        sa.CheckConstraint("chunks > 0", name="ck_document_vocabulary_chunks_positive"),
    )
    op.create_index("ix_document_vocabulary_store_field", "document_vocabulary", ["store", "field"])

    # A value reachable by a name that is not itself a stored value: 'Matthaeus' ->
    # 'W. H. Matthaeus' and 'William H. Matthaeus'. Many-to-many, because one surname
    # covers several spellings and one full name yields one surname.
    op.create_table(
        "document_vocabulary_alias",
        sa.Column("store", sa.Text(), nullable=False),
        sa.Column("field", sa.Text(), nullable=False),
        sa.Column("alias", sa.Text(), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.Column("kind", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("store", "field", "alias", "value"),
        sa.CheckConstraint("kind in ('surname','account')", name="ck_document_vocabulary_alias_kind"),
    )
    op.create_index("ix_document_vocabulary_alias_lookup",
                    "document_vocabulary_alias", ["store", "field", "alias"])

    # The staleness check. Compared against collection.count() on first use rather
    # than at boot: count() alone costs 3.8 s on github, and a server that stays up
    # for days should not pay it per restart (design §5).
    op.create_table(
        "document_vocabulary_scan",
        sa.Column("store", sa.Text(), primary_key=True),
        sa.Column("collection", sa.Text(), nullable=False),
        sa.Column("chunks", sa.Integer(), nullable=False),
        sa.Column("built_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("now()")),
    )


def downgrade() -> None:
    op.drop_table("document_vocabulary_scan")
    op.drop_index("ix_document_vocabulary_alias_lookup", table_name="document_vocabulary_alias")
    op.drop_table("document_vocabulary_alias")
    op.drop_index("ix_document_vocabulary_store_field", table_name="document_vocabulary")
    op.drop_table("document_vocabulary")
