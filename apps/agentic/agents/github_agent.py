from abc import ABC, abstractmethod
from typing import Annotated, Literal, Sequence

from pydantic import BaseModel, Field
from typing import Dict

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import tools_condition
from langchain.tools.retriever import create_retriever_tool

from apps.agentic.core.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.messages import WorkerState
from apps.agentic.core.utils import build_llm
from apps.agentic.core.constants import GITHUB_DB_NAME, GITHUB_COLLECTION_NAME

from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentGrade(BaseModel):
    """Binary score for relevance check."""
    binary_score: str = Field(description="Relevance score 'yes' or 'no'")


class GitHubAgent(ABC):

    def __init__(self):
        tool_name = "github_agent_tool"
        tool_description = "Search and return information about GitHub repositories."
        self.__llm = build_llm()

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
        self.__agent = self._create_agent()


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


    @property
    def retriever_tool(self):
        """
        Get the retriever tool for the GitHub agent.
        """
        return self.__retriever_tool


    @property
    def llm(self):
        """
        Get the language model used by the agent.
        """

        return self.__llm
    

    @property
    def agent(self):
        """
        Get the compiled agent state graph.
        """

        return self.__agent


    async def invoke_model(self, state: WorkerState, config=None) -> WorkerState:
        """
        Invoke the agent with the current state.
        """

        messages = state["messages"]
        prompt_messages = self.prompt.format_messages(messages=messages)
        result = await self.tooled_llm.ainvoke(prompt_messages)
        return {"messages": [result]}

  
    def __grade_documents(self, state) -> Literal["generate", "rewrite"]:
        """
        Determines whether the retrieved documents are relevant to the question.

        Args:
            state (messages): The current state

        Returns:
            str: A decision for whether the documents are relevant or not
        """

        llm_with_tool = self.llm.with_structured_output(DocumentGrade)

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

        response = self.llm.invoke(msg)
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

        prompt = hub.pull("rlm/rag-prompt")
        llm = build_llm()

        rag_chain = prompt | llm | StrOutputParser()
        response = rag_chain.invoke({"context": docs, "question": question})
        return {"messages": [response]}
    

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
            .add_node("model", self.__invoke_model)
            .add_node("retrieve", self.retriever_tool)
            .add_node("rewrite", self.__rewrite) 
            .add_node("generate", self.__generate) 
            .add_edge(START, "model")
            .add_edge("tools", "model")
            .add_conditional_edges(
                "model",
                tools_condition,
                {
                    "tools": "retrieve",
                    END: END,
                }
            )
            .add_conditional_edges(
                "retrieve",
                self.__grade_documents,
                {
                    "generate": "generate", 
                    "rewrite": "rewrite"
                }
            )
            .add_edge("generate", END)
            .add_edge("rewrite", "model")
        )

        return graph.compile()
