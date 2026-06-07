from __future__ import annotations

import shortuuid
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.agents.plots.time_series_report_agent import TimeSeriesReportAgent
from apps.agentic.agents.time_series.time_series_data_fetcher_agent import TimeSeriesDataFetcherAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_time_series_report_agent = TimeSeriesReportAgent()


class SubagentRequest(BaseModel):
    request: str = Field(..., description="Request to send to the subagent")


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Time Series Data Fetcher Agent which retrieves time series
            data from external data sources via MCP. The agent discovers available MCP tools
            automatically on launch. Pass the series_id, source, and any date range in the request.
        """,
        positive_examples=[
            PositiveExample(input="Fetch the UNRATE series from FRED."),
            PositiveExample(input="Get US GDP data from FRED from 2000 to 2024."),
        ],
        requires_context=[
            "A series_id must already be known before calling this tool. "
            "Use delegate_to_time_series_report_agent or ask the user to search FRED first.",
        ],
        suggests_followup=[
            "delegate_to_time_series_report_agent to create a report from the fetched data.",
        ],
    ),
)
async def delegate_to_time_series_data_fetcher_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    agent = await TimeSeriesDataFetcherAgent.create()
    result = await agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Time Series Report Agent which creates, retrieves,
            lists, and plots time series reports. A report groups a set of time series cache IDs
            under a title and description for later reference.
            Use after collecting form data for report creation, or directly for list/get/plot requests.
            IMPORTANT: Always use this agent to plot a report — never delegate report plots to
            delegate_to_time_series_data_fetcher_agent.
        """,
        positive_examples=[
            PositiveExample(input="List all my time series reports."),
            PositiveExample(input="Show me the report with ID 0c9997f3-bbed-46d4-a8bb-570518b3653e."),
            PositiveExample(input="What reports do I have?"),
            PositiveExample(input="Plot the unemployment report."),
            PositiveExample(input="Plot the report with ID 0c9997f3-bbed-46d4-a8bb-570518b3653e."),
            PositiveExample(input="Generate a chart for my GDP report."),
        ],
        negative_examples=[
            NegativeExample(
                input="Fetch the UNRATE series from FRED.",
                reason="Use delegate_to_time_series_data_fetcher_agent to fetch raw data.",
            ),
        ],
        requires_context=[
            "For creating a report: form data (title, description, time_series_ids, time_range) "
            "must already be collected via request_human_form before calling this tool.",
            "For plotting without a specific report named: a report_id must already be selected "
            "via request_human_form before calling this tool.",
        ],
    ),
)
async def delegate_to_time_series_report_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _time_series_report_agent.agent.ainvoke(state, config)

    raw = result["messages"][-1].content
    if isinstance(raw, str):
        final = raw
    else:
        final = "\n".join(
            block.get("text", "")
            for block in raw
            if isinstance(block, dict) and block.get("type") == "text"
        )

    extra_html = [
        msg.content
        for msg in result["messages"]
        if isinstance(msg, ToolMessage) and isinstance(msg.content, str)
        and "<img" in msg.content and msg.content not in final
    ]
    if extra_html:
        logger.debug(f"delegate_to_time_series_report_agent: appending {len(extra_html)} HTML fragment(s)")
        return final + "\n\n" + "\n\n".join(extra_html)
    return final


class TimeSeriesAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "TimeSeriesAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            delegate_to_time_series_data_fetcher_agent,
            delegate_to_time_series_report_agent,
        ]
        super().__init__(tools, "time_series_agent_tool_node", mcp_tools=mcp_tools)

    def create_prompt(self):
        system_prompt = """
<instructions>
You are a time series agent responsible for all time series data fetching and report operations.
Route each request to the appropriate tool using the rules below.
</instructions>

<output_rule>
CRITICAL: When you receive a tool result your ONLY job is to copy its content to the user EXACTLY
as returned — character for character, with zero modifications.

- Do NOT add introductory text, headers, summaries, or commentary of any kind.
- Do NOT rephrase, condense, or reformat the tool output.
- Do NOT strip markdown, HTML tags, code fences, or any other formatting.
- Do NOT omit any section of the tool result, regardless of its length.
- Output the complete tool result verbatim as your entire response.

The tool responses contain precise formatting (HTML tags, image references, markdown, JSON blocks)
that must be preserved exactly. Any modification breaks downstream rendering.
</output_rule>

<data_fetching>
When the user wants to fetch time series data from an external source (e.g. FRED), call
delegate_to_time_series_data_fetcher_agent. A series_id must be known before calling this tool.
</data_fetching>

<reports>
When the user wants to create, retrieve, list, or plot a time series report, call
delegate_to_time_series_report_agent. Pass the full request including any report ID, title,
or form data.
</reports>
"""
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
