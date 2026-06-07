from __future__ import annotations

import pandas as pd

from apps.agentic.core.document_loaders.etf.etf_parser import normalize_date


class ProSharesParser:
    """
    Parser for ProShares' performance CSV export.

    The file has one row per fund × return-period combination.
    We deduplicate on Fund Symbol, keeping Fund Name and Inception Date.
    """

    FUND_FAMILY = "ProShares"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        df = pd.read_csv(path)
        df.columns = [str(c).strip() for c in df.columns]
        df = df.dropna(subset=["Fund Symbol", "Fund Name"])
        df = df.drop_duplicates(subset=["Fund Symbol"])

        if limit is not None:
            df = df.iloc[:limit]

        records: list[dict] = []
        for _, row in df.iterrows():
            ticker = str(row.get("Fund Symbol", "")).strip()
            fund_name = str(row.get("Fund Name", "")).strip()
            if not ticker or not fund_name:
                continue
            inception_raw = row.get("Inception Date")
            if inception_raw and str(inception_raw) != "nan":
                # Stored as datetime string like "2007-02-01 00:00:00.000"
                inception = normalize_date(str(inception_raw)[:10])
            else:
                inception = None
            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": None,
                    "category": None,
                    "inception_date": inception,
                    "aum": None,
                    "expense_ratio": None,
                    "benchmark_index": None,
                }
            )
        return records
