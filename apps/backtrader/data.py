"""
data.py

Readers for backtrader backtest output files.

"""

from pandas import read_csv, DataFrame


def read_backtrader_data(file_path: str) -> DataFrame:
    """
    Read a backtrader back test output file at the specified path

    Parameters
    ----------
    file_path: str
        File path.

    Returns
    -------
    Pandas DataFrame
        Backtrader output data.
    """

    data = read_csv(file_path, index_col=0, parse_dates=["datetime"], date_format='%Y-%m-%d %H:%M:%S.%f')
    data.fillna(0.0, inplace=True)
    return data
