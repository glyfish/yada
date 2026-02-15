import shortuuid

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.prompt_mgr import pull_prompt
from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent
from apps.agentic.agents.plots.time_series_plot_agent import TimeSeriesPlotAgent
from lib.logger import get_logger

logger = get_logger("YADA")

_search_agent = SearchAgent()
_bar_chart_agent = BarChartAgent()
_time_series_plot_agent = TimeSeriesPlotAgent()

@tool
async def delegate_to_search_agent(request: str) -> str:
    """
    Delegate a request to the Search Agent which performs web searches. Use for factual questions, 
    current events, data lookup, or research.

    Examples of when to use this tool:
        - "What is the history of Tullahoma TN"
        - "Compare the populations of the 10 largest cities in the world"
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _search_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool
async def delegate_to_bar_chart_agent(request: str) -> str:
    """
    Delegate a request to the Bar Chart Agent which creates bar charts from categorical data.
    Use this when the user wants to visualize data as a bar chart.

    Examples of when to use this tool:
        - "Compare the populations of the 10 largest cities in the world in a bar chart"
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _bar_chart_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content

@tool
async def delegate_to_time_series_plot_agent(request: str) -> str:
    """
    Delegate a request to the Time Series Plot Agent which creates time series plots from temporal data.
    Use this when the user wants to visualize data over time.

    Examples of when to use this tool:
        - "Plot a time series for the population of Tennessee."
        - "Plot the population of Tennessee."
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _time_series_plot_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content

class OrchestratorAgent(ReactAgent):

    def __init__(self):
        tools = [delegate_to_search_agent, 
                 delegate_to_bar_chart_agent,
                 delegate_to_time_series_plot_agent]
        tool_node_name = "orchestrator_tool_node"
        super().__init__(tools, tool_node_name)

    def create_prompt(self):
        return pull_prompt("orchestrator")
