from __future__ import annotations

import pandas as pd

from apps.agentic.core.document_loaders.etf.etf_parser import normalize_aum, normalize_date


class VanEckParser:
    """
    Parser for VanEck's HTML-table-as-XLS export.

    Columns present: Ticker, Name, Vehicle, Asset Class, Category,
                     Inception Date, Total Net Assets, Factsheet
    """

    FUND_FAMILY = "VanEck"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        tables = pd.read_html(path, flavor="lxml")
        df = tables[0]

        df.columns = [str(c).strip() for c in df.columns]

        if limit is not None:
            df = df.iloc[:limit]

        records: list[dict] = []
        for _, row in df.iterrows():
            ticker = str(row.get("Ticker", "")).strip()
            fund_name = str(row.get("Name", "")).strip()
            if not ticker or not fund_name:
                continue
            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": str(row.get("Asset Class", "")).strip() or None,
                    "category": str(row.get("Category", "")).strip() or None,
                    "inception_date": normalize_date(row.get("Inception Date")),
                    "aum": normalize_aum(row.get("Total Net Assets")),
                    "expense_ratio": None,
                    "benchmark_index": None,
                }
            )
        return records
