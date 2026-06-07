from __future__ import annotations

import re


def _parse_expense(raw: str) -> float | None:
    """Convert '0.05' or '$0.06^{\\ddagger}$' → float like 0.0005."""
    if not raw or raw.strip() in ("", "-"):
        return None
    # Strip LaTeX fragments like $...$
    clean = re.sub(r"\$[^$]*\$", "", raw).strip()
    try:
        return float(clean) / 100
    except ValueError:
        return None


_TABLE_ROW = re.compile(
    r"^\|\s*(.+?)\s*\|\s*([A-Z]{1,6})\s*\|\s*([\d.$^\\{}]+|-)\s*\|"
)
_HEADER_PATTERN = re.compile(
    r"Fund name", re.IGNORECASE
)
_SECTION_PATTERN = re.compile(r"^##?\s+")


class ISharesParser:
    """
    Parser for iShares/Blackrock Markdown table export.

    Each markdown table row has: Fund name | Trading symbol | Expense ratio (%)
    Section headers (##) are captured as asset_class context.
    """

    FUND_FAMILY = "iShares"

    def parse(self, path: str, limit: int | None = None) -> list[dict]:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        records: list[dict] = []
        current_section = ""

        for line in lines:
            line = line.rstrip()

            if _SECTION_PATTERN.match(line):
                current_section = re.sub(r"^##?\s*", "", line).strip()
                continue

            m = _TABLE_ROW.match(line)
            if not m:
                continue

            fund_name_raw, ticker, expense_raw = m.group(1), m.group(2), m.group(3)

            # Skip header rows like "Fund name | Trading symbol | …"
            if _HEADER_PATTERN.search(fund_name_raw):
                continue

            # Strip markdown escape backslashes and HTML tags
            fund_name = re.sub(r"\\([&|])", r"\1", fund_name_raw).strip()
            fund_name = re.sub(r"<[^>]+>", "", fund_name).strip()

            expense_ratio = _parse_expense(expense_raw)

            records.append(
                {
                    "ticker": ticker,
                    "fund_name": fund_name,
                    "fund_family": self.FUND_FAMILY,
                    "asset_class": current_section or None,
                    "category": None,
                    "inception_date": None,
                    "aum": None,
                    "expense_ratio": expense_ratio,
                    "benchmark_index": None,
                }
            )

            if limit is not None and len(records) >= limit:
                break

        return records
