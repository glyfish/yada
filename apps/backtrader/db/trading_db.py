"""
trading_db.py

Persistence for strategy runs in every trading mode.

One database per environment (``YADA_DB_URL``). Inside it the run-output tables
(``runs``, ``orders``, ``trades``, ``positions``, ``broker``, ``analyzers``,
``indicators``, ``asset_prices``) exist once per *mode* -- ``backtest``, ``paper``,
``live`` -- each in its own Postgres schema with identical definitions, so the same
strategy code writes the same records whether it is simulating or trading. Shared
tables live in the ``trading`` schema: ``strategy_configs`` is the unit that moves
through the promotion pipeline (identified by a hash of strategy + params +
universe) and ``promotions`` is the audit log of its stage changes.
``public.price_series`` holds reference price data.

The table definitions here are the source of truth for the alembic migration that
creates them (revision 0004); ``compare_metadata`` is used to keep the two in step.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
from datetime import datetime, UTC
from enum import Enum
from typing import Any, Optional

import numpy
import pandas
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Index, Integer,
                        MetaData, String, Table, create_engine, func, insert, select, text, update)
from sqlalchemy.dialects.postgresql import JSONB, insert as pg_insert
import backtrader as bt

from lib.utils import read_yahoo_data


DEFAULT_DB_URL = "postgresql://yada@localhost/yada"
TRADING_SCHEMA = "trading"
MODES = ("backtest", "paper", "live")
MODE_TABLES = ("runs", "orders", "trades", "positions", "broker", "analyzers", "indicators", "asset_prices")

# Strategy params that describe the *run* rather than the strategy. They are excluded
# from the strategy config identity.
RUN_PARAMS = frozenset({"ensemble_id", "mode", "tier", "broker_account"})


# ----------------------------------------------------------------------------------
# Enumerations
# ----------------------------------------------------------------------------------

class MappedEnum(Enum):

    @classmethod
    def list(cls):
        return [c.value for c in cls]


class Mode(str, MappedEnum):
    """Where a run executes: historical simulation, a sandbox broker, or real fills."""
    Backtest = 'backtest'
    Paper = 'paper'
    Live = 'live'


class Stage(str, MappedEnum):
    """Where a strategy config sits in the promotion pipeline."""
    Exploratory = 'exploratory'
    Paper = 'paper'
    Live = 'live'
    Retired = 'retired'


class Tier(str, MappedEnum):
    """Exploratory runs are disposable; production runs back a promoted config."""
    Exploratory = 'exploratory'
    Production = 'production'


class RunStatus(str, MappedEnum):
    Running = 'running'
    Completed = 'completed'
    Failed = 'failed'


class OrderExecutionType(str, MappedEnum):
    """
    Order execution type.
    """

    Market = 'Market'
    Close = 'Close'
    Limit = 'Limit'
    Stop = 'Stop'
    StopLimit = 'StopLimit'
    StopTrail = 'StopTrail'
    StopTrailLimit = 'StopTrailLimit'
    Historical = 'Historical'


class OrderStatusType(str, MappedEnum):
    """
    Order status type.
    """

    Created = 'Created'
    Submitted = 'Submitted'
    Accepted = 'Accepted'
    Partial = 'Partial'
    Completed = 'Completed'
    Canceled = 'Canceled'
    Expired = 'Expired'
    Margin = 'Margin'
    Rejected = 'Rejected'


class OrderType(str, MappedEnum):
    """
    Order type.
    """

    Buy = 'Buy'
    Sell = 'Sell'


class TradeStatus(str, MappedEnum):
    """
    Trade status.
    """

    Created = 'Created'
    Open = 'Open'
    Closed = 'Closed'


# ----------------------------------------------------------------------------------
# Identity and value helpers
# ----------------------------------------------------------------------------------

def config_id(strategy: str, params: dict, universe: list[str]) -> str:
    """
    Identity of a strategy config: a hash of the strategy name, its parameters, and the
    universe it trades. Parameter and universe order do not matter.
    """

    canonical = json.dumps({"strategy": strategy, "params": jsonable(params), "universe": sorted(universe)},
                           sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def jsonable(value: Any) -> Any:
    """
    Convert a value into something the JSONB columns accept: dict keys become strings,
    datetimes become ISO strings, numpy scalars become Python scalars.
    """

    if isinstance(value, dict):
        return {(k.isoformat() if isinstance(k, (datetime, _dt.date)) else str(k)): jsonable(v)
                for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (datetime, _dt.date)):
        return value.isoformat()
    if isinstance(value, numpy.generic):
        return value.item()
    return value


def to_ts(value: datetime | _dt.date | None) -> Optional[datetime]:
    """
    Normalize a bar date/datetime to a timezone-aware UTC datetime. backtrader hands
    back naive datetimes; a bare date is taken as midnight UTC.
    """

    if value is None:
        return None
    if not isinstance(value, datetime):
        return datetime(value.year, value.month, value.day, tzinfo=UTC)
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value


# ----------------------------------------------------------------------------------
# Table definitions
# ----------------------------------------------------------------------------------
# Every table is declared with an explicit schema into a caller-supplied MetaData, so
# the mode tables' foreign keys to trading.strategy_configs resolve within one object.

def trading_tables(metadata: MetaData) -> MetaData:
    """Tables shared by every mode, in the `trading` schema."""

    Table(
        "strategy_configs", metadata,
        Column("config_id", String(32), primary_key=True),
        Column("strategy", String(256), nullable=False),
        Column("params", JSONB, nullable=False),
        Column("universe", JSONB, nullable=False),
        Column("stage", String(32), nullable=False, server_default=Stage.Exploratory.value),
        Column("description", String(1024), nullable=True),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        schema=TRADING_SCHEMA,
    )
    Table(
        "promotions", metadata,
        Column("id", BigInteger, primary_key=True, autoincrement=True),
        Column("config_id", String(32), ForeignKey(f"{TRADING_SCHEMA}.strategy_configs.config_id"), nullable=False),
        Column("from_stage", String(32), nullable=False),
        Column("to_stage", String(32), nullable=False),
        Column("evidence_mode", String(32), nullable=True),
        Column("evidence_run_id", String(256), nullable=True),
        Column("promoted_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("notes", String(4096), nullable=True),
        Index("ix_trading_promotions_config", "config_id"),
        schema=TRADING_SCHEMA,
    )
    return metadata


def public_tables(metadata: MetaData) -> MetaData:
    """Reference data shared by every mode, in the default schema."""

    Table(
        "price_series", metadata,
        Column("ticker", String(256), primary_key=True),
        Column("date", Date, primary_key=True),
        Column("open_price", Float, nullable=False),
        Column("high_price", Float, nullable=False),
        Column("low_price", Float, nullable=False),
        Column("close_price", Float, nullable=False),
        Column("adj_close_price", Float, nullable=False),
        Column("volume", Float, nullable=False),
        Column("open_interest", Float, nullable=False),
    )
    return metadata


def mode_tables(metadata: MetaData, mode: str) -> MetaData:
    """The run-output tables for one mode, in the schema named after it."""

    if mode not in MODES:
        raise ValueError(f"Unknown trading mode {mode!r}; expected one of {MODES}")

    runs_fk = f"{mode}.runs.run_id"

    Table(
        "runs", metadata,
        Column("run_id", String(256), primary_key=True),
        Column("config_id", String(32), ForeignKey(f"{TRADING_SCHEMA}.strategy_configs.config_id"), nullable=False),
        Column("tier", String(32), nullable=False, server_default=Tier.Exploratory.value),
        Column("ensemble_id", String(256), nullable=True),
        Column("status", String(32), nullable=False, server_default=RunStatus.Running.value),
        Column("started_at", DateTime(timezone=True), nullable=False),
        Column("ended_at", DateTime(timezone=True), nullable=True),
        Column("broker_account", String(256), nullable=True),
        Column("notes", String(4096), nullable=True),
        Index(f"ix_{mode}_runs_config", "config_id"),
        schema=mode,
    )
    Table(
        "broker", metadata,
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), primary_key=True),
        Column("ts", DateTime(timezone=True), primary_key=True),
        Column("cash", Float, nullable=False),
        Column("value", Float, nullable=False),
        schema=mode,
    )
    Table(
        "positions", metadata,
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), primary_key=True),
        Column("ticker", String(256), primary_key=True),
        Column("ts", DateTime(timezone=True), primary_key=True),
        Column("adjbase", Float, nullable=False),
        Column("price", Float, nullable=False),
        Column("price_orig", Float, nullable=False),
        Column("size", Integer, nullable=False),
        Column("upclosed", Float, nullable=False),
        Column("upopened", Float, nullable=False),
        Column("updt", DateTime(timezone=True), nullable=True),
        schema=mode,
    )
    Table(
        "orders", metadata,
        Column("id", BigInteger, primary_key=True, autoincrement=True),
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), nullable=False),
        Column("ref", Integer, nullable=False),
        Column("ticker", String(256), nullable=False),
        Column("ts", DateTime(timezone=True), nullable=False),
        Column("order_status", String(256), nullable=False),
        Column("order_type", String(256), nullable=False),
        Column("exec_type", String(256), nullable=False),
        Column("trade_id", BigInteger, nullable=True),
        Column("price", Float, nullable=False),
        Column("value", Float, nullable=False),
        Column("size", Integer, nullable=False),
        Column("commission", Float, nullable=False),
        Column("pnl", Float, nullable=False),
        Index(f"ix_{mode}_orders_run_ref", "run_id", "ref"),
        Index(f"ix_{mode}_orders_run_ts", "run_id", "ts"),
        schema=mode,
    )
    Table(
        "trades", metadata,
        Column("id", BigInteger, primary_key=True, autoincrement=True),
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), nullable=False),
        Column("ref", Integer, nullable=False),
        Column("ticker", String(256), nullable=False),
        Column("ts", DateTime(timezone=True), nullable=False),
        Column("status", String(256), nullable=False),
        Column("trade_id", BigInteger, nullable=True),
        Column("size", Integer, nullable=False),
        Column("price", Float, nullable=False),
        Column("value", Float, nullable=False),
        Column("commission", Float, nullable=False),
        Column("pnl", Float, nullable=False),
        Column("pnlcomm", Float, nullable=False),
        Column("dtopen", DateTime(timezone=True), nullable=True),
        Column("dtclose", DateTime(timezone=True), nullable=True),
        Column("baropen", Integer, nullable=False),
        Column("barclose", Integer, nullable=False),
        Column("barlen", Integer, nullable=False),
        Column("is_long", Boolean, nullable=False),
        Index(f"ix_{mode}_trades_run_ref", "run_id", "ref"),
        Index(f"ix_{mode}_trades_run_ts", "run_id", "ts"),
        schema=mode,
    )
    Table(
        "analyzers", metadata,
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), primary_key=True),
        Column("analyzer", String(256), primary_key=True),
        Column("value", JSONB, nullable=False),
        Column("parameters", JSONB, nullable=True),
        schema=mode,
    )
    Table(
        "indicators", metadata,
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), primary_key=True),
        Column("ticker", String(256), primary_key=True),
        Column("indicator", String(256), primary_key=True),
        Column("ts", DateTime(timezone=True), primary_key=True),
        Column("value", JSONB, nullable=False),
        Column("params", JSONB, nullable=True),
        schema=mode,
    )
    Table(
        "asset_prices", metadata,
        Column("run_id", String(256), ForeignKey(runs_fk, ondelete="CASCADE"), primary_key=True),
        Column("ticker", String(256), primary_key=True),
        Column("ts", DateTime(timezone=True), primary_key=True),
        Column("open_price", Float, nullable=False),
        Column("high_price", Float, nullable=False),
        Column("low_price", Float, nullable=False),
        Column("close_price", Float, nullable=False),
        schema=mode,
    )
    return metadata


def build_metadata(modes: tuple[str, ...] = MODES) -> MetaData:
    """Every table in the database that this module owns, in one MetaData."""

    metadata = MetaData()
    trading_tables(metadata)
    public_tables(metadata)
    for mode in modes:
        mode_tables(metadata, mode)
    return metadata


def trading_metadata() -> MetaData:
    return trading_tables(MetaData())


def public_metadata() -> MetaData:
    return public_tables(MetaData())


def mode_metadata(mode: str) -> MetaData:
    """One mode's tables (plus the trading tables they reference)."""
    return mode_tables(trading_tables(MetaData()), mode)


