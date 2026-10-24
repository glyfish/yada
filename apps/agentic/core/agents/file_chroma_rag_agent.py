from abc import abstractmethod

from langchain_core.documents import Document
from langchain_core.messages import AIMessage
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
        docs = messages[-1].content

        # Append the full text of the best-ranked file.
        #
        # This re-ran the retriever and took its top result, which is a different
        # question from the one the graph just answered: the retriever ranks by
        # embedding distance, the grader by relevance to the question. So the file
        # stapled onto the answer could be -- and sometimes was -- one the grader had
        # already rejected. The graded chunks are in the state now, so take the top of
        # those instead: same file in the ordinary case, the right file in the case
        # where they disagree, and one fewer query either way.
        files_section = ""
        try:
            seen, top_files = set(), []
            for chunk in state.get("hits") or []:
                if not chunk.path or chunk.path in seen:
                    continue
                seen.add(chunk.path)
                top_files.append(Document(page_content=chunk.text, metadata=chunk.metadata))
                if len(top_files) >= 1:
                    break

            files_section = self.read_file(top_files) or "" if top_files else ""
        except Exception as e:
            logger.error(f"Full-file append skipped because of error: {e}")

        prompt = self._generate_prompt
        logger.debug(f"RAG Agent generate prompt: {prompt}")

        rag_chain = prompt | self.llm | StrOutputParser()
        answer_text = rag_chain.invoke({"context": docs, "question": question})
        final_text = answer_text + (files_section if files_section else "")
        return {"messages": [AIMessage(content=final_text)]}


    @abstractmethod
    def read_file(self, top_files):
        """
        Read the contents of the specified files.
        """

        raise NotImplementedError("Subclasses must implement the read_file method to read files.")
