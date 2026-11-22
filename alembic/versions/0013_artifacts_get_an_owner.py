"""Give artifacts an owner, before there are any artifacts to orphan

Nothing in yada has needed the concept of a user: the server is one person's, bound to
loopback, and a report is simply *the* report. Saving artifacts changes that — a report
is something a person made, and the moment the server leaves 127.0.0.1 (`run()` already
warns it is unauthenticated there) "whose report is this" has no answer and no way to
acquire one retroactively.

So this adds the column while `time_series_reports` holds **zero rows**. The mechanism is
swappable afterwards and the schema is not: a report written today without an owner can
never be attributed, while an owner column nothing yet reads costs a migration and
changes no behaviour.

**Artifacts are owned; fetched data is shared.** `time_series_cache` deliberately gets no
owner. A FRED series is the same series for everyone, the TTL is a property of the
series' update cadence rather than of who asked, and per-user copies would multiply
fetches of identical data. Ownership belongs to what a person *made*, not to what the
server *retrieved* on their behalf.

**`created_by` is nullable, and that is the auth switch.** With no rows in `app_user` the
server runs exactly as it does now — unauthenticated, reports written with a NULL owner.
Insert the first user and a token becomes required. Adding a user is the act that turns
authentication on, so there is no separate flag that can disagree with the table.

**The token is stored hashed.** A bearer token in the database is a credential at rest,
and this one is read on every inbound message — headers are per-message on streamable
HTTP, not per-session, so the lookup is hot. `token_sha256` keeps the table from being
worth stealing. Create a user with:

    python -c "import hashlib; print(hashlib.sha256(b'<token>').hexdigest())"
    INSERT INTO app_user (name, token_sha256) VALUES ('troy', '<hash>');

`disabled_at` rather than DELETE is how a token is revoked, which is why the foreign key
restricts: deleting a user would destroy the attribution the column exists to carry.

`idx_tsr_report_title` is replaced by `(created_by, report_title)`. The plain index from
0001 served a title search that was always global; once a title is only meaningful within
one person's reports, the composite is the index that search actually uses — and titles
were never unique anyway, which is a defect this makes visible rather than creates.

Nothing reads either of these yet. Resolution (middleware reads the token, stamps the
owner) and enforcement (reads scoped to the owner) are separate changes, because
enforcement has to cover `api/main.py`'s CRUD surface and the four title-lookup sites
together or it leaves a bypass.

Revision ID: 0013
Revises: 0012
Create Date: 2026-11-22
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

revision = "0013"
down_revision = "0012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # `app_user`, not `user`: USER is a reserved word in Postgres and resolves to the
    # session user, so an unquoted reference would silently mean something else.
    op.create_table(
        "app_user",
        sa.Column("user_id", UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        # The sha256 of the bearer token, hex. Never the token itself -- see the module
        # docstring for how to mint one by hand.
        sa.Column("token_sha256", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("now()")),
        # Revocation. Set this rather than deleting the row, so the reports the user
        # made keep an owner that resolves to a name.
        sa.Column("disabled_at", sa.DateTime(timezone=True), nullable=True),
        sa.UniqueConstraint("token_sha256", name="uq_app_user_token"),
        sa.UniqueConstraint("name", name="uq_app_user_name"),
    )

    op.add_column(
        "time_series_reports",
        sa.Column("created_by", UUID(as_uuid=True), nullable=True),
    )
    # RESTRICT, not CASCADE or SET NULL. A user is disabled, never deleted; if one is
    # deleted anyway, failing loudly is better than silently unowning their reports or
    # silently destroying them.
    op.create_foreign_key(
        "fk_tsr_created_by", "time_series_reports", "app_user",
        ["created_by"], ["user_id"], ondelete="RESTRICT",
    )

    # No backfill. Every existing row's owner is genuinely unknown -- the column is being
    # added precisely because nothing recorded it -- and inventing one would make
    # "unowned, from before users existed" indistinguishable from "owned by troy".
    # The table holds zero rows today, so this is a statement about intent, not volume.

    # The 0001 index served a global title search. Titles are only meaningful within one
    # owner's set now, so lead with the owner; a lookup that still wants every match
    # across owners is a sequential scan it should not have been doing.
    op.drop_index("idx_tsr_report_title", table_name="time_series_reports")
    op.create_index("idx_tsr_owner_title", "time_series_reports",
                    ["created_by", "report_title"])


def downgrade() -> None:
    op.drop_index("idx_tsr_owner_title", table_name="time_series_reports")
    op.create_index("idx_tsr_report_title", "time_series_reports", ["report_title"])

    op.drop_constraint("fk_tsr_created_by", "time_series_reports", type_="foreignkey")
    op.drop_column("time_series_reports", "created_by")

    # Drops the users too, which is the real reversal: their only purpose was to own the
    # column above. The tokens were hashed, so nothing recoverable is lost -- a user
    # coming back means minting a new token anyway.
    op.drop_table("app_user")
