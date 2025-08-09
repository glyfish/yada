from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence

from pydantic import BaseModel, Field
from typing import Dict

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm, should_continue
from apps.agentic.core.constants import GITHUB_DB_NAME, GITHUB_COLLECTION_NAME

from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentGrade(BaseModel):
    """Binary score for relevance check."""
    binary_score: str = Field(description="Relevance score 'yes' or 'no'")


class GitHubAgent(ABC):

    def __init(self):
        tool_name = "github_agent_tool"
        tool_description = "Search and return information about GitHub repositories."

        self.__doc_loader = ChromaDocumentLoader(GITHUB_DB_NAME, GITHUB_COLLECTION_NAME)
        self.__retriever = self.__doc_loader.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )
        self.__retriever_tool = create_retriever_tool(
            self.__retriever,
            tool_name,
            tool_description)
        self.__tools = [self.__retriever_tool]

    @property
    def doc_loader(self):
        """
        Get the document loader for the GitHub agent.
        """
        return self.__doc_loader


    @property
    def retriever(self):
        """
        Get the retriever for the GitHub agent.
        """
        return self.__retriever
    
    @property
    def tools(self):
        """
        Get the tools available to the GitHub agent.
        """
        return self.__tools


    def __grade_documents(self, state) -> Literal["generate", "rewrite"]:
        """
        Determines whether the retrieved documents are relevant to the question.

        Args:
            state (messages): The current state

        Returns:
            str: A decision for whether the documents are relevant or not
        """

        model = build_llm()
        llm_with_tool = model.with_structured_output(DocumentGrade)

        system_prompt = ChatPromptTemplate(
            template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
            Here is the retrieved document: \n\n {context} \n\n
            Here is the user question: {question} \n
            If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
            Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
            input_variables=["context", "question"],
        )

        chain = system_prompt | llm_with_tool
        
        messages = state["messages"]
        last_message = messages[-1]

        question = messages[0].content
        docs = last_message.content

        scored_result = chain.invoke({"question": question, "context": docs})
        score = scored_result.binary_score
        logger.debug(f"Graded documents with score: {score}")

        return "generate" if score == "yes" else "rewrite"
    

    def __rewrite(self, state):
        """
        Transform the query to produce a better question.

        Args:
            state (messages): The current state

        Returns:
            dict: The updated state with re-phrased question
        """

        print("---TRANSFORM QUERY---")
        messages = state["messages"]
        question = messages[0].content

        msg = [
            HumanMessage(
                content=f""" \n 
        Look at the input and try to reason about the underlying semantic intent / meaning. \n 
        Here is the initial question:
        \n ------- \n
        {question} 
        \n ------- \n
        Formulate an improved question: """,
            )
        ]

        # Grader
        model = model = build_llm()

        response = model.invoke(msg)
        return {"messages": [response]}


    def __generate(self, state):
        """
        Generate answer

        Args:
            state (messages): The current state

        Returns:
            dict: The updated state with re-phrased question
        """
        messages = state["messages"]
        question = messages[0].content
        last_message = messages[-1]

        docs = last_message.content

        # Prompt
        prompt = hub.pull("rlm/rag-prompt")

        # LLM
        llm = build_llm()

        # Post-processing
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Chain
        rag_chain = prompt | llm | StrOutputParser()

        # Run
        response = rag_chain.invoke({"context": docs, "question": question})
        return {"messages": [response]}