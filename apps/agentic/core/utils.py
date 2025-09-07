import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END

from apps.agentic.core.messages import WorkerState


def load_api_key(filepath=".keys/.chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()


def set_chatgpt_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".chatgpt_key")
    os.environ["OPENAI_API_KEY"] = load_api_key(filepath)


def set_langsmith_env(project_name="pr-crushing-rowing-30", tracing=False, filedir=".keys"):
    filepath = os.path.join(filedir, ".langsmith_key")
    os.environ["LANGSMITH_API_KEY"] = load_api_key(filepath)
    os.environ["LANGCHAIN_TRACING_V2"] = "true" if tracing else "false"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = project_name


def set_tavily_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".tavily_key")
    os.environ["TAVILY_API_KEY"] = load_api_key(filepath)


def set_github_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".github_key")
    os.environ["GITHUB_API_KEY"] = load_api_key(filepath)


def set_fred_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".fred_key")
    os.environ["FRED_API_KEY"] = load_api_key(filepath)


def set_bls_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".bls_key")    
    os.environ["BLS_API_KEY"] = load_api_key(filepath)


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

