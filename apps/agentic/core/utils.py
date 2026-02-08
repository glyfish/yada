import os
import yaml

from pathlib import Path
from collections.abc import Iterable
from apps.agentic.core.constants import RESEARCH_DOCUMENTS_METADATA_FILE

def load_api_key(filepath=".keys/.chatgpt_key"):
    with open(filepath, "r") as file:
        return file.read().strip()


def set_chatgpt_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".chatgpt_key")
    os.environ["OPENAI_API_KEY"] = load_api_key(filepath)


def set_anthropic_env(filedir=".keys"):
    filepath = os.path.join(filedir, ".anthropic_key")
    os.environ["ANTHROPIC_API_KEY"] = load_api_key(filepath)


def set_langsmith_env(project_name="yada", tracing=True, filedir=".keys"):
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
    os.environ["USER_AGENT"] = "yada/0.1 (troy@gly.fish)"


def log_input(x):
    print("\n🔍 INPUT DATA:", x)
    return x


def log_output(x):
    print("\n✅ OUTPUT RESULT:", x)
    return x


def load_research_documents_metadata(yaml_path: str | Path | None = None) -> list[dict]:
    """
    Load the research document metadata YAML file.

    Args:
        yaml_path: Optional override path. Defaults to RESEARCH_DOCUMENTS_METADATA_FILE.

    Returns:
        A list of metadata dictionaries (one per research document).
    """

    target = Path(yaml_path or RESEARCH_DOCUMENTS_METADATA_FILE)
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()

    if not target.exists():
        raise FileNotFoundError(f"Research documents metadata file not found: {target}")

    with target.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or []

    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, Iterable):
        raise ValueError(f"Expected sequence in {target}, received {type(data).__name__}")

    records: list[dict] = []
    for entry in data:
        if isinstance(entry, dict):
            records.append(entry)
        else:
            raise ValueError(f"Metadata entry must be a mapping, received {type(entry).__name__}")

    return records


async def load_research_documents(doc_loader, research_library_files_path):
    document_meta_data = load_research_documents_metadata(research_library_files_path)
    for meta_data in document_meta_data:
        note_path = os.path.join("../..", meta_data["path"])
        print(f"Loading research document: {note_path}")
        await doc_loader.load_document(str(note_path), meta_data=meta_data)