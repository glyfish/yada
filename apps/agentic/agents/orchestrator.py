import shortuuid
from pydantic import BaseModel, Field
from typing import Literal, Tuple, Dict, Any, Optional

from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode

from apps.agentic.core.agents.query_filters import build_filter_and_query
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.agents.human_input_node import HumanInputNode
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent
from apps.agentic.agents.plots.time_series_plot_agent import TimeSeriesPlotAgent
from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.data.data_info_agent import DataInfoAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent
from apps.agentic.agents.document.document_loader_agent import DocumentLoaderAgent
from apps.agentic.agents.data.data_fetcher_agent import DataFetcherAgent
from apps.agentic.agents.plots.time_series_report_agent import TimeSeriesReportAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_search_agent = SearchAgent()
_bar_chart_agent = BarChartAgent()
_time_series_plot_agent = TimeSeriesPlotAgent()
_data_info_agent = DataInfoAgent()
_document_loader_agent = DocumentLoaderAgent()
_time_series_report_agent = TimeSeriesReportAgent()

class RequestHumanFormInput(BaseModel):
    form_type: Literal[
        "load_research_document",
        "load_github_repo",
        "load_pdf_document",
        "create_time_series_report",
    ] = Field(
        ...,
        description="The form type to request from the user.",
    )
    prefill: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional pre-filled values for form fields extracted from the user's request. "
            "For create_time_series_report: keys are report_title, report_description, "
            "time_series_ids, time_range_from, time_range_to."
        ),
    )


class DocumentSubagentSearchInput(BaseModel):
    """
    Input schema for the document search agents.
    """

    request: str = Field(..., description="Request to send to the document search agent")      
    query: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        """
        ChromaDB where-filter returned by extract_document_query_from_request. 
        Do NOT construct this dict manually. Always call extract_document_query_from_request 
        first and pass its returned filter dict here unchanged.
        """
        ,
    )

class SubagentRequest(BaseModel):
    """
    Input schema for the subagent requests.
    """

    request: str = Field(..., description="Request to send to the subagent")


