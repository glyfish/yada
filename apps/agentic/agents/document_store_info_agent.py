from pydantic import BaseModel, Field
from typing import Dict
import shortuuid

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

import os
import sys
import numpy
from functools import lru_cache

from pathlib import Path

from apps.agentic.core.agents.tool_agent import ToolAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH, DB_PATH
from apps.agentic.core.document_loaders.research_note_document_loader import (
    ResearchNoteChromaDocumentLoader,
)

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


class ResearchNoteMetadataListInput(BaseModel):
    """Schema for slicing research note metadata rows."""

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


class ResearchNoteTitleQueryInput(BaseModel):
    """Schema for filtering research note titles by metadata."""

    author: str | None = Field(
        default=None,
        description="Author name to filter by (case-insensitive substring match).",
    )
    topic: str | None = Field(
        default=None,
        description="Topic text to filter by (case-insensitive substring match).",
    )
    tag: str | None = Field(
        default=None,
        description="Require that the note contains this tag (case-insensitive).",
    )
    limit: int = Field(
        default=25,
        ge=1,
        le=200,
        description="Maximum number of titles to return (default 25).",
    )



class DocumentStoreInfoAgent(ToolAgent):
    """
    Handle requests for information about document libraries.
    """

    def __init__(self):
        tools = [
            DocumentStoreInfoAgent.repository_names,
            DocumentStoreInfoAgent.filenames_for_repository,
            DocumentStoreInfoAgent.research_note_metadata_summary,
            DocumentStoreInfoAgent.research_note_titles_by_metadata,
        ]
        tool_node_name = "document_info_tool_node"

        super().__init__(tools, tool_node_name)

    
    def create_prompt(self):
        """
        Create the prompt template for the BarChartAgent agent.
        This defines how the model should interpret the messages and what it should do.
        """
    
        system_prompt = """
        You are an expert in retrieving information about the contents of documents available in all
        the document stores. The tools allow you to:
        - List repository names and filenames for code repositories.
        - Summarize metadata for research notes, including filename, title, author, topic, and tags.
        - Filter research note titles using author/topic/tag metadata.
        Call the appropriate tool when the user asks about any of these data sources.
        """

        logger.debug(f"DocumentInfoAgent Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in plain text."),
        ])


    @staticmethod
    @lru_cache(maxsize=1)
    def _research_note_metadata(db_path=DB_PATH) -> list[dict]:
        """
        Aggregate research note metadata from the Chroma collection, one row per file.
        """

        loader = ResearchNoteChromaDocumentLoader(db_path)
        collection = getattr(loader.vectorstore, "_collection", None)
        if collection is None:
            logger.warning("Research note vector store collection unavailable.")
            return []

        try:
            result = collection.get(include=["metadatas"], limit=100_000)
        except Exception as exc:
            logger.error("Failed to read research note metadata: %s", exc)
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

            tags = meta.get("tags") or ""
            normalized_tags = [t.strip() for t in str(tags).split(",") if t.strip()]

            aggregated[path] = {
                "filename": meta.get("filename") or Path(path).name,
                "path": path,
                "title": meta.get("title") or Path(path).stem,
                "author": meta.get("author") or "",
                "topic": meta.get("topic") or "",
                "tags": normalized_tags,
            }

        return list(aggregated.values())
    
    
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
    @tool(args_schema=ResearchNoteMetadataListInput)
    def research_note_metadata_summary(
        max_results: int = 100, start_after: str | None = None
    ) -> list[dict]:
        """
        Return metadata (filename, title, author, topic, tags) for research notes.

        Parameters
        ----------
        max_results: int
            Maximum number of metadata rows to return (default 100, capped at 1,000).
        start_after: str | None
            Filename or path to start after (pagination aid).
        """

        rows = DocumentStoreInfoAgent._research_note_metadata()
        if not rows:
            return []

        rows = sorted(rows, key=lambda r: (r.get("filename") or r.get("path") or "").lower())

        start_index = 0
        if start_after:
            token = start_after.lower()
            for idx, row in enumerate(rows):
                filename = (row.get("filename") or "").lower()
                path = (row.get("path") or "").lower()
                if token == filename or token == path:
                    start_index = idx + 1
                    break

        end_index = min(start_index + max_results, len(rows))
        return rows[start_index:end_index]


    @staticmethod
    @tool(args_schema=ResearchNoteTitleQueryInput)
    def research_note_titles_by_metadata(
        author: str | None = None,
        topic: str | None = None,
        tag: str | None = None,
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
        tag: str | None
            Case-insensitive tag match (must be present in tags list).
        limit: int
            Maximum number of results to return (default 25, capped at 200).
        """

        rows = DocumentStoreInfoAgent._research_note_metadata()
        if not rows:
            return []

        filtered = []
        author_token = author.lower() if author else None
        topic_token = topic.lower() if topic else None
        tag_token = tag.lower() if tag else None

        for row in rows:
            row_author = (row.get("author") or "").lower()
            row_topic = (row.get("topic") or "").lower()
            row_tags = [t.lower() for t in (row.get("tags") or [])]

            if author_token and author_token not in row_author:
                continue
            if topic_token and topic_token not in row_topic:
                continue
            if tag_token and tag_token not in row_tags:
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
                "tags": item.get("tags"),
            }
            for item in filtered
        ]
