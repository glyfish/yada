from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

from functools import lru_cache

from pathlib import Path

from apps.agentic.core.agents.react_agent import ReactAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.research_library_document_loader import (
    ResearchLibraryChromaDocumentLoader,
)
from apps.agentic.core.document_loaders.document_library_loader import (
    DocumentLibraryLoader,
)

from apps.agentic.agents.document.code_repo_agent import CodeRepoAgent
from apps.agentic.agents.document.fred_data_info_agent import FredDataInfoAgent
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.agents.document.pdf_document_library_agent import PDFDocumentLibraryAgent

from lib.logger import get_logger

logger = get_logger("YADA")

class RepositoryFilesInput(BaseModel):
    """Schema for requesting filenames within a repository."""
    account: str = Field(
        ...,
        description="GitHub account/owner name, e.g., 'troystribling'.",
    )
    repository: str = Field(
        ...,
        description="Repository name, e.g., 'yada'.",
    )
    max_results: int = Field(
        default=250,
        ge=1,
        le=5000,
        description="Maximum number of filenames to return (default 250).",
    )


class ResearchLibraryMetadataListInput(BaseModel):
    """Schema for slicing research library metadata rows."""

    max_results: int = Field(
        default=100,
        ge=1,
        le=1000,
        description="Maximum number of research note metadata rows to return (default 100).",
    )
    start_after: str | None = Field(
        default=None,
        description="Filename or path after which to start the listing (exclusive).",
    )


class ResearchLibraryTitleQueryInput(BaseModel):
    """Schema for filtering research library titles by metadata."""

    author: str | None = Field(
        default=None,
        description="Author name to filter by (case-insensitive substring match).",
    )
    topic: str | None = Field(
        default=None,
        description="Topic text to filter by (case-insensitive substring match).",
    )
    shelf: str | None = Field(
        default=None,
        description="Require that the document belongs to this shelf (case-insensitive).",
    )
    limit: int = Field(
        default=100,
        ge=1,
        le=200,
        description="Maximum number of titles to return (default 100).",
    )


class DocumentLibraryMetadataListInput(BaseModel):
    """Schema for slicing PDF document library metadata rows."""

    max_results: int = Field(
        default=100,
        ge=1,
        le=1000,
        description="Maximum number of PDF document metadata rows to return (default 100).",
    )
    start_after: str | None = Field(
        default=None,
        description="Filename or path after which to start the listing (exclusive).",
    )


class DocumentLibraryTitleQueryInput(BaseModel):
    """Schema for filtering PDF document titles by metadata."""

    author: str | None = Field(
        default=None,
        description="Author name to filter by (case-insensitive substring match).",
    )
    topic: str | None = Field(
        default=None,
        description="Topic text to filter by (case-insensitive substring match).",
    )
    shelf: str | None = Field(
        default=None,
        description="Require that the document belongs to this shelf (case-insensitive).",
    )
    limit: int = Field(
        default=100,
        ge=1,
        le=200,
        description="Maximum number of titles to return (default 100).",
    )

def collect_metadata_rows(loader, row_factory) -> list[dict]:
    collection = getattr(loader.vectorstore, "_collection", None)
    if collection is None:
        logger.warning("Vector store collection unavailable for loader %s", loader)
        return []

    try:
        result = collection.get(include=["metadatas"], limit=100_000)
    except Exception as exc:
        logger.error("Failed to read metadata: %s", exc)
        return []

    metadatas = result.get("metadatas") or []
    aggregated: dict[str, dict] = {}

    for meta in metadatas:
        if not meta:
            continue
        path = meta.get("path") or meta.get("filename")
        if not path:
            continue
        if path in aggregated:
            continue

        aggregated[path] = row_factory(meta, path)

    return list(aggregated.values())


def paginate_metadata_rows(rows: list[dict], max_results: int, start_after: str | None) -> list[dict]:
    if not rows:
        return []

    sorted_rows = sorted(rows, key=lambda r: (r.get("filename") or r.get("path") or "").lower())
    start_index = 0
    if start_after:
        token = start_after.lower()
        for idx, row in enumerate(sorted_rows):
            filename = (row.get("filename") or "").lower()
            path = (row.get("path") or "").lower()
            if token in {filename, path}:
                start_index = idx + 1
                break

    end_index = min(start_index + max_results, len(sorted_rows))
    return sorted_rows[start_index:end_index]

