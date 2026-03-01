import shortuuid
from pydantic import BaseModel, Field
from typing import Tuple, Dict, Any, Optional

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.query_filters import build_filter_and_query
from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent
from apps.agentic.agents.plots.time_series_plot_agent import TimeSeriesPlotAgent
from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.document_store_info_agent import DocumentStoreInfoAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent

from lib.logger import get_logger

logger = get_logger("YADA")

_search_agent = SearchAgent()
_bar_chart_agent = BarChartAgent()
_time_series_plot_agent = TimeSeriesPlotAgent()
_document_store_info_agent = DocumentStoreInfoAgent()

class DocumentSubagentSearchInput(BaseModel):
    """
    Input schema for the document search agents.
    """

    request: str = Field(..., description="Request to send to the document search agent")      
    query: Optional[Dict[str, Any]] = Field(default=None, description="The search query to find relevant documents in the document store")

class SubagentRequest(BaseModel):
    """
    Input schema for the subagent requests.
    """

    request: str = Field(..., description="Request to send to the subagent")      

@tool(args_schema=SubagentRequest)
async def delegate_to_search_agent(request: str) -> str:
    """
    Delegate a request to the Search Agent which performs web searches. Use for factual questions, 
    current events, data lookup, or research.

    Examples of when to use this tool:
        - "What is the history of Tullahoma TN"
        - "Compare the populations of the 10 largest cities in the world"

    Returns: str
        The search results from the Search Agent.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _search_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=SubagentRequest)
async def delegate_to_bar_chart_agent(request: str) -> str:
    """
    Delegate a request to the Bar Chart Agent which creates bar charts from categorical data.
    Use this when the user wants to visualize data as a bar chart.

    Examples of when to use this tool:
        - "Compare the populations of the 10 largest cities in the world in a bar chart"

    Returns: str
        Returns the generated bar chart as an HTML image tag string with a summary
        of results displayed above the chart. The HTML string should be rendered verbatim in the 
        frontend to display the chart.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _bar_chart_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=SubagentRequest)
async def delegate_to_time_series_plot_agent(request: str) -> str:
    """
    Delegate a request to the Time Series Plot Agent which creates time series plots from temporal data.
    Use this when the user wants to visualize data over time.

    Examples of when to use this tool:
        - "Plot a time series for the population of Tennessee."
        - "Plot the population of Tennessee using all available data."

    Returns: str
        Returns the generated time series plot as an HTML image tag string with a summary
        of results displayed above the chart. The HTML string should be rendered verbatim in the 
        frontend to display the chart.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _time_series_plot_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=SubagentRequest)
async def delegate_to_document_store_info_agent(request: str) -> str:
    """
    Delegate a request to the Document Store Info Agent which provides 
    information about the documents in the document stores.
    
    The available document stores include:
    1. Research Library: A collection of reference documents for research.
    2. Code Repository: A collection of reference documents for source code.
    3. FRED Data Information: A collection of documents describing time series data from the

    Examples of when to use this tool:
        - "List repository names for my code repositories."
        - "What document shelves do I have in my research library?"
        - "What are the titles of the documents in the 'publications' shelf in my research library?"

    In requests for available metadata values assume the following equivalences:
    - 'my code repositories', 'my code' → requester's indexed repositories in the code repository vector store.
    - 'my research library' → requester's indexed research library in the research_library vector store.
    - 'FRED data' → FRED data information document store.
    
    If asked to retrieve values for a specific metadata values extract the values
    from the document store metadata and determine the number of distinct values for the metadata fields. If the number of distinct values is less than 10 return the list of distinct values. 
    If the number of distinct values is greater than 10 return a summary of the most common values and their counts.
    
    Metadata Values
    - For code repositories: repository names, file types, programming languages.
    - For research library: document shelves, document authors, document tags.
    - For FRED data information: category_name, series_id, series_title, popularity
    
    Returns: str
        The results from the Document Store Info Agent.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    result = await _document_store_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=DocumentSubagentSearchInput)
