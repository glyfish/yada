from typing import Dict, List
import shortuuid
import numpy

from lib.plots import bar, multibar
from lib.utils import generate_plot_file_name

from lib.logger import get_logger

logger = get_logger("YADA")


def generate_multi_bar_chart(categories: List[str], datasets: List[Dict[str, float]], labels: List[str],
                                title: str, xlabel: str, ylabel: str, xlabel_rotation: float) -> str:
    """
    Create a grouped multi-bar chart from multiple datasets.

    Parameters
    ----------
        categories: List[str]
            Shared category labels for the x-axis
        datasets: List[Dict[str, float]]
            One dict per dataset mapping category to value
        labels: List[str]
            Legend label for each dataset
        title: str
            Title of the chart
        xlabel: str
            Chart xlabel
        ylabel: str
            Chart ylabel
        xlabel_rotation: float
            Rotation angle for the x-axis labels

    Returns:
        str: Relative file path to the rendered plot image
    """

    logger.debug(f"Calling generate_multi_bar_chart: title: {title}, xlabel: {xlabel}, ylabel: {ylabel}")

    x = numpy.array(categories)
    y = [numpy.array([d[c] for c in categories]) for d in datasets]

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("multi_bar_chart", path="./html/plots", uuid=uuid)

    multibar(y, x, labels=labels, xlabel_rotation=xlabel_rotation,
                xlabel=xlabel, ylabel=ylabel, title=title,
                figsize=(10, 6), file_name=output_file_name)

    return generate_plot_file_name("multi_bar_chart", path="./plots", uuid=uuid)


def generate_bar_chart(data: Dict[str, float], title: str, xlabel: str, ylabel: str, xlabel_rotation: int) -> str:
    """
    Create a bar chart from the provided data.
    
    Parameters
    ----------
        data: Dict[str, float]
            Dictionary where keys are labels and values are numeric values to plot
        title: str
            Title of the chart
        xlabel: str
            Chart xlabel
        ylabel: str
            chart ylabel
        xlabel_rotation: int
            Rotation angle for the x-axis labels
        
    Returns:
        str: A string representation of the bar chart
    """

    x = numpy.array(list(data.keys()))
    y = data.values()

    logger.debug(f"Calling generate_bar_chart: {data}, title: {title}, xlabel: {xlabel}, ylabel: {ylabel}, xlabel_rotation: {xlabel_rotation}")

    uuid = shortuuid.uuid()
    output_file_name = generate_plot_file_name("bar_chart", path="./html/plots", uuid=uuid)

    bar(y, x, alpha=1.0, bar_width=0.9, xlabel_rotation=xlabel_rotation,
        xlabel=xlabel, ylabel=ylabel, title=title,
        figsize=(10, 6), file_name=output_file_name)

    # Return file path for HTML rendering
    # Note: The file path is relative to the HTML directory
    return generate_plot_file_name("bar_chart", path="./plots", uuid=uuid)
