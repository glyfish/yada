from numpy.typing import NDArray
import shortuuid

from lib.plots import curve, stack, comparison, PlotType, twinx, twinx_comparison
from lib.utils import generate_plot_file_name

from lib.logger import get_logger

logger = get_logger("YADA")


def generate_time_series_plot(time: NDArray, values: NDArray, title: str, xlabel: str, ylabel: str,
                                plot_axis_type: PlotType) -> str:
    """
    Generate a single time series plot.

    Parameters
    ----------
        time: NDArray
            Array of timestamps for the x-axis
        values: NDArray
            Array of numeric values for the y-axis
        title: str
            Title of the chart
        xlabel: str
            Chart xlabel
        ylabel: str
            Chart ylabel
        plot_axis_type: PlotType
            Type of plot axis (e.g., YLOG for logarithmic y-axis)

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_time_series_plot: title: {title}, xlabel: {xlabel}, "
                    f"ylabel: {ylabel}, plot_axis_type: {plot_axis_type}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("time_series_plot", path="./html/plots", uuid=uuid)

    curve(values, time, xlabel=xlabel, ylabel=ylabel, title=title, figsize=(10, 6),
            file_name=output_file_name, plot_axis_type=plot_axis_type)

    return generate_plot_file_name("time_series_plot", path="./plots", uuid=uuid)



def generate_time_series_stack(time: NDArray, values: list[NDArray], title: str, xlabel: str,
                                ylabels: list[str] | None, labels: list[str] | None,
                                plot_axis_type: PlotType) -> str:
    """
    Generate a stacked time series plot.

    Parameters
    ----------
        time: NDArray
            Timestamps for the x-axis
        values: list[NDArray]
            One array of values per stacked plot
        title: str
            Title of the chart
        xlabel: str
            Chart xlabel
        ylabels: list[str] | None
            Y-axis label for each stacked plot
        labels: list[str] | None
            Text label annotated on each stacked plot
        plot_axis_type: PlotType
            Type of plot axis

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_time_series_stack: title: {title}, xlabel: {xlabel}, "
                    f"ylabels: {ylabels}, plot_axis_type: {plot_axis_type}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("time_series_stack", path="./html/plots", uuid=uuid)

    stack(values, time, xlabel=xlabel, ylabels=ylabels, labels=labels, title=title,
            file_name=output_file_name, plot_axis_type=plot_axis_type)

    return generate_plot_file_name("time_series_stack", path="./plots", uuid=uuid)


def generate_time_series_comparison(time: NDArray, values: list[NDArray], title: str, xlabel: str,
                                    ylabel: str, labels: list[str] | None,
                                    plot_axis_type: PlotType) -> str:
    """
    Generate a comparison time series plot with multiple series on the same axis.

    Parameters
    ----------
        time: NDArray
            Timestamps for the x-axis
        values: list[NDArray]
            One array of values per series
        title: str
            Title of the chart
        xlabel: str
            Chart xlabel
        ylabel: str
            Chart ylabel
        labels: list[str] | None
            Legend label for each series
        plot_axis_type: PlotType
            Type of plot axis

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_time_series_comparison: title: {title}, xlabel: {xlabel}, "
                    f"ylabel: {ylabel}, plot_axis_type: {plot_axis_type}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("time_series_comparison", path="./html/plots", uuid=uuid)

    comparison(values, time, xlabel=xlabel, ylabel=ylabel, title=title, labels=labels,
                figsize=(10, 6), file_name=output_file_name, plot_axis_type=plot_axis_type)

    return generate_plot_file_name("time_series_comparison", path="./plots", uuid=uuid)


def generate_time_series_twinx(time: NDArray, left: NDArray, right: NDArray, title: str, xlabel: str,
                               left_ylabel: str, right_ylabel: str, plot_axis_type: PlotType,
                               labels: list[str] | None = None) -> str:
    """
    Generate a single time series plot.

    Parameters
    ----------
    time: NDArray
        Timestamps for the x-axis
    left : numpy.ndarray
        Value plotted on left y-axis.
    right : numpy.ndarray
        Value plotted on right y-axis.
    title : string, optional
        Plot title (default is None)
    xlabel : string, optional
        Plot x-axis label (default is 'x')
    left_ylabel : string, optional
        Plot left y-axis label (default is 'y')
    right_ylabel : string, optional
        Plot left y-axis label (default is 'y')
    labels : [string], optional
        Curve labels shown in legend.
    plot_axis_type : PlotAxisType
        Axis type. (default PlotAxisType.LINEAR)

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_time_series_twinx: title: {title}, xlabel: {xlabel}, "
                    f"left_ylabel: {left_ylabel}, right_ylabel: {right_ylabel}, plot_axis_type: {plot_axis_type}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("time_series_twinx", path="./html/plots", uuid=uuid)

    twinx(left, right, time, xlabel=xlabel, left_ylabel=left_ylabel, right_ylabel=right_ylabel, title=title,
          labels=labels, figsize=(10, 6), file_name=output_file_name, plot_axis_type=plot_axis_type)

    return generate_plot_file_name("time_series_twinx", path="./plots", uuid=uuid)


def generate_time_series_twinx_comparison(time: NDArray, left: list[NDArray], right: list[NDArray], title: str, xlabel: str,
                                          left_ylabel: str, right_ylabel: str, plot_axis_type: PlotType,
                                          labels: list[str] | None = None) -> str:
    """
    Generate a single time series plot.

    Parameters
    ----------
    time: NDArray
        Timestamps for the x-axis
    left : list[numpy.ndarray]
        Value plotted on left y-axis.
    right : list[numpy.ndarray]
        Value plotted on right y-axis.
    title : string, optional
        Plot title (default is None)
    xlabel : string, optional
        Plot x-axis label (default is 'x')
    left_ylabel : string, optional
        Plot left y-axis label (default is 'y')
    right_ylabel : string, optional
        Plot left y-axis label (default is 'y')
    labels : [string], optional
        Curve labels shown in legend.
    plot_axis_type : PlotAxisType
        Axis type. (default PlotAxisType.LINEAR)

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_time_series_twinx_comparison: title: {title}, xlabel: {xlabel}, "
                    f"left_ylabel: {left_ylabel}, right_ylabel: {right_ylabel}, plot_axis_type: {plot_axis_type}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("time_series_twinx_comparison", path="./html/plots", uuid=uuid)

    twinx_comparison(left, right, time, xlabel=xlabel, left_ylabel=left_ylabel, right_ylabel=right_ylabel, title=title,
                     labels=labels, figsize=(10, 6), file_name=output_file_name, plot_axis_type=plot_axis_type)

    return generate_plot_file_name("time_series_twinx_comparison", path="./plots", uuid=uuid)
