"""Who is calling: resolve a bearer token to an `app_user` row, per message.

Not per session. On streamable HTTP the SDK hands middleware the Starlette request for
the message being processed, and a `tools/call` on an established session carries *that
POST's* ``Authorization`` header rather than the one sent at ``initialize`` -- verified
against mcp 2.3.0. So identity is resolved on every inbound message and never cached
against a session id.

The switch is the table, not a flag
-----------------------------------
With **no rows in `app_user`** the server behaves exactly as it did before 0013:
unauthenticated, `current_user()` is None, artifacts are written with a NULL owner. That
is the local single-user case, and it is the default because it is what loopback
deployment has always been.

Insert **one user** and a token becomes required: a message with no token, an unknown
token, or a disabled user's token is refused. Adding a user is therefore the act that
turns authentication on, which is better than a flag that can disagree with the table --
`YADA_REQUIRE_AUTH=1` set against an empty table locks everyone out, and unset against a
populated one silently serves everyone's artifacts to anyone.

What this is NOT
----------------
`ServerMiddleware` runs *after* the HTTP request has been accepted, so a refusal here is
a JSON-RPC error, not a 401 with ``WWW-Authenticate``. That is adequate for a client
holding a configured token and inadequate for one that expects to discover how to
authenticate. Getting a real 401 means building the Starlette app
(``server.streamable_http_app(...)``) and running uvicorn directly, instead of
``server.run(...)``; the SDK's own ``token_verifier`` path does this, but it cannot be
used for a static token without also supplying `AuthSettings` with an `issuer_url`,
which is OAuth-shaped config for something that is not OAuth.

Tokens are compared by sha256. The database stores the hash, so a dump of `app_user` is
not a set of working credentials.
"""

from __future__ import annotations

import hashlib
from contextvars import ContextVar
from dataclasses import dataclass

import sqlalchemy as sa
from sqlalchemy.engine import Engine

from apps.core.environment import db_url
from lib.logger import get_logger

logger = get_logger("YADA")


class AuthRequired(Exception):
    """Users exist and this message carried no usable token."""


@dataclass(frozen=True, slots=True)
class Caller:
    user_id: str | None   # None when no users are configured
    name: str             # "anonymous" in that case, for the log


ANONYMOUS = Caller(user_id=None, name="anonymous")

_current: ContextVar[Caller] = ContextVar("yada_caller", default=ANONYMOUS)
_engine: Engine | None = None


def _conn():
    global _engine
    if _engine is None:
        _engine = sa.create_engine(db_url(), pool_pre_ping=True)
    return _engine.connect()


def current_caller() -> Caller:
    """The caller for the message being handled. ANONYMOUS outside a request."""
    return _current.get()


def current_user_id() -> str | None:
    """The owner to stamp on, and scope by. None when auth is off."""
    return _current.get().user_id


def bearer_of(headers) -> str | None:
    """Pull the token out of an Authorization header, case-insensitively."""
    if not headers:
        return None
    raw = headers.get("authorization") or headers.get("Authorization")
    if not raw:
        return None
    parts = raw.split(None, 1)
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None
    return parts[1].strip() or None


def resolve(token: str | None) -> Caller:
    """
    Resolve a token to a caller, or raise AuthRequired.

    Queried per message rather than cached: `app_user` is a handful of rows behind a
    unique index, and a cache would mean a revoked token keeps working for its lifetime
    -- which is the one thing revocation is for.
    """
    with _conn() as conn:
        users = conn.execute(sa.text(
            "SELECT count(*) FROM app_user WHERE disabled_at IS NULL")).scalar() or 0
        if users == 0:
            # Auth is off. Not an error, and not a warning either -- this is the
            # ordinary local case, and logging it every message would be noise.
            return ANONYMOUS
        if not token:
            # Channel-neutral: this message reaches an MCP client, which sends a
            # header, and a browser, which exchanges the token for a cookie at
            # POST /api/session. Naming one of them is wrong for the other.
            raise AuthRequired("This server requires a token.")
        digest = hashlib.sha256(token.encode()).hexdigest()
        row = conn.execute(sa.text("""
            SELECT user_id, name, disabled_at FROM app_user WHERE token_sha256 = :h"""),
            {"h": digest}).fetchone()

    if row is None:
        # Deliberately the same message as a disabled user: distinguishing them tells an
        # unauthenticated caller which of their guesses was once valid.
        raise AuthRequired("Token not recognised.")
    if row[2] is not None:
        raise AuthRequired("Token not recognised.")
    return Caller(user_id=str(row[0]), name=row[1])


def bind(headers) -> tuple[Caller, object]:
    """Resolve and install the caller for this message. Returns (caller, reset token)."""
    caller = resolve(bearer_of(headers))
    return caller, _current.set(caller)


def release(token) -> None:
    _current.reset(token)
