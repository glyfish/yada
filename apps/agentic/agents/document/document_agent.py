from __future__ import annotations

import shortuuid
from typing import Any, Dict, Optional

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from pydantic import BaseModel, Field

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.agents.llm_filter_extractor import (
    extract_etf_filters,
    extract_fred_filters,
    extract_code_repo_filters,
    extract_research_library_filters,
)
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent
from apps.agentic.agents.document.etf_data_info_agent import ETFDataInfoAgent
from apps.agentic.agents.document.document_loader_agent import DocumentLoaderAgent
from apps.agentic.db.series_cache import SeriesCache

from lib.logger import get_logger

logger = get_logger("YADA")

_document_loader_agent = DocumentLoaderAgent()


class SubagentRequest(BaseModel):
    request: str = Field(..., description="Request to send to the subagent")


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a document loading request to the Document Loader Agent.
            Use for loading research documents (Markdown), GitHub repositories,
            or ETF data (load_etf_data / reload_etf_data). Pass the full request string.
        """,
        positive_examples=[
            PositiveExample(input="Load the research document into the library."),
            PositiveExample(input="Load the GitHub repository troystribling/yada."),
            PositiveExample(input="Load all GitHub repositories."),
            PositiveExample(input="Load ETF data for VanEck Asset Management."),
            PositiveExample(input="Update the ETF database."),
            PositiveExample(input="Reload all ETF data."),
        ],
    ),
)
async def delegate_to_document_loader_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _document_loader_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Code Repository Search Agent which searches and retrieves code
            from indexed GitHub repositories. Use this when the user wants to search for specific
            code or files in Troy Stribling's GitHub repositories.
            Requests should contain explicit reference to 'my code' or 'code database'.
        """,
        positive_examples=[
            PositiveExample(input="Where is MIDI output handled in my code?"),
            PositiveExample(input="Find the latest commit message for the file that handles MIDI output in my code."),
            PositiveExample(input="What programming languages do I use in my code?"),
        ],
    ),
)
async def delegate_to_code_repository_search_agent(request: str) -> str:
    where, cleaned_query = await extract_code_repo_filters(request)
    state = {"messages": [HumanMessage(content=cleaned_query)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    code_repo_agent = CodeRepoAgent(query=where)
    result = await code_repo_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Research Library Search Agent which searches and retrieves
            documents from the research library.
            Requests should contain explicit reference to 'my research' or 'research library'.
        """,
        positive_examples=[
            PositiveExample(input="Look in my research library for the definition of a Carnot Cycle."),
            PositiveExample(input="Search my research library for constraints on kinetic energy in MHD."),
        ],
    ),
)
async def delegate_to_research_library_search_agent(request: str) -> str:
    where, cleaned_query = await extract_research_library_filters(request)
    state = {"messages": [HumanMessage(content=cleaned_query)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    research_library_agent = ResearchLibraryAgent(query=where)
    result = await research_library_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the FRED Data Info Search Agent which searches and retrieves
            documents from the FRED data information store. FRED (Federal Reserve Economic Data)
            is a database of economic time series. Use to find FRED series identifiers.
            Requests should contain explicit reference to FRED.
        """,
        positive_examples=[
            PositiveExample(input="What time series are available for Commodities in the FRED data?"),
            PositiveExample(input="What price indexes are in FRED for Farm Products?"),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot a time series for the population of Tennessee.",
                reason="Use FRED Data Info only when the request explicitly references FRED data.",
            ),
        ],
        suggests_followup=[
            "delegate_to_time_series_plot_agent once a FRED series_id is known and a plot is requested.",
        ],
    ),
)
async def delegate_to_fred_data_info_search_agent(request: str) -> str:
    where, cleaned_query = await extract_fred_filters(request)
    state = {"messages": [HumanMessage(content=cleaned_query)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    fred_data_info_agent = FredDataInfoAgent(query=where)
    result = await fred_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the ETF Data Info Search Agent which searches and retrieves
            ETF and mutual fund information from the ETF document store. Data covers ~36K ETFs
            from the FinanceDatabase package.
            Use for questions about ETFs, mutual funds, fund families, or investment strategies.
        """,
        positive_examples=[
            PositiveExample(input="What VanEck ETFs focus on dividend growth?"),
            PositiveExample(input="What bond ETFs focus on high yield?"),
            PositiveExample(input="What ETFs are available for frontier markets?"),
            PositiveExample(input="Show me equity ETFs from iShares."),
        ],
    ),
)
async def delegate_to_etf_data_info_search_agent(request: str) -> str:
    where, cleaned_query = await extract_etf_filters(request)
    state = {"messages": [HumanMessage(content=cleaned_query)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    etf_data_info_agent = ETFDataInfoAgent(query=where)
    result = await etf_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


async def search_series_rows(source: str, query: str) -> list[dict[str, str]]:
    """
    Structured search over the ETF or FRED metadata store for the report-builder
    selection table. Reuses the same LLM filter extraction as the chat search
    agents, then maps retriever hits to rows keyed for the table and the
    downstream /api/series/fetch call.

    Each row: native_id (ticker or FRED series_id), title, source (the *fetch*
    source — 'tiingo' for ETFs, 'fred' for FRED), observation_start/end (known
    only for FRED before fetch), plus a few display-only fields. Deduplicated by
    native_id, order preserved.
    """
    source = source.strip().lower()

    if source in ("etf", "tiingo"):
        where, cleaned = await extract_etf_filters(query)
        hits = await ETFDataInfoAgent(query=where).retriever.ainvoke(cleaned)
        native_key, title_key, fetch_source = "ticker", "name", "tiingo"
        extra_keys = ("family", "category_group", "category", "exchange")
    elif source == "fred":
        where, cleaned = await extract_fred_filters(query)
        hits = await FredDataInfoAgent(query=where).retriever.ainvoke(cleaned)
        native_key, title_key, fetch_source = "series_id", "series_title", "fred"
        extra_keys = ("frequency", "units", "seasonal_adjustment")
    else:
        raise ValueError(f"Unsupported search source '{source}'. Expected 'etf' or 'fred'.")

    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for d in hits:
        m = d.metadata or {}
        native_id = str(m.get(native_key) or "").strip()
        if not native_id or native_id in seen:
            continue
        seen.add(native_id)
        row = {
            "native_id": native_id,
            "title": str(m.get(title_key) or ""),
            "source": fetch_source,
            "observation_start": str(m.get("observation_start") or ""),
            "observation_end": str(m.get("observation_end") or ""),
        }
        for k in extra_keys:
            row[k] = str(m.get(k) or "")
        rows.append(row)

    # Backfill observation dates from the cache for series already fetched. ETF
    # metadata carries no obs range, but once a ticker is fetched the cache does —
    # so a previously-cached selection shows its real date span in the table.
    blanks = [r["native_id"] for r in rows if not r["observation_start"] or not r["observation_end"]]
    cached = SeriesCache._get_obs_ranges_by_source_sync(fetch_source, blanks)
    for r in rows:
        c = cached.get(r["native_id"])
        if not c:
            continue
        if not r["observation_start"]:
            r["observation_start"] = str(c["observation_start"] or "")
        if not r["observation_end"]:
            r["observation_end"] = str(c["observation_end"] or "")

    return rows


class DocumentAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "DocumentAgent":
        return cls()

    _SEARCH_TOOLS = {
        "delegate_to_code_repository_search_agent",
        "delegate_to_research_library_search_agent",
        "delegate_to_fred_data_info_search_agent",
        "delegate_to_etf_data_info_search_agent",
    }

    def __init__(self, mcp_tools: list = []):
        tools = [
            delegate_to_document_loader_agent,
            delegate_to_code_repository_search_agent,
            delegate_to_research_library_search_agent,
            delegate_to_fred_data_info_search_agent,
            delegate_to_etf_data_info_search_agent,
        ]
        super().__init__(tools, "document_agent_tool_node", mcp_tools=mcp_tools)

    def _create_agent(self):
        def route_after_tools(state: WorkerState):
            for msg in reversed(state["messages"]):
                if isinstance(msg, ToolMessage):
                    if msg.name in DocumentAgent._SEARCH_TOOLS:
                        return END
                    break
            return "model"

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self._node.model_runner)
            .add_node("tools", self.tool_node)
            .add_edge(START, "model")
            .add_conditional_edges("tools", route_after_tools, {"model": "model", END: END})
            .add_conditional_edges("model", tools_condition, {"tools": "tools", END: END})
        )
        return graph.compile(checkpointer=checkpointer)

    def create_prompt(self):
        system_prompt = """
<instructions>
You are a document agent responsible for all document loading and search operations.
Route each request to the appropriate tool using the rules below.
</instructions>

<document_loading>
When the user wants to load or update a document store, call delegate_to_document_loader_agent
and pass the full request string. Applies to:
- Research documents (Markdown notes)
- GitHub repositories
- ETF data (load or reload the ETF ChromaDB store)
</document_loading>

<document_search>
When the user wants to search a document store, pass the full request directly to the
appropriate search agent:
- Code search (user says 'my code' or 'code database') → delegate_to_code_repository_search_agent
- Research library (user says 'my research' or 'research library') → delegate_to_research_library_search_agent
- FRED metadata (user says 'FRED', 'FRED data', or 'FRED time series') → delegate_to_fred_data_info_search_agent
- ETF / mutual fund search (user asks about ETFs, funds, fund families, or investment strategies) → delegate_to_etf_data_info_search_agent
</document_search>
"""
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
