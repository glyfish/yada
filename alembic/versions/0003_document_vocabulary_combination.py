"""document store vocabulary combinations

What each store holds for every distinct COMBINATION of its indexed fields, so a
describe under a filter reports the filtered subset rather than the whole store.

0002 records marginals -- one row per (store, field, value) with that value's own
count. Marginals cannot answer a conjunction. Asked "what file types are in zgomot",
they can only offer the store-wide extension histogram: right shape, right counts,
wrong question, and plausible enough that a model will cite it. The only way to notice
is to already know zgomot is Ruby. That is the silent-mismatch failure the document
design exists to remove, so it must not be reintroduced by the tool meant to prevent it.

Asking Chroma instead is not an option: a filter matching 384 chunks costs 3.8 s
(measured 2026-10-24), against a tool whose premise is microseconds.

One row per distinct tuple rather than the design's two named cross-tabs
(`account->repo`, `repo->ext`), because the generic form answers ANY conjunction for
the same size and covers research_library's three fields, which pairs do not.

Measured cardinality -- four orders of magnitude below the chunk counts, as with 0002:

    github            961 rows   415,006 chunks   10,763 files
    research_library   64 rows     4,875 chunks       64 files

Revision ID: 0003
Revises: 0002
Create Date: 2026-10-24
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "document_vocabulary_combination",
        sa.Column("store", sa.Text(), nullable=False),
        # Every indexed field of this store with its value for these chunks, e.g.
        # {"account": "troystribling", "repo": "zgomot", "ext": ".rb"}. JSONB rather
        # than columns because the two stores share no fields, and metadata_filter.py
        # already filters Chroma-style where-dicts against JSONB in this database.
        #
        # NOT named `values`, though that reads better: SQLAlchemy's ColumnCollection
        # already has a .values() method, so `table.c.values` silently resolves to the
        # method rather than the column and fails as "may not be passed as a SQL
        # expression", a long way from anything mentioning this table.
        sa.Column("field_values", JSONB(), nullable=False),
        sa.Column("chunks", sa.Integer(), nullable=False),
        # Distinct files, not chunks. A describe reports both because they answer
        # different questions -- 340 chunks across 28 files in zgomot's Ruby.
        sa.Column("documents", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("store", "field_values"),
        sa.CheckConstraint("chunks > 0", name="ck_document_vocabulary_combination_chunks"),
        sa.CheckConstraint("documents > 0", name="ck_document_vocabulary_combination_documents"),
    )
    # Containment (`field_values @> '{"repo":"zgomot"}'`) is how a single resolved value is
    # queried. At ~1,000 rows a sequential scan would also do; the index is here so the
    # access pattern stays correct if a store grows.
    op.create_index("ix_document_vocabulary_combination_values",
                    "document_vocabulary_combination", ["field_values"],
                    postgresql_using="gin")


def downgrade() -> None:
    op.drop_index("ix_document_vocabulary_combination_values",
                  table_name="document_vocabulary_combination")
    op.drop_table("document_vocabulary_combination")
