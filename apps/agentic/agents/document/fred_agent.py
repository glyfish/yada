from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage
from langchain.prompts import PromptTemplate

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.document_loaders.document_library_loader import DocumentLibraryLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class FredAgent(ChromaRAGAgent):
    """
    Agent for searching descriptions of time series data of FRED (Federal Reserve Economic Data) 
    website.

    Query filters
    -------------
    The agent supports the following query filters to refine searches:

    Example Queries:
    - Look in the document library for the definition of a stochastic matrix.

    """

    def __init__(self, query):
        tool_name = "research_note_agent_tool"
        tool_description = """
            FRED Document Retriever
            Description: Search and retrieve data from the FRED document store which contains
                        data about time series from the FRED (Federal Reserve Economic Data) website.
        """

        prompt_template = """
            You are an expert in retrieving information about time series from the FRED (Federal Reserve Economic Data)
            website based on the contents of documents describing the data. The time series data is organized in a 
            hierarchy of categories that describe the type of data contained in each time series. The categories are described"
            in the markdown documents contained in the document store. The categories form a hierarchy from broad to specific.
            Following is a description of the document metadata.
            - category_id : {metadata[category_id]} Time series category identifier.
            - category_name: {metadata[category_name]} Time series category name.
            - category_path: {metadata[category_path]} Hierarchy path of the time series category.
            - filename: {metadata[filename]} name of document file.
            - frequency: {metadata[frequency]} time frequency of data observations.
            - observation_end: {metadata[observation_end]} End date of time series observations.
            - observation_start: {metadata[observation_start]} Start date of time series observations.
            - popularity: {metadata[popularity]} Popularity score of the time series.
            - seasonal_adjustment: {metadata[seasonal_adjustment]} Indicates if data is seasonally adjusted.
            - series_id: {metadata[series_id]} Time series identifier.
            - series_title: {metadata[series_title]} Title of the time series.
            - units: {metadata[units]} Units of measurement for the time series data.
            ---
            {page_content}"
        """

        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, DocumentLibraryLoader(), query)


    def read_file(self, top_files):
        """
        """

        pass

