import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END

def load_api_key(filepath="../.chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()


def set_chatgpt_env():
    os.environ["OPENAI_API_KEY"] = load_api_key()


def set_langsmith_env(project_name="pr-crushing-rowing-30", tracing=False):
    os.environ["LANGSMITH_API_KEY"] = load_api_key("../.langsmith_key")
    os.environ["LANGCHAIN_TRACING_V2"] = "true" if tracing else "false"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "pr-crushing-rowing-30"


def set_tavily_env():
    os.environ["TAVILY_API_KEY"] = load_api_key("../.tavily_key")


def log_input(x):
    print("\n🔍 INPUT DATA:", x)
    return x


def log_output(x):
    print("\n✅ OUTPUT RESULT:", x)
    return x


def build_llm():
    """Build an LLM with a custom model name."""
    return ChatOpenAI(model="gpt-4", temperature=0.5)


def get_last_message(state) -> BaseMessage:
    """Get the last message from a list of messages."""
    return state["messages"][-1]
