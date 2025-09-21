from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence
from pathlib import Path

from pydantic import BaseModel, Field
from typing import Dict

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate
from langgraph.prebuilt import tools_condition
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import ToolNode

from apps.agentic.core.constants import GITHUB_DB_NAME, GITHUB_COLLECTION_NAME, GITHUB_LOCAL_PATH
from apps.agentic.core.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.github_document_loader import GitHubChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentGrade(BaseModel):
    """Binary score for relevance check."""
    binary_score: str = Field(description="Relevance score 'yes' or 'no'")


class CodeRepoAgent(ChromaRAGAgent):

    def __init__(self, query):
        tool_name = "github_agent_tool"
        tool_description = (
            "Troy Stribling Code Retriever"
            "Description: Search and retrieve content from Troy Stribling’s GitHub repositories "
            "(i.e. my GitHub Repositories) indexed in the vector store. "
            "The vector store contains various types of content (code, READMEs, docs, issues, commit messages). " 
            "Use this for any query about 'my code', 'my repo(s)', or requests for specific files/functions."
        )

        prompt_template = (
            "You are searching Troy Stribling’s code (i.e. my code) in his indexed GitHub repositories.vector store to answer "
            "requests about his code. Information about the code can be found in the metadata attached to each file. "
            "Following is a description of the metadata. The programming language should be deduced from the file extension."
            "- GitHub account: {metadata[account]}"
            "- Repository name: {metadata[repo]}"
            "- Git branch name: {metadata[branch]}"
            "- File path: {metadata[path]}"
            "- File extension: {metadata[ext]}"
            "- Programming language: {programming_language}"
            "- Latest Commit: {metadata[commit]}"
            "---"
            "{page_content}"
        )
        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, GitHubChromaDocumentLoader(), query)


    def read_file(self, top_files):
        files_section = ""
        for d in top_files:
            acct   = d.metadata.get("account")
            repo   = d.metadata.get("repo")
            commit = d.metadata.get("commit")
            ts     = d.metadata.get("commit_ts")
            path   = d.metadata.get("path")

            # Try reading from the local filesystem clone
            file_path = Path(GITHUB_LOCAL_PATH) / (acct or "") / (repo or "") / (path or "")
            full = None
            try:
                full = file_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                full = None

            if not full:
                continue

            if len(full) > 30000:
                full = full[:30000] + "\n\n<!-- truncated -->\n"

            # Derive extension from metadata or file path and map to a markdown fence language
            name_lower = Path(path).name.lower() if path else ""
            ext_path = Path(path).suffix.lower() if path else ""
            ext = (d.metadata.get("ext") or ext_path or "").lower()

            lang_map = {
                ".py": "python",
                ".rb": "ruby",
                ".rs": "rust",
                ".js": "javascript",
                ".ts": "typescript",
                ".jsx": "jsx",
                ".tsx": "tsx",
                ".go": "go",
                ".java": "java",
                ".kt": "kotlin",
                ".c": "c",
                ".h": "c",
                ".cpp": "cpp",
                ".hpp": "cpp",
                ".cs": "csharp",
                ".php": "php",
                ".swift": "swift",
                ".scala": "scala",
                ".sql": "sql",
                ".sh": "bash",
                ".json": "json",
                ".toml": "toml",
                ".ini": "ini",
                ".conf": "ini",
                ".yml": "yaml",
                ".yaml": "yaml",
                ".md": "markdown",
                ".mdx": "markdown",
                ".rdoc": "markdown",
                ".html": "html",
                ".xml": "xml",
                ".css": "css",
                ".txt": "text",
            }

            if not ext:
                if name_lower == "makefile":
                    lang = "makefile"
                elif name_lower == "dockerfile":
                    lang = "dockerfile"
                else:
                    lang = "plaintext"
            else:
                lang = lang_map.get(ext, "plaintext")

            header = f"### {path}\n{acct}/{repo}@{commit}, {ts}"
            files_section += ("\n\n-----\n\n#\n" + header + f"\n\n```{lang}\n{full}\n```\n")

        return files_section
