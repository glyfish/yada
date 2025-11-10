from pydantic import BaseModel, Field
from typing import Dict
import shortuuid

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

import os
import sys
import numpy

from pathlib import Path

from apps.agentic.core.agents.tool_agent import ToolAgent
from apps.agentic.core.constants import GITHUB_LOCAL_PATH

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


class DocumentStoreInfoAgent(ToolAgent):
    """
    Handle requests for information about document libraries.
    """

    def __init__(self):
        tools = [
            DocumentStoreInfoAgent.repository_names,
            DocumentStoreInfoAgent.filenames_for_repository,
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
        the document stores. The types of information you can collect is enabled by the tools you can access.
        The tools will allow you to list the file names, document titles, authors and other information
        available in the document metadata.
        """

        logger.debug(f"DocumentInfoAgent Agent prompt: {system_prompt}")

        return ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            ("system", "If you choose to call a tool, do so; otherwise, provide your findings in plain text."),
        ])
    
    
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