# ----------------------------------------------------------------------------------
# Database interface
# ----------------------------------------------------------------------------------

class TradingDb:
    """
    Interface to the trading tables for one mode.

    Parameters
    ----------
    mode : str
        ``backtest``, ``paper`` or ``live`` -- selects the schema written to.
    url : str, optional
        Database URL; defaults to ``YADA_DB_URL`` (one database per environment).

    Properties
    ----------
    engine : sqlalchemy.engine.base.Engine
        Database engine.
    mode : str
        The mode this instance writes to.
    """

    def __init__(self, mode: str = Mode.Backtest.value, url: Optional[str] = None):
        self.mode = Mode(mode).value
        self.schema = self.mode
        self.__db_url = url or os.getenv("YADA_DB_URL", DEFAULT_DB_URL)
        self.engine = create_engine(self.__db_url, isolation_level="AUTOCOMMIT")
        self.metadata = build_metadata()


    def table(self, name: str) -> Table:
        """The mode-scoped table with the given name."""
        return self.metadata.tables[f"{self.schema}.{name}"]


    @property
    def strategy_configs(self) -> Table:
        return self.metadata.tables[f"{TRADING_SCHEMA}.strategy_configs"]


    @property
    def promotions(self) -> Table:
        return self.metadata.tables[f"{TRADING_SCHEMA}.promotions"]


    @property
    def price_series(self) -> Table:
        return self.metadata.tables["price_series"]


    # ---- strategy configs, runs, and promotions -----------------------------------

    def ensure_strategy_config(self, strategy: str, params: dict, universe: list[str],
                               description: Optional[str] = None) -> str:
        """
        Register a strategy config if it is not already known and return its id. Calling
        this at the start of every run keeps the registry truthful: a config exists
        because something actually ran it.
        """

        cid = config_id(strategy, params, universe)
        stmt = pg_insert(self.strategy_configs).values(
            config_id=cid, strategy=strategy, params=jsonable(params), universe=sorted(universe),
            description=description,
        ).on_conflict_do_nothing(index_elements=["config_id"])
        self._execute(stmt)
        return cid


    def fetch_strategy_config(self, config_id: str) -> pandas.DataFrame:
        return self._read(f"SELECT * FROM {TRADING_SCHEMA}.strategy_configs WHERE config_id = :config_id",
                          config_id=config_id)


    def fetch_strategy_configs(self, stage: Optional[str] = None) -> pandas.DataFrame:
        query = f"SELECT * FROM {TRADING_SCHEMA}.strategy_configs"
        if stage:
            return self._read(query + " WHERE stage = :stage ORDER BY created_at", stage=Stage(stage).value)
        return self._read(query + " ORDER BY created_at")


    def insert_run(self, run_id: str, config_id: str, ensemble_id: Optional[str] = None,
                   tier: str = Tier.Exploratory.value, started_at: Optional[datetime] = None,
                   broker_account: Optional[str] = None, notes: Optional[str] = None):
        """
        Record the start of a run of a strategy config in this mode.
        """

        self._execute(insert(self.table("runs")).values(
            run_id=run_id, config_id=config_id, tier=Tier(tier).value, ensemble_id=ensemble_id,
            status=RunStatus.Running.value, started_at=to_ts(started_at or datetime.now(UTC)),
            broker_account=broker_account, notes=notes,
        ))


    def finish_run(self, run_id: str, status: str = RunStatus.Completed.value, ended_at: Optional[datetime] = None):
        runs = self.table("runs")
        self._execute(update(runs).where(runs.c.run_id == run_id).values(
            status=RunStatus(status).value, ended_at=to_ts(ended_at or datetime.now(UTC))))


    def fetch_run(self, run_id: str) -> pandas.DataFrame:
        """
        Fetch a run together with the strategy config it executed.
        """

        return self._read(f"""
        SELECT r.*, c.strategy, c.params, c.universe, c.stage
        FROM {self.schema}.runs r
        JOIN {TRADING_SCHEMA}.strategy_configs c USING (config_id)
        WHERE r.run_id = :run_id
        """, run_id=run_id)


    def fetch_runs(self, config_id: Optional[str] = None, tier: Optional[str] = None) -> pandas.DataFrame:
        clauses, params = [], {}
        if config_id:
            clauses.append("r.config_id = :config_id"); params["config_id"] = config_id
        if tier:
            clauses.append("r.tier = :tier"); params["tier"] = Tier(tier).value
        where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
        return self._read(f"""
        SELECT r.*, c.strategy, c.stage
        FROM {self.schema}.runs r
        JOIN {TRADING_SCHEMA}.strategy_configs c USING (config_id)
        {where}
        ORDER BY r.started_at
        """, **params)


    def promote(self, config_id: str, to_stage: str, evidence_run_id: Optional[str] = None,
                evidence_mode: Optional[str] = None, notes: Optional[str] = None) -> str:
        """
        Move a strategy config to a new stage of the pipeline (backtest -> paper -> live
        -> retired), recording the run that justified the move. Returns the previous stage.
        """

        to_stage = Stage(to_stage).value
        if evidence_mode is not None:
            evidence_mode = Mode(evidence_mode).value
        configs, promotions = self.strategy_configs, self.promotions

        # Stage read + audit row + stage update must be atomic; the default engine is
        # autocommit, so run this on a transactional connection.
        with self.engine.connect().execution_options(isolation_level="READ COMMITTED") as connection:
            with connection.begin():
                row = connection.execute(select(configs.c.stage).where(configs.c.config_id == config_id)).first()
                if row is None:
                    raise ValueError(f"Unknown strategy config: {config_id}")
                from_stage = row.stage
                connection.execute(insert(promotions).values(
                    config_id=config_id, from_stage=from_stage, to_stage=to_stage,
                    evidence_mode=evidence_mode, evidence_run_id=evidence_run_id, notes=notes))
                connection.execute(update(configs).where(configs.c.config_id == config_id).values(stage=to_stage))
        return from_stage


    def fetch_promotions(self, config_id: Optional[str] = None) -> pandas.DataFrame:
        query = f"SELECT * FROM {TRADING_SCHEMA}.promotions"
        if config_id:
            return self._read(query + " WHERE config_id = :config_id ORDER BY promoted_at", config_id=config_id)
        return self._read(query + " ORDER BY promoted_at")


    # ---- per-bar run output ----------------------------------------------------------

    def insert_broker(self, run_id: str, ts: datetime | _dt.date, broker: bt.BrokerBase):
        """
        Insert broker state.

        Parameters
        ----------
        run_id : str
            Unique identifier for the run.
        ts : datetime
            Bar timestamp.
        broker : bt.BrokerBase
            backtrader broker
        """

        self._execute(insert(self.table("broker")).values(
            run_id=run_id, ts=to_ts(ts), cash=broker.getcash(), value=broker.getvalue()))


    def insert_position(self, run_id: str, ts: datetime | _dt.date, ticker: str, position: bt.Position):
        """
        Insert current position into the database.
        """

        self._execute(insert(self.table("positions")).values(
            run_id=run_id, ts=to_ts(ts), ticker=ticker,
            adjbase=position.adjbase, price=position.price, price_orig=position.price_orig,
            size=position.size, upclosed=position.upclosed, upopened=position.upopened,
            updt=to_ts(position.updt) if isinstance(position.updt, (datetime, _dt.date)) else None))


    def insert_trade(self, run_id: str, ts: datetime | _dt.date, ticker: str, trade: bt.Trade):
        """
        Insert a trade state change into the database.
        """

        dtclose = trade.close_datetime() if trade.dtclose > 0.0 else None
        dtopen = trade.open_datetime() if trade.dtopen > 0.0 else None
        trade_status = TradeStatus.list()[trade.status]

        self._execute(insert(self.table("trades")).values(
            run_id=run_id, ref=trade.ref, ticker=ticker, ts=to_ts(ts), status=trade_status,
            trade_id=trade.tradeid, size=trade.size, price=trade.price, value=trade.value,
            commission=trade.commission, pnl=trade.pnl, pnlcomm=trade.pnlcomm,
            dtopen=to_ts(dtopen), dtclose=to_ts(dtclose),
            baropen=trade.baropen, barclose=trade.barclose, barlen=trade.barlen, is_long=trade.long))


    def insert_order(self, run_id: str, ts: datetime | _dt.date, ticker: str, order: bt.Order):
        """
        Insert an order state change into the database.
        """

        order_type = order.ordtypename()
        order_exec_type = OrderExecutionType.list()[order.exectype]
        order_status = OrderStatusType.list()[order.status]

        order_data = order.executed if order_status == OrderStatusType.Completed.value else order.created

        self._execute(insert(self.table("orders")).values(
            run_id=run_id, ref=order.ref, ticker=ticker, ts=to_ts(ts),
            order_status=order_status, order_type=order_type, exec_type=order_exec_type,
            trade_id=order.tradeid, price=order_data.price, value=order_data.value,
            size=order_data.size, commission=order_data.comm, pnl=order_data.pnl))


    def insert_asset_price(self, run_id: str, data):
        """
        Insert the current bar of a data feed into the database.

        Parameters
        ----------
        run_id : str
            Unique identifier for the run.
        data :
            A backtrader data feed.
        """

        self._execute(insert(self.table("asset_prices")).values(
            run_id=run_id, ts=to_ts(data.datetime.datetime(0)), ticker=data._name,
            open_price=data.open[0], high_price=data.high[0], low_price=data.low[0], close_price=data.close[0]))

    insert_yahoo_asset_price = insert_asset_price


    def insert_indicator(self, run_id: str, ts: datetime | _dt.date, ticker: str, indicator: str,
                         value: dict, params: Optional[dict] = None):
        self._execute(insert(self.table("indicators")).values(
            run_id=run_id, ts=to_ts(ts), ticker=ticker, indicator=indicator,
            value=jsonable(value), params=jsonable(params) if params is not None else None))


    def insert_zscore_indicator(self, run_id: str, ts: datetime | _dt.date, ticker: str, zscore: float,
                                period: int, stake_multiple: float):
        self.insert_indicator(run_id, ts, ticker, 'zscore', {'zscore': zscore},
                              {'period': period, 'stake_multiple': stake_multiple})


    def insert_analyzer(self, run_id: str, analyzer: str, value: Any, parameters: Optional[dict] = None):
        """
        Persist a backtrader analyzer result for a run.
        """

        self._execute(insert(self.table("analyzers")).values(
            run_id=run_id, analyzer=analyzer, value=jsonable(value),
            parameters=jsonable(parameters) if parameters is not None else None))


    # ---- reference price data --------------------------------------------------------

    def insert_price_series(self, ticker: str, date: _dt.date, open_price: float, high_price: float, low_price: float,
                            close_price: float, adj_close_price: float, volume: float, open_interest: float):
        self._execute(insert(self.price_series).values(
            ticker=ticker, date=date, open_price=open_price, high_price=high_price, low_price=low_price,
            close_price=close_price, adj_close_price=adj_close_price, volume=volume, open_interest=open_interest))


    def insert_yahoo_price_series(self, ticker: str, file_root: str = '../../../data/algorithmic_trading'):
        """
        Load a Yahoo quote CSV into the price series table.
        """

        file_path = os.path.abspath(f"{file_root}/{ticker}.csv")
        data = read_yahoo_data(file_path)
        data.rename(columns={"Open": "open_price", "High": "high_price", "Low": "low_price", "Close": "close_price",
                             "Adj Close": "adj_close_price", "Volume": "volume"}, inplace=True)
        data.index.names = ['date']
        data['ticker'] = numpy.full(len(data), ticker)
        data.to_sql("price_series", self.engine, schema="public", if_exists="append")


    def fetch_price_series(self, ticker: str, start_date: Optional[str] = None,
                           end_date: Optional[str] = None) -> pandas.DataFrame:
        query, params = "SELECT * FROM public.price_series WHERE ticker = :ticker", {"ticker": ticker}
        if start_date:
            query += " AND date >= :start_date"; params["start_date"] = start_date
        if end_date:
            query += " AND date <= :end_date"; params["end_date"] = end_date
        return self._read(query + " ORDER BY date ASC", **params)


    # ---- run output queries ----------------------------------------------------------
    # Every query also returns `date` (the UTC calendar date of `ts`) and the run's
    # ensemble_id, which is what the dashboards consume.

    def fetch_broker(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT b.ts, (b.ts AT TIME ZONE 'UTC')::date AS date, b.run_id, r.ensemble_id, b.cash, b.value
        FROM {self.schema}.broker b JOIN {self.schema}.runs r USING (run_id)
        WHERE b.run_id = :run_id ORDER BY b.ts
        """, run_id=run_id)


    def fetch_position(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT p.ts, (p.ts AT TIME ZONE 'UTC')::date AS date, p.run_id, p.ticker, r.ensemble_id,
               p.adjbase, p.price, p.price_orig, p.size, p.upclosed, p.upopened, p.updt
        FROM {self.schema}.positions p JOIN {self.schema}.runs r USING (run_id)
        WHERE p.run_id = :run_id ORDER BY p.ts
        """, run_id=run_id)


    def fetch_trades(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT t.ts, (t.ts AT TIME ZONE 'UTC')::date AS date, t.run_id, t.ref, t.ticker, r.ensemble_id,
               t.status, t.trade_id, t.size, t.price, t.value, t.commission, t.pnl, t.pnlcomm,
               t.dtopen, t.dtclose, t.baropen, t.barclose, t.barlen, t.is_long
        FROM {self.schema}.trades t JOIN {self.schema}.runs r USING (run_id)
        WHERE t.run_id = :run_id ORDER BY t.ts, t.id
        """, run_id=run_id)


    def fetch_orders(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT o.ts, (o.ts AT TIME ZONE 'UTC')::date AS date, o.run_id, o.ref, o.ticker, r.ensemble_id,
               o.order_status, o.order_type, o.exec_type, o.trade_id, o.price, o.value, o.size,
               o.commission, o.pnl
        FROM {self.schema}.orders o JOIN {self.schema}.runs r USING (run_id)
        WHERE o.run_id = :run_id ORDER BY o.ts, o.id
        """, run_id=run_id)


    def fetch_asset_price(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT a.ts, (a.ts AT TIME ZONE 'UTC')::date AS date, a.run_id, a.ticker, r.ensemble_id,
               a.open_price, a.high_price, a.low_price, a.close_price
        FROM {self.schema}.asset_prices a JOIN {self.schema}.runs r USING (run_id)
        WHERE a.run_id = :run_id ORDER BY a.ts
        """, run_id=run_id)


    def fetch_zscore_indicator(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"""
        SELECT i.ts, (i.ts AT TIME ZONE 'UTC')::date AS date, i.run_id, i.ticker, i.indicator, r.ensemble_id,
               (i.value->>'zscore')::float AS zscore,
               (i.params->>'period')::int AS half_life,
               (i.params->>'stake_multiple')::float AS stake_multiple
        FROM {self.schema}.indicators i JOIN {self.schema}.runs r USING (run_id)
        WHERE i.run_id = :run_id AND i.indicator = 'zscore' ORDER BY i.ts
        """, run_id=run_id)


    def fetch_analyzers(self, run_id: str) -> pandas.DataFrame:
        return self._read(f"SELECT * FROM {self.schema}.analyzers WHERE run_id = :run_id ORDER BY analyzer",
                          run_id=run_id)


    # ---- private ---------------------------------------------------------------------

    def _execute(self, statement):
        with self.engine.connect() as connection:
            connection.execute(statement)


    def _read(self, query: str, **params) -> pandas.DataFrame:
        return pandas.read_sql(text(query), self.engine, params=params)