class DocumentStoreInfoAgent(ReactAgent):
    """
    Handle requests for information about document libraries.
    """

    def __init__(self):
        tools = [
            DocumentStoreInfoAgent.repository_names,
            DocumentStoreInfoAgent.filenames_for_repository,
            DocumentStoreInfoAgent.research_library_metadata_summary,
            DocumentStoreInfoAgent.research_library_titles_by_metadata,
            DocumentStoreInfoAgent.document_library_metadata_summary,
            DocumentStoreInfoAgent.document_library_titles_by_metadata,
        ]
        tool_node_name = "document_info_tool_node"

        super().__init__(tools, tool_node_name)

    
    def create_prompt(self):
        """
        Create the prompt template for the document library agent.
        """
    
        system_prompt = f"""
        <instructions>
        You are an expert in retrieving information about the contents of documents available in all
        the document stores. The tools allow you to:
        - List repository names and filenames for code repositories.
        - Summarize metadata for research notes, including filename, title, author, topic, and shelf.
        - Filter research note titles using author/topic/shelf metadata.
        - Summarize metadata for PDF documents, including filename, title, authors, published date, topic, and shelf.
        - Filter PDF document titles using author/topic/shelf metadata.
        Call the appropriate tool when the user asks about any of these data sources.

        You also have access to descriptions of the query filters that can be used to
        refine searches in the document stores. If the user asks for information about
        the query filters use the following descriptions to answer their question. Only respond
        with information about the query filters, usage examples for the filters
        and which agents they apply to. Do not make a request to the document agents for a response.
        </instructions>
    

        {CodeRepoAgent.QUERY_FILTERS}   

        {FredDataInfoAgent.QUERY_FILTERS}

        {ResearchLibraryAgent.QUERY_FILTERS}

        {PDFDocumentLibraryAgent.QUERY_FILTERS}
        """

        logger.debug(f"DocumentInfoAgent Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])


    @staticmethod
    @lru_cache(maxsize=1)
    def _research_library_metadata(db_path=DB_PATH) -> list[dict]:
        """
        Aggregate research library metadata from the Chroma collection, one row per file.
        """

        loader = ResearchLibraryChromaDocumentLoader(db_path)

        def _row_factory(meta, path):
            shelf = (meta.get("shelf") or "").strip()
            return {
                "filename": meta.get("filename") or Path(path).name,
                "path": path,
                "title": meta.get("title") or Path(path).stem,
                "author": meta.get("author") or "",
                "topic": meta.get("topic") or "",
                "shelf": shelf,
            }

        return collect_metadata_rows(loader, _row_factory)


    @staticmethod
    @lru_cache(maxsize=1)
    def _document_library_metadata(db_path=DB_PATH) -> list[dict]:
        """
        Aggregate PDF document metadata from the Chroma collection, one row per file.
        """

        loader = DocumentLibraryLoader(db_path)

        def _row_factory(meta, path):
            shelf = (meta.get("shelf") or meta.get("tags") or "").strip()
            authors = meta.get("authors") or ""
            normalized_authors = [a.strip() for a in str(authors).split(",") if a.strip()]
            return {
                "filename": meta.get("filename") or Path(path).name,
                "path": path,
                "title": meta.get("title") or Path(path).stem,
                "authors": normalized_authors,
                "published_date": meta.get("published_date") or "",
                "topic": meta.get("topic") or "",
                "shelf": shelf,
            }

        return collect_metadata_rows(loader, _row_factory)
    
    
    @staticmethod
    @tool
    def repository_names() -> list[str]:
        """
        Obtain a list of repository names in the code repository document store.        

        Returns:
            list[str]
                The names of the repositories available in the code repository 
                document store.
        """

        base_path = Path(GITHUB_LOCAL_PATH)
        if not base_path.exists():
            logger.warning(f"GitHub local path '{base_path}' does not exist.")
            return []

        repo_names: list[str] = []
        for account_dir in sorted(p for p in base_path.iterdir() if p.is_dir()):
            for repo_dir in sorted(p for p in account_dir.iterdir() if p.is_dir()):
                repo_names.append(f"{account_dir.name}/{repo_dir.name}")

        return repo_names


    @staticmethod
    @tool(args_schema=RepositoryFilesInput)
    def filenames_for_repository(account: str, repository: str, max_results: int = 250) -> list[str]:
        """
        List filenames within a specific repository stored under .repos.

        Parameters
        ----------
        account: str
            GitHub account/owner name.
        repository: str
            Repository name.
        max_results: int
            Maximum number of filenames to return (capped at 5,000).

        Returns:
            list[str]
                Relative file paths within the requested repository.
        """

        base_path = Path(GITHUB_LOCAL_PATH)
        repo_path = base_path / account / repository

        if not repo_path.exists():
            logger.warning("Repository path does not exist: %s", repo_path)
            return []

        files: list[str] = []
        limit = max(1, min(max_results, 5000))

        for path in repo_path.rglob("*"):
            if path.is_file():
                files.append(str(path.relative_to(repo_path)))
                if len(files) >= limit:
                    break

        return files


    @staticmethod
    @tool(args_schema=ResearchLibraryMetadataListInput)
    def research_library_metadata_summary(
        max_results: int = 100, start_after: str | None = None
    ) -> list[dict]:
        """
        Return metadata (filename, title, author, topic, shelf) for research notes.

        Parameters
        ----------
        max_results: int
            Maximum number of metadata rows to return (default 100, capped at 1,000).
        start_after: str | None
            Filename or path to start after (pagination aid).
        """

        rows = DocumentStoreInfoAgent._research_library_metadata()
        return paginate_metadata_rows(rows, max_results, start_after)


    @staticmethod
    @tool(args_schema=DocumentLibraryMetadataListInput)
    def document_library_metadata_summary(
        max_results: int = 100, start_after: str | None = None
    ) -> list[dict]:
        """
        Return metadata (filename, title, authors, published date, topic, shelf) for PDF documents.

        Parameters
        ----------
        max_results: int
            Maximum number of metadata rows to return (default 100, capped at 1,000).
        start_after: str | None
            Filename or path to start after (pagination aid).
        """

        rows = DocumentStoreInfoAgent._document_library_metadata()
        return paginate_metadata_rows(rows, max_results, start_after)


    @staticmethod
    @tool(args_schema=ResearchLibraryTitleQueryInput)
    def research_library_titles_by_metadata(
        author: str | None = None,
        topic: str | None = None,
        shelf: str | None = None,
        limit: int = 25,
    ) -> list[dict]:
        """
        Return research note titles filtered by metadata fields.

        Parameters
        ----------
        author: str | None
            Case-insensitive substring match on the author name.
        topic: str | None
            Case-insensitive substring match on the topic.
        shelf: str | None
            Case-insensitive shelf match.
        limit: int
            Maximum number of results to return (default 25, capped at 200).
        """

        rows = DocumentStoreInfoAgent._research_library_metadata()
        if not rows:
            return []

        filtered = []
        author_token = author.lower() if author else None
        topic_token = topic.lower() if topic else None
        shelf_token = shelf.lower() if shelf else None

        for row in rows:
            row_author = (row.get("author") or "").lower()
            row_topic = (row.get("topic") or "").lower()
            row_shelf = (row.get("shelf") or "").lower()

            if author_token and author_token not in row_author:
                continue
            if topic_token and topic_token not in row_topic:
                continue
            if shelf_token and shelf_token != row_shelf:
                continue

            filtered.append(row)
            if len(filtered) >= limit:
                break

        return [
            {
                "title": item.get("title"),
                "filename": item.get("filename"),
                "author": item.get("author"),
                "topic": item.get("topic"),
                "shelf": item.get("shelf"),
            }
            for item in filtered
        ]


    @staticmethod
    @tool(args_schema=DocumentLibraryTitleQueryInput)
    def document_library_titles_by_metadata(
        author: str | None = None,
        topic: str | None = None,
        shelf: str | None = None,
        limit: int = 25,
    ) -> list[dict]:
        """
        Return PDF document titles filtered by metadata fields.

        Parameters
        ----------
        author: str | None
            Case-insensitive substring match on the author names.
        topic: str | None
            Case-insensitive substring match on the topic.
        shelf: str | None
            Case-insensitive shelf match.
        limit: int
            Maximum number of results to return (default 25, capped at 200).
        """

        rows = DocumentStoreInfoAgent._document_library_metadata()
        if not rows:
            return []

        filtered = []
        author_token = author.lower() if author else None
        topic_token = topic.lower() if topic else None
        shelf_token = shelf.lower() if shelf else None

        for row in rows:
            row_authors = [a.lower() for a in (row.get("authors") or [])]
            row_topic = (row.get("topic") or "").lower()
            row_shelf = (row.get("shelf") or "").lower()

            if author_token and not any(author_token in a for a in row_authors):
                continue
            if topic_token and topic_token not in row_topic:
                continue
            if shelf_token and shelf_token != row_shelf:
                continue

            filtered.append(row)
            if len(filtered) >= limit:
                break

        return [
            {
                "title": item.get("title"),
                "filename": item.get("filename"),
                "authors": item.get("authors"),
                "published_date": item.get("published_date"),
                "topic": item.get("topic"),
                "shelf": item.get("shelf"),
            }
            for item in filtered
        ]
