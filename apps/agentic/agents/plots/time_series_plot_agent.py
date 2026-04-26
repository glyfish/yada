from pydantic import BaseModel, Field
from numpy.typing import NDArray
import shortuuid

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.series_cache import SeriesCache
from apps.agentic.core.series_ref import SeriesRef

import os
import sys
import numpy
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from lib import config
from lib.plots import curve, stack, comparison, PlotType
from lib.utils import generate_plot_file_name
from lib.logger import get_logger

logger = get_logger("YADA")


def _load_series(series_ref_json: str, date_from: str | None, date_to: str | None) -> tuple[list[datetime], list[float]]:
    ref = SeriesRef.from_json(series_ref_json)
    entry = SeriesCache._get_by_cache_id_sync(ref.cache_id)
    if entry is None:
        raise ValueError(f"Series {ref.native_id} not found in cache")
    observations = entry["data"].get("observations", [])
    times, values = [], []
    for obs in observations:
        if obs.get("value") == ".":
            continue
        d = obs["date"]
        if date_from and d < date_from:
            continue
        if date_to and d > date_to:
            continue
        times.append(datetime.strptime(d, "%Y-%m-%d"))
        values.append(float(obs["value"]))
    return times, values

class SeriesFromCacheInput(BaseModel):
    """Input schema for single-series cache-based plot."""
    series_ref: str = Field(..., description="SeriesRef JSON string returned by the data fetcher agent")
    date_from: str | None = Field(None, description="Filter start date ISO format YYYY-MM-DD (inclusive)")
    date_to: str | None = Field(None, description="Filter end date ISO format YYYY-MM-DD (inclusive)")
    title: str = Field(default="Time Series Plot", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class MultiSeriesFromCacheInput(BaseModel):
    """Input schema for multi-series cache-based plots."""
    series_refs: list[str] = Field(..., description="List of SeriesRef JSON strings, one per series")
    date_from: str | None = Field(None, description="Filter start date ISO format YYYY-MM-DD (inclusive)")
    date_to: str | None = Field(None, description="Filter end date ISO format YYYY-MM-DD (inclusive)")
    title: str = Field(default="Time Series Plot", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_labels: list[str] | None = Field(default=None, description="Y-axis label for each series")
    y_axis_label: str = Field(default="Value", description="Shared y-axis label (comparison plot only)")
    labels: list[str] | None = Field(default=None, description="Legend or annotation label for each series")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class TimeSeriesPlotInput(BaseModel):
    """Input schema for the time series plot generator."""
    time: list[datetime] = Field(..., description="Array of time series timestamps")
    values: list[float] = Field(..., description="Array of numeric values corresponding to the timestamps")
    title: str = Field(default="Time Series Plot", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class TimeSeriesStackInput(BaseModel):
    """Input schema for the time series stack plot generator."""
    time: list[datetime] = Field(..., description="Timestamps shared across all series")
    values: list[list[float]] = Field(..., description="List of numeric series, one per stacked plot")
    title: str = Field(default="Time Series Stack", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_labels: list[str] | None = Field(default=None, description="Y-axis label for each stacked plot")
    labels: list[str] | None = Field(default=None, description="Text label annotated on each stacked plot")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class TimeSeriesComparisonInput(BaseModel):
    """Input schema for the time series comparison plot generator."""
    time: list[datetime] = Field(..., description="Timestamps shared across all series")
    values: list[list[float]] = Field(..., description="List of numeric series to overlay on the same axis")
    title: str = Field(default="Time Series Comparison", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    labels: list[str] | None = Field(default=None, description="Legend label for each series")
    plot_axis_type: PlotType = Field(default=PlotType.LINEAR, description="Type of plot axis")


class TimeSeriesPlotAgent(ReactAgent):
    """
    Time Series Plot Agent that uses a language model to generate time series plot data.
    It can call tools like TavilySearchResults to fetch search results.
    """

    @classmethod
    async def create(cls) -> "TimeSeriesPlotAgent":
        return cls()


    def __init__(self, mcp_tools: list = []):
        tools = [
            TimeSeriesPlotAgent.time_series_plot_from_cache,
            TimeSeriesPlotAgent.time_series_stack_from_cache,
            TimeSeriesPlotAgent.time_series_comparison_from_cache,
            TimeSeriesPlotAgent.time_series_plot_tool,
            TimeSeriesPlotAgent.time_series_stack_tool,
            TimeSeriesPlotAgent.time_series_comparison_tool,
        ]
        tool_node_name = "time_series_plot_tool_node"

        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
        pyplot.style.use(config.glyfish_style)

        super().__init__(tools, tool_node_name, mcp_tools=mcp_tools)


    def create_prompt(self):
        """
        Create the prompt template for the time series plot agent.
        This defines how the model should interpret the messages and what it should do.
        """

        system_prompt = """
            <instructions>
            You are a time series plot generator. You may use the following tools to generate time series plots:

            When the request contains a SeriesRef JSON string (from the data fetcher agent), use the cache tools:
            - time_series_plot_from_cache: single series from cache
            - time_series_stack_from_cache: multiple series stacked on separate axes, each from cache
            - time_series_comparison_from_cache: multiple series overlaid on the same axis, each from cache

            When raw time and value arrays are provided directly, use:
            - time_series_plot_tool: single time series
            - time_series_stack_tool: multiple series on separate vertically stacked axes
            - time_series_comparison_tool: multiple series overlaid on the same axis

            Always provide insightful commentary on the data in markdown format above the chart. Then, on a 
            new line with a blank line before it, include the HTML fragment returned by the tool to 
            display the chart image. Do not mix the HTML fragment within the markdown text.

            When writing commentary, do not use the $ symbol for currency as it will be interpreted as a
            math delimiter by the markdown renderer. Use the currency name or abbreviation instead
            (e.g. "USD", "EUR", "4,086B" not "$4,086B").
            </instructions>

            <tool_instructions>
            time_series_plot_tool
                Use when the user wants to plot a single time series.
                Input
                    - time: list[datetime]
                        Timestamps for the x-axis of the data points.
                    - values: list[float]
                        Numeric values for the y-axis.
                    - title: str
                        Title of the chart.
                    - x_axis_label: str
                        Label for the x-axis.
                    - y_axis_label: str
                        Label for the y-axis.
                    - plot_axis_type: PlotType
                        Type of plot axis (e.g., LINEAR, YLOG, XLOG, LOGLOG).
                Output
                    - The tool will return an HTML fragment containing the plot image that should be
                      inserted into the tool response. The returned response should be in markdown and should
                      include commentary on the data displayed above the chart, followed by the returned
                      HTML fragment.

            time_series_stack_tool
                Use when the user wants to see multiple time series each on its own axis, stacked vertically.
                Input
                    - time: list[datetime]
                        Timestamps shared across all series.
                    - values: list[list[float]]
                        One list of values per stacked plot.
                    - title: str
                        Title of the chart.
                    - x_axis_label: str
                        Label for the shared x-axis.
                    - y_axis_labels: list[str] | None
                        Y-axis label for each stacked plot.
                    - labels: list[str] | None
                        Text label annotated on each stacked plot.
                    - plot_axis_type: PlotType
                        Type of plot axis (e.g., LINEAR, YLOG, XLOG, LOGLOG).
                Output
                    - The tool will return an HTML fragment containing the plot image that should be
                      inserted into the tool response. The returned response should be in markdown and should
                      include commentary on the data displayed above the chart, followed by the returned
                      HTML fragment.

            time_series_comparison_tool
                Use when the user wants to compare multiple time series overlaid on the same axis.
                Input
                    - time: list[datetime]
                        Timestamps shared across all series.
                    - values: list[list[float]]
                        One list of values per series.
                    - title: str
                        Title of the chart.
                    - x_axis_label: str
                        Label for the x-axis.
                    - y_axis_label: str
                        Label for the y-axis.
                    - labels: list[str] | None
                        Legend label for each series.
                    - plot_axis_type: PlotType
                        Type of plot axis (e.g., LINEAR, YLOG, XLOG, LOGLOG).
                Output
                    - The tool will return an HTML fragment containing the plot image that should be
                      inserted into the tool response. The returned response should be in markdown and should
                      include commentary on the data displayed above the chart, followed by the returned
                      HTML fragment.
            </tool_instructions>
            """

        logger.debug(f"Time Series Plot Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
    @tool_spec(
        args_schema=SeriesFromCacheInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a single time series plot for a series stored in the cache.
                Use when the request contains a SeriesRef JSON string from the data fetcher agent.
                Optionally filter the date range with date_from and date_to (YYYY-MM-DD).
                Returns an HTML fragment with the rendered chart.
                """,
            positive_examples=[
                PositiveExample(input='Plot {"source":"fred","native_id":"UNRATE","cache_id":"..."} since 2000.'),
            ],
        ),
    )
    def time_series_plot_from_cache(series_ref: str,
                                    date_from: str | None,
                                    date_to: str | None,
                                    title: str,
                                    x_axis_label: str,
                                    y_axis_label: str,
                                    plot_axis_type: PlotType) -> str:
        times, values = _load_series(series_ref, date_from, date_to)
        file = TimeSeriesPlotAgent.generate_time_series_plot(
            time=numpy.array(times),
            values=numpy.array(values),
            title=title,
            xlabel=x_axis_label,
            ylabel=y_axis_label,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=MultiSeriesFromCacheInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a stacked time series plot for multiple series stored in the cache,
                each on its own vertically stacked axis sharing a common time axis.
                Use when the request contains multiple SeriesRef JSON strings.
                Optionally filter the date range with date_from and date_to (YYYY-MM-DD).
                Returns an HTML fragment with the rendered chart.
                """,
            positive_examples=[
                PositiveExample(input="Stack UNRATE and GDP from cache since 2000."),
            ],
        ),
    )
    def time_series_stack_from_cache(series_refs: list[str],
                                     date_from: str | None,
                                     date_to: str | None,
                                     title: str,
                                     x_axis_label: str,
                                     y_axis_labels: list[str] | None,
                                     labels: list[str] | None,
                                     plot_axis_type: PlotType,
                                     **kwargs) -> str:
        all_times, all_values = zip(*[_load_series(r, date_from, date_to) for r in series_refs])
        file = TimeSeriesPlotAgent.generate_time_series_stack(
            time=numpy.array(all_times[0]),
            values=[numpy.array(v) for v in all_values],
            title=title,
            xlabel=x_axis_label,
            ylabels=y_axis_labels,
            labels=labels,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=MultiSeriesFromCacheInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a comparison time series plot for multiple series stored in the cache,
                overlaid on the same axis.
                Use when the request contains multiple SeriesRef JSON strings.
                Optionally filter the date range with date_from and date_to (YYYY-MM-DD).
                Returns an HTML fragment with the rendered chart.
                """,
            positive_examples=[
                PositiveExample(input="Compare UNRATE and GDP from cache on the same chart."),
            ],
        ),
    )
    def time_series_comparison_from_cache(series_refs: list[str],
                                          date_from: str | None,
                                          date_to: str | None,
                                          title: str,
                                          x_axis_label: str,
                                          y_axis_label: str,
                                          labels: list[str] | None,
                                          plot_axis_type: PlotType,
                                          **kwargs) -> str:
        all_times, all_values = zip(*[_load_series(r, date_from, date_to) for r in series_refs])
        file = TimeSeriesPlotAgent.generate_time_series_comparison(
            time=numpy.array(all_times[0]),
            values=[numpy.array(v) for v in all_values],
            title=title,
            xlabel=x_axis_label,
            ylabel=y_axis_label,
            labels=labels,
            plot_axis_type=plot_axis_type,
        )
        return f'<div class="time-series-plot"><img src="{file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=TimeSeriesPlotInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a single time series plot from timestamped numeric data.
                
                Returns an HTML fragment with the rendered chart for display in the UI.
                The returned response should place all markdown commentary first, 
                followed by the HTML fragment on its own line with a blank line before it.
                Do not mix the HTML fragment within the markdown text.
                
                Use plot_axis_type=YLOG for data spanning many orders of magnitude.
                """,
            positive_examples=[
                PositiveExample(input="Plot the US GDP over time."),
                PositiveExample(input="Show me a time series of Tennessee population."),
            ],
            requires_context=[
            ],
            negative_examples=[
                NegativeExample(input="Compare sales by region in a chart.",
                                reason="Categorical data requires a bar chart, not a time series."),
            ],
        ),
    )
    def time_series_plot_tool(time: list[datetime],
                              values: list[float],
                              title: str,
                              x_axis_label: str,
                              y_axis_label: str,
                              plot_axis_type: PlotType) -> str:

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

        return f'<div class="time-series-plot"><img src="{time_series_file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=TimeSeriesStackInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a stacked time series plot with multiple series each on its own vertically stacked axis
                that share a common time axis. 
                
                Returns an HTML fragment with the rendered chart for display in the UI.
                The returned response should place all markdown commentary first, 
                followed by the HTML fragment on its own line with a blank line before it.
                Do not mix the HTML fragment within the markdown text.
                
                Use when the user wants to compare multiple time series without overlapping.
                
                This type of plot is especially useful when the series have different scales or units, as it allows 
                each series to be scaled independently while still sharing the same time axis for easy comparison of
                trends and patterns over time. Use plot_axis_type=YLOG for data spanning many orders of magnitude.
                
                Use this plot if the user explicitly asks for "stacked" time series comparison or if they want to see each 
                series on its own axis.
                """,
            positive_examples=[
                PositiveExample(input="Plot GDP, population, and unemployment rate over time as stacked charts."),
                PositiveExample(input="Show me temperature, humidity, and pressure as stacked time series."),
            ],
            requires_context=[
            ],
            negative_examples=[
                NegativeExample(input="Overlay multiple time series on the same axis.",
                                reason="Use time_series_comparison_tool for overlaid series."),
            ],
        ),
    )
    def time_series_stack_tool(time: list[datetime],
                               values: list[list[float]],
                               title: str,
                               x_axis_label: str,
                               y_axis_labels: list[str] | None,
                               labels: list[str] | None,
                               plot_axis_type: PlotType) -> str:

        logger.debug(f"Calling time_series_stack_tool: title: {title}, "
                     f"xlabel: {x_axis_label}, ylabels: {y_axis_labels}, plot_axis_type: {plot_axis_type}")

        time_series_file = TimeSeriesPlotAgent.generate_time_series_stack(
            time=numpy.array(time),
            values=[numpy.array(v) for v in values],
            title=title,
            xlabel=x_axis_label,
            ylabels=y_axis_labels,
            labels=labels,
            plot_axis_type=plot_axis_type
        )

        logger.debug(f"Generated time series stack file: {time_series_file}")

        return f'<div class="time-series-plot"><img src="{time_series_file}"></div>'


    @staticmethod
    @tool_spec(
        args_schema=TimeSeriesComparisonInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a comparison time series plot with multiple series overlaid on the same 
                x and y axis.

                Returns an HTML fragment with the rendered chart for display in the UI.
                
                Use when the user wants to compare multiple time series on the same scale
                to easily compare trends and patterns. This type of plot is especially useful when the series have 
                similar scales or units. Use plot_axis_type=YLOG for data spanning many orders of magnitude.
                
                Use this plot if the user explicitly asks for "overlaid" time series comparison or if they want to see each 
                series on the same axis.
                """,
            positive_examples=[
                PositiveExample(input="Compare US and UK GDP over time on the same chart."),
                PositiveExample(input="Overlay the stock prices of Apple and Microsoft over time."),
            ],
            requires_context=[
            ],
            negative_examples=[
                NegativeExample(input="Show each time series on its own axis.",
                                reason="Use time_series_stack_tool for separate axes."),
            ],
        ),
    )
    def time_series_comparison_tool(time: list[datetime],
                                    values: list[list[float]],
                                    title: str,
                                    x_axis_label: str,
                                    y_axis_label: str,
                                    labels: list[str] | None,
                                    plot_axis_type: PlotType) -> str:

        logger.debug(f"Calling time_series_comparison_tool: title: {title}, "
                     f"xlabel: {x_axis_label}, ylabel: {y_axis_label}, plot_axis_type: {plot_axis_type}")

        time_series_file = TimeSeriesPlotAgent.generate_time_series_comparison(
            time=numpy.array(time),
            values=[numpy.array(v) for v in values],
            title=title,
            xlabel=x_axis_label,
            ylabel=y_axis_label,
            labels=labels,
            plot_axis_type=plot_axis_type
        )

        logger.debug(f"Generated time series comparison file: {time_series_file}")

        return f'<div class="time-series-plot"><img src="{time_series_file}"></div>'


    @staticmethod
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


    @staticmethod
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


    @staticmethod
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
