from __future__ import annotations

import re
import pandas as pd


def _extract_inception_date(since_inception: str | None) -> str | None:
    """Extract YYYY-MM-DD from 'x.xx% (MM/DD/YYYY)'."""
    if not since_inception or str(since_inception).strip() == "nan":
        return None
    match = re.search(r"\((\d{2}/\d{2}/\d{4})\)", str(since_inception))
    if not match:
        return None
    m, d, y = match.group(1).split("/")
    return f"{y}-{int(m):02d}-{int(d):02d}"


def _parse_expense(raw) -> float | None:
    """Convert '0.04%' → 0.0004."""
    if raw is None or str(raw).strip() in ("", "nan", "---"):
        return None
    s = str(raw).strip().rstrip("%")
    try:
        return float(s) / 100
    except ValueError:
        return None


class VanguardParser:
    """
    Parser for Vanguard's ETF CSV export.

    Rows 0-3: BOM + title/subtitle noise.
    Row 4 (skiprows=3): column headers.
    Columns include: Fund name, Symbol, …, Since inception, Expense ratio, …, Benchmark.
    """

    FUND_FAMILY = "Vanguard"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        df = pd.read_csv(path, skiprows=3, encoding="utf-8-sig")
        df.columns = [str(c).strip() for c in df.columns]
        df = df.dropna(subset=["Fund name", "Symbol"], how="all")
        df = df[df["Symbol"].str.len() <= 6]

        # Column names include a date suffix — find them dynamically
        since_col = next((c for c in df.columns if c.startswith("Since inception")), None)
        expense_col = next((c for c in df.columns if c.startswith("Expense ratio")), None)

        if limit is not None:
            df = df.iloc[:limit]

        records: list[dict] = []
        for _, row in df.iterrows():
            ticker = str(row.get("Symbol", "")).strip()
            fund_name = str(row.get("Fund name", "")).strip()
            if not ticker or not fund_name or ticker == "nan":
                continue
            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": None,
                    "category": None,
                    "inception_date": _extract_inception_date(row.get(since_col) if since_col else None),
                    "aum": None,
                    "expense_ratio": _parse_expense(row.get(expense_col) if expense_col else None),
                    "benchmark_index": str(row.get("Benchmark", "")).strip() or None,
                }
            )
        return records
