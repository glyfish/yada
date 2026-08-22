"""
environment.py

Which environment -- and therefore which database -- this process talks to.

``YADA_ENV`` selects the environment: ``dev`` (the default, so a missing setting can
never land on production data) or ``prod``. Each maps to its own database
(``yada_dev`` / ``yada``). ``YADA_DB_URL`` may override the URL for non-default hosts
or credentials, but it must agree with ``YADA_ENV`` -- an override pointing at the
other environment's database is rejected.

Every reader of the database URL (the series/report caches, ``TradingDb``, alembic)
resolves it here, and the API verifies the database on startup: its schema must be
at the code's alembic head and the trading schemas must exist, or the process refuses
to serve (see ``verify_database``).
"""

from __future__ import annotations

import os
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[2]

ENVIRONMENTS = {
    "dev": "postgresql://yada@localhost/yada_dev",
    "prod": "postgresql://yada@localhost/yada",
}
DEFAULT_ENVIRONMENT = "dev"

# Schemas the trading layer relies on (created by the initial migration).
REQUIRED_SCHEMAS = ("trading", "backtest", "paper", "live")


class EnvironmentConfigError(RuntimeError):
    """YADA_ENV / YADA_DB_URL are inconsistent or invalid."""


class DatabaseStateError(RuntimeError):
    """The environment's database is not in the state the code expects."""


def _database_of(url: str) -> str:
    return url.rsplit("/", 1)[-1].split("?", 1)[0]


def _redact(url: str) -> str:
    return re.sub(r"://([^:/@]+):[^@]*@", r"://\1:***@", url)


@dataclass(frozen=True)
class Environment:
    name: str
    db_url: str

    @property
    def database(self) -> str:
        return _database_of(self.db_url)

    def describe(self) -> str:
        return f"environment={self.name} database={self.database} url={_redact(self.db_url)}"


def current_environment(environ: Mapping[str, str] | None = None) -> Environment:
    """
    Resolve the environment from ``YADA_ENV`` (+ optional ``YADA_DB_URL``). With no
    explicit mapping the process environment is used, after loading the project's
    ``.env`` (values already in the shell take precedence).
    """

    if environ is None:
        load_dotenv(ROOT / ".env")
        environ = os.environ

    name = (environ.get("YADA_ENV") or DEFAULT_ENVIRONMENT).strip().lower()
    if name not in ENVIRONMENTS:
        raise EnvironmentConfigError(f"YADA_ENV={name!r} is not one of {sorted(ENVIRONMENTS)}")

    url = (environ.get("YADA_DB_URL") or "").strip() or ENVIRONMENTS[name]
    database = _database_of(url)
    for other, other_url in ENVIRONMENTS.items():
        if other != name and database == _database_of(other_url):
            raise EnvironmentConfigError(
                f"YADA_DB_URL points at the {other} database ({database}) but YADA_ENV={name}")
    return Environment(name, url)


def db_url() -> str:
    """The current environment's database URL."""
    return current_environment().db_url


def alembic_head() -> str | None:
    """The schema revision the code expects (the head of the alembic chain)."""

    from alembic.config import Config
    from alembic.script import ScriptDirectory

    return ScriptDirectory.from_config(Config(str(ROOT / "alembic.ini"))).get_current_head()


def verify_database(environment: Environment | None = None) -> str:
    """
    Check that the environment's database is migrated to the code's alembic head and
    has the trading schemas. Returns a one-line description; raises
    ``DatabaseStateError`` otherwise.
    """

    from alembic.runtime.migration import MigrationContext
    from sqlalchemy import create_engine, inspect

    environment = environment or current_environment()
    head = alembic_head()
    engine = create_engine(environment.db_url, pool_pre_ping=True)
    try:
        with engine.connect() as connection:
            current = MigrationContext.configure(connection).get_current_revision()
            schemas = set(inspect(connection).get_schema_names())
    finally:
        engine.dispose()

    problems = []
    if current != head:
        problems.append(f"schema revision {current or 'none'} != code head {head} "
                        f"(run: YADA_ENV={environment.name} alembic upgrade head)")
    missing = [s for s in REQUIRED_SCHEMAS if s not in schemas]
    if missing:
        problems.append(f"missing schemas {missing}")
    if problems:
        raise DatabaseStateError(f"{environment.describe()}: " + "; ".join(problems))
    return f"{environment.describe()} revision={current}"
