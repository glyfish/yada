from langchain_core.messages import AIMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph, START, END

from apps.agentic.core.agents.chroma_rag_agent import ChromaRAGAgent
from apps.agentic.core.agents.messages import WorkerState
from apps.agentic.core.checkpointer import checkpointer
from apps.agentic.core.document_loaders.etf.finance_database_loader import FinanceDatabaseLoader
from apps.agentic.core.document_loaders.etf.exchange_metadata import EXCHANGES, CURRENCIES
from lib.logger import get_logger

logger = get_logger("YADA")

def _fmt_exchange(code: str) -> str:
    if code == "N/A":
        return code
    info = EXCHANGES.get(code)
    if info:
        return f"{code} — {info['name']} ({info['location']})"
    return code


def _fmt_currency(code: str) -> str:
    if code == "N/A":
        return code
    info = CURRENCIES.get(code)
    if info:
        return f"{code} — {info['name']} ({info['country']})"
    return code


class ETFDataInfoAgent(ChromaRAGAgent):
    """
    Agent for searching ETF and mutual fund information stored in ChromaDB.
    Data is sourced from the FinanceDatabase package (~36K ETFs).
    """

    @classmethod
    async def create(cls, query=None) -> "ETFDataInfoAgent":
        return cls(query)

    def __init__(self, query):
        tool_name = "etf_data_info_agent_tool"
        tool_description = """
            ETF Document Retriever
            Description: Search and retrieve ETF and mutual fund information from the ETF document
                        store. Data covers ~36K ETFs sourced from the FinanceDatabase package,
                        including fund name, ticker, family, asset class, category, exchange,
                        currency, and investment strategy description.
        """

        document_prompt_template = """
            You are an expert in retrieving information about ETFs and mutual funds.
            The documents describe funds sourced from the FinanceDatabase package.
            Following is a description of the document metadata.
            - ticker: {{metadata[ticker]}} Fund ticker symbol.
            - name: {{metadata[name]}} Fund name.
            - family: {{metadata[family]}} Fund family or asset manager.
            - category_group: {{metadata[category_group]}} Broad asset class.
            - category: {{metadata[category]}} Specific fund category.
            - exchange: {{metadata[exchange]}} Exchange code.
            - currency: {{metadata[currency]}} Fund currency.
            - isin: {{metadata[isin]}} ISIN code.
            ---
            {page_content}
        """

        document_prompt = PromptTemplate.from_template(template=document_prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, FinanceDatabaseLoader(), query,
                         retriever_k=100, retriever_fetch_k=200)


    def _generate(self, state):
        """
        Build the answer deterministically from the retrieved rows — no LLM
        generation step. The output format lives here (not in a prompt); keep it
        in sync with the fields emitted by _retrieve.
        """
        docs = state["messages"][-1].content
        rows = self._parse_rows(docs)
        if not rows:
            return {"messages": [AIMessage(content="No matching ETFs found.")]}

        grouped: dict[str, list[dict[str, str]]] = {}
        for row in rows:
            key = row["family"] if row["family"] != "N/A" else "Unknown Family"
            grouped.setdefault(key, []).append(row)

        out: list[str] = ["ETF Search Results"]
        for family, fund_rows in grouped.items():
            out.append("")
            out.append(f"## {family}")
            for row in fund_rows:
                out.append(f"- **{row['ticker']}** — {row['name']}")
                out.append(f"  - Asset Class: {row['category_group']}")
                out.append(f"  - Category: {row['category']}")
                out.append(f"  - Exchange: {_fmt_exchange(row['exchange'])}")
                out.append(f"  - Currency: {_fmt_currency(row['currency'])}")
                out.append(f"  - ISIN: {row['isin']}")

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
            lines.append(f"ticker={val(m, 'ticker')}")
            lines.append(f"name={val(m, 'name')}")
            lines.append(f"family={val(m, 'family')}")
            lines.append(f"category_group={val(m, 'category_group')}")
            lines.append(f"category={val(m, 'category')}")
            lines.append(f"exchange={val(m, 'exchange')}")
            lines.append(f"currency={val(m, 'currency')}")
            lines.append(f"isin={val(m, 'isin')}")

        return {"messages": [SystemMessage(content="\n".join(lines))]}


    def _parse_rows(self, payload: str) -> list[dict[str, str]]:
        required = [
            "ticker",
            "name",
            "family",
            "category_group",
            "category",
            "exchange",
            "currency",
            "isin",
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
