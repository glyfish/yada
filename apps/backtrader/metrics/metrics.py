"""
metrics.py

Metrics computed from backtrader backtest order output.

"""

import numpy
from pandas import DataFrame


def compute_sharpe_ratio(orders: DataFrame, risk_free_return: float=0.0) -> float:
    """
    Calculate the Sharpe ratio for a time series using a rolling window. The order of the
    time series is assumed oldest data to most recent data.

    Parameters
    ----------
    orders : DataFrame
        Orders DataFrame.
    risk_free_return: float
        The risk-free return.
    Returns
    -------
    float
        The Sharpe ratio.
    """

    completed_orders = orders.query('order_status == "Completed"')

    pnl = completed_orders.pnl.to_numpy()
    cost = numpy.abs(completed_orders['size'].to_numpy() * completed_orders.price.to_numpy())
    daily_return = 100.0 * (pnl / cost) - risk_free_return

    return numpy.mean(daily_return) / numpy.std(daily_return)


def compute_rate_of_return(orders: DataFrame) -> float:
    """
    Calculate the rate of return.

    Parameters
    ----------
    orders : DataFrame
        Orders DataFrame.

    Returns
    -------
    float
        The rate of return.
    """

    completed_orders = orders.query('order_status == "Completed"')

    pnl = completed_orders.pnl.to_numpy()
    cost = numpy.abs(completed_orders['size'].to_numpy() * completed_orders.price.to_numpy())

    return 100.0 * numpy.sum(pnl) / numpy.sum(cost)


def compute_daily_rate_of_return(orders: DataFrame) -> tuple[numpy.ndarray, numpy.ndarray]:
    """
    Calculate the daily rate of return.

    Parameters
    ----------
    orders : DataFrame
        Orders DataFrame.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        Order dates and the per-order daily rate of return.
    """

    completed_orders = orders.query('order_status == "Completed"')

    pnl = completed_orders.pnl.to_numpy()
    cost = numpy.abs(completed_orders['size'].to_numpy() * completed_orders.price.to_numpy())

    daily_return = 100.0 * (pnl / cost)

    return completed_orders.date.to_numpy(), daily_return
