from __future__ import annotations

import os
import requests
import yaml
from pathlib import Path
from urllib.parse import urlparse

from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.tool_spec import PositiveExample, ToolSpec, tool_spec
from apps.agentic.core.document_loaders.github_document_loader import GitHubChromaDocumentLoader
from apps.agentic.core.document_loaders.research_library_document_loader import ResearchLibraryChromaDocumentLoader
from apps.agentic.core.document_loaders.document_library_loader import DocumentLibraryLoader
from apps.agentic.core.constants import (
    GITHUB_API,
    GITHUB_ACCOUNTS,
    GITHUB_LOCAL_PATH,
    RESEARCH_LIBRARY_LOCAL_PATH,
    RESEARCH_DOCUMENTS_METADATA_FILE,
    PDF_DOCUMENT_LIBRARY_LOCAL_PATH,
)

from lib.logger import get_logger

logger = get_logger("YADA")

PROJECT_ROOT = Path(__file__).resolve().parents[4]


class LoadResearchDocumentInput(BaseModel):
    filename: str = Field(..., description="Filename of the research document to load.")
    title: str = Field(..., description="Document title.")
    authors: str = Field(..., description="Document authors.")
    document_date: str = Field(..., description="Publication or document date.")
    topic: str = Field(..., description="Topic or subject area.")
    shelf: str = Field(..., description="Library shelf to assign the document to.")


class LoadGitHubRepoInput(BaseModel):
    account: str = Field(..., description="GitHub account or organization name.")
    repo: str = Field(..., description="Repository name.")


class LoadPDFDocumentInput(BaseModel):
    filename: str = Field(..., description="Filename of the PDF document to load.")
    title: str = Field(..., description="Document title.")
    authors: str = Field(..., description="Document authors.")
    published_date: str = Field(..., description="Publication date.")
    topic: str = Field(..., description="Topic or subject area.")
    shelf: str = Field(..., description="Library shelf to assign the document to.")


def _resolve_research_note_path(filename: str) -> Path:
    base_dir = Path(RESEARCH_LIBRARY_LOCAL_PATH).resolve()
    if not base_dir.exists():
        raise FileNotFoundError(f"Research library directory '{base_dir}' not found.")

    candidate = (base_dir / filename).resolve()
    try:
        candidate.relative_to(base_dir)
    except ValueError:
        raise ValueError("Filename must be inside the research library directory.")

    if candidate.exists() and candidate.is_file():
        return candidate

    matches = list(base_dir.rglob(Path(filename).name))
    for match in matches:
        if match.is_file():
            return match

    raise FileNotFoundError(f"Research document '{filename}' not found under {base_dir}.")


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


def _clone_or_pull(repo_name: str, repo_url: str, local_path: str) -> None:
    from git import Repo

    if os.path.exists(local_path):
        try:
            repo = Repo(local_path)
            repo.remotes.origin.pull()
            logger.info(f"Pulled {local_path}")
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
        - load_pdf_document: Load a PDF into the document library.
    """

    @classmethod
    async def create(cls) -> "DocumentLoaderAgent":
        return cls()

    def __init__(self, mcp_tools: list = []):
        tools = [
            DocumentLoaderAgent.load_research_document,
            DocumentLoaderAgent.load_github_repo,
            DocumentLoaderAgent.load_all_github_repos,
            DocumentLoaderAgent.load_pdf_document,
        ]
        super().__init__(tools, "document_loader_tool_node", mcp_tools=mcp_tools)


    def create_prompt(self):
        system_prompt = """
            <instructions>
            You are a document loader agent. Use the available tools to load documents
            into the appropriate document stores. After loading, confirm success or report
            any errors to the user.

            - Use load_research_document for Markdown research notes.
            - Use load_github_repo to index a single GitHub repository.
            - Use load_all_github_repos to index all configured GitHub repositories.
            - Use load_pdf_document for PDF documents.
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
        title: str,
        authors: str,
        document_date: str,
        topic: str,
        shelf: str,
    ) -> str:
        note_path = _resolve_research_note_path(filename)
        try:
            relative_note_path = note_path.relative_to(PROJECT_ROOT)
        except ValueError:
            relative_note_path = note_path

        meta_data = {
            "filename": filename,
            "path": str(relative_note_path),
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
        args_schema=LoadPDFDocumentInput,
        metadata=ToolSpec(
            primary_function="""
            Load a PDF document into the PDF document library store.
            """,
            positive_examples=[
                PositiveExample(input="Load the PDF document jaynes_prob_theory.pdf into the document library."),
            ],
        ),
    )
    async def load_pdf_document(
        filename: str,
        title: str,
        authors: str,
        published_date: str,
        topic: str,
        shelf: str,
    ) -> str:
        pdf_path = os.path.join(PDF_DOCUMENT_LIBRARY_LOCAL_PATH, filename)
        meta_data = {
            "filename": filename,
            "path": pdf_path,
            "title": title,
            "authors": authors,
            "published_date": published_date,
            "topic": topic,
            "shelf": shelf,
        }

        doc_loader = DocumentLibraryLoader()
        await doc_loader.load_document(pdf_path, meta_data=meta_data)

        return f"Loaded PDF document: {title}."
