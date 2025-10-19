from pydantic import BaseModel, Field
from typing import Dict
import shortuuid

from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.utils import build_llm

import os
import sys
import numpy

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from apps.agentic.core.agents.tool_agent import ToolAgent

from lib import config
from lib.plots import bar
from lib.utils import generate_plot_file_name
from lib.logger import get_logger

logger = get_logger("YADA")

class BarChartInput(BaseModel):
    """Input schema for the bar chart generator."""
    data: Dict[str, float] = Field(..., description="Dictionary where keys are labels and values are numeric values to plot")
    title: str = Field(default="Bar Chart", description="Title of the chart")
    x_axis_label: str = Field(default="Category", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")
    xlabel_rotation: float = Field(default=0.0, description="Rotation angle for the x-axis labels")

class BarChartAgent(ToolAgent):
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
    
        system_prompt = (
            "You are a chart generator. You may use the bar_chart_tool tool to generate a bar chart "
            "as instructed by the user. The bar_chart_tool takes the following parameters: a dictionary "
            "containing the data points to plot with keys identifying the data categories and values as the numeric "
            "values to plot, a plot title, a description label of the categories to label the x-axis, a label for "
            "the y-axis describing the data values and a rotation angle for "
            "the x-axis labels should be 90 degrees if the largest category string is larger than 7 characters "
            "or 45 degrees if the largest category string is greater than 2 characters "
            "otherwise the rotation should be zero. Sort the values in descending order. The bar_chart_tool will return a path to the plot image file. "
            "The returned response should be in markdown and should include commentary on the data displayed above and " 
            "the html plot image should be styled using the bar_chart CSS class in an enclosing div. "
            "If more than two variables are provided put the data in separate plots" 
        )

        logger.debug(f"Bar Chart Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in plain text."),
        ])
    
    
    @staticmethod
    @tool(args_schema=BarChartInput)
    def bar_chart_tool(data: Dict[str, float], 
                       title: str,  
                       x_axis_label: str, 
                       y_axis_label: str,
                       xlabel_rotation: float) -> str:
        """Generate a bar chart from data points and display it.
        
        Parameters
        ----------
            data: Dict[str, float]
                Dictionary where keys are labels and values are numeric values to plot
            title: str
                Title of the chart.
            x_axis_label: str
                Label for the x-axis.
            y_axis_label: str
                Label for the y-axis.
            xlabel_rotation: int
                Rotation angle for the x-axis labels.
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

        logger.debug(f"Calling bar_chart_tool: {data}, title: {title}, xlabel: {x_axis_label}, ylabel: {y_axis_label}, xlabel_rotation: {xlabel_rotation}")

        bar_chart_file = BarChartAgent.generate_bar_chart(
            data=data, 
            title=title, 
            xlabel=x_axis_label, 
            ylabel=y_axis_label, 
            xlabel_rotation=xlabel_rotation
        )

        logger.debug(f"Generated bar chart file: {bar_chart_file}")
        
        return bar_chart_file


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
    
