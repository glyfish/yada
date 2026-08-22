"""
Hermetic tests for the trading persistence layer: config identity, table
definitions, and value normalisation. No database is touched -- SQLAlchemy engines
are lazy, so constructing a TradingDb does not connect.
"""

from datetime import date, datetime, UTC, timedelta, timezone

import numpy
import pytest

from apps.backtrader.db.trading_db import (
    MODES, MODE_TABLES, TRADING_SCHEMA, TradingDb, build_metadata, config_id, jsonable, mode_metadata,
    public_metadata, to_ts, trading_metadata,
)
from apps.backtrader.db.backtest_db import BacktestDb

URL = "postgresql://nobody@localhost/unused"


def test_config_id_is_stable_and_order_independent():
    a = config_id("LongZScore", {"half_life": 124, "stake_multiple": 100}, ["CAD=X", "EUR=X"])
    b = config_id("LongZScore", {"stake_multiple": 100, "half_life": 124}, ["EUR=X", "CAD=X"])
    assert a == b
    assert len(a) == 16


def test_config_id_changes_with_strategy_params_or_universe():
    base = config_id("LongZScore", {"half_life": 124}, ["CAD=X"])
    assert config_id("ShortZScore", {"half_life": 124}, ["CAD=X"]) != base
    assert config_id("LongZScore", {"half_life": 125}, ["CAD=X"]) != base
    assert config_id("LongZScore", {"half_life": 124}, ["EUR=X"]) != base


@pytest.mark.parametrize("mode", MODES)
def test_mode_metadata_defines_the_full_table_set_in_its_own_schema(mode):
    metadata = mode_metadata(mode)
    assert {n for n in metadata.tables if n.startswith(f"{mode}.")} == {f"{mode}.{t}" for t in MODE_TABLES}

    runs = metadata.tables[f"{mode}.runs"]
    assert [fk.target_fullname for fk in runs.c.config_id.foreign_keys] == [f"{TRADING_SCHEMA}.strategy_configs.config_id"]

    for name in MODE_TABLES:
        if name == "runs":
            continue
        fks = list(metadata.tables[f"{mode}.{name}"].c.run_id.foreign_keys)
        assert fks and fks[0].target_fullname == f"{mode}.runs.run_id"
        assert fks[0].ondelete == "CASCADE", f"{mode}.{name} rows must go with their run"


def test_mode_tables_are_identical_across_modes():
    def shape(metadata, mode):
        return {name.split(".", 1)[1]: [(c.name, type(c.type).__name__, c.nullable, c.primary_key)
                                        for c in table.columns]
                for name, table in metadata.tables.items() if name.startswith(f"{mode}.")}
    shapes = [shape(mode_metadata(m), m) for m in MODES]
    assert shapes[0] == shapes[1] == shapes[2]


def test_event_tables_allow_many_rows_per_bar():
    # Orders and trades are event logs: a ref passes through several states, and live
    # trading fills intraday -- so neither (run_id, ts) nor (run_id, ref) may be the key.
    for name in ("orders", "trades"):
        table = mode_metadata("live").tables[f"live.{name}"]
        assert [c.name for c in table.primary_key.columns] == ["id"]


def test_shared_and_reference_tables():
    assert set(trading_metadata().tables) == {f"{TRADING_SCHEMA}.strategy_configs", f"{TRADING_SCHEMA}.promotions"}
    assert set(public_metadata().tables) == {"price_series"}


def test_build_metadata_holds_every_owned_table():
    metadata = build_metadata()
    assert len(metadata.tables) == 2 + 1 + 3 * len(MODE_TABLES)
    # foreign keys resolve within the one MetaData (this is what alembic's comparison needs):
    # every mode's runs table sorts after the strategy_configs table it references
    order = [t.fullname for t in metadata.sorted_tables]
    for mode in MODES:
        assert order.index(f"{TRADING_SCHEMA}.strategy_configs") < order.index(f"{mode}.runs")


def test_mode_metadata_rejects_unknown_mode():
    with pytest.raises(ValueError):
        mode_metadata("prod")


def test_trading_db_mode_selects_schema():
    db = TradingDb("paper", url=URL)
    assert db.schema == "paper"
    assert db.table("orders").schema == "paper"
    assert db.strategy_configs.schema == TRADING_SCHEMA
    assert db.price_series.schema is None


def test_trading_db_rejects_unknown_mode():
    with pytest.raises(ValueError):
        TradingDb("prod", url=URL)


def test_backtest_db_is_the_backtest_mode():
    assert BacktestDb(url=URL).mode == "backtest"


def test_jsonable_makes_values_storable():
    when = datetime(2026, 1, 2, 3, 4, 5)
    value = {when: numpy.float64(1.5), "nested": [numpy.int64(3), (date(2026, 1, 2),)], 2024: None}
    assert jsonable(value) == {when.isoformat(): 1.5, "nested": [3, ["2026-01-02"]], "2024": None}


def test_to_ts_normalises_to_aware_utc():
    assert to_ts(None) is None
    assert to_ts(date(2026, 1, 2)) == datetime(2026, 1, 2, tzinfo=UTC)
    assert to_ts(datetime(2026, 1, 2, 15, 30)) == datetime(2026, 1, 2, 15, 30, tzinfo=UTC)
    aware = datetime(2026, 1, 2, 15, 30, tzinfo=timezone(timedelta(hours=-5)))
    assert to_ts(aware) is aware
