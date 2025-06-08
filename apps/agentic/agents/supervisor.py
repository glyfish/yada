from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.messages import get_last_message, WorkerState
from apps.agentic.core.utils import build_llm, should_continue

class SupervisorAgent:
    """
    Supervisor Agent that manages the flow of the researcher agent.
    It decides whether to continue with the model or call a tool based on the last message.
    """

    def __init__(self):
        self.__llm = build_llm()


    def invoke(self, state: WorkerState, config=None) -> WorkerState:
        """Invoke the agent with the current state."""
        return self.agent.invoke(state, config)
    

    def __create_prompt(self):
        """
        Create the prompt template for the supervisor agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        system_prompt = (
            "You are a supervisor tasked with delegating user requests to a team of agents. The agents you supervise" 
            "are called {team_members}. {team_member_0} performs search requests. {team_member_1} plots data as a bar chart. "
            "You must determine which of the agents should process the user request and respond with the name of the all agents"
            "required. If there is no agent that can respond to the request return FINISH." 
            "It is possible that a request would require multiple agents and be executed in some order."
            "You should return all the agents that should be called in the order they should be called."
        )

        team_members = ["researcher", "plotter"]
        options = ["FINISH"] + team_members 

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "Given the conversation above, who should act next? Or should we FINISH Select one of: {options}"
            )
        ])

        return  prompt.partial(options=", ".join(options), 
                               team_members=", ".join(team_members), 
                               team_member_0=team_members[0], 
                               team_member_1=team_members[1])



    def __create_agent_node(agent, node_name: str):
        def node(state, config):
            result = agent.invoke(state, config)
            last_message = get_last_message(result)
            content: str = last_message.content
            return {
                "messages": [
                    HumanMessage(content=content, name=node_name)
                ]
            }
        return node
