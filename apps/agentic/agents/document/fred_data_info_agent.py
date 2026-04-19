from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.document_loaders.fred_document_loader import FREDChromaDocumentLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class FredDataInfoAgent(ChromaRAGAgent):
    """
    Agent for searching descriptions of time series data of FRED (Federal Reserve Economic Data) 
    website.    
    """

    QUERY_FILTERS =  """
        **fred_data_info Query Filters**
        The agent supports the following query filters to refine searches:
        - category_id:<n>                  Exact category ID match
        - category_name:"..."              Category name (use quotes for multi-word)
        - series_id:<id>                   Exact series ID match
        - popularity:<n>                   Exact popularity score
        - popularity:>n | >=n | <n | <=n   Popularity comparison
        - last_updated:YYYY-MM-DD          Exact date match
        - last_updated:after YYYY-MM-DD    Updated after date
        - last_updated:before YYYY-MM-DD   Updated before date

        **Example Queries Using Filter**
        - popularity:>40 What time series are available for Commodities in the FRED data?
        - category_name:"Farm Products" What price indexes are in FRED?
        - series_id:WPU01 What are the FRED series details?
        - category_id:33528 What are the FRED series details?
        - popularity:<50 last_updated:after 2025-01-01 What time series are available for 
            Commodities in the FRED data??
        - category_name:"Final Demand" popularity:>10 What FRED PPI series are available?
    """

    @classmethod
    async def create(cls, query=None) -> "FredDataInfoAgent":
        return cls(query)

    def __init__(self, query):
        tool_name = "fred_data_info_agent_tool"
        tool_description = """
            FRED Document Retriever
            Description: Search and retrieve data from the FRED document store which contains
                        data about time series from the FRED (Federal Reserve Economic Data) website.
        """

        document_prompt_template = """
            You are an expert in retrieving information about time series from the FRED (Federal Reserve Economic Data)
            website based on the contents of documents describing the data. The time series data is organized in a
            hierarchy of categories that describe the type of data contained in each time series. The categories are described
            in the markdown documents contained in the document store. The categories form a hierarchy from broad to specific.
            Following is a description of the document metadata.
            - category_id : {{metadata[category_id]}} Time series category identifier.
            - category_name: {{metadata[category_name]}} Time series category name.
            - category_path: {{metadata[category_path]}} Hierarchy path of the time series category.
            - filename: {{metadata[filename]}} name of document file.
            - frequency: {{metadata[frequency]}} time frequency of data observations.
            - observation_end: {{metadata[observation_end]}} End date of time series observations.
            - observation_start: {{metadata[observation_start]}} Start date of time series observations.
            - popularity: {{metadata[popularity]}} Popularity score of the time series.
            - seasonal_adjustment: {{metadata[seasonal_adjustment]}} Indicates if data is seasonally adjusted.
            - series_id: {{metadata[series_id]}} Time series identifier.
            - series_title: {{metadata[series_title]}} Title of the time series.
            - units: {{metadata[units]}} Units of measurement for the time series data.
            ---
            {page_content}
        """

        document_prompt = PromptTemplate.from_template(template=document_prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, FREDChromaDocumentLoader(), query,
                         retriever_k=50, retriever_fetch_k=200)

        self._generate_prompt = ChatPromptTemplate.from_messages([("human", """
            You are an expert assistant answering questions about FRED (Federal Reserve Economic Data) time series.
            Use the retrieved context below to answer the question. The context contains metadata about FRED time
            series including series_id, series_title, frequency, units, observation dates, category, and popularity.
            
            ALWAYS follow the following instructions when answering and do not deviate from them under any circumstance:
            - List matching series with their series_id, title, frequency, popularity score, and units
            - Include observation date ranges when relevant
            - Group results by category_path if multiple series are returned
            - If you don't know the answer from the context, say so clearly

            Question: {question}
            Context: {context}
            Answer:
        """
        )])

