from pydantic import BaseModel, Field
from numpy.typing import NDArray
import shortuuid

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool

from apps.agentic.core.agents.react_agent import ReactAgent

import os
import sys
import numpy
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from lib import config
from lib.plots import curve, PlotType
from lib.utils import generate_plot_file_name
from lib.logger import get_logger

logger = get_logger("YADA")

class TimeSeriesPlotInput(BaseModel):
    """Input schema for the time series plot generator."""
    time: list[datetime] = Field(..., description="Array of time series timestamps")
    values: list[float] = Field(..., description="Array of numeric values corresponding to the timestamps")
    title: str = Field(default="Time Series Plot", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class TimeSeriesPlotAgent(ReactAgent):
    """
    Time Series Plot Agent that uses a language model to generate time series plot data.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        tools = [TimeSeriesPlotAgent.time_series_plot_tool]
        tool_node_name = "time_series_plot_tool_node"

        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
        pyplot.style.use(config.glyfish_style)

        super().__init__(tools, tool_node_name)


    def create_prompt(self):
        """
        Create the prompt template for the time series plot agent.
        This defines how the model should interpret the messages and what it should do.
        """

        system_prompt = (
            "You are a time series plot generator.You may use the time_series_plot_tool tool to generate a time series plot "
            "based on the provided data. The input will include an array of timestamps, an array of numeric values, "
            "a title for the plot, labels for the x-axis and y-axis, and the type of plot axis "
            "(e.g., LINEAR, YLOG, XLOG, LOGLOG). "
            "The plot image should be styled using the time_series_plot CSS class in an enclosing div. "
            "If more than two variables are provided put the data in separate plots" 
        )

        logger.debug(f"Time Series Plot Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
    @tool(args_schema=TimeSeriesPlotInput)
    def time_series_plot_tool(time: list[datetime], 
                              values: list[float], 
                              title: str, 
                              x_axis_label: str, 
                              y_axis_label: str,
                              plot_axis_type: PlotType) -> str:
        """Generate a time series plot from data points and display it.

        Parameters
        ----------
            time: list[datetime]
                Array of timestamps for the x-axis
            values: list[float]
                Array of numeric values for the y-axis
            title: str
                Title of the chart.
            x_axis_label: str
                Label for the x-axis.
            y_axis_label: str
                Label for the y-axis.
            plot_axis_type: PlotType
                Type of plot axis (e.g., YLOG for logarithmic y-axis)
                (Possible values: LINEAR, YLOG, XLOG, LOGLOG)
        Returns:
            plot file name: str
                The file name of the generated bar chart image.
            
        Example:
            input = BarChartInput(
                data={"A": 10, "B": 20, "C": 15},
                title="Sample Chart",
                x_axis_label="Letter",
                y_axis_label="Count",
                xlabel_rotation=45
            )
        """

        logger.debug(f"Calling time_series_plot_tool: {(time, values)}, title: {title}, "
                     f"xlabel: {x_axis_label}, ylabel: {y_axis_label}, plot_axis_type: {plot_axis_type}")

        time_series_file = TimeSeriesPlotAgent.generate_time_series_plot(
            time=numpy.array(time), 
            values=numpy.array(values),
            title=title, 
            xlabel=x_axis_label, 
            ylabel=y_axis_label,
            plot_axis_type=plot_axis_type
        )

        logger.debug(f"Generated time series file: {time_series_file}")

        return time_series_file

    @staticmethod
    def generate_time_series_plot(time: NDArray, values: NDArray, title: str, xlabel: str, ylabel: str,
                                  plot_axis_type: PlotType) -> str:
        """
        Create a bar chart from the provided data.
        
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
                chart ylabel
            plot_axis_type: PlotType
                Type of plot axis (e.g., YLOG for logarithmic y-axis)
                (Possible values: PlotType.LINEAR, PlotType.YLOG, PlotType.XLOG, PlotType.LOGLOG)

        Returns:
            str: A string representation of the bar chart
        """

        logger.debug(f"Calling generate_time_series_plot: {time}, {values}, title: {title}, xlabel: {xlabel}, "
                     f"ylabel: {ylabel}, plot_axis_type: {plot_axis_type}")

        uuid = shortuuid.uuid()
        output_file_name = generate_plot_file_name("time_series_plot", path="./html/plots", uuid=uuid)

        curve(values, time, xlabel=xlabel, ylabel=ylabel, title=title, figsize=(10, 6), 
              file_name=output_file_name, plot_axis_type=plot_axis_type)

        # Return file path for HTML rendering
        # Note: The file path is relative to the HTML directory
        return generate_plot_file_name("time_series_plot", path="./plots", uuid=uuid)
