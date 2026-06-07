from __future__ import annotations

import os

from langchain_core.documents import Document

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.document_loaders.etf.etf_parser import ETFParser
from apps.agentic.core.constants import ETF_DB_NAME, ETF_COLLECTION_NAME, DB_PATH

from lib.logger import get_logger

logger = get_logger("YADA")


class ETFDocumentLoader(ChromaDocumentLoader):
    """
    ChromaDB loader for ETF/mutual-fund metadata.

    Each record parsed by the injected ETFParser becomes one Document whose
    page_content is a human-readable Markdown block and whose metadata carries
    the structured fields for filtering.

    A Tavily search is issued per fund to fetch a short description; pass
    tavily_client=None to skip that step (useful in tests / notebooks).
    """

    def __init__(
        self,
        parser: ETFParser,
        tavily_client=None,
        db_path: str = DB_PATH,
    ):
        super().__init__(ETF_DB_NAME, ETF_COLLECTION_NAME, db_path)
        self._parser = parser
        self._tavily = tavily_client

    def delete_by_fund_family(self, fund_family: str) -> int:
        """Delete all docs for a fund family. Returns count deleted."""
        collection = getattr(self._vectorstore, "_collection", None)
        if collection is None:
            return 0
        result = collection.get(where={"fund_family": fund_family}, include=[])
        ids = result.get("ids") or []
        if ids:
            collection.delete(ids=ids)
            logger.info(f"ETFDocumentLoader: deleted {len(ids)} docs for fund_family='{fund_family}'")
        return len(ids)

    async def reload_document(self, path: str, fund_family: str, limit: int | None = None, **kwargs):
        """Delete existing docs for fund_family, then load from path."""
        deleted = self.delete_by_fund_family(fund_family)
        logger.info(f"ETFDocumentLoader: cleared {deleted} existing docs for '{fund_family}'")
        await self.load_document(path, limit=limit, **kwargs)

    async def load_document(self, path: str, limit: int | None = None, **kwargs):
        """
        Parse the file at *path* with the injected parser, fetch Tavily
        descriptions, and write documents into ChromaDB.
        """
        records = self._parser.parse(path, limit=limit)
        if not records:
            logger.warning(f"ETFDocumentLoader: no records returned from {path}")
            return

        documents: list[Document] = []
        for rec in records:
            description = await self._fetch_description(rec)

            aum_str = f"${rec['aum']:,.0f}" if rec["aum"] else "N/A"
            expense_str = f"{rec['expense_ratio']:.2%}" if rec.get("expense_ratio") else "N/A"

            page_content = "\n".join([
                f"# {rec['fund_name']}",
                "",
                f"- **Ticker:** {rec['ticker']}",
                f"- **Fund Family:** {rec['fund_family']}",
                f"- **Asset Class:** {rec.get('asset_class') or 'N/A'}",
                f"- **Category:** {rec.get('category') or 'N/A'}",
                f"- **Inception Date:** {rec.get('inception_date') or 'N/A'}",
                f"- **AUM:** {aum_str}",
                f"- **Expense Ratio:** {expense_str}",
                f"- **Benchmark:** {rec.get('benchmark_index') or 'N/A'}",
                "",
                "## Description",
                description or "No description available.",
            ])

            doc_metadata = {
                "ticker": rec["ticker"],
                "fund_name": rec["fund_name"],
                "fund_family": rec["fund_family"],
                "asset_class": rec.get("asset_class") or "",
                "category": rec.get("category") or "",
                "inception_date": rec.get("inception_date") or "",
                "aum": rec["aum"] if rec["aum"] is not None else 0.0,
                "expense_ratio": rec.get("expense_ratio") or 0.0,
                "benchmark_index": rec.get("benchmark_index") or "",
            }

            documents.append(Document(page_content=page_content, metadata=doc_metadata))

        BATCH = 128
        for i in range(0, len(documents), BATCH):
            self.vectorstore.add_documents(documents[i : i + BATCH])

        logger.info(
            f"ETFDocumentLoader: loaded {len(documents)} ETF documents from {path} "
            f"into collection {self.collection_name}."
        )

    async def load_all_documents(self, base_path: str = "", limit: int | None = None, **kwargs):
        """
        Not used in the current design — ETF files are loaded one-at-a-time
        via load_document. Raises NotImplementedError to satisfy the ABC.
        """
        raise NotImplementedError(
            "ETFDocumentLoader does not support load_all_documents. "
            "Call load_document(path, limit=N) for each fund-family file."
        )

    async def _fetch_description(self, rec: dict) -> str | None:
        if self._tavily is None:
            return None
        try:
            query = f"{rec['ticker']} {rec['fund_name']} ETF investment strategy"
            result = await self._tavily.ainvoke({"query": query})
            if isinstance(result, dict):
                return result.get("answer") or None
            return str(result) if result else None
        except Exception as exc:
            logger.warning(
                f"ETFDocumentLoader: Tavily search failed for {rec['ticker']}: {exc}"
            )
            return None
