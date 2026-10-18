from pathlib import Path
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from apps.agentic.core.constants import (PROGRAMMING_LANGUAGE_MAP)
from apps.agentic.core.agents.file_chroma_rag_agent import FileChromaRAGAgent
from apps.agentic.core.document_loaders.github_document_loader import GitHubChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class CodeRepoAgent(FileChromaRAGAgent):
    """
    Code Repository Agent that uses a vector store index of GitHub repositories to answer questions about code.
    It is designed to handle queries related to code, repositories, files, functions, and classes
    stored in the indexed GitHub repositories.
    """

    # Prepended to every retrieved chunk so the grader and the generating model can
    # see which file a chunk came from -- the _generate prompt below instructs the
    # model to cite exactly these, and until now none of them reached it. `commit` is
    # on 99.87% of chunks rather than 100%; missing keys are skipped, not an error.
    DOCUMENT_HEADER_KEYS = (
        ("repo", "Repository"),
        ("file_path", "File path"),
        ("branch", "Branch"),
        ("ext", "Extension"),
        ("commit", "Commit"),
    )

    QUERY_FILTERS =  """
        **code_repository_search Query Filters**
        The agent supports the following query filters to refine searches:
        - account: GitHub account name (e.g., account:troystribling)
        - repo: Repository name (e.g., repo:BlueCap)
        - ext: File extension (e.g., ext:rb, ext:js, ext:py)
        - before: Date to filter commits before (e.g., before:2014-01-01)
        - after: Date to filter commits after (e.g., after:2014-01-01)
        
        **Example Queries Using Filter**
        - repo:zgomot In my code where is MIDI output handled?
        - account:troystribling repo:zgomot ext:rb before:2014-01-01 In my code where is MIDI output handled?
        - account:troystribling repo:zgomot ext:rb after:2014-01-01 In my code where is MIDI output handled?
    """


    @classmethod
    async def create(cls, query=None) -> "CodeRepoAgent":
        return cls(query)

    def __init__(self, query):
        tool_name = "github_agent_tool"
        
        tool_description = (
            "Troy Stribling Code Retriever"
            "Description: Search and retrieve content from Troy Stribling’s GitHub repositories "
            "(i.e. my GitHub Repositories) indexed in the vector store. "
            "The vector store contains various types of content (code, READMEs, docs, issues, commit messages). " 
            "Use this for any query about 'my code', 'my repo(s)', or requests for specific files/functions."
        )

        super().__init__(tool_name, tool_description, GitHubChromaDocumentLoader(), query)

        self._generate_prompt = ChatPromptTemplate.from_messages([("human", """                                                                   
        You are an expert assistant answering questions about Troy Stribling's code repositories.
        Use the retrieved context below to answer the question. Each chunk is preceded by a header
        carrying its Repository, File path, Branch, Extension and Commit. Deduce the programming
        language from the file extension.

        When answering:
        - Reference the file path and repository name when discussing specific code
        - Format code snippets in fenced code blocks with the appropriate language identifier
        - Cite the commit hash or branch when version context is relevant
        - If you don't know the answer from the context, say so clearly

        Question: {question}
        Context: {context}
        Answer:
        """
        )])


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
