from __future__ import annotations

import re
import pandas as pd


def _normalize_expense(raw) -> float | None:
    """Convert '0.10%' → 0.001."""
    if raw is None or str(raw).strip() in ("", "nan", "-"):
        return None
    s = str(raw).strip()
    had_percent = s.endswith("%")
    s = s.rstrip("%")
    try:
        val = float(s)
        return val / 100 if had_percent else val
    except ValueError:
        return None


def _parse_inception(raw) -> str | None:
    """Convert 'Jun 25 2018' or 'Nov 18 2004' → ISO YYYY-MM-DD."""
    if raw is None or str(raw).strip() in ("", "nan"):
        return None
    try:
        return pd.to_datetime(str(raw)).strftime("%Y-%m-%d")
    except Exception:
        return str(raw)


class StateStreetParser:
    """
    Parser for State Street's XLSX export.

    Row 0: disclaimer text — skip.
    Row 1: column headers (Ticker, Name, Inception Date, Gross Expense Ratio, Asset Class …).
    Row 2: return-period sub-headers — skip.
    Rows 3+: data.
    """

    FUND_FAMILY = "State Street"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        df = pd.read_excel(path, skiprows=[0, 2], header=0)
        df.columns = [str(c).strip() for c in df.columns]
        df = df.dropna(subset=["Ticker", "Name"], how="all")

        if limit is not None:
            df = df.iloc[:limit]

        records: list[dict] = []
        for _, row in df.iterrows():
            ticker = re.sub(r"[®™]", "", str(row.get("Ticker", ""))).strip()
            fund_name = str(row.get("Name", "")).strip()
            if not ticker or not fund_name or ticker == "nan":
                continue
            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": str(row.get("Asset Class", "")).strip() or None,
                    "category": None,
                    "inception_date": _parse_inception(row.get("Inception Date")),
                    "aum": None,
                    "expense_ratio": _normalize_expense(row.get("Gross Expense Ratio")),
                    "benchmark_index": str(row.get("Primary Index", "")).strip() or None,
                }
            )
        return records
