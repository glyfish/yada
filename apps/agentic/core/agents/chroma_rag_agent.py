from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, cast

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate
from langchain.tools.retriever import create_retriever_tool
from pydantic import BaseModel, Field

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.llm_factory import agent_llm_model, scoring_llm_model
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.constants import RAG_SCORE_THRESHOLD
from langsmith.run_helpers import traceable

from lib.logger import get_logger

logger = get_logger("YADA")


def _normalize_chroma_filter(query: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensure a ChromaDB where-filter is valid. A flat dict with multiple keys
    is not accepted by ChromaDB — it requires a logical operator ($and/$or).
    This wraps any such flat dict in $and so the filter works regardless of
    how the caller constructed it.
    """
    if not query:
        return query
    if any(k.startswith("$") for k in query):
        return query
    if len(query) > 1:
        return {"$and": [{k: v} for k, v in query.items()]}
    return query


class DocumentGrade(BaseModel):
    """Binary relevance score for a retrieved document chunk."""
    relevant: bool = Field(description="True if the document is relevant to the question")


class ChromaRAGAgent(ABC):

    def __init__(self, retriever_tool_name: str, retriever_tool_description: str, document_prompt: PromptTemplate,
                 doc_loader: ChromaDocumentLoader, query: Dict[str, Any]={}, retriever_k=8, retriever_fetch_k=40,
                 score_threshold: Optional[float]=RAG_SCORE_THRESHOLD):
        self.retriever_tool_name = retriever_tool_name
        self.retriever_tool_description = retriever_tool_description
        self._query = query

        self._llm = agent_llm_model()
        self._doc_loader = doc_loader

        normalized_query = _normalize_chroma_filter(query)
        search_kwargs = {"k": retriever_k, "fetch_k": retriever_fetch_k, "filter": normalized_query}
        if score_threshold is not None:
            search_kwargs["score_threshold"] = score_threshold

        self._vectorstore = self._doc_loader.vectorstore
        self._retriever = self._vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs=search_kwargs
        )

        self._retriever_tool = create_retriever_tool(
            self._retriever,
            retriever_tool_name,
            retriever_tool_description,
            document_prompt=document_prompt,
            document_separator="\n\n-----\n\n",)
        self._tools = [self._retriever_tool]
        self._tooled_llm = self._llm.bind_tools(self._tools)
        self._generate_prompt = hub.pull("rlm/rag-prompt")
        self._grader_llm = scoring_llm_model().with_structured_output(DocumentGrade)
        self._grade_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are a relevance grader. Assess whether the retrieved document contains "
             "information that is useful for answering the question. "
             "Keyword or semantic relevance is sufficient — the document does not need to fully answer the question. "
             "Set relevant=true if the document is useful, relevant=false otherwise."),
            ("human", "Question: {question}\n\nDocument:\n{document}"),
        ])
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
    def query(self):
        """
        Get the query filter used by the agent.
        """

        return self._query


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
        docs = messages[-1].content

        prompt = self._generate_prompt
        logger.debug(f"RAG Agent generate prompt: {prompt}")

        rag_chain = prompt | self.llm | StrOutputParser()
        response = rag_chain.invoke({"context": docs, "question": question})
        full_response = f"{response}\n\n---\n\n**Retrieved Documents:**\n\n{docs}"
        return {"messages": [AIMessage(content=full_response)]}
    

    def _retrieve(self, state):
        messages = state["messages"]
        question = messages[0].content if hasattr(messages[0], "content") else str(messages[0])
        try:
            hits = self.retriever.invoke(question)
        except Exception as e:
            logger.error(f"Retriever error: {e}")
            return {"messages": [SystemMessage(content=f"Retriever error: {e}")]}

        logger.info(f"Retrieved {len(hits)} documents for query: {question}")

        sep = "\n\n-----\n\n"
        parts = []
        for i, d in enumerate(hits, 1):
            parts.append(f"Document {i}:\n{d.page_content}")

        context = sep.join(parts) if parts else "(no results)"
        return {"messages": [SystemMessage(content=context)]}


    def _grade_documents(self, state):
        """
        Grade retrieved document chunks for relevance and filter out irrelevant ones.

        Args:
            state: The current graph state. Reads the question from messages[0]
                   and the retrieved context from messages[-1] (set by _retrieve).

        Returns:
            dict: Updated messages with a SystemMessage containing only relevant chunks.
        """

        messages = state["messages"]
        question = messages[0].content
        docs_content = messages[-1].content

        sep = "\n\n-----\n\n"
        chunks = [c for c in docs_content.split(sep) if c.strip()]

        if not chunks:
            return {"messages": [SystemMessage(content="(no results)")]}

        grader = self._grade_prompt | self._grader_llm
        relevant = []
        for chunk in chunks:
            try:
                result = cast(DocumentGrade, grader.invoke({"question": question, "document": chunk}))
                if result.relevant:
                    relevant.append(chunk)
            except Exception as e:
                logger.warning(f"Grading error, keeping chunk: {e}")
                relevant.append(chunk)

        logger.info(f"Document grading: {len(relevant)}/{len(chunks)} chunks passed")
        context = sep.join(relevant) if relevant else "(no relevant results found)"
        return {"messages": [SystemMessage(content=context)]}


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
            .add_node("grade", self._grade_documents)
            .add_node("generate", self._generate)
            .add_edge(START, "retrieve")
            .add_edge("retrieve", "grade")
            .add_edge("grade", "generate")
            .add_edge("generate", END)
        )
        return graph.compile(checkpointer=checkpointer)


    @traceable(run_type="chain", name="ChromaRAGAgent._invoke_model")
    async def _invoke_model(self, state: WorkerState, config=None) -> dict[str, Any]:
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
