from pydantic import BaseModel, Field
from typing import Dict
from numpy.typing import NDArray
import shortuuid

from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool

from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm, should_continue

import os
import sys
import numpy
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

from lib import config
from lib.plots import bar
from lib.utils import generate_plot_file_name
from lib.logger import get_logger

logger = get_logger("YADA")

class TimeSeriesPlotInput(BaseModel):
    """Input schema for the time series plot generator."""
    time: NDArray[numpy.datetime64] = Field(..., description="Array of time series timestamps")
    values: NDArray[numpy.float64] = Field(..., description="Array of numeric values corresponding to the timestamps")
    title: str = Field(default="Time Series Plot", description="Title of the chart")
    x_axis_label: str = Field(default="Time", description="Label for the x-axis")
    y_axis_label: str = Field(default="Value", description="Label for the y-axis")


class TimeSeriesPlotAgent:
    """
    Time Series Plot Agent that uses a language model to generate time series plot data.
    It can call tools like TavilySearchResults to fetch search results.
    """

    def __init__(self):
        self.__llm = build_llm()
        self.__prompt = self.__create_prompt()
        self.__tools = [TimeSeriesPlotAgent.time_series_plot_tool]
        self.__tool_node = ToolNode(self.__tools, name="time_series_plot_tool_node")
        self.__tooled_llm = self.__llm.bind_tools(self.__tools)
        self.__agent = self.__create_agent()

        sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
        pyplot.style.use(config.glyfish_style)

    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """
        return self.__agent
    

    async def __invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        """
        Invoke the agent with the current state.
        """
        messages = state["messages"]
        prompt_messages = self.__prompt.format_messages(messages=messages)
        result = await self.__tooled_llm.ainvoke(prompt_messages)
        return {"messages": [result]}
    

    def __create_prompt(self):
        """
        Create the prompt template for the time series plot agent.
        This defines how the model should interpret the messages and what it should do.
        """

        system_prompt = (
            "You are a time series plot generator. Given the conversation below, "
            "generate a time series plot based on the provided data. "
            "The input will include an array of timestamps, an array of numeric values, "
            "a title for the plot, and labels for the x-axis and y-axis. "
            "The plot image should be styled using the time_series_plot CSS class in an enclosing div."
        )

        logger.debug(f"Time Series Plot Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
    

    def __create_agent(self):
        """
        Create the state graph for the time series plot agent.
        This defines the flow of the agent's operations.
        """

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self.__invoke_model)
            .add_node("tool", self.__tool_node)
            .add_edge(START, "model")
            .add_edge("tool", "model")
            .add_conditional_edges(
                "model",
                should_continue,
                {
                    "tool": "tool",
                    END: END,
                }
            )
        )

        return graph.compile()