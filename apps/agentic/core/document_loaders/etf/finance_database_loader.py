from __future__ import annotations

import asyncio

import financedatabase as fd
from langchain_core.documents import Document

from apps.agentic.core.document_loaders.chroma_document_loader import ChromaDocumentLoader
from apps.agentic.core.constants import ETF_DB_NAME, ETF_COLLECTION_NAME, DB_PATH

from lib.logger import get_logger

logger = get_logger("YADA")


class FinanceDatabaseLoader(ChromaDocumentLoader):
    """
    ChromaDB loader for ETF metadata sourced from the FinanceDatabase package.

    Downloads the full ETF universe (~36K funds) from the FinanceDatabase GitHub
    repository (updated weekly) and indexes each fund as a ChromaDB document.
    The fund's `summary` field from the prospectus is the primary semantic content;
    no Tavily enrichment is needed.

    Metadata stored per document:
        ticker, name, summary, category_group, category, family,
        exchange, currency, isin
    """

    def __init__(self, db_path: str = DB_PATH):
        super().__init__(ETF_DB_NAME, ETF_COLLECTION_NAME, db_path)

    def delete_all(self) -> int:
        """Delete every document in the etf-info collection. Returns count deleted."""
        collection = getattr(self._vectorstore, "_collection", None)
        if collection is None:
            return 0
        total = collection.count()
        if total == 0:
            return 0
        self._vectorstore.reset_collection()
        logger.info(f"FinanceDatabaseLoader: deleted {total} documents from '{self.collection_name}'")
        return total


    @staticmethod
    def _str(val) -> str:
        import pandas as pd
        if val is None or (isinstance(val, float) and pd.isna(val)):
            return ""
        s = str(val).strip()
        return "" if s == "nan" else s


    def _build_documents(self, df) -> list[Document]:
        documents: list[Document] = []
        for ticker, row in df.iterrows():
            name = self._str(row.get("name"))
            summary = self._str(row.get("summary"))
            category_group = self._str(row.get("category_group"))
            category = self._str(row.get("category"))
            family = self._str(row.get("family"))
            exchange = self._str(row.get("exchange"))
            currency = self._str(row.get("currency"))
            isin = self._str(row.get("isin"))

            if not name or not ticker:
                continue

            parts = [f"# {name}", f"- **Ticker:** {ticker}"]
            if family:
                parts.append(f"- **Fund Family:** {family}")
            if category_group:
                parts.append(f"- **Asset Class:** {category_group}")
            if category:
                parts.append(f"- **Category:** {category}")
            if exchange:
                parts.append(f"- **Exchange:** {exchange}")
            if currency:
                parts.append(f"- **Currency:** {currency}")
            if summary:
                parts += ["", "## Description", summary]

            documents.append(Document(
                page_content="\n".join(parts),
                metadata={
                    "ticker": str(ticker),
                    "name": name,
                    "category_group": category_group,
                    "category": category,
                    "family": family,
                    "exchange": exchange,
                    "currency": currency,
                    "isin": isin,
                },
            ))
        return documents


    async def load_all_documents(
        self,
        family: str | list | None = None,
        category_group: str | list | None = None,
        category: str | list | None = None,
        exchange: str | list | None = None,
        **kwargs,
    ):
        """
        Download ETF data from FinanceDatabase and write to ChromaDB.

        Pass filter arguments to load a subset instead of all 36K funds:
            family="VanEck Asset Management"
            exchange="PCX"              # US-listed only
            category_group="Equities"
        """
        logger.info("FinanceDatabaseLoader: downloading ETF data from FinanceDatabase...")
        df = await asyncio.to_thread(
            lambda: fd.ETFs().select(
                family=family,
                category_group=category_group,
                category=category,
                exchange=exchange,
            )
        )
        logger.info(f"FinanceDatabaseLoader: {len(df)} ETFs downloaded, building documents...")

        documents = self._build_documents(df)
        total = len(documents)
        logger.info(f"FinanceDatabaseLoader: {total} documents built ({len(df) - total} skipped), writing to ChromaDB...")

        BATCH = 128
        LOG_EVERY = 2000
        written = 0
        for i in range(0, total, BATCH):
            self.vectorstore.add_documents(documents[i : i + BATCH])
            written += len(documents[i : i + BATCH])
            if written % LOG_EVERY < BATCH or written == total:
                logger.info(f"FinanceDatabaseLoader: {written}/{total} documents written...")

        logger.info(
            f"FinanceDatabaseLoader: done — {total} ETF documents "
            f"in collection '{self.collection_name}'."
        )

    
    async def reload_all_documents(
        self,
        family: str | list | None = None,
        category_group: str | list | None = None,
        category: str | list | None = None,
        exchange: str | list | None = None,
        **kwargs,
    ):
        """Wipe the collection then reload from FinanceDatabase."""
        logger.info("FinanceDatabaseLoader: starting reload — deleting existing documents...")
        deleted = self.delete_all()
        logger.info(f"FinanceDatabaseLoader: {deleted} documents deleted, starting ingest...")
        await self.load_all_documents(
            family=family,
            category_group=category_group,
            category=category,
            exchange=exchange,
            **kwargs,
        )
        logger.info("FinanceDatabaseLoader: reload complete.")

    async def load_document(self, path: str, **kwargs):
        raise NotImplementedError(
            "FinanceDatabaseLoader does not support load_document. "
            "Call load_all_documents() or reload_all_documents()."
        )
