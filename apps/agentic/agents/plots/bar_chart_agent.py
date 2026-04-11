from pydantic import BaseModel, Field
from typing import Dict, List
import shortuuid

from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.core.agents.messages import WorkerState

import os
import sys
import numpy

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from apps.agentic.core.agents.react_agent import ReactAgent

from lib import config
from lib.plots import bar, multibar
from lib.utils import generate_plot_file_name
from lib.logger import get_logger

logger = get_logger("YADA")

class BarChartInput(BaseModel):
    """
    Input schema for the bar chart generator.
    """
    
    data: Dict[str, float] = Field(..., description="Dictionary where keys are labels and values are numeric values to plot")
    title: str = Field(default="Bar Chart", description="Title of the chart")
    x_axis_label: str = Field(default="Category", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    xlabel_rotation: float = Field(default=0.0, description="Rotation angle for the x-axis labels")

class MultiBarChartInput(BaseModel):
    """
    Input schema for the multi-bar chart generator.
    """

    categories: List[str] = Field(..., description="Shared category labels for the x-axis (same for all datasets)")
    datasets: List[Dict[str, float]] = Field(..., description="List of datasets, each a dict mapping category label to value. All dicts must have the same keys as categories.")
    labels: List[str] = Field(..., description="Legend label for each dataset")
    title: str = Field(default="Multi-Bar Chart", description="Title of the chart")
    x_axis_label: str = Field(default="Category", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    xlabel_rotation: float = Field(default=0.0, description="Rotation angle for the x-axis labels")


class BarChartAgent(ReactAgent):
    """
    BarChart Agent that uses a language model to generate bar chart data.
    It can call tools like TavilySearchResults to fetch search results.
    """

    @classmethod
    async def create(cls) -> "BarChartAgent":
        return cls()

    def __init__(self):
        tools = [BarChartAgent.bar_chart_tool,
                 BarChartAgent.multi_bar_chart_tool]
        tool_node_name = "bar_chart_tool_node"

        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
        pyplot.style.use(config.glyfish_style)

        super().__init__(tools, tool_node_name)

    
    def create_prompt(self):
        """
        Create the prompt template for the BarChartAgent agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        system_prompt = """
            <instructions>
            You are a chart generator. You may use the following tools to generate bar charts:
            - bar_chart_tool: single dataset bar chart
            - multi_bar_chart_tool: grouped bar chart comparing multiple datasets across shared categories

            Always provide insightful commentary on the data in markdown format above the chart. Then, on a 
            new line with a blank line before it, include the HTML fragment returned by the tool to 
            display the chart image. Do not mix the HTML fragment within the markdown text.

            When writing commentary, do not use the $ symbol for currency as it will be interpreted as a
            math delimiter by the markdown renderer. Use the currency name or abbreviation instead
            (e.g. "USD", "EUR", "4,086B" not "$4,086B").
            </instructions>

            <tool_instructions>
            bar_chart_tool
                Use when there is a single dataset to display as a bar chart.
                Input
                    - data: Dict[str, float]
                        Data points to plot with keys identifying the data categories and values to plot
                    - title: str
                        A brief description of the chart to use as the title
                    - x_axis_label: str
                        A label for the x-axis describing the data categories
                    - y_axis_label: str
                        A label for the y-axis describing the data values
                    - xlabel_rotation: float
                        A rotation angle for the x-axis labels the x-axis labels should be 90 degrees if the
                        largest category string is larger than 7 characters or 45 degrees if the largest category string is
                        greater than 2 characters otherwise the rotation should be zero. Sort the values in descending order.
                Output
                    - The bar_chart_tool will return an HTML fragment containing the plot image that should be
                      inserted into the tool response. The returned response should be in markdown and should
                      include commentary on the data displayed above the chart, followed by the returned
                      HTML fragment.
                    - If you choose to call a tool, do so; otherwise, provide your findings in plain text

            multi_bar_chart_tool
                Use when comparing multiple datasets across the same categories (e.g. GDP of several countries
                across multiple years). Maximum 6 datasets. All datasets must share the same categories.
                Input
                    - categories: List[str]
                        Shared category labels for the x-axis, same for all datasets.
                    - datasets: List[Dict[str, float]]
                        One dict per dataset, each mapping category label to numeric value.
                    - labels: List[str]
                        Legend label for each dataset.
                    - title: str
                        A brief description of the chart to use as the title.
                    - x_axis_label: str
                        A label for the x-axis describing the categories.
                    - y_axis_label: str
                        A label for the y-axis describing the values.
                    - xlabel_rotation: float
                        Rotation angle for x-axis labels. Use 90 if the longest category label exceeds
                        7 characters, 45 if it exceeds 2 characters, otherwise 0.
                Output
                    - The multi_bar_chart_tool will return an HTML fragment containing the plot image that should be
                      inserted into the tool response. The returned response should be in markdown and should
                      include commentary on the data displayed above the chart, followed by the returned
                      HTML fragment.
            </tool_instructions>
            """

        logger.debug(f"Bar Chart Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
    
    
    @staticmethod
    @tool_spec(
        args_schema=BarChartInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a bar chart image from labeled numeric data.
                
                Returns an HTML fragment with the rendered chart for display in the UI.
                The returned response should place all markdown commentary first, 
                followed by the HTML fragment on its own line with a blank line before it.
                Do not mix the HTML fragment within the markdown text.

                Sort values in descending order. Use xlabel_rotation=90 if the longest category label
                exceeds 7 characters, 45 if it exceeds 2 characters, otherwise 0.
                If more than two variables are provided, put the data in separate plots.
                """
            ,
            positive_examples=[
                PositiveExample(input="Create a bar chart of sales by region."),
                PositiveExample(input="Plot the GDP of these countries as a bar chart."),
                PositiveExample(input="Show me a bar chart comparing the populations of these cities."),
            ],
            requires_context=[
            ],
            negative_examples=[
                NegativeExample(input="Plot this data as a time series.", 
                                reason="Time series data requires a line chart, not a bar chart."),
            ],
        ),
    )
    def bar_chart_tool(data: Dict[str, float],
                       title: str,
                       x_axis_label: str,
                       y_axis_label: str,
                       xlabel_rotation: int) -> str:

        logger.debug(f"Calling bar_chart_tool: {data}, title: {title}, xlabel: {x_axis_label}, "
                     f"ylabel: {y_axis_label}, xlabel_rotation: {xlabel_rotation}")

        bar_chart_file = BarChartAgent.generate_bar_chart(
            data=data, 
            title=title, 
            xlabel=x_axis_label, 
            ylabel=y_axis_label, 
            xlabel_rotation=xlabel_rotation
        )

        logger.debug(f"Generated bar chart file: {bar_chart_file}")

        return f'<div class="bar-chart"><img src="{bar_chart_file}"></div>'


    @staticmethod
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


    @staticmethod
    @tool_spec(
        args_schema=MultiBarChartInput,
        metadata=ToolSpec(
            primary_function=
                """
                Generate a grouped multi-bar chart comparing multiple datasets across shared categories.
                
                Returns an HTML fragment with the rendered chart for display in the UI.
                The returned response should place all markdown commentary first, 
                followed by the HTML fragment on its own line with a blank line before it.
                Do not mix the HTML fragment within the markdown text.

                Use when the user wants to compare multiple datasets side-by-side per category.
                Maximum 6 datasets. All datasets must share the same category labels.
                Use xlabel_rotation=90 if the longest category label exceeds 7 characters,
                45 if it exceeds 2 characters, otherwise 0.
                """,
            positive_examples=[
                PositiveExample(input="Compare GDP of the US, China, and Germany across the last 5 years."),
                PositiveExample(input="Show me a grouped bar chart of sales by region for these 4 products."),
            ],
            requires_context=[
            ],
            negative_examples=[
                NegativeExample(input="Plot a single dataset as a bar chart.",
                                reason="Use bar_chart_tool for a single dataset."),
                NegativeExample(input="Plot this data as a time series.",
                                reason="Time series data requires a line chart, not a bar chart."),
            ],
        ),
    )
    def multi_bar_chart_tool(categories: List[str],
                             datasets: List[Dict[str, float]],
                             labels: List[str],
                             title: str,
                             x_axis_label: str,
                             y_axis_label: str,
                             xlabel_rotation: float) -> str:

        logger.debug(f"Calling multi_bar_chart_tool: title: {title}, xlabel: {x_axis_label}, "
                     f"ylabel: {y_axis_label}, labels: {labels}, xlabel_rotation: {xlabel_rotation}")

        bar_chart_file = BarChartAgent.generate_multi_bar_chart(
            categories=categories,
            datasets=datasets,
            labels=labels,
            title=title,
            xlabel=x_axis_label,
            ylabel=y_axis_label,
            xlabel_rotation=xlabel_rotation
        )

        logger.debug(f"Generated multi-bar chart file: {bar_chart_file}")

        return f'<div class="bar-chart"><img src="{bar_chart_file}"></div>'


    @staticmethod
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

