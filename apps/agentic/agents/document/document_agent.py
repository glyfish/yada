from __future__ import annotations

import shortuuid
from typing import Any, Dict, Optional, Tuple

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from pydantic import BaseModel, Field

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.agents.query_filters import build_filter_and_query
from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent
from apps.agentic.agents.document.etf_data_info_agent import ETFDataInfoAgent
from apps.agentic.agents.document.document_loader_agent import DocumentLoaderAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_document_loader_agent = DocumentLoaderAgent()


class DocumentSubagentSearchInput(BaseModel):
    request: str = Field(..., description="Request to send to the document search agent")
    query: Optional[Dict[str, Any]] = Field(
        default=None,
        description="""
        ChromaDB where-filter returned by extract_document_query_from_request.
        Do NOT construct this dict manually. Always call extract_document_query_from_request
        first and pass its returned filter dict here unchanged.
        """,
    )


class SubagentRequest(BaseModel):
    request: str = Field(..., description="Request to send to the subagent")


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Extract a document query and any filter prefixes from a user request before passing
            it to a document search agent. Always call this first when the request may contain
            filter prefixes (e.g. title:, shelf:, popularity:).
            Returns a cleaned query string and an optional filters dictionary.
        """,
        positive_examples=[
            PositiveExample(input="popularity:>40 What time series are available for Commodities in the FRED data?"),
            PositiveExample(input="title:Thermodynamics Look in my research library for the definition of a Carnot Cycle."),
            PositiveExample(input="shelf:publications Look in my research library for constraints on kinetic and magnetic "
                                  "energy in MHD relevant to magnetic dynamos?"),
        ],
        suggests_followup=[
            "delegate_to_fred_data_info_search_agent to find FRED time series using the extracted query and filters.",
            "delegate_to_etf_data_info_search_agent to find ETF/fund information using the extracted query and filters.",
            "delegate_to_research_library_search_agent to find research library documents using the extracted query and filters.",
            "delegate_to_code_repository_search_agent to find code using the extracted query and filters.",
        ],
    ),
)
async def extract_document_query_from_request(request: str) -> Tuple[str, Optional[Dict[str, Any]]]:
    return build_filter_and_query(request)


@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate a document loading request to the Document Loader Agent.
            Use for loading research documents (Markdown), GitHub repositories, PDF documents,
            or ETF data (load_etf_data / reload_etf_data). Pass the full request string.
        """,
        positive_examples=[
            PositiveExample(input="Load the research document into the library."),
            PositiveExample(input="Load the GitHub repository troystribling/yada."),
            PositiveExample(input="Load all GitHub repositories."),
            PositiveExample(input="Load the PDF document jaynes_prob_theory.pdf."),
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
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Code Repository Search Agent which searches and retrieves code
            from indexed GitHub repositories. Use this when the user wants to search for specific
            code or files in Troy Stribling's GitHub repositories. The following metadata fields are
            available for filtering and retrieval:
                account: Github account name (e.g. account:troystribling)
                repo: Repository name (e.g. repo:BlueCap)
                ext: File extension (e.g. ext:rb)
                before: Date before which to search (e.g. before:2023-01-01)
                after: Date after which to search (e.g. after:2022-01-01)
            Requests should contain explicit reference to 'my code' or 'code database'.
        """,
        positive_examples=[
            PositiveExample(input="account:troystribling repo:zgomot ext:rb Where is MIDI output handled in my code?"),
            PositiveExample(input="Find the latest commit message for the file that handles MIDI output in my code."),
            PositiveExample(input="What programming languages do I use in my code?"),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'.",
        ],
    ),
)
async def delegate_to_code_repository_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    code_repo_agent = CodeRepoAgent(query=query)
    result = await code_repo_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the Research Library Search Agent which searches and retrieves
            documents from the research library. Metadata fields available for filtering:
            shelf, author, topic. Requests should contain explicit reference to 'my research'
            or 'research library'.
        """,
        positive_examples=[
            PositiveExample(input="title:Thermodynamics Look in my research library for the definition of a Carnot Cycle."),
            PositiveExample(input="shelf:publications Look in my research library for constraints on kinetic and magnetic "
                                  "energy in MHD relevant to magnetic dynamos?"),
            PositiveExample(input="Look in my research library for the definition of a Carnot Cycle."),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'.",
        ],
    ),
)
async def delegate_to_research_library_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    research_library_agent = ResearchLibraryAgent(query=query)
    result = await research_library_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the FRED Data Info Search Agent which searches and retrieves
            documents from the FRED data information store. FRED (Federal Reserve Economic Data)
            is a database of economic time series. Use to find FRED series identifiers.
            Metadata fields available: category_name, series_id, series_title, popularity,
            category_id, popularity:> | >= | < | <=, last_updated, last_updated:after,
            last_updated:before. Requests should contain explicit reference to FRED.
        """,
        positive_examples=[
            PositiveExample(input="popularity:>40 What time series are available for Commodities in the FRED data?"),
            PositiveExample(input="popularity:>40 What price indexes are in FRED for Farm Products?"),
            PositiveExample(input="category_name:'Farm Products' What price indexes are in FRED?"),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'. "
            "All requests should contain an explicit reference to FRED, FRED data, or FRED time series.",
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
async def delegate_to_fred_data_info_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    fred_data_info_agent = FredDataInfoAgent(query=query)
    result = await fred_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function="""
            Delegate a request to the ETF Data Info Search Agent which searches and retrieves
            ETF and mutual fund information from the ETF document store. Data covers ~36K ETFs
            from the FinanceDatabase package. Metadata fields available for filtering:
            family, category_group, category, exchange.
            Use for questions about ETFs, mutual funds, fund families, or investment strategies.
        """,
        positive_examples=[
            PositiveExample(input="family:\"VanEck Asset Management\" What international equity ETFs does VanEck offer?"),
            PositiveExample(input="category_group:\"Fixed Income\" What bond ETFs focus on high yield?"),
            PositiveExample(input="What ETFs are available for frontier markets?"),
            PositiveExample(input="exchange:PCX Show me ETFs that trade on PCX."),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'.",
        ],
    ),
)
async def delegate_to_etf_data_info_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    etf_data_info_agent = ETFDataInfoAgent(query=query)
    result = await etf_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


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
            extract_document_query_from_request,
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
- PDF documents
- ETF data (load or reload the ETF ChromaDB store)
</document_loading>

<document_search>
When the user wants to search a document store:
1. Always call extract_document_query_from_request first to extract any filter prefixes
   and the cleaned query string.
2. Pass the cleaned query string as 'request' and the extracted filters as 'query' to the
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
