"""
backtest_db.py

Backward-compatible entry point: ``BacktestDb`` is ``TradingDb`` fixed to the
``backtest`` mode. New code should use ``TradingDb(mode)`` directly.
"""

from typing import Optional

from apps.backtrader.db.trading_db import (  # noqa: F401 -- re-exported
    TradingDb, Mode, Stage, Tier, RunStatus,
    OrderExecutionType, OrderStatusType, OrderType, TradeStatus,
    config_id, jsonable, to_ts, mode_metadata, trading_metadata, public_metadata,
)


class BacktestDb(TradingDb):

    def __init__(self, url: Optional[str] = None):
        super().__init__(Mode.Backtest.value, url)
