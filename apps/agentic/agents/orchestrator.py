import shortuuid
from pydantic import BaseModel, Field
from typing import Literal, Dict, Any, Optional, Sequence

from apps.agentic.core.tool_spec import PositiveExample, NegativeExample, ToolSpec, tool_spec
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.llm_factory import router_llm_model
from apps.agentic.core.agents.human_input_node import HumanInputNode
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.plots.plot_agent import PlotAgent
from apps.agentic.agents.data.data_info_agent import DataInfoAgent
from apps.agentic.agents.document.document_agent import DocumentAgent
from apps.agentic.agents.time_series.time_series_agent import TimeSeriesAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_search_agent = SearchAgent()
_plot_agent = PlotAgent()
_data_info_agent = DataInfoAgent()
_document_agent = DocumentAgent()
_time_series_agent = TimeSeriesAgent()

def _content_to_text(content) -> str:
    """
    Flatten a message's content to plain text. LangChain content is sometimes a list
    of blocks (Anthropic format, e.g. [{"type": "text", "text": "..."}]); join their
    text so downstream rendering gets the markdown/HTML, not the list's repr.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for chunk in content:
            if isinstance(chunk, dict):
                text = chunk.get("text")
                if isinstance(text, str):
                    parts.append(text)
                    continue
            parts.append(str(chunk))
        return "\n".join(parts)
    return str(content)


def assemble_delegate_output(messages: Sequence) -> Optional[str]:
    """
    Build the orchestrator's final response from delegate tool output, verbatim.

    Uses the LAST batch of tool calls in the current turn:
      - Independent requests -> the model issues parallel tool calls (one AIMessage
        with several tool_calls) -> every result is included, in order.
      - Dependent chain -> the final step is the last sequential tool call -> only
        that result is returned (earlier intermediates are omitted).

    Scoped to the current turn (after the most recent user / injected-form message)
    so a conversational turn never echoes a previous turn's tool results. Returns
    None when the turn produced no assistant message at all.
    """
    start = 0
    for i, msg in enumerate(messages):
        if isinstance(msg, HumanMessage):
            start = i
    turn = messages[start + 1:]

    last_tool_call_idx = -1
    for i, msg in enumerate(turn):
        if isinstance(msg, AIMessage) and getattr(msg, "tool_calls", None):
            last_tool_call_idx = i

    tool_msgs = (
        [m for m in turn[last_tool_call_idx + 1:] if isinstance(m, ToolMessage)]
        if last_tool_call_idx >= 0 else []
    )

    if not tool_msgs:
        # Pure conversational reply — fall back to the model's own message.
        for msg in reversed(turn):
            if isinstance(msg, AIMessage):
                return _content_to_text(msg.content)
        return None

    return "\n\n".join(_content_to_text(m.content) for m in tool_msgs)


class RequestHumanFormInput(BaseModel):
    form_type: Literal[
        "load_research_document",
        "load_github_repo",
        "create_time_series_report",
        "select_time_series_report",
    ] = Field(
        ...,
        description="The form type to request from the user.",
    )
    prefill: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional pre-filled values for form fields extracted from the user's request. "
            "For create_time_series_report: keys are report_title, report_description, "
            "time_series_ids, time_range_from, time_range_to. When the user describes the "
            "series by a search rather than explicit cache IDs, instead pass 'searches': a list "
            "of {source, query} objects, one per data store named — source is 'etf' or 'fred', "
            "query is the natural-language criteria for that store. "
            "For load_github_repo: keys are account, repo."
        ),
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
            PositiveExample(input="Plot a time series of the population of Tennessee"),
        ],
        suggests_followup=[
            "delegate_to_plot_agent if the result contains data to visualize",
        ],
        negative_examples=[
            NegativeExample(
                input="What VanEck ETFs focus on dividend growth?",
                reason="ETF and mutual fund queries go to delegate_to_document_agent, not web search.",
            ),
            NegativeExample(
                input="What bond ETFs are available from iShares?",
                reason="ETF queries go to delegate_to_document_agent which has a local ETF store.",
            ),
        ],
    ),
)
async def delegate_to_search_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _search_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_plot_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate all chart and visualization requests to the Plot Agent, which routes
            to either the Bar Chart Agent (categorical data) or the Time Series Plot Agent
            (temporal data). Returns the generated chart as an HTML image tag string.
        """,
        positive_examples=[
            PositiveExample(input="Compare the populations of the 10 largest cities in the world in a bar chart."),
            PositiveExample(input="Plot a time series for the population of Tennessee."),
            PositiveExample(input="Compare the population of Tennessee and Alabama over time."),
        ],
        negative_examples=[
            NegativeExample(
                input="Plot the unemployment report.",
                reason="Report plots must go to delegate_to_time_series_agent, not here.",
            ),
        ],
    ),
)
async def delegate_to_plot_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _plot_agent.agent.ainvoke(state, config)
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
            PositiveExample(input="What time series reports do I have?"),
            PositiveExample(input="Show me the details of the unemployment report."),
            PositiveExample(input="List files in troystribling/zgomot."),
            PositiveExample(input="What are the document shelves available in my research library?"),
            PositiveExample(input="What are the titles of the documents in the 'publications' shelf in my research library?"),
        ],
        negative_examples=[
            NegativeExample(
                input="Fetch the UNRATE series from FRED.",
                reason="Use delegate_to_time_series_agent to fetch new data from external sources.",
            ),
        ],
    ),
)
async def delegate_to_data_info_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


