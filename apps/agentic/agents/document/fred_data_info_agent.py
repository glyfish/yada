from langchain_core.messages import AIMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.checkpointer import checkpointer
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

        self._generate_prompt = ChatPromptTemplate.from_messages([  # type: ignore[assignment]
            ("system", """
            You are an expert assistant answering questions about FRED (Federal Reserve Economic Data) time series.

            CRITICAL — output rules you must never deviate from:
            - Group results by category. Show the category name and category_id as a header for each group.
            - Never render a table. Never use markdown table syntax (pipes and dashes). Bullet lists only.
            - For every series output a block exactly in this format, with no fields omitted:

              **<series_id>**
              - Title: <series_title>
              - Frequency: <frequency>
              - Units: <units>
              - Observation Start: <observation_start>
              - Observation End: <observation_end>
              - Seasonal Adjustment: <seasonal_adjustment>
              - Popularity: <popularity>
              - Category Path: <category_path>

            - If a field value is missing write "N/A". Never skip or omit a field.
            - Never summarize or condense the list. Show every returned series in full.
            """),
            ("human", """
            Question: {question}
            Context: {context}
            Answer:
            """),
        ])


    def _generate(self, state):
        docs = state["messages"][-1].content
        rows = self._parse_rows(docs)
        if not rows:
            return {"messages": [AIMessage(content="No matching FRED series found.")]}

        grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
        for row in rows:
            key = (row["category_name"], row["category_id"])
            grouped.setdefault(key, []).append(row)

        out: list[str] = ["FRED Time Series Results"]
        for (category_name, category_id), series_rows in grouped.items():
            out.append("")
            out.append(f"## {category_name} (category_id: {category_id})")
            for row in series_rows:
                out.append(f"- **{row['series_id']}**")
                out.append(f"  - Title: {row['series_title']}")
                out.append(f"  - Frequency: {row['frequency']}")
                out.append(f"  - Units: {row['units']}")
                out.append(f"  - Observation Start: {row['observation_start']}")
                out.append(f"  - Observation End: {row['observation_end']}")
                out.append(f"  - Seasonal Adjustment: {row['seasonal_adjustment']}")
                out.append(f"  - Popularity: {row['popularity']}")
                out.append(f"  - Category Path: {row['category_path']}")

        return {"messages": [AIMessage(content="\n".join(out))]}


    def _retrieve(self, state):
        question = state["messages"][0].content if state.get("messages") else ""
        hits = self.retriever.invoke(question)
        if not hits:
            return {"messages": [SystemMessage(content="")]}

        def val(meta: dict, key: str) -> str:
            v = meta.get(key)
            return "N/A" if v is None or v == "" else str(v)

        lines: list[str] = []
        for d in hits:
            m = d.metadata or {}
            lines.append("||ROW||")
            lines.append(f"category_id={val(m, 'category_id')}")
            lines.append(f"category_name={val(m, 'category_name')}")
            lines.append(f"category_path={val(m, 'category_path')}")
            lines.append(f"series_id={val(m, 'series_id')}")
            lines.append(f"series_title={val(m, 'series_title')}")
            lines.append(f"frequency={val(m, 'frequency')}")
            lines.append(f"units={val(m, 'units')}")
            lines.append(f"observation_start={val(m, 'observation_start')}")
            lines.append(f"observation_end={val(m, 'observation_end')}")
            lines.append(f"seasonal_adjustment={val(m, 'seasonal_adjustment')}")
            lines.append(f"popularity={val(m, 'popularity')}")

        return {"messages": [SystemMessage(content="\n".join(lines))]}


    def _parse_rows(self, payload: str) -> list[dict[str, str]]:
        required = [
            "category_id",
            "category_name",
            "category_path",
            "series_id",
            "series_title",
            "frequency",
            "units",
            "observation_start",
            "observation_end",
            "seasonal_adjustment",
            "popularity",
        ]
        rows: list[dict[str, str]] = []
        current: dict[str, str] = {}

        for raw_line in payload.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line == "||ROW||":
                if current:
                    rows.append({k: current.get(k, "N/A") for k in required})
                    current = {}
                continue
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            current[k.strip()] = v.strip() or "N/A"

        if current:
            rows.append({k: current.get(k, "N/A") for k in required})
        return rows


    def _create_agent(self):
        graph = (
            StateGraph(WorkerState)
            .add_node("retrieve", self._retrieve)
            .add_node("generate", self._generate)
            .add_edge(START, "retrieve")
            .add_edge("retrieve", "generate")
            .add_edge("generate", END)
        )
        return graph.compile(checkpointer=checkpointer)