# delegate_to_search_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Search Agent that performs web searches.
            Use for factual questions, current events, data lookup, or research
            if no other tool can fulfill the request. The Search Agent can also
            be used to search for data to visualize with the plotting agents.
            """,
        positive_examples=[
            PositiveExample(input="What is the history of Tullahoma TN"),
            PositiveExample(input="Compare the populations of the 10 largest cities in the world."),
            PositiveExample(input="Plot a timeseries of the population of Tennessee"),
        ],
        suggests_followup=[
            "delegate_to_bar_chart_agent if the result contains categorical data to visualize",
            "delegate_to_time_series_plot_agent if the result contains temporal data to visualize",
        ],
    ),
)
async def delegate_to_search_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _search_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_bar_chart_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Bar Chart Agent which creates bar charts from categorical data.
            Use this when the user wants to visualize data as a bar chart.
            Returns the generated bar chart as an HTML image tag string with a summary of results
            displayed above the chart. The HTML string should be rendered verbatim in the frontend.
            """,
        positive_examples=[
            PositiveExample(input="Compare the populations of the 10 largest cities in the world in a bar chart"),
        ],
        negative_examples=[
            NegativeExample(input="Plot the US GDP in a time series using FRED data", 
                            reason="Use the FRED Data Info Agent to look up FRED time series information first")
        ],
    ),
)
async def delegate_to_bar_chart_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _bar_chart_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_time_series_plot_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Time Series Plot Agent which creates time series plots from temporal data.
            Use this when the user wants to visualize data over time.
            Returns the generated time series plot as an HTML image tag string with a summary of results
            displayed above the chart. The HTML string should be rendered verbatim in the frontend.
            """,
        positive_examples=[
            PositiveExample(input="Plot a time series for the population of Tennessee."),
            PositiveExample(input="Plot the population of Tennessee using all available data."),
            PositiveExample(input="Compare the population of Tennessee and Alabama over time in the same plot."),
            PositiveExample(input="Plot the GDP and population of Tennessee over time as stacked charts."),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot the unemployment report.",
                reason="Report plots must go to delegate_to_time_series_report_agent, not here.",
            ),
            NegativeExample(
                input="Generate a chart for my GDP report.",
                reason="Report plots must go to delegate_to_time_series_report_agent, not here.",
            ),
        ],
    ),
)
async def delegate_to_time_series_plot_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _time_series_plot_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_data_info_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Data Info Agent which provides information about
            all data and document stores. Available stores: time series reports (time_series_reports table),
            time series cache (previously fetched time series), Research Library (reference docs),
            Code Repository (source code), FRED Data Information (economic time series metadata).
            Use for listing or inspecting what is already stored — not for fetching new data.
            Map pronouns: 'my code repositories'/'my code' → code repository vector store;
            'my research library' → research_library vector store; 'FRED data' → FRED data information store;
            'cached time series'/'time series cache' → time_series_cache table;
            'my reports'/'time series reports' → time_series_reports table.
            If asked for distinct metadata values, return the list when count < 10, otherwise summarize the most common values.
            Metadata fields — code repositories: repository names, file types, programming languages;
            research library: document shelves, authors, tags; FRED: category_name, series_id, series_title, popularity.
            """,
        positive_examples=[
            PositiveExample(input="List all cached time series."),
            PositiveExample(input="Show me the details for UNRATE in the cache."),
            PositiveExample(input="What time series do I have cached?"),
            PositiveExample(input="List all time series reports."),
            PositiveExample(input="What reports do I have?"),
            PositiveExample(input="Show me the details of the unemployment report."),
            PositiveExample(input="List files in troystribling/zgomot."),
            PositiveExample(input="What are the document shelves available in my research library?"),
            PositiveExample(input="What are the titles of the documents in the 'publications' shelf in my research library?"),
        ],
        negative_examples=[
            NegativeExample(
                input="Fetch the UNRATE series from FRED.",
                reason="Use delegate_to_data_fetcher_agent to fetch new data from external sources.",
            ),
        ],
    ),
)
async def delegate_to_data_info_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_code_repository_search_agent
@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Code Repository Search Agent which searches and retrieves code
            from indexed GitHub repositories. Use this when the user wants to search for specific
            code or files in Troy Stribling's GitHub repositories. The following metadata fields are 
            available for filtering and retrieval,
                account: Github account name (e.g. account:troystribling)
                repo: Repository name (e.g. repo:BlueCap)
                ext: File extension (e.g. ext:rb)
                before: Date before which to search (e.g. before:2023-01-01)
                after: Date after which to search (e.g. after:2022-01-01)
            Requests should contain explicit reference to 'my code' or 'code database' to ensure they are routed
            to the Code Repository Search Agent.
            """,
        positive_examples=[
            PositiveExample(input="account:troystribling repo:zgomot ext:rb Where is MIDI output handled in my code?"),
            PositiveExample(input="Find the latest commit message for the file that handles MIDI output in my code."),
            PositiveExample(input="What programming languages do I use in my code?"),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'. ",
            "Request should contain reference to 'my code' / 'code database' → requester's indexed repositories in the code repository vector store",
        ],
    ),
)
async def delegate_to_code_repository_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    code_repo_agent = CodeRepoAgent(query=query)
    result = await code_repo_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content

# delegate_to_research_library_search_agent
@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Research Library Search Agent which searches and retrieves documents
            from the research library. The following metadata fields are available for filtering and retrieval: 
            shelf, author and topic. Requests should contain explicit reference to 'my research' or 
            'research library' to ensure they are routed here.
            """,
        positive_examples=[
            PositiveExample(input="title:Thermodynamics Look in my research library for the definition of a Carnot Cycle."),
            PositiveExample(input="shelf:publications Look in my research library for constraints on kinetic and magnetic energy in MHD relevant to magnetic dynamos?"),
            PositiveExample(input="Look in my research library for the definition of a Carnot Cycle"),
        ],
        requires_context=[
            "Call extract_document_query_from_request first to extract query filters and the cleaned query string. "
            "Then pass the cleaned query string as 'request' and extracted filters as 'query'. ",
            "Request should contain reference to 'my research' → requester's indexed research library in the research_library vector store",
        ],
    ),
)
async def delegate_to_research_library_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    research_library_agent = ResearchLibraryAgent(query=query)
    result = await research_library_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content

