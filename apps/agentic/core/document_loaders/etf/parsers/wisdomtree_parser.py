from __future__ import annotations

import pandas as pd

from apps.agentic.core.document_loaders.etf.etf_parser import normalize_date


class WisdomTreeParser:
    """
    Parser for WisdomTree's XLSX export.

    Columns: Fund, Ticker, Asset Class, Sub Asset Class,
             Inception Date (ISO), Shares Outstanding, Net Expense Ratio, NAV
    Header is on row 3 (0-indexed); rows 0-2 are title/date noise.
    """

    FUND_FAMILY = "WisdomTree"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        df = pd.read_excel(path, header=3)
        df.columns = [str(c).strip() for c in df.columns]
        # Drop rows where both Fund and Ticker are missing
        df = df.dropna(subset=["Fund", "Ticker"], how="all")

        if limit is not None:
            df = df.iloc[:limit]

        records: list[dict] = []
        for _, row in df.iterrows():
            ticker = str(row.get("Ticker", "")).strip()
            fund_name = str(row.get("Fund", "")).strip()
            if not ticker or not fund_name or ticker == "nan":
                continue
            raw_exp = row.get("Net Expense Ratio")
            expense_ratio = float(raw_exp) if raw_exp and str(raw_exp) != "nan" else None
            inception_raw = row.get("Inception Date")
            inception = normalize_date(str(inception_raw)) if inception_raw and str(inception_raw) != "nan" else None
            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": str(row.get("Asset Class", "")).strip() or None,
                    "category": str(row.get("Sub Asset Class", "")).strip() or None,
                    "inception_date": inception,
                    "aum": None,
                    "expense_ratio": expense_ratio,
                    "benchmark_index": None,
                }
            )
        return records