# delegate_to_time_series_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate all time series requests to the Time Series Agent, which handles
            data fetching from external sources and all report operations (create, list,
            get, plot). Pass the full request including any series IDs, report IDs, or
            form data already collected.
        """,
        positive_examples=[
            PositiveExample(input="Fetch the UNRATE series from FRED."),
            PositiveExample(input="List all my time series reports."),
            PositiveExample(input="Plot the unemployment report."),
            PositiveExample(input="Create a report from time series IDs abc123, def456."),
        ],
        requires_context=[
            "For fetching data: a series_id must already be known — search FRED via "
            "delegate_to_document_agent first if needed.",
            "For creating a report: call request_human_form with form_type='create_time_series_report' first.",
            "For plotting without a specific report named: call request_human_form with "
            "form_type='select_time_series_report' first, then pass the returned report_id.",
        ],
        negative_examples=[
            NegativeExample(
                input="Search for GDP time series in FRED.",
                reason="Use delegate_to_document_agent to search FRED metadata for series IDs.",
            ),
        ],
    ),
)
async def delegate_to_time_series_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _time_series_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


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
        ],
    ),
)
def request_human_form(form_type: str) -> str:
    # Return value is never used — the graph routes to human_input before
    # a ToolMessage is produced. This body exists only to satisfy LangChain's
    # tool registration requirement.
    return f"Requesting form: {form_type}"


# delegate_to_document_agent
@tool_spec(
    args_schema=SubagentRequest,
    metadata=ToolSpec(
        primary_function="""
            Delegate all document-related requests to the Document Agent, which handles
            both document loading and document search operations.
            Use for: loading research documents, GitHub repos, or ETF data;
            searching code, research library, FRED metadata, or ETF/fund information.
        """,
        positive_examples=[
            PositiveExample(input="Load a research document into the library."),
            PositiveExample(input="Load all GitHub repositories."),
            PositiveExample(input="Search my research library for the definition of the Carnot Cycle."),
            PositiveExample(input="What time series are available for GDP in the FRED data that have an end date within a year of today?"),
            PositiveExample(input="Find MIDI output handling in my code in troystribling/zgomot."),
            PositiveExample(input="Load ETF data for VanEck into the database."),
            PositiveExample(input="Update the ETF database."),
            PositiveExample(input="What VanEck fixed income ETFs are available on US Exchanges?"),
        ],
        requires_context=[
            "For load_research_document and load_github_repo: "
            "call request_human_form first to collect required fields from the user. "
            "For load_all_github_repos: call directly without a form.",
        ],
    ),
)
async def delegate_to_document_agent(request: str) -> str:
    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()}, recursion_limit=50)
    result = await _document_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content

class OrchestratorAgent(ReactAgent):

    @classmethod
    async def create(cls) -> "OrchestratorAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            request_human_form,
            delegate_to_search_agent,
            delegate_to_plot_agent,
            delegate_to_time_series_agent,
            delegate_to_data_info_agent,
            delegate_to_document_agent,
        ]
        tool_node_name = "orchestrator_tool_node"
        # Orchestrator only routes to sub-agents — run it on the cheaper router model.
        super().__init__(tools, tool_node_name, mcp_tools=mcp_tools, llm_factory=router_llm_model)


    def _create_agent(self):
        """
        Override the default ReAct graph to inject the human_input node and
        a passthrough node.

        When the LLM calls request_human_form the conditional edge routes
        to human_input instead of the tool node. After the user submits the
        form and the graph resumes, human_input injects the validated form
        data as a HumanMessage and routes back to the model node, which then
        calls delegate_to_document_loader_agent to complete the action.

        When the model produces no further tool calls, the passthrough node
        returns the last ToolMessage content verbatim as the final AIMessage,
        preventing the LLM from reformatting or wrapping delegate output.
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
                return "passthrough"
            if any(tc["name"] == "request_human_form" for tc in tool_calls):
                return "human_input"
            return "tools"

        def passthrough(state: WorkerState):
            content = assemble_delegate_output(state["messages"])
            if content is None:
                return {}
            return {"messages": [AIMessage(content=content)]}

        graph = (
            StateGraph(WorkerState)
            .add_node("model", self._node.model_runner)
            .add_node("tools", tool_node)
            .add_node("human_input", HumanInputNode())
            .add_node("passthrough", passthrough)
            .add_edge(START, "model")
            .add_edge("tools", "model")
            .add_edge("human_input", "model")
            .add_edge("passthrough", END)
            .add_conditional_edges(
                "model",
                route_model,
                {"tools": "tools", "human_input": "human_input", "passthrough": "passthrough"},
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

When you call multiple tools, how to assemble the final response depends on how they relate:
- Dependent chain — one tool's output feeds the next (e.g. fetch a time series, then plot it).
  Your final response should contain ONLY the verbatim output of the LAST tool in the chain. Do
  not include the raw data or intermediate results from earlier tools.
- Independent results — the user asked for several distinct things in one request (e.g. an ETF
  search AND a FRED search, or two separate plots). Your final response must contain the verbatim
  output of EVERY such tool, one after another in the order requested, each copied exactly and
  separated by a blank line. Never drop or summarize any of them.
</instructions>

<output_rule>
CRITICAL: When you receive a tool result your ONLY job is to copy its content to the user EXACTLY
as returned — character for character, with zero modifications.

- Do NOT add introductory text, headers, summaries, or commentary of any kind.
- Do NOT rephrase, condense, or reformat the tool output.
- Do NOT strip markdown, HTML tags, code fences, or any other formatting.
- Do NOT omit any section of the tool result, regardless of its length.
- Output the complete tool result verbatim as your entire response. When the request produced
  multiple independent results, output ALL of them verbatim, separated by a blank line — never just one.

The tool responses contain precise formatting (HTML tags, image references, markdown, JSON blocks)
that must be preserved exactly. Any modification breaks downstream rendering.
</output_rule>


<documents>
Delegate all document loading and search requests to delegate_to_document_agent.

Document loading — call request_human_form first to collect required fields, then pass the
form data as the request to delegate_to_document_agent:
   - Loading a research note → form_type: load_research_document
   - Loading a GitHub repository → form_type: load_github_repo.
     If the user's request already names the account and/or repository (e.g.
     "update the glyfish/meida repository" or "load the yada repo from glyfish"),
     pass them in prefill so the form is pre-populated. Keys: account, repo.
No form required — pass request directly to delegate_to_document_agent:
   - load_all_github_repos
   - load_etf_data (load ETF data into the store)
   - reload_etf_data (wipe and reload the ETF store — agent will ask for confirmation)

Document search (code, research library, FRED, ETF/funds) — pass the raw user request directly to
delegate_to_document_agent without any pre-processing.
</documents>

<time_series>
Delegate all time series data fetching and report operations to delegate_to_time_series_agent.

When the user wants to create a time series report:
1. Call request_human_form with form_type: create_time_series_report to collect the title,
   description, comma-separated list of time series cache IDs, and time range from the user.
   If the user's request already contains any of these values, pass them in prefill so the
   form fields are pre-populated. Keys: report_title, report_description, time_series_ids,
   time_range_from (required, YYYY-MM-DD), time_range_to (optional, YYYY-MM-DD).
2. After the user submits the form, pass the form data as the request to delegate_to_time_series_agent.

SPECIAL CASE — the user describes the series to include by a SEARCH instead of giving
explicit cache IDs (e.g. "create a report using fixed income ETFs available on US exchanges",
"build a report from FRED GDP series still being updated", or a COMPOUND request naming more
than one store such as "create a report using FRED GDP series and VanEck fixed income ETFs"):
1. Still call request_human_form with form_type: create_time_series_report, but instead of
   time_series_ids pass a prefill key 'searches': a list of {{source, query}} objects, ONE PER
   DATA STORE the user named.
   - source: "etf" for ETFs / mutual funds / stock tickers, "fred" for FRED economic series.
   - query: the natural-language criteria for THAT store (the part of the request about it,
     e.g. "fixed income ETFs available on US exchanges").
   A single-store request produces a one-element list; a compound request produces one entry
   per store. The form searches every store and shows one combined selection table; on submit
   its data is a normal create_time_series_report payload (with the chosen cache IDs resolved).
2. After the user submits the form, pass the form data as the request to delegate_to_time_series_agent.
Do NOT delegate the search yourself — the form runs the searches. Only pass 'searches' in prefill.

When the user wants to PLOT a time series report but does NOT specify which report:
1. Call request_human_form with form_type: select_time_series_report. This presents the user
   with a searchable list of available reports to pick from.
2. After the user selects a report, the form data will contain a report_id field.
   Pass "Plot the report with ID <report_id>" to delegate_to_time_series_agent.

When the user wants to PLOT a specific report by name or ID, call delegate_to_time_series_agent directly.
When the user wants to list, retrieve, or fetch time series data, call delegate_to_time_series_agent directly.
NEVER route a report plot to delegate_to_plot_agent — report plotting is handled within delegate_to_time_series_agent.

When the user wants to DELETE a time series report but does NOT specify which report:
1. Call request_human_form with form_type: select_time_series_report to let the user pick.
2. After the user selects a report, pass "Delete the report with ID <report_id>" to delegate_to_time_series_agent.

When the user wants to DELETE a specific report by name or ID, call delegate_to_time_series_agent directly.
</time_series>

<examples>
In the following request examples the expected routing to subagent tools by
subagent function is indicated.

<example>
<input>
Search my research library for the definition of the Carnot Cycle.
</input>
<output>
1. Call delegate_to_document_agent with the user's request.
</output>
</example>

<example>
<input>
Compare the populations of the 10 largest European cities in a bar chart.
</input>
<output>
1. Retrieve requested data using delegate_to_search_agent if no other data source is available.
2. Pass the data to delegate_to_plot_agent.
</output>
</example>

<example>
<input>
Plot the US GDP in a time series using FRED data.
</input>
<output>
1. Call delegate_to_document_agent to search for the GDP series ID in the FRED document store.
2. Call delegate_to_time_series_agent with the series ID to fetch the data.
3. Pass the data to delegate_to_plot_agent.
</output>
</example>

<example>
<input>
What VanEck ETFs focus on dividend growth?
</input>
<output>
1. Call delegate_to_document_agent with the user's request. The ETF store is local — do NOT use web search.
</output>
</example>

<example>
<input>
What bond ETFs are available from iShares?
</input>
<output>
1. Call delegate_to_document_agent with the user's request. ETF/mutual fund queries always go to the document agent.
</output>
</example>

</examples>
"""
        
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])