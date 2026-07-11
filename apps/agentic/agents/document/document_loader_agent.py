from __future__ import annotations

import os
import requests
import yaml
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.llm_factory import router_llm_model
from apps.agentic.core.tool_spec import PositiveExample, ToolSpec, tool_spec
from apps.agentic.core.document_loaders.github_document_loader import GitHubChromaDocumentLoader
from apps.agentic.core.document_loaders.research_library_document_loader import ResearchLibraryChromaDocumentLoader
from apps.agentic.core.document_loaders.etf.finance_database_loader import FinanceDatabaseLoader
from apps.agentic.core.constants import (
    GITHUB_API,
    GITHUB_ACCOUNTS,
    GITHUB_LOCAL_PATH,
    RESEARCH_LIBRARY_LOCAL_PATH,
    RESEARCH_DOCUMENTS_METADATA_FILE,
)

from lib.logger import get_logger

logger = get_logger("YADA")

PROJECT_ROOT = Path(__file__).resolve().parents[4]


class LoadResearchDocumentInput(BaseModel):
    filename: str = Field(..., description="Filename of the research document to load.")
    path: str = Field(..., description="Full file path to the document.")
    title: str = Field(..., description="Document title.")
    authors: str = Field(..., description="Document authors.")
    document_date: str = Field(..., description="Publication or document date.")
    topic: str = Field(..., description="Topic or subject area.")
    shelf: str = Field(..., description="Library shelf to assign the document to.")


class LoadGitHubRepoInput(BaseModel):
    account: str = Field(..., description="GitHub account or organization name.")
    repo: str = Field(..., description="Repository name.")


class LoadETFDataInput(BaseModel):
    family: Optional[str] = Field(default=None, description="Fund family to load (e.g. 'VanEck Asset Management'). Omit to load all families.")
    category_group: Optional[str] = Field(default=None, description="Asset class to load (e.g. 'Equities'). Omit to load all asset classes.")
    category: Optional[str] = Field(default=None, description="Category to load (e.g. 'High Yield Bonds'). Omit to load all categories.")
    exchange: Optional[str] = Field(default=None, description="Exchange code to load (e.g. 'PCX'). Omit to load all exchanges.")


def _append_research_document_metadata(meta_data: dict) -> None:
    metadata_path = (PROJECT_ROOT / RESEARCH_DOCUMENTS_METADATA_FILE).resolve()
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    if not metadata_path.exists():
        metadata_path.write_text("# Research Notes\n", encoding="utf-8")

    record = {
        "filename": meta_data.get("filename"),
        "path": meta_data.get("path"),
        "title": meta_data.get("title"),
        "authors": meta_data.get("authors"),
        "published_date": meta_data.get("document_date") or "",
        "topic": meta_data.get("topic"),
        "shelf": meta_data.get("shelf") or "",
    }

    entry_yaml = yaml.safe_dump([record], sort_keys=False)
    with metadata_path.open("a", encoding="utf-8") as handle:
        handle.write("\n" + entry_yaml)


def _remote_default_branch(repo) -> str:
    """Resolve the remote's default branch, e.g. 'main'."""
    try:
        return repo.remotes.origin.refs.HEAD.reference.name.split("/")[-1]
    except Exception:
        # Fall back to the locally checked-out branch.
        return repo.active_branch.name


def _clone_or_pull(repo_name: str, repo_url: str, local_path: str) -> None:
    from git import Repo

    if os.path.exists(local_path):
        try:
            # .repos is a read-only indexing mirror — we never commit here, so a
            # fetch + hard reset to the remote's default branch is the correct,
            # idempotent update. Unlike `git pull` it survives force-pushes and
            # history rewrites (which otherwise fail with "Need to specify how to
            # reconcile divergent branches").
            repo = Repo(local_path)
            repo.remotes.origin.fetch(prune=True)
            branch = _remote_default_branch(repo)
            repo.git.reset("--hard", f"origin/{branch}")
            logger.info(f"Updated {local_path} to origin/{branch}")
        except Exception as e:
            logger.error(f"Failed to update {local_path}: {e}")
    else:
        try:
            Repo.clone_from(repo_url, local_path)
            logger.info(f"Cloned {repo_name} from {repo_url} to {local_path}")
        except Exception as e:
            logger.error(f"Failed to clone {repo_name} from {repo_url}: {e}")


