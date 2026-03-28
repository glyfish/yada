from pydantic import BaseModel, Field
from typing import Dict
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
from lib.plots import bar
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

class BarChartAgent(ReactAgent):
    """
    BarChart Agent that uses a language model to generate bar chart data.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        tools = [BarChartAgent.bar_chart_tool]
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
            You are a chart generator. You may use the bar_chart_tool tool to generate a bar chart 
            as instructed by the user.
            </instructions>

            <tool_instructions>
            bar_chart_tool
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
                    - If more than two variables are provided put the data in separate plots.
                    - If you choose to call a tool, do so; otherwise, provide your findings in plain text
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
                Returns a file path to the rendered chart for display in the UI.
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
    
