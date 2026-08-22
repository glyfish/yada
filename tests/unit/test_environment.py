"""
Hermetic tests for environment resolution (apps/core/environment.py). Explicit
mappings are passed so neither the process environment nor .env is consulted.
"""

import pytest

from apps.core.environment import (
    DEFAULT_ENVIRONMENT, ENVIRONMENTS, Environment, EnvironmentConfigError, alembic_head,
    current_environment,
)


def test_default_is_dev_and_never_prod():
    env = current_environment({})
    assert env.name == DEFAULT_ENVIRONMENT == "dev"
    assert env.database == "yada_dev"
    assert env.db_url == ENVIRONMENTS["dev"]


def test_prod_must_be_asked_for():
    env = current_environment({"YADA_ENV": "prod"})
    assert env.name == "prod" and env.database == "yada"


def test_environment_name_is_case_insensitive_and_validated():
    assert current_environment({"YADA_ENV": " Prod "}).name == "prod"
    with pytest.raises(EnvironmentConfigError):
        current_environment({"YADA_ENV": "staging"})


def test_url_override_is_honoured():
    env = current_environment({"YADA_ENV": "dev", "YADA_DB_URL": "postgresql://u:pw@db.example:5432/yada_dev"})
    assert env.db_url.startswith("postgresql://u:pw@db.example") and env.database == "yada_dev"


def test_override_pointing_at_the_other_environment_is_rejected():
    with pytest.raises(EnvironmentConfigError):
        current_environment({"YADA_ENV": "dev", "YADA_DB_URL": "postgresql://yada@localhost/yada"})
    with pytest.raises(EnvironmentConfigError):
        current_environment({"YADA_ENV": "prod", "YADA_DB_URL": "postgresql://yada@localhost/yada_dev"})


def test_describe_redacts_credentials():
    env = Environment("dev", "postgresql://user:secret@localhost:5432/yada_dev?sslmode=require")
    assert env.database == "yada_dev"
    assert "secret" not in env.describe()
    assert "user:***@" in env.describe()


def test_code_head_is_the_rolled_up_initial_schema():
    assert alembic_head() == "0001"