class DocumentLoaderAgent(ReactAgent):
    """
    Loads documents into the document stores.

    Tools:
        - load_research_document: Load a Markdown research note into the research library.
        - load_github_repo: Clone or pull a GitHub repository and index it.
        - load_all_github_repos: Clone or pull all configured GitHub repos and index them.
    """

    @classmethod
    async def create(cls) -> "DocumentLoaderAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            DocumentLoaderAgent.load_research_document,
            DocumentLoaderAgent.load_github_repo,
            DocumentLoaderAgent.load_all_github_repos,
            DocumentLoaderAgent.load_etf_data,
            DocumentLoaderAgent.reload_etf_data,
        ]
        super().__init__(tools, "document_loader_tool_node", mcp_tools=mcp_tools,
                         llm_factory=router_llm_model)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a document loader agent. Use the available tools to load documents
            into the appropriate document stores. After loading, confirm success or report
            any errors to the user.

            - Use load_research_document for Markdown research notes.
            - Use load_github_repo to index a single GitHub repository.
            - Use load_all_github_repos to index all configured GitHub repositories.
            - Use load_etf_data to add ETF data from FinanceDatabase into the ETF store.
              Optional filters: family, category_group, category, exchange.
              Omitting all filters loads the full universe (~36K funds, ~10 min).
            - Use reload_etf_data to wipe the ETF collection and reload from FinanceDatabase.
              CRITICAL: Before calling reload_etf_data you MUST ask the user to confirm.
              Say exactly: "This will wipe the entire ETF collection and reload from
              FinanceDatabase. Reply yes to proceed." Do not call reload_etf_data until
              the user has replied with an explicit "yes".
            </instructions>
            """

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
    @tool_spec(
        args_schema=LoadResearchDocumentInput,
        metadata=ToolSpec(
            primary_function="""
            Load a Markdown research note into the research library document store.
            """,
            positive_examples=[
                PositiveExample(input="Load the research document jaynes_prob_theory.pdf into the research library."),
            ],
        ),
    )
    async def load_research_document(
        filename: str,
        path: str,
        title: str,
        authors: str,
        document_date: str,
        topic: str,
        shelf: str,
    ) -> str:
        note_path = Path(path)
        if not note_path.exists():
            return f"Error: file not found at path '{path}'."

        meta_data = {
            "filename": filename,
            "path": path,
            "title": title,
            "authors": authors,
            "document_date": document_date,
            "topic": topic,
            "shelf": shelf,
        }

        doc_loader = ResearchLibraryChromaDocumentLoader()
        await doc_loader.load_document(str(note_path), meta_data=meta_data)
        _append_research_document_metadata(meta_data)

        return f"Loaded research document: {title}."


    @staticmethod
    @tool_spec(
        args_schema=LoadGitHubRepoInput,
        metadata=ToolSpec(
            primary_function="""
            Clone or pull a single GitHub repository and index it in the code store.
            """,
            positive_examples=[
                PositiveExample(input="Load the yada repository for the troystribling account."),
            ],
        ),
    )
    async def load_github_repo(account: str, repo: str) -> str:
        github_api_key = os.environ["GITHUB_API_KEY"]
        headers = {"Authorization": f"token {github_api_key}"}

        user_resp = requests.get(f"{GITHUB_API}/user", headers=headers)
        if user_resp.status_code != 200:
            return "Error: failed to fetch authenticated GitHub user."

        auth_username = user_resp.json()["login"]
        clone_url = f"https://github.com/{account}/{repo}.git"
        auth_clone_url = clone_url.replace("https://", f"https://{auth_username}:{github_api_key}@")
        local_path = os.path.join(GITHUB_LOCAL_PATH, account, repo)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        _clone_or_pull(repo, auth_clone_url, local_path)

        doc_loader = GitHubChromaDocumentLoader()
        await doc_loader.load_document(local_path)

        return f"Loaded GitHub repository {account}/{repo}."


    @staticmethod
    @tool_spec(
        args_schema=None,
        metadata=ToolSpec(
            primary_function="""
            Clone or pull all configured GitHub repositories and index them in the code store.
            """,
            positive_examples=[
                PositiveExample(input="Load all GitHub repositories."),
                PositiveExample(input="Update all GitHub repos in the code store."),
            ],
        ),
    )
    async def load_all_github_repos() -> str:
        github_api_key = os.environ["GITHUB_API_KEY"]
        headers = {"Authorization": f"token {github_api_key}"}

        user_resp = requests.get(f"{GITHUB_API}/user", headers=headers)
        if user_resp.status_code != 200:
            return "Error: failed to fetch authenticated GitHub user."

        auth_username = user_resp.json()["login"]
        doc_loader = GitHubChromaDocumentLoader()

        for account in GITHUB_ACCOUNTS:
            if account == auth_username:
                url = f"{GITHUB_API}/user/repos?per_page=100&visibility=all"
            else:
                url = f"{GITHUB_API}/orgs/{account}/repos?per_page=100&type=all"

            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                return f"Error: failed to fetch repos for {account}: {resp.text}"

            for repo in resp.json():
                repo_name = repo["name"]
                clone_url = repo["clone_url"]
                auth_clone_url = clone_url.replace("https://", f"https://{auth_username}:{github_api_key}@")
                parsed_url = urlparse(auth_clone_url)
                owner = parsed_url.path.split("/")[1]
                local_path = os.path.join(GITHUB_LOCAL_PATH, owner, repo_name)
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                _clone_or_pull(repo_name, auth_clone_url, local_path)

            logger.info(f"Updated all repos for {account}")

        await doc_loader.load_all_documents()

        return "All GitHub repositories cloned or updated and indexed successfully."


    @staticmethod
    @tool_spec(
        args_schema=LoadETFDataInput,
        metadata=ToolSpec(
            primary_function="""
            Load ETF data from FinanceDatabase into the ETF ChromaDB store.
            All filter arguments are optional; omitting them loads the full universe (~36K funds).
            """,
            positive_examples=[
                PositiveExample(input="Load ETF data for VanEck Asset Management."),
                PositiveExample(input="Load all ETF data into the store."),
                PositiveExample(input="Load Fixed Income ETFs on the PCX exchange."),
            ],
        ),
    )
    async def load_etf_data(
        family: Optional[str] = None,
        category_group: Optional[str] = None,
        category: Optional[str] = None,
        exchange: Optional[str] = None,
    ) -> str:
        loader = FinanceDatabaseLoader()
        await loader.load_all_documents(
            family=family,
            category_group=category_group,
            category=category,
            exchange=exchange,
        )
        return "ETF data loaded successfully."


    @staticmethod
    @tool_spec(
        args_schema=LoadETFDataInput,
        metadata=ToolSpec(
            primary_function="""
            Wipe the existing ETF ChromaDB collection and reload from FinanceDatabase.
            IMPORTANT: only call this tool after the user has explicitly confirmed with "yes".
            """,
            positive_examples=[
                PositiveExample(input="Reload all ETF data. yes"),
                PositiveExample(input="Wipe and reload the ETF store for VanEck. yes"),
            ],
        ),
    )
    async def reload_etf_data(
        family: Optional[str] = None,
        category_group: Optional[str] = None,
        category: Optional[str] = None,
        exchange: Optional[str] = None,
    ) -> str:
        loader = FinanceDatabaseLoader()
        await loader.reload_all_documents(
            family=family,
            category_group=category_group,
            category=category,
            exchange=exchange,
        )
        return "ETF collection wiped and reloaded successfully."
