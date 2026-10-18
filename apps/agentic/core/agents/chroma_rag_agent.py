from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, cast

from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.llm_factory import agent_llm_model, scoring_llm_model
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.constants import RAG_SCORE_THRESHOLD
from apps.agentic.core.output_style import OUTPUT_STYLE

from lib.logger import get_logger

logger = get_logger("YADA")


def _normalize_chroma_filter(query: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Ensure a ChromaDB where-filter is valid. Returns None when query is empty
    so the caller can omit the filter entirely (ChromaDB rejects an empty where dict).
    Wraps flat multi-key dicts in $and (ChromaDB 1.0.x requires exactly one top-level operator).
    """
    if not query:
        return None
    if any(k.startswith("$") for k in query):
        return query
    if len(query) > 1:
        return {"$and": [{k: v} for k, v in query.items()]}
    return query


class DocumentGrade(BaseModel):
    """Binary relevance score for a retrieved document chunk."""
    relevant: bool = Field(description="True if the document is relevant to the question")


class ChromaRAGAgent(ABC):

    #: (metadata key, label) pairs prepended to every retrieved chunk, for the keys
    #: that store actually carries. Both the grader and the generating model read
    #: this header, so it is what lets them tell *where* a chunk came from.
    #:
    #: History worth knowing: a header like this existed from 78a446b (2025-09-14)
    #: and was deleted by a two-line edit in 9573310 (2025-11-30, "added metadata to
    #: file when document is added" -- added at index time, removed at read time).
    #: Nothing replaced it, and ef53ff5 (2026-03-01) then pointed the grader at the
    #: stripped text. Measured cost on one file-location query: the grader kept 2/8
    #: chunks without the header and 4/8 with it, and the model, told by its own
    #: prompt to "cite the commit hash or branch", guessed file paths instead.
    #:
    #: Missing keys are skipped, so partial-coverage fields are safe to list.
    DOCUMENT_HEADER_KEYS: tuple[tuple[str, str], ...] = ()

    def __init__(self, retriever_tool_name: str, retriever_tool_description: str,
                 doc_loader: ChromaDocumentLoader, query: Optional[Dict[str, Any]] = None, retriever_k=8, retriever_fetch_k=40,
                 score_threshold: Optional[float]=RAG_SCORE_THRESHOLD):
        self.retriever_tool_name = retriever_tool_name
        self.retriever_tool_description = retriever_tool_description
        self._query = query

        self._llm = agent_llm_model()
        self._doc_loader = doc_loader

        normalized_query = _normalize_chroma_filter(query)
        search_kwargs: dict = {"k": retriever_k, "fetch_k": retriever_fetch_k}
        if normalized_query is not None:
            search_kwargs["filter"] = normalized_query
        if score_threshold is not None:
            search_kwargs["score_threshold"] = score_threshold

        self._vectorstore = self._doc_loader.vectorstore
        self._retriever = self._vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs=search_kwargs
        )

        # Chroma metadata filters are exact equality, so a filter that is merely
        # close matches NOTHING rather than matching less -- authors:"W. H. Matthaeus"
        # against a store holding only comma-joined full author strings returns 0 of
        # 4,875, while the same query unfiltered puts the right paper at rank 1. The
        # agent then reports "no relevant documents", which the user cannot tell apart
        # from an empty corpus. Keep an unfiltered retriever so _retrieve can degrade
        # instead of failing closed.
        self._unfiltered_retriever = (
            self._vectorstore.as_retriever(
                search_type="mmr",
                search_kwargs={k: v for k, v in search_kwargs.items() if k != "filter"},
            )
            if normalized_query is not None
            else None
        )

        # Inline copy of the canonical hub prompt "rlm/rag-prompt": pulling public
        # hub prompts is disabled by default (untrusted serialized objects) and the
        # pull added a network dependency at agent-creation time.
        self._generate_prompt = ChatPromptTemplate.from_messages([
            ("human",
             "You are an assistant for question-answering tasks. Use the following "
             "pieces of retrieved context to answer the question. If you don't know "
             "the answer, just say that you don't know. Use three sentences maximum "
             "and keep the answer concise.\n"
             "Question: {question} \nContext: {context} \nAnswer:"),
        ])
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

        prompt_messages = prompt.format_messages(context=docs, question=question)
        if prompt_messages and isinstance(prompt_messages[0], SystemMessage):
            prompt_messages[0] = SystemMessage(content=f"{prompt_messages[0].content}\n\n{OUTPUT_STYLE}")
        else:
            prompt_messages.insert(0, SystemMessage(content=OUTPUT_STYLE))
        response = (self.llm | StrOutputParser()).invoke(prompt_messages)
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

        def header_for(metadata: dict) -> str:
            fields = [f"{label}: {metadata.get(key)}"
                      for key, label in self.DOCUMENT_HEADER_KEYS
                      if metadata.get(key) not in (None, "")]
            return " | ".join(fields)

        if not hits and self._unfiltered_retriever is not None:
            logger.warning(
                f"Filter matched nothing ({self._query!r}); retrying unfiltered."
            )
            try:
                hits = self._unfiltered_retriever.invoke(question)
            except Exception as e:
                logger.error(f"Unfiltered retry error: {e}")
            else:
                logger.info(f"Unfiltered retry retrieved {len(hits)} documents.")

        sep = "\n\n-----\n\n"
        parts = []
        for i, d in enumerate(hits, 1):
            header = header_for(d.metadata or {})
            parts.append(f"Document {i}:\n{header}\n---\n{d.page_content}"
                         if header else f"Document {i}:\n{d.page_content}")

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


