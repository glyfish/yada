from __future__ import annotations

import shortuuid
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent
from apps.agentic.agents.plots.time_series_plot_agent import TimeSeriesPlotAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_bar_chart_agent = BarChartAgent()
_time_series_plot_agent = TimeSeriesPlotAgent()


class SubagentRequest(BaseModel):
    request: str = Field(..., description="Request to send to the subagent")


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Bar Chart Agent which creates bar charts from categorical data.
            Use when the user wants to visualize labeled, non-temporal data as a bar chart.
            Returns the generated chart as an HTML image tag string.
        """,
        positive_examples=[
            PositiveExample(input="Compare the populations of the 10 largest cities in the world in a bar chart."),
            PositiveExample(input="Plot the GDP of these countries as a bar chart."),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot the US GDP over time.",
                reason="Temporal data requires delegate_to_time_series_plot_agent.",
            ),
        ],
    ),
)
async def delegate_to_bar_chart_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _bar_chart_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Time Series Plot Agent which creates time series plots
            from temporal data. Use when the user wants to visualize data over time.
            Returns the generated chart as an HTML image tag string.
        """,
        positive_examples=[
            PositiveExample(input="Plot a time series for the population of Tennessee."),
            PositiveExample(input="Compare the population of Tennessee and Alabama over time."),
            PositiveExample(input="Plot GDP and unemployment rate over time as stacked charts."),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot the unemployment report.",
                reason="Report plots must go to delegate_to_time_series_agent, not here.",
            ),
            NegativeExample(
                input="Compare sales by region in a bar chart.",
                reason="Categorical data requires delegate_to_bar_chart_agent.",
            ),
        ],
    ),
)
async def delegate_to_time_series_plot_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _time_series_plot_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


class PlotAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "PlotAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            delegate_to_bar_chart_agent,
            delegate_to_time_series_plot_agent,
        ]
        super().__init__(tools, "plot_agent_tool_node", mcp_tools=mcp_tools)

    def create_prompt(self):
        system_prompt = """
<instructions>
You are a plot agent responsible for all chart and visualization requests.
Route each request to the appropriate tool using the rules below.
</instructions>

<bar_charts>
When the user wants to visualize categorical or labeled data (not time-based), call
delegate_to_bar_chart_agent. Examples: comparing values across countries, cities, products,
or categories.
</bar_charts>

<time_series>
When the user wants to visualize data over time, call delegate_to_time_series_plot_agent.
Examples: plotting trends, comparing time series, stacked time series.
Do NOT use this for report plots — those are handled by the time series agent.
</time_series>
"""
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
