from typing import Type
import os.path
from datetime import datetime, UTC
import random

import backtrader as bt
import shortuuid

from apps.backtrader.db.trading_db import TradingDb, RUN_PARAMS, jsonable


class GlyfishStrategy(bt.Strategy):
    """
    The GlyfishStrategy is a container for reusable elements in Strategies.

    Every run registers the strategy config it executes -- derived from the strategy's
    actual backtrader params and the data feeds it trades -- and records its output in
    the tables of the mode it runs in (backtest, paper, live). The run-level params
    below describe the run, not the strategy, and are not part of the config identity.
    """

    params = (
        # Identifier grouping related runs (e.g. a parameter sweep)
        ('ensemble_id', None),
        # Where this run executes: backtest, paper or live (selects the schema written to)
        ('mode', 'backtest'),
        # exploratory runs are disposable; production runs back a promoted config
        ('tier', 'exploratory'),
        # Broker account for paper/live runs
        ('broker_account', None),
    )

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission, current  bar_executed
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Add database interface for the mode this run executes in
        self.db = TradingDb(self.p.mode)

        # Create run identifier
        self.run_id = shortuuid.ShortUUID().random(length=12)
        self.ensemble_id = self.p.ensemble_id
        self.time_stamp = datetime.now(UTC)

        # Maintain trade ID
        self.tradeid = None

        # Register the strategy config this run executes and the run itself
        strategy_params = {k: v for k, v in self.p._getkwargs().items() if k not in RUN_PARAMS}
        universe = [d._name for d in self.datas]
        self.config_id = self.db.ensure_strategy_config(self.__class__.__name__, jsonable(strategy_params), universe)
        self.db.insert_run(self.run_id, self.config_id, ensemble_id=self.ensemble_id, tier=self.p.tier,
                           started_at=self.time_stamp, broker_account=self.p.broker_account)
        self.log(f"Run ID={self.run_id}, Config ID={self.config_id}, Ensemble ID={self.ensemble_id}, Mode={self.p.mode}",
                 dt=self.time_stamp)


    def get_tradeid(self):
        """
        Create a new trade ID if one does not exist and return it
        or the current value.
        """

        if self.tradeid is None:
            self.tradeid = random.getrandbits(32)
        return self.tradeid
    

    def log(self, txt: str, dt: datetime | None=None):
        """
        Logging function for strategy.

        Parameters
        ----------
        txt : str
            Text to be logged.
        dt : datetime, optional
            Date and time to be logged. The default is None.
        """

        dt = dt or self.current_date()
        print(f"{dt.isoformat()}, {txt}")


    def current_date(self):
        """
        Get the current bar date.
        """

        return self.datas[0].datetime.date(0)


    def current_ts(self):
        """
        Get the current bar timestamp.
        """

        return self.datas[0].datetime.datetime(0)


    def ticker(self):
        """
        Get the name of the primary data feed.
        """

        return self.datas[0]._name


    def notify_cashvalue(self, cash, value):
        self.log(f"Cash={cash:.2f}, Value={value:.2f}")


    def notify_trade(self, trade: bt.Trade):
        """
        Called when a trade has a state change.

        Parameters
        ----------
        trade : bt.Trade
            The trade that has changed state.
        """
        
        self.db.insert_trade(self.run_id, self.current_ts(), self.ticker(), trade)
        
        if not trade.isclosed:
            return
        self.tradeid = None

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' % (trade.pnl, trade.pnlcomm))


    def notify_order(self, order: bt.Order):
        """
        Called when an order has a state change.

        Parameters
        ----------
        order : bt.Order
            The order that has changed state.
        """
        
        self.db.insert_order(self.run_id, self.current_ts(), self.ticker(), order)

        if order.status in [order.Submitted, order.Accepted]:
            return
        
        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"BUY EXECUTED, Price {order.executed.price:.2f}, Cost {order.executed.value:.2f}, Comm {order.executed.comm:.2f}")
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log(f"SHORT EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm {order.executed.comm:.2f}")

            # save bar when order was executed
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None


    def next(self):
        """
        Called on each new bar.
        """

        #  Log the closing price
        self.log(f"Close {self.dataclose[0]:.2f}")

        # Insert broker and asset price data into database
        self.db.insert_broker(self.run_id, self.current_ts(), self.broker)
        self.db.insert_asset_price(self.run_id, self.datas[0])


    def stop(self):
        """
        Called when the run ends.
        """

        self.db.finish_run(self.run_id)


    @staticmethod
    def create_ensemble_id():
        return shortuuid.ShortUUID().random(length=12)
    

    @staticmethod
    def load_yahoo_finance_data(file_path: str, start_date: datetime, end_date: datetime):  
        dataname = os.path.abspath(file_path)
        data = bt.feeds.YahooFinanceCSVData(
            dataname=dataname,
            fromdate = start_date,
            todate = end_date,
            reverse=False)
        return data
    

    @staticmethod
    def backtest(data, strategy: Type[bt.Strategy], ensemble_id: str, cash: float = 1000.0, commission: float = 0.0,
                 tier: str = 'exploratory', mode: str = 'backtest'):
        cerebro = bt.Cerebro()
        # Add the Data Feed to Cerebro
        cerebro.adddata(data)

        # Add a strategy, with the run-level params
        cerebro.addstrategy(strategy, ensemble_id=ensemble_id, mode=mode, tier=tier)

        # Set cash start
        cerebro.broker.setcash(cash)

        # Set the commission - 0.1% ... divide by 100 to remove the %
        cerebro.broker.setcommission(commission=commission)

        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = "sharpe")
        cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name = "sharpe_a")
        cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name = "annual_return")
        cerebro.addanalyzer(bt.analyzers.Returns, _name = "returns")
        cerebro.addanalyzer(bt.analyzers.TimeReturn, _name = "time_return")
        cerebro.addanalyzer(bt.analyzers.VWR, _name = "vwr")
        cerebro.addanalyzer(bt.analyzers.PositionsValue, _name = "position_value")

        # Print out the starting conditions
        print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")

        # Run over everything
        strats = cerebro.run()
        strat = strats[0]

        # Persist the analyzer results with the run
        for name, analyzer in strat.analyzers.getitems():
            strat.db.insert_analyzer(strat.run_id, name, analyzer.get_analysis())

        # Print out the final result
        print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}, Run ID: {strat.run_id}, "
              f"Config ID: {strat.config_id}, Ensemble ID: {ensemble_id}")
        print(f"Sharp Ratio: {strat.analyzers.sharpe.get_analysis()}")
        print(f"Annualized Sharp Ratio: {strat.analyzers.sharpe_a.get_analysis()}")
        print(f"Annual Return: {strat.analyzers.annual_return.get_analysis()}")
        print(f"Returns: {strat.analyzers.returns.get_analysis()}")
        print(f"Variable Weight Ratio: {strat.analyzers.vwr.get_analysis()}")

        return cerebro
