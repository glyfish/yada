from pathlib import Path
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate

from apps.agentic.core.constants import (PROGRAMMING_LANGUAGE_MAP)
from apps.agentic.core.agents.file_chroma_rag_agent import FileChromaRAGAgent
from apps.agentic.core.document_loaders.github_document_loader import GitHubChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentGrade(BaseModel):
    """Binary score for relevance check."""
    binary_score: str = Field(description="Relevance score 'yes' or 'no'")


class CodeRepoAgent(FileChromaRAGAgent):
    """
    Code Repository Agent that uses a vector store index of GitHub repositories to answer questions about code.
    It is designed to handle queries related to code, repositories, files, functions, and classes
    stored in the indexed GitHub repositories.
    """

    QUERY_FILTERS =  """
        **code_repository_search Query Filters**
        The agent supports the following query filters to refine searches:
        - account: GitHub account name (e.g., account:troystribling)
        - repo: Repository name (e.g., repo:zgomot)
        - ext: File extension (e.g., ext:rb, ext:js, ext:py)
        - before: Date to filter commits before (e.g., before:2014-01-01)
        - after: Date to filter commits after (e.g., after:2014-01-01)
        
        **Example Queries Using Filter**
        - account:troystribling repo:zgomot ext:rb Where is MIDI output handled?
        - account:troystribling repo:zgomot ext:rb before:2014-01-01 Where is MIDI output handled?
        - account:troystribling repo:zgomot ext:rb after:2014-01-01 Where is MIDI output handled?
    """


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
            "You are searching Troy Stribling’s code (i.e. my code) in his indexed GitHub repositories vector store to answer "
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
        if not top_files:
            return ""

        files_section = ""
        for d in top_files:
            if not d or not getattr(d, "page_content", None):
                continue

            metadata = d.metadata or {}
            acct   = metadata.get("account")
            repo   = metadata.get("repo")
            commit = metadata.get("commit")
            ts     = metadata.get("commit_ts")
            path   = metadata.get("path")

            content = d.page_content or ""
            if len(content) > 30000:
                content = content[:30000] + "\n\n<!-- truncated -->\n"

            name_lower = Path(path).name.lower() if path else ""
            ext_path = Path(path).suffix.lower() if path else ""
            ext = (metadata.get("ext") or ext_path or "").lower()

            if not ext:
                if name_lower == "makefile":
                    lang = "makefile"
                elif name_lower == "dockerfile":
                    lang = "dockerfile"
                else:
                    lang = "plaintext"
            else:
                lang = PROGRAMMING_LANGUAGE_MAP.get(ext, "plaintext")

            header = f"### {path}\n{acct}/{repo}@{commit}, {ts}"
            files_section += ("\n\n-----\n\n#\n" + header + f"\n\n```{lang}\n{content}\n```\n")

        return files_section
