from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END
from apps.agentic.core.messages import get_last_message, WorkerState


def create_agent_node(agent, node_name: str):
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


def should_continue(state: WorkerState):
    messages = state["messages"]
    ai_message = messages[-1]
    
    # Check if it's an AI message with tool calls
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tool"
    return END
