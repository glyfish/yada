from typing import Optional

from lib.logger import get_logger

from langchain_core.messages import HumanMessage
from langgraph.graph import END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import langchain

from apps.agentic.core.agents.messages import get_last_message, WorkerState
from apps.agentic.core.utils import build_llm
from langsmith.run_helpers import traceable

from apps.agentic.agents.search_agent import SearchAgent
from apps.agentic.agents.document.document_library_agent import DocumentLibraryAgent
from apps.agentic.agents.plots.bar_chart_agent import BarChartAgent
from apps.agentic.agents.plots.time_series_plot_agent import TimeSeriesPlotAgent
from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.document_store_info_agent import DocumentStoreInfoAgent

from apps.agentic.core.agents.query_filters import build_filter_and_query


logger = get_logger("YADA")

class SupervisorAgent:
    """
    Supervisor Agent that manages the flow of the researcher agent.
    It decides whether to continue with the model or call a tool based on the last message.
    """

    def __init__(self):
        self._llm = build_llm()        
        

    @property
    def agent(self): 
        """
        Get the compiled agent state graph.
        """
        return self._agent
    
    
    @traceable(run_type="chain", name="SupervisorAgent.process_request")
    async def process_request(self, request: str, session_id: Optional[str] = None) -> WorkerState:
        """
        Process a user request and initialize the state.

        Parameters
        ----------
            request: str
                The user request to process.
        Returns:
            WorkerState
                The initial state with the user request.
        """
        
        clean_request, query = build_filter_and_query(request)
        logger.debug(f"Processed request: {clean_request}, {query}")

        # build workers (they close over query in CodeRepoAgent, ResearchDocumentAgent, etc)
        self._create_workers(query)

        # build the supervisor routing LLM
        prompt = self._create_prompt()
        self._agent = prompt | self._llm

        # initial graph state: just the user question
        state: WorkerState = {"messages": [HumanMessage(content=clean_request)]}

        # ask supervisor LLM which nodes to run
        config = {}
        if session_id is not None:
            config = {"configurable": {"thread_id": session_id}}

        supervisor_output = await self.agent.ainvoke(state, config)
        routes = [item.strip() for item in supervisor_output.content.split(",")]
        logger.debug(f"Supervisor decided to call: {routes}")

        # If supervisor says FINISH, just return the initial state (no tool chosen)
        if "FINISH" in routes:
            logger.debug("No further action required. Finishing conversation.")
            return state

        # Execute workers in order, feeding each one's output into the next
        for node_name in routes:
            logger.debug(f"Calling node: {node_name}")
            if node_name not in self._workers:
                raise RuntimeError(f"Unknown worker: {node_name}")

            worker = self._workers[node_name]
            state = await worker(state, config)
            logger.debug(f"State after {node_name}: {state}")

        # CRITICAL: return the final state AS-IS
        return state


    def _create_prompt(self):
        """
        Create the prompt template for the supervisor agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        system_prompt = """
        You are a supervisor for Troy Stribling tasked with delegating tool requests to a team of agents. 
        The agents you supervise are called {team_members}.
            * {researcher}
                Performs search requests when data is needed
            * {bar_chart_generator} 
                Plots categorical data as a bar chart. 
            * {time_series_generator} 
                Generates time series plots for time varying numerical data.
            * {code_repository_search} 
                Searches Troy Stribling's code repositories for relevant code snippets and generates 
                reports as requested. If there is a mention of 'my code', 'my repo(s)', 'my project', 'YADA', 'glyfish', 
                'troystribling', a file path, a filename, or a function/class, you MUST call the 'Troy Stribling Code Repository Agent'.
            * {research_library_search} 
                Searches Troy Stribling's research library for relevant information and generates
                reports as requested. If there is a mention of 'my research', 'my documents', 'my papers', 'my articles',
                'Troy Stribling research documents', you MUST call the 'Troy Stribling Research Library Agent'.
            * {document_library_search} 
                Searches PDF document library for relevant information and generates 
                reports as requested. If there is a mention of 'document library', 'pdf documents', 'articles', 'documents'
                you MUST call the Document Library Agent"
            * {document_store_info} 
                Retrieves information requested from the specified document store. If there is a request
                referencing one of the known document stores for the document filenames, titles, authors or other
                data available in the document store meta data you MUST call the Document Information Agent.
                The available document stores are: Code Repositories, Research Documents and Document Library.
                
                Example {document_store_info} Questions
                1. What repositories are available in my code repositories.
                2. List the files in the troystribling/SimpleFutures repository.

                {document_store_info} File listing Instructions
                1. DO NOT LIST these Files in the output: .gitignore, *.xcodeproj
                2. Ignore the files in the directory .git and do not list it in the output.


        Map pronouns:
            * 'my code', 'code database' → Troy Stribling’s indexed repos in the vector store.
            * 'code database' → Troy Stribling’s indexed repos in the vector store.
            * 'my research', → Troy Stribling’s indexed research library in the vector store.
                
        Your Task
            You task is to determine which of the agents should process the user request and respond with the name of the all agents
            required. If there is no agent that can respond to the request return FINISH. 
            It is possible that a request would require multiple agents and be executed in some order.
            You should return all the agents that should be called in the order they should be called.
        """

        team = list(self._workers.keys())
        options = ["FINISH"] + team

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "Given the conversation above, who should act next? Or should we FINISH Select one of: {options}"
            )
        ])

        formatted_system_prompt = prompt.format(messages=[],
                                                options=", ".join(options),
                                                team_members=", ".join(team),
                                                researcher=team[0],
                                                bar_chart_generator=team[1],
                                                time_series_generator=team[2],
                                                code_repository_search=team[3],
                                                research_library_search=team[4],
                                                document_library_search=team[5],
                                                document_store_info=team[6])
        logger.debug(f"Supervisor prompt: {formatted_system_prompt}")

        return  prompt.partial(options=", ".join(options),
                               team_members=", ".join(team),
                               researcher=team[0],
                               bar_chart_generator=team[1],
                               time_series_generator=team[2],
                               code_repository_search=team[3],
                               research_library_search=team[4],
                               document_library_search=team[5],
                               document_store_info=team[6])



    def _create_agent_node(self, agent, node_name: str):
        async def node(state, config):
            logger.debug(f"Invoking worker: {node_name}")
            logger.debug(f"Request Message: {get_last_message(state).content}")

            result = await agent.ainvoke(state, config)

            # For debugging, we can still log what came back
            try:
                last_message = get_last_message(result)
                logger.debug(f"{node_name} response Message: {last_message.content}")
            except Exception:
                logger.debug(f"{node_name} returned non-standard result: {result}")

            # CRITICAL: return the agent result directly, don't rewrap
            return result

        return traceable(run_type="chain", name=node_name)(node)


    def _create_workers(self, query):
        self._workers = {            
            "researcher": self._create_agent_node(SearchAgent().agent, "researcher"),
            "bar_chart_generator": self._create_agent_node(BarChartAgent().agent, "bar_chart_generator"),
            "time_series_generator": self._create_agent_node(TimeSeriesPlotAgent().agent, "time_series_generator"),
            "code_repository_search": self._create_agent_node(CodeRepoAgent(query).agent, "code_repository_search"),
            "research_library_search": self._create_agent_node(ResearchLibraryAgent(query).agent, "research_library_search"),
            "document_library_search": self._create_agent_node(DocumentLibraryAgent(query).agent, "document_library_search"),
            "document_store_info": self._create_agent_node(DocumentStoreInfoAgent().agent, "document_store_info"),
        }