# delegate_to_fred_data_info_search_agent
@tool_spec(
    args_schema=DocumentSubagentSearchInput,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the FRED Data Info Search Agent which searches and retrieves documents
            from the FRED data information store. FRED (Federal Reserve Economic Data) is a database of
            economic data time series. Use this tool to find FRED time series identifiers for specific
            economic indicators. The following metadata fields are available for filtering and retrieval: 
            category_name, series_id, series_title, popularity, category_id, popularity, 
            popularity:> | >= | < | <=, last_updated, last_updated:after, last_updated:before.
            Requests should contain explicit reference to FRED data or FRED time series to ensure 
            they are routed here. 
            """,
        positive_examples=[
            PositiveExample(input="popularity:>40 What time series are available for Commodities in the FRED data?"),
            PositiveExample(input="popularity:>40 What price indexes are in FRED for Farm Products?"),
            PositiveExample(input="category_name:'Farm Products' What price indexes are in FRED?"),
        ],
        requires_context=[
            """
            Call extract_document_query_from_request first to extract query filters and the cleaned query string.
            Then pass the cleaned query string as 'request' and extracted filters as 'query'.,
            All requests should contain an explicit reference to FRED, FRED data, or 
            FRED time series to ensure they are routed here first.
            """
        ],
        negative_examples=[
            NegativeExample(input="Plot a time series for the population of Tennessee.", 
                            reason="Use the FRED Data Info Agent to look up FRED time series only if the request explicitly references FRED data."
            ),
        ],
        suggests_followup=[
            "delegate_to_time_series_plot_agent once a FRED series_id is known to visualize the time series and if a plot is requested",
        ],
    ),
)
async def delegate_to_fred_data_info_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    fred_data_info_agent = FredDataInfoAgent(query=query)
    result = await fred_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_data_fetcher_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Data Fetcher Agent which retrieves data from
            external data sources via MCP. The agent discovers available MCP tools automatically on launch.
            Pass the series_id, source, and any date range in the request string.
            """,
        positive_examples=[
            PositiveExample(input="Plot the US GDP time series using FRED data."),
            PositiveExample(input="Fetch the UNRATE series from FRED."),
        ],
        requires_context=[
            "A series_id must already be known. Call delegate_to_fred_data_info_search_agent first to find it.",
        ],
        negative_examples=[
            NegativeExample(input="Search for GDP time series in FRED.",
                            reason="Use delegate_to_fred_data_info_search_agent to find series IDs first."),
        ],
        suggests_followup=[
            "delegate_to_time_series_plot_agent to visualize the returned data.",
        ],
    ),
)

async def delegate_to_data_fetcher_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    data_fetcher_agent = await DataFetcherAgent.create()
    result = await data_fetcher_agent.agent.ainvoke(state, config)
    content = result["messages"][-1].content
    logger.debug(f"Data Fetcher Agent returned content: {content}")
    return content


# delegate_to_time_series_report_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a request to the Time Series Report Agent which creates, retrieves,
            lists, and plots time series reports. A report groups a set of time series cache IDs
            under a title and description for later reference.
            Use after collecting form data for report creation, or directly for list/get/plot requests.
            IMPORTANT: Always use this agent to plot a report — never delegate report plots to
            delegate_to_time_series_plot_agent.
            """,
        positive_examples=[
            PositiveExample(input="List all my time series reports."),
            PositiveExample(input="Show me the report with ID abc-123."),
            PositiveExample(input="What reports do I have?"),
            PositiveExample(input="Plot the unemployment report."),
            PositiveExample(input="Plot the report with ID abc-123."),
            PositiveExample(input="Generate a chart for my GDP report."),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot the unemployment report.",
                reason="Do NOT route report plots to delegate_to_time_series_plot_agent. Use delegate_to_time_series_report_agent instead.",
            ),
        ],
        requires_context=[
            "For creating a report: call request_human_form with form_type='create_time_series_report' first.",
        ],
    ),
)
async def delegate_to_time_series_report_agent(request: str) -> str:
    from langchain_core.messages import ToolMessage
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
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
        if isinstance(msg, ToolMessage) and isinstance(msg.content, str) and "<img" in msg.content and msg.content not in final
    ]
    if extra_html:
        logger.debug(f"delegate_to_time_series_report_agent: appending {len(extra_html)} HTML fragment(s)")
        return final + "\n\n" + "\n\n".join(extra_html)
    return final


# request_human_form
@tool_spec(
    args_schema=RequestHumanFormInput,
    metadata=ToolSpec(
        primary_function=
            """
            Signal that structured user input is required before proceeding.
            Calling this tool suspends execution and presents the specified form
            to the user. The graph resumes automatically once the user submits.
            """,
        positive_examples=[
            PositiveExample(input="Load a research document into the library."),
            PositiveExample(input="Add the yada repo to my code store."),
            PositiveExample(input="Load a PDF into the document library."),
        ],
    ),
)
def request_human_form(form_type: str) -> str:
    # Return value is never used — the graph routes to human_input before
    # a ToolMessage is produced. This body exists only to satisfy LangChain's
    # tool registration requirement.
    return f"Requesting form: {form_type}"


# delegate_to_document_loader_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Delegate a document loading request to the Document Loader Agent
            after form data has been collected from the user. Pass the full
            form data JSON as the request string.
            """,
        positive_examples=[
            PositiveExample(input="Load all GitHub repositories."),
        ],
        requires_context=[
            "For load_research_document, load_github_repo, and load_pdf_document: "
            "call request_human_form first to collect required fields from the user. "
            "For load_all_github_repos: call directly without a form.",
        ],
    ),
)
async def delegate_to_document_loader_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _document_loader_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# extract_document_query_from_request
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function=
            """
            Extract a document query and any filter prefixes from a user request before passing it to a document search agent.
            Always call this first when the request may contain filter prefixes (e.g. title:, shelf:, popularity:).
            Returns a cleaned query string and an optional filters dictionary.
            """,
        positive_examples=[
            PositiveExample(input="popularity:>40 What time series are available for Commodities in the FRED data?"),
            PositiveExample(input="title:Thermodynamics Look in my research library for the definition of a Carnot Cycle."),
            PositiveExample(input="shelf:publications Look in my research library for constraints on kinetic and magnetic " \
                                  "energy in MHD relevant to magnetic dynamos?"),
        ],
        suggests_followup=[
            "delegate_to_fred_data_info_search_agent to find information about FRED time series using the extracted query and filters.",
            "delegate_to_research_library_search_agent to find documents in the research library using the extracted query and filters.",
            "delegate_to_code_repository_search_agent to find code in the code repository using the extracted query and filters.",
        ],
    ),
)
async def extract_document_query_from_request(request: str) -> Tuple[str, Optional[Dict[str, Any]]]:
    return build_filter_and_query(request)

class OrchestratorAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "OrchestratorAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            request_human_form,
            delegate_to_search_agent,
            delegate_to_bar_chart_agent,
            delegate_to_time_series_plot_agent,
            delegate_to_time_series_report_agent,
            delegate_to_data_fetcher_agent,
            delegate_to_data_info_agent,
            delegate_to_document_loader_agent,
            delegate_to_code_repository_search_agent,
            delegate_to_research_library_search_agent,
            delegate_to_fred_data_info_search_agent,
            extract_document_query_from_request,
        ]
        tool_node_name = "orchestrator_tool_node"
        super().__init__(tools, tool_node_name, mcp_tools=mcp_tools)


    def _create_agent(self):
        """
        Override the default ReAct graph to inject the human_input node.

        When the LLM calls request_human_form the conditional edge routes
        to human_input instead of the tool node. After the user submits the
        form and the graph resumes, human_input injects the validated form
        data as a HumanMessage and routes back to the model node, which then
        calls delegate_to_document_loader_agent to complete the action.
        """
        all_tools = self._node.tools

        # Separate request_human_form from the rest so it never reaches ToolNode
        tool_names_for_node = {t.name for t in all_tools if t.name != "request_human_form"}
        tools_for_node = [t for t in all_tools if t.name in tool_names_for_node]

        tool_node = ToolNode(tools_for_node, name=self._tool_node_name)

        def route_model(state: WorkerState):
            last = state["messages"][-1]
            tool_calls = getattr(last, "tool_calls", None)
            if not tool_calls:
                return END
            if any(tc["name"] == "request_human_form" for tc in tool_calls):
                return "human_input"
            return "tools"

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self._node.model_runner)
            .add_node("tools", tool_node)
            .add_node("human_input", HumanInputNode())
            .add_edge(START, "model")
            .add_edge("tools", "model")
            .add_edge("human_input", "model")
            .add_conditional_edges(
                "model",
                route_model,
                {"tools": "tools", "human_input": "human_input", END: END},
            )
        )
        return graph.compile(checkpointer=checkpointer)


    def create_prompt(self):
        system_prompt = """
# Orchestrator

<instructions>
You are an orchestrator agent that receives and routes all request to subagents
for processing in the YADA app. The name YADA is taken from the Hebrew word meaning
"to know", The YADA app is a research application that has access to tools that perform the 
following functions,

1. Web search
2. Access external data sources
3. Statistical model analysis and simulation
4. Data visualization
5. Document search

The are two types document stores used in the app. One type contains reference documents for source code
and research. Documents of this type will be referred to as "reference documents". The others contain 
documentation for APIs that may need to be consulted for information before making a request. 
Documents of this type will be referred as "API documents".

Analyze the user's request and call the appropriate tool(s) in the correct order.
A request may require multiple subagents called sequentially, for example searching for data
and then plotting it. Pass the full context needed for each subagent to do its job.

When multiple tools are called in sequence, your final response should only contain the verbatim output
from the last tool in the chain. Do not include raw data or intermediate results from earlier tools.
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


<document_loading>
When the user wants to load a document into a document store:
1. Call request_human_form with the appropriate form_type to collect required fields:
   - Loading a research note → form_type: load_research_document
   - Loading a GitHub repository → form_type: load_github_repo
   - Loading a PDF document → form_type: load_pdf_document
2. After the user submits the form, call delegate_to_document_loader_agent with the form data.
Exception: load_all_github_repos requires no form — call delegate_to_document_loader_agent directly.
</document_loading>

<time_series_reports>
When the user wants to create a time series report:
1. Call request_human_form with form_type: create_time_series_report to collect the title,
   description, comma-separated list of time series cache IDs, and time range from the user.
   If the user's request already contains any of these values, pass them in prefill so the
   form fields are pre-populated. Keys: report_title, report_description, time_series_ids,
   time_range_from (required, YYYY-MM-DD), time_range_to (optional, YYYY-MM-DD).
2. After the user submits the form, pass the form data as the request to delegate_to_time_series_report_agent.

When the user wants to list, retrieve, or PLOT a time series report, call delegate_to_time_series_report_agent directly.
NEVER route a report plot to delegate_to_time_series_plot_agent — report plotting is handled entirely within delegate_to_time_series_report_agent.
</time_series_reports>

<examples>
In the following request examples the expected routing to subagent tools by
subagent function is indicated.

<example>
<input>
Search my research library for the definition of the Carnot Cycle.
</input>
<output>
1. Call extract_document_query_from_request to extract the query and any filters from the request.
2. Perform a document search over the appropriate reference document database.
</output>
</example>

<example>
<input>
Compare the populations of the 10 largest European cities in a bar chart.
</input>
<output>
1. Retrieve requested data using the appropriate data source tool. If no data source tool is available
   do a web search for the data.
2. Pass the data to the appropriate visualization tool.
</output>
</example>

<example>
<input>
Plot the US GDP in a time series using FRED data.
</input>
<output>
1. Call extract_document_query_from_request to extract the query and any filters from the request.
2. Search for the time series documentation in the appropriate document store.
3. Using the data from step 1 construct an API request for the data.
4. Pass the data to the appropriate visualization tool.
</output>
</example>

</examples>
"""
        
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])