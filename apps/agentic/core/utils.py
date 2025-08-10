import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END

from apps.agentic.core.messages import WorkerState


def load_api_key(filepath=".chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()


def set_chatgpt_env():
    os.environ["OPENAI_API_KEY"] = load_api_key()


def set_langsmith_env(project_name="pr-crushing-rowing-30", tracing=False):
    os.environ["LANGSMITH_API_KEY"] = load_api_key(".langsmith_key")
    os.environ["LANGCHAIN_TRACING_V2"] = "true" if tracing else "false"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "pr-crushing-rowing-30"


def set_tavily_env():
    os.environ["TAVILY_API_KEY"] = load_api_key(".tavily_key")


def set_github_env():
    os.environ["GITHUB_API_KEY"] = load_api_key(".github_key")

def set_user_agent():
    os.environ["USER_AGENT"] = "yada/0.1 (troy.stribling@gly.fish)"

def log_input(x):
    print("\n🔍 INPUT DATA:", x)
    return x


def log_output(x):
    print("\n✅ OUTPUT RESULT:", x)
    return x


def build_llm(model="gpt-4.1") -> ChatOpenAI:
    """
    Build an LLM with a custom model name.
    """

    return ChatOpenAI(model=model, temperature=1)
