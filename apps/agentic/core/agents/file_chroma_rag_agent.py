from abc import abstractmethod

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent

from lib.logger import get_logger

logger = get_logger("YADA")


class FileChromaRAGAgent(ChromaRAGAgent):
    """
    Base class for file-based Chroma RAG agents that are distributed over multiple chunks.
    This class extends ChromaRAGAgent and requires subclasses to implement file-reading logic.
    """

    def _generate(self, state):
        """
        Generate answer and optionally append reconstructed full-file content.

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
        files_section = ""
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

            files_section = self.read_file(top_files) or ""
        except Exception as e:
            logger.error(f"Full-file append skipped because of error: {e}")

        prompt = self._generate_prompt
        logger.debug(f"RAG Agent generate prompt: {prompt}")

        rag_chain = prompt | self.llm | StrOutputParser()
        answer_text = rag_chain.invoke({"context": docs, "question": question})
        final_text = answer_text + (files_section if files_section else "")
        return {"messages": [AIMessage(content=final_text)]}

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
            parts.append(f"{d.page_content}")

        context = sep.join(parts) if parts else "(no results)"
        return {"messages": [HumanMessage(content=context)]}

    @abstractmethod
    def read_file(self, top_files):
        """
        Read the contents of the specified files.
        """

        raise NotImplementedError("Subclasses must implement the read_file method to read files.")
