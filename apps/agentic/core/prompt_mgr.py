import os
from pathlib import Path

from langchain import hub
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from lib.logger import get_logger

logger = get_logger("YADA")

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"
HUB_OWNER = os.environ.get("LANGCHAIN_HUB_OWNER", "")
HUB_ENABLED = bool(os.environ.get("LANGCHAIN_API_KEY") or os.environ.get("LANGSMITH_API_KEY"))


def _hub_name(prompt_name: str) -> str:
    """
    Build the fully qualified hub prompt name: owner/prompt_name.
    """

    return f"{HUB_OWNER}/{prompt_name}" if HUB_OWNER else prompt_name


def _load_local(prompt_name: str) -> str:
    """
    Read a prompt markdown file from the local prompts directory.
    """

    path = PROMPTS_DIR / f"{prompt_name}.md"
    return path.read_text()


def _build_chat_prompt(system_text: str) -> ChatPromptTemplate:
    """
    Wrap a system prompt string into a ChatPromptTemplate with a messages placeholder.
    """

    return ChatPromptTemplate.from_messages([
        ("system", system_text),
        MessagesPlaceholder(variable_name="messages"),
    ])


def push_prompt(prompt_name: str) -> None:
    """
    Read a local markdown prompt file and push it to LangChain Hub.
    """

    system_text = _load_local(prompt_name)
    prompt = _build_chat_prompt(system_text)
    hub_name = _hub_name(prompt_name)
    hub.push(hub_name, prompt, new_repo_is_public=False)
    logger.info(f"Pushed prompt '{hub_name}' to LangChain Hub")


def pull_prompt(prompt_name: str) -> ChatPromptTemplate:
    """
    Load a prompt from the local markdown file.
    """

    logger.debug(f"Loading prompt '{prompt_name}' from local file")
    return _build_chat_prompt(_load_local(prompt_name))


def push_all() -> None:
    """
    Push all markdown prompt files in the prompts directory to LangChain Hub.
    """
    
    for path in PROMPTS_DIR.glob("*.md"):
        push_prompt(path.stem)