async def delegate_to_code_repository_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    """
    Delegate a request to the Code Repository Search Agent which searches and retrieves code from 
    indexed GitHub repositories. Use this when the user wants to search for specific 
    code or files in Troy Stribling's GitHub repositories.

    **Map pronouns**
    - 'my code', 'code database' → requester's indexed repositories in the code repository vector store.
    - 'code database' → requester's indexed repos in the code repository vector store.

    Examples of when to use this tool:
        - "account:troystribling repo:zgomot ext:rb Where is MIDI output handled in my code?"
        - "Find the latest commit message for the file that handles MIDI output in my code"
        - "What programming languages do I use in my code?"

    Returns: str
        The search results from the Code Repository Search Agent.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    code_repo_agent = CodeRepoAgent(query=query)
    result = await code_repo_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=DocumentSubagentSearchInput)
async def delegate_to_research_library_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    """
    Delegate a request to the Research Library Search Agent which searches and retrieves documents from 
    the research library. Use this when the user wants to search for specific documents in the research library.

    **Map pronouns**
    - 'my research', → requester's indexed research library in the research_library vector store.

    Examples of when to use this tool:
        - "title:Thermodynamics Look in my research library for the definition of a Carnot Cycle."
        - "shelf:publications Look in my research library for the definition of a Carnot Cycle"
        - "Look in my research library for the definition of a Carnot Cycle"
    Returns: str
        The search results from the Research Library Search Agent.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    research_library_agent = ResearchLibraryAgent(query=query)
    result = await research_library_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=DocumentSubagentSearchInput)
async def delegate_to_fred_data_info_search_agent(request: str, query: Optional[Dict[str, Any]] = None) -> str:
    """
    Delegate a request to the Fred Data Info Search Agent which searches and retrieves documents from the
    Fred data information. FRED stands for Federal Reserve Economic Data and is a database of economic data 
    time series. Use this tool to find the FRED time series identifier for a specific economic indicator.

    Examples of when to use this tool:
        - "popularity:>40 What time series are available for Commodities in the FRED data?"
        - "What price indexes are in FRED for Farm Products?"
        - "category_name:'Farm Products' What price indexes are in FRED?"

    Always call extract_document_query_from_request first to extract any query filters and the 
    cleaned query string from the user request. Pass the cleaned query string as the 'query' argument 
    when calling this tool and the extracted query filters as the 'query' argument when constructing the 
    FredDataInfoAgent instance.

    Returns: str
        The search results from the Fred Data Info Search Agent.
    """

    state = {"messages": [HumanMessage(content=request)]}
    config = RunnableConfig(configurable={"thread_id": shortuuid.uuid()})
    fred_data_info_agent = FredDataInfoAgent(query=query)
    result = await fred_data_info_agent.agent.ainvoke(state, config)
    return result["messages"][-1].content


@tool(args_schema=SubagentRequest)
async def extract_document_query_from_request(request: str) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    Extract a document query from a user request for document search for all
    document stores. For document search query filters can be prepended to the request, extracted 
    during processing and applied when making the query.

    Examples of when to use this tool:
        - "title:Thermodynamics Look in the document library for the definition of a Carnot Cycle."
        - "shelf:publications Look in the document library for the definition of a Carnot Cycle"
        - "popularity:>40 What time series are available for Commodities in the FRED data?"

    Returns: Tuple[str, Optional[Dict[str, Any]]]
        A tuple containing the cleaned query string and an optional dictionary of filters.
    """

    return build_filter_and_query(request)  

class OrchestratorAgent(ReactAgent):

    def __init__(self):
        tools = [delegate_to_search_agent, 
                 delegate_to_bar_chart_agent,
                 delegate_to_time_series_plot_agent,
                 delegate_to_document_store_info_agent,
                 delegate_to_code_repository_search_agent,
                 delegate_to_research_library_search_agent,
                 delegate_to_fred_data_info_search_agent,
                 extract_document_query_from_request]
        tool_node_name = "orchestrator_tool_node"
        super().__init__(tools, tool_node_name)


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
and research. Documents of this type will be referred to as "reference documents". The others contain documentation for APIs that may need to be consulted for information before making a request. Documents of this type will be referred as "API documents". The first type o

Analyze the user's request and call the appropriate tool(s) in the correct order.
A request may require multiple subagents called sequentially, for example searching for data
and then plotting it. Pass the full context needed for each subagent to do its job.

When multiple tools are called in sequence, your final response should only contain the verbatim output
from the last tool in the chain. Do not include raw data or intermediate results from earlier tools.

When you receive a tool result, return it to the user exactly as-is. Do not summarize, rephrase,
or strip any HTML, markdown, or formatting from tool output. The tool responses contain precise
formatting (including HTML tags, image references, and CSS classes) that must be preserved verbatim.
</instructions>


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
1. Call extract_document_query_from_request to extract the query and any filters from the request.
2. Retrieve requested data using the appropriate data source tool. If no data source tool is available
   do a web search for the data.
3. Pass the data to the appropriate visualization tool.
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