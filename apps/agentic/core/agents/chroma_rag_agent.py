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


class ChunkScore(BaseModel):
    """Relevance of one retrieved chunk, scored relative to the others in the batch."""
    index: int = Field(description="The document's number, exactly as labelled 'Document N:' in the context")
    score: float = Field(description="Relevance from 0.0 (unrelated) to 1.0 (directly answers the question)")


class ChunkRanking(BaseModel):
    """Scores for every chunk in one batch, so they can be compared against each other."""
    scores: list[ChunkScore] = Field(description="One entry per document, in any order")


class ChromaRAGAgent(ABC):

    #: (metadata key, label) pairs prepended to every retrieved chunk, for the keys
    #: that store actually carries. Both the grader and the generating model read
    #: this header, so it is what lets them tell *where* a chunk came from.
    #:
    #: History worth knowing: a header like this existed from 78a446b (2025-09-14)
    #: and was deleted by a two-line edit in 9573310 (2025-11-30, "added metadata to
    #: file when document is added" -- added at index time, removed at read time).
    #: Nothing replaced it, and ef53ff5 (2026-03-01) then pointed the grader at the
    #: stripped text. Measured on claude-haiku-4-5 with one file-location query: the
    #: ranker scored 5/8 chunks through without the header and 6/8 with it (gaining
    #: lib/zgomot/midi/note.rb, losing nothing), and the model, told by its own prompt
    #: to "cite the commit hash or branch", guessed file paths instead of citing them.
    #:
    #: Missing keys are skipped, so partial-coverage fields are safe to list.
    DOCUMENT_HEADER_KEYS: tuple[tuple[str, str], ...] = ()

    #: Keep chunks scoring at least this fraction of the best score in the batch.
    #: Relative, never absolute -- see the note in _grade_documents. 1.0 would keep
    #: only ties with the best; 0.0 keeps everything the ranker saw.
    #:
    #: FITTED 2026-10-24, not guessed. 63 labelled research_library queries (each
    #: document's `topic` description as the query, that document as ground truth),
    #: scored by F2 -- recall weighted over precision, because dropping a needed chunk
    #: costs more than admitting a spare one. 0.55 is a genuine local maximum:
    #:     floor  0.45   0.50   0.55   0.60   0.65
    #:     F2     0.796  0.802  0.815  0.801  0.779
    #: 24 of 63 queries keep a different set at 0.55 than at 0.50, and 0.55 wins in
    #: 97.0% of 2,000 bootstrap resamples. Alternatives measured on the same vectors:
    #: elbow/largest-gap 0.745, top-5 0.717, absolute-0.5 0.805.
    #:
    #: The set is synthetic -- topic sentences are curator-written, not how anyone asks --
    #: so this is a first fit. Revalidate against real queries in §1.4.
    grade_relative_floor: float = 0.55

    #: Hard cap on chunks passed to the generating model, applied after the floor.
    grade_top_n: int = 8

    #: If even the best chunk scores below this, nothing retrieved is relevant and
    #: the honest answer is to return nothing. This one IS absolute, and that is not
    #: a contradiction of the relative floor above: "how many of these candidates
    #: are worth keeping" is a comparative question, "is any of this about the
    #: question at all" is not. Unlike RAG_SCORE_THRESHOLD -- an absolute cutoff on
    #: cosine distance, whose observed band is a narrow ~0.51-0.65 -- this applies
    #: to an LLM-assigned 0-1 relevance score, where 0.0 means the model was asked
    #: about Kubernetes and shown Ruby MIDI code.
    grade_min_score: float = 0.15

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
        # One call that sees every chunk at once, rather than one yes/no call per
        # chunk. The old design asked "is this useful?" of each chunk in isolation,
        # which cannot compare them: it could reject the best chunk available, and
        # could reject all of them, which is the confident-empty answer users hit.
        # It also cost one LLM call per chunk.
        self._grader_llm = scoring_llm_model().with_structured_output(ChunkRanking)
        self._grade_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You rank retrieved documents by how well they help answer a question. "
             "You will be given every candidate at once; score them against each other, "
             "not against an absolute standard. Each document is labelled 'Document N:' "
             "and begins with a metadata header giving its source — a document's origin "
             "is evidence of relevance, so weigh it alongside the text. "
             "Score 1.0 for a document that directly answers the question, around 0.5 for "
             "one that is related but incidental, and near 0.0 for one that is unrelated. "
             "Return exactly one score for every document you are given, using its N."),
            ("human", "Question: {question}\n\nDocuments:\n{documents}"),
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

        try:
            ranking = cast(ChunkRanking, (self._grade_prompt | self._grader_llm).invoke(
                {"question": question, "documents": docs_content}))
            scored = {s.index: s.score for s in ranking.scores if 1 <= s.index <= len(chunks)}
        except Exception as e:
            # Ranking is an optimisation, not a gate. If it fails, hand the model
            # everything retrieved rather than nothing.
            logger.warning(f"Ranking failed, passing all {len(chunks)} chunks: {e}")
            return {"messages": [SystemMessage(content=sep.join(chunks))]}

        # A chunk the ranker omitted scores 0.0 rather than being silently dropped.
        ranked = sorted(((scored.get(i, 0.0), i, c) for i, c in enumerate(chunks, 1)),
                        key=lambda t: (-t[0], t[1]))

        # Relative floor, deliberately not absolute. RAG_SCORE_THRESHOLD is an
        # absolute cutoff and is unusable for exactly this reason: the observed
        # relevance band is narrow (~0.51-0.65), so 0.50 admits everything and 0.52
        # empties a working query. Keeping everything within a fraction of the BEST
        # observed score adapts to whatever the distribution happens to be, and
        # cannot return nothing -- the top chunk always clears its own floor. That
        # is the property the old binary gate lacked: it answered N independent
        # yes/no questions and could answer "no" to all of them.
        best = ranked[0][0]
        if best < self.grade_min_score:
            logger.info(
                f"Document ranking: nothing relevant (best={best:.2f} < "
                f"{self.grade_min_score}); returning no results for: {question}")
            return {"messages": [SystemMessage(content="(no relevant results found)")]}

        floor = best * self.grade_relative_floor
        keep = [(s, i, c) for s, i, c in ranked if s >= floor][:self.grade_top_n]

        logger.info(
            f"Document ranking: kept {len(keep)}/{len(chunks)} "
            f"(best={best:.2f}, floor={floor:.2f}, scores="
            f"{[round(s, 2) for s, _, _ in ranked]})")

        # The score travels with the chunk: the generating model can weigh a weak
        # hit accordingly, and it is the per-result score structured MCP output needs.
        context = sep.join(f"{c}\n[relevance: {s:.2f}]" for s, _, c in keep)
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


