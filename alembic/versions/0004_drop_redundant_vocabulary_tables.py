"""drop the redundant vocabulary tables

`document_vocabulary` and `document_vocabulary_alias` are materialised derivations of
`document_vocabulary_combination`, which 0003 added. Measured against both live stores
on 2026-10-25, every figure reproduces exactly:

    marginals    sum chunks grouped by one key   -> identical for all 6 fields
    coverage     sum chunks where the key exists -> identical for all 6 fields
    surnames     split_authors + surname over the author values -> 22 of 22
    accounts     the account/repo pair in each github row       ->  2 of 2

The reverse does not hold: joints cannot be rebuilt from marginals, which is why
`describe_code(repo="zgomot")` needed 0003 in the first place. One direction of
derivation works, so there is one source of truth, and these two tables are not it.

They exist because 0002 came first. Keeping them means two write paths producing counts
that must agree -- they cannot disagree today, since one transaction writes both, but
nothing enforces it, and "the marginals say one thing and the joints another" is the
silent mismatch this whole design exists to remove.

`document_vocabulary_scan` stays. Two of its three columns are also derivable -- `chunks`
is the sum of the combination chunks and `collection` is a constant in code -- but
`built_at` is not, and the staleness warning is worth more with a date in it.

Irreversible in the strict sense: the downgrade recreates the tables empty, since their
contents come from a rebuild, not from this migration.

Revision ID: 0004
Revises: 0003
Create Date: 2026-10-25
"""

from alembic import op
import sqlalchemy as sa

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_index("ix_document_vocabulary_alias_lookup", table_name="document_vocabulary_alias")
    op.drop_table("document_vocabulary_alias")
    op.drop_index("ix_document_vocabulary_store_field", table_name="document_vocabulary")
    op.drop_table("document_vocabulary")


def downgrade() -> None:
    # Recreated empty, exactly as 0002 defined them. Run a rebuild to repopulate.
    op.create_table(
        "document_vocabulary",
        sa.Column("store", sa.Text(), nullable=False),
        sa.Column("field", sa.Text(), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.Column("chunks", sa.Integer(), nullable=False),
        sa.Column("field_chunks", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("store", "field", "value"),
        sa.CheckConstraint("chunks > 0", name="ck_document_vocabulary_chunks_positive"),
    )
    op.create_index("ix_document_vocabulary_store_field", "document_vocabulary", ["store", "field"])

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
