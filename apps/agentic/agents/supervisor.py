from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import langchain

from lib.logger import get_logger

from apps.agentic.core.messages import get_last_message, WorkerState
from apps.agentic.core.utils import build_llm, should_continue
from apps.agentic.agents.search import SearchAgent
from apps.agentic.agents.bar_chart import BarChartAgent

logger = get_logger("YADA")

class SupervisorAgent:
    """
    Supervisor Agent that manages the flow of the researcher agent.
    It decides whether to continue with the model or call a tool based on the last message.
    """

    def __init__(self):
        self.__llm = build_llm()
        
        self.__workers = {
            "researcher": self.__create_agent_node(SearchAgent().agent, "researcher"),
            "bar_chart_generator": self.__create_agent_node(BarChartAgent().agent, "bar_chart_generator")   
        }

        self.__prompt = self.__create_prompt()
        self.__agent = self.__prompt | self.__llm
        

    @property
    def agent(self): 
        """
        Get the compiled agent state graph.
        """
        return self.__agent
    
    
    async def process_request(self, request: str) -> WorkerState:
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
        
        agent_msg = {"messages": [HumanMessage(content=request)]}
        supervisor_output = await self.agent.ainvoke(agent_msg)
        next_nodes = [item.strip() for item in supervisor_output.content.split(",")]
        logger.debug(f"Supervisor decided to call: {next_nodes}")

        if "FINISH" in next_nodes:
            logger.debug("No further action required. Finishing conversation.")
            return agent_msg

        for node in next_nodes:
            logger.debug(f"Calling node: {node}")
            
            if node not in self.__workers:
                raise RuntimeError(f"Unknown worker: {node}")

            worker = self.__workers[node]
            agent_msg = await worker(agent_msg, {})

        return agent_msg


    def __create_prompt(self):
        """
        Create the prompt template for the supervisor agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        system_prompt = (
            "You are a supervisor tasked with delegating user requests to a team of agents. The agents you supervise " 
            "are called {team_members}. {researcher} performs search requests. {bar_chart_generator} plots data as a bar chart. "
            "You must determine which of the agents should process the user request and respond with the name of the all agents "
            "required. If there is no agent that can respond to the request return FINISH. " 
            "It is possible that a request would require multiple agents and be executed in some order. "
            "You should return all the agents that should be called in the order they should be called."
        )

        team = list(self.__workers.keys())
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
                                                bar_chart_generator=team[1])
        logger.debug(f"Supervisor prompt: {formatted_system_prompt}")

        return  prompt.partial(options=", ".join(options), 
                               team_members=", ".join(team), 
                               researcher=team[0], 
                               bar_chart_generator=team[1])



    def __create_agent_node(self, agent, node_name: str):
        async def node(state, config):
            logger.debug(f"Invoking worker: {node_name}")
            logger.debug(f"Request Message: {get_last_message(state).content}")
            result = await agent.ainvoke(state, config)
            last_message = get_last_message(result)
            content = last_message.content
            logger.debug(f"{node_name} response Message: {content}")
            return {
                "messages": [
                    HumanMessage(content=content, name=node_name)
                ]
            }
        return node
