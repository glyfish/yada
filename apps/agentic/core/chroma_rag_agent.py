from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence, Any
import re

from pydantic import BaseModel, Field
from typing import Dict

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langgraph.prebuilt import tools_condition
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import ToolNode

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm

from lib.logger import get_logger

logger = get_logger("YADA")


class ChromaRAGAgent(ABC):

    def __init__(self, tool_name: str, tool_description: str, document_prompt: str, db_name: str, collection_name: str, 
                 query: Dict[str, Any]={}, db_path: str=".db"):
        self.tool_name = tool_name
        self.tool_description = tool_description
        self._query = query

        self._llm = build_llm()
        self._doc_loader = ChromaDocumentLoader(db_name, collection_name, db_path)

        logger.debug(f"Chroma query: {query}")

        self._vectorstore = self._doc_loader.vectorstore
        self._retriever = self._vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 8, "fetch_k": 40, "filter": query}
        )

        self._retriever_tool = create_retriever_tool(
            self._retriever,
            tool_name,
            tool_description,
            document_prompt=document_prompt,
            document_separator="\n\n-----\n\n",)
        self._tools = [self._retriever_tool]
        self._retriever_tool_node = ToolNode(self._tools)
        self._tooled_llm = self._llm.bind_tools(self._tools)
        self._agent = self._create_agent()


    @property
    def doc_loader(self):
        """
        Get the document loader for the GitHub agent.
        """
        return self._doc_loader


    @property
    def retriever(self):
        """
        Get the retriever for the GitHub agent.
        """
        return self._retriever
    

    @property
    def tools(self):
        """
        Get the tools available to the GitHub agent.
        """
        return self._tools


    @property
    def retriever_tool(self):
        """
        Get the retriever tool for the GitHub agent.
        """
        return self._retriever_tool


    @property
    def vectorstore(self):
        """
        Get the vector store for the GitHub agent.
        """
        return self._vectorstore


    @property
    def llm(self):
        """
        Get the language model used by the agent.
        """

        return self._llm
    

    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """

        return self._agent


    @property
    def tooled_llm(self):
        """
        Get the language model bound with tools.
        """

        return self._tooled_llm


    @property
    def retriever_tool_node(self):
        """
        Get the retriever tool node.
        """

        return self._retriever_tool_node


    @property
    def query(self):
        """
        Get the query filter used by the agent.
        """

        return self._query

    
    async def _invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        """
        Invoke the agent with the current state.
        """

        messages = state["messages"]

        try:
            result = await self.tooled_llm.ainvoke(messages)
            return {"messages": [result]}
        except Exception as e:
            logger.error(f"Error invoking model: {e}")
            return {"messages": [f"Error: {e}"]}
    

    def _generate(self, state):
        """
        Generate answer

        Args:
            state (messages): The current state

        Returns:
            dict: The answer to the question.
        """

        messages = state["messages"]
        question = messages[0].content
        last_message = messages[-1]

        docs = last_message.content

        # Build full-file section from the top retrieved file(s)
        try:
            hits = self.retriever.invoke(question)

            # Deduplicate by file path and pick the top one
            seen, top_files = set(), []
            for d in hits:
                path = d.metadata.get("path")
                if not path or path in seen:
                    continue
                seen.add(path)
                top_files.append(d)
                if len(top_files) >= 1:
                    break

            files_section = self.read_file(top_files)
        except Exception as e:
            logger.error(f"Full-file append skipped because of error: {e}")


        prompt = hub.pull("rlm/rag-prompt")
        logger.debug(f"Code repository generate prompt: {prompt}")

        llm = build_llm()

        rag_chain = prompt | llm | StrOutputParser()
        answer_text = rag_chain.invoke({"context": docs, "question": question})
        final_text = answer_text + (files_section if files_section else "")
        return {"messages": [final_text]}    


    def _retrieve(self, state):
        messages = state["messages"]
        question = messages[0].content if hasattr(messages[0], "content") else str(messages[0])
        try:
            hits = self.retriever.invoke(question)
        except Exception as e:
            logger.error(f"Retriever error: {e}")
            return {"messages": [HumanMessage(content=f"Retriever error: {e}")]}
        sep = "\n\n-----\n\n"
        parts = []
        for d in hits:
            md = d.metadata or {}
            header = f"{md.get('account','')}/{md.get('repo','')}@{md.get('commit','')} — {md.get('path','')} — {md.get('commit_ts','')}".strip(" —")
            parts.append(f"{header}\n\n{d.page_content}")
        context = sep.join(parts) if parts else "(no results)"
        return {"messages": [HumanMessage(content=context)]}


    def _create_agent(self):
        """
        Create a tool node for the agent.

        Args:
            agent (StateGraph): The agent state graph.
            name (str): The name of the tool node.

        Returns:
            ToolNode: The created tool node.
        """

        graph = (
            StateGraph(WorkerState)
            .add_node("retrieve", self._retrieve)
            .add_node("generate", self._generate)
            .add_edge(START, "retrieve")
            .add_edge("retrieve", "generate") 
            .add_edge("generate", END)
        )
        return graph.compile()


    @abstractmethod
    def read_file(self, top_files):
        """
        Read the contents of the specified files.
        """

        raise NotImplementedError("Subclasses must implement the read_file method to read files.")


    @staticmethod
    def extract_snippet(text: str, needle: str, context_lines: int = 12) -> str | None:
        """Return a code excerpt around the first match of `needle` (regex)."""
        lines = text.splitlines()
        # join with newlines to search reliably
        joined = "\n".join(lines)
        m = re.search(needle, joined, re.IGNORECASE)
        if not m:
            return None
        # map char offsets to line numbers
        upto = joined[:m.start()]
        start_line = upto.count("\n")
        lo = max(0, start_line - context_lines)
        hi = min(len(lines), start_line + context_lines)
        snippet = "\n".join(lines[lo:hi])
        return snippet