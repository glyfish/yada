from __future__ import annotations

import re
from datetime import date
from typing import Optional, cast

from langchain_core.prompts import ChatPromptTemplate
from langsmith.run_helpers import traceable
from pydantic import BaseModel, Field

from apps.agentic.core.agents.query_filters import build_filter_and_query
from apps.agentic.core.llm_factory import filter_llm_model
from lib.logger import get_logger

logger = get_logger("YADA")


def _iso_to_yyyymmdd(value: Optional[str]) -> Optional[int]:
    """
    ISO date/datetime string -> YYYYMMDD integer, matching the numeric date fields
    written by the FRED loader. Chroma range operators ($gte/$lte) require int/float,
    not strings. Returns None when the value is missing or unparseable.
    """
    if not isinstance(value, str):
        return None
    m = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", value)
    if not m:
        return None
    return int(m.group(1) + m.group(2) + m.group(3))


# ---------- Pydantic filter models ----------

class ETFFilters(BaseModel):
    family: Optional[list[str]] = Field(
        None,
        description="""
        Fund family name(s) as stored in FinanceDatabase. Always return a list, even for one value.
        Normalize colloquial names to their full form:
        'VanEck' → 'VanEck Asset Management',
        'iShares' or 'BlackRock' → 'BlackRock Asset Management',
        'Vanguard' → 'Vanguard',
        'SPDR' or 'State Street' → 'State Street Global Advisors',
        'Invesco' → 'Invesco Investment Management',
        'WisdomTree' → 'WisdomTree Asset Management',
        'ProShares' → 'ProShares',
        'First Trust' → 'First Trust Advisors'.
        If you are not certain of the exact canonical name, return null.
        """,
    )
    category_group: Optional[list[str]] = Field(
        None,
        description="""
        Broad asset class(es). Always return a list, even for one value.
        Each value must be one of these exact strings as stored in the ETF database:
        'Alternatives', 'Cash', 'Commodities', 'Communication Services',
        'Consumer Discretionary', 'Consumer Staples', 'Currencies', 'Derivatives',
        'Energy', 'Equities', 'Financials', 'Fixed Income', 'Health Care',
        'Industrials', 'Information Technology', 'Materials', 'Real Estate', 'Utilities'.
        Map user language: 'bond'/'bonds'/'debt' → 'Fixed Income',
        'stock'/'stocks'/'equity'/'equities' → 'Equities',
        'commodity'/'commodities'/'gold'/'oil' → 'Commodities',
        'real estate'/'REIT' → 'Real Estate',
        'tech'/'technology' → 'Information Technology'.
        Return null if the user does not mention an asset class.
        """,
    )
    category: Optional[list[str]] = Field(
        None,
        description="""
        Specific fund category or categories. Always return a list, even for one value.
        Each value must be one of these exact strings as stored in the ETF database:
        'Alternative', 'Alternatives', 'Blend', 'Bonds', 'Cash',
        'Commercial Real Estate', 'Commodities Broad Basket', 'Communications',
        'Consumer Discretionary', 'Consumer Staples', 'Corporate Bonds', 'Currencies',
        'Derivatives', 'Developed Markets', 'Emerging Markets', 'Energy', 'Equities',
        'Factors', 'Financials', 'Fixed Income', 'Frontier Markets', 'Government Bonds',
        'Growth', 'Health Care', 'High Yield Bonds', 'Industrials',
        'Inflation-Protected Securities', 'Investment Grade Bonds',
        'Large Blend', 'Large Cap', 'Materials', 'Micro Cap', 'Mid Cap',
        'Money Market Instruments', 'Municipal Bonds', 'REITs',
        'Real Estate Development', 'Real Estate Services', 'Residential Real Estate',
        'Small Cap', 'Technology', 'Trading', 'Treasury Bonds', 'Utilities', 'Value'.
        IMPORTANT: 'Dividend Growth' is NOT a valid category value — do not set it.
        Only set when the user names a category matching one of the values above exactly.
        Return null otherwise.
        """,
    )
    exchange: Optional[list[str]] = Field(
        None,
        description="""
        Exchange code(s). Always return a list, even for one value.
        Each value must be one of these exact strings as stored in the ETF database:
        'AMS', 'AQS', 'ASE', 'ASX', 'ATH', 'BER', 'BRU', 'BTS', 'BUD', 'CPH',
        'DOH', 'DUS', 'EBS', 'FRA', 'GER', 'HAM', 'HAN', 'HEL', 'ICE', 'IST',
        'JPX', 'KSC', 'LIS', 'LIT', 'LSE', 'MCE', 'MCX', 'MEX', 'MIL', 'MUN',
        'NCM', 'NEO', 'NGM', 'NIM', 'NMS', 'NYQ', 'OSL', 'PAR', 'PCX', 'PNK',
        'PRA', 'SAU', 'SES', 'SET', 'STO', 'TAI', 'TLV', 'TOR', 'TWO', 'VIE'.
        US exchanges are: ASE, NCM, NIM, NMS, NYQ, PCX, PNK.
        Only set when the user names specific exchanges or a named group. Return null otherwise.
        """,
    )
    cleaned_query: str = Field(
        ...,
        description="""
        The user's question with entity mentions removed, suitable for semantic vector search.
        Keep enough content to make a meaningful search.
        Example: 'What VanEck ETFs focus on dividend growth?' → 'ETFs that focus on dividend growth'.
        If stripping entities leaves fewer than 3 words, return the full original query.
        """,
    )


class FredFilters(BaseModel):
    category_name: Optional[str] = Field(
        None,
        description="""
        FRED category name as stored in the database. Must be one of these exact strings:
        'Component Shares of GDP per Capita (Constant Prices)',
        'Component Shares of GDP per Capita (Current Prices)',
        'Construction',
        'Current Price GDP, Capital and Total Factor Productivity',
        'Daily Federal Funds Rate, 1928-54',
        'Data on the nominal term structure model from Kim and Wright',
        'Distribution of Commodities',
        'Economic Policy Uncertainty',
        'Exchange Rates',
        'Exchange Rates and GDP Price Levels',
        'Financial Status of Business',
        'Foreign Trade',
        'GDP per Capita (Current Prices)',
        'Government and Finance',
        'Gross Domestic Income, Adjustments for Changes in Terms of Trade',
        'Historical Federal Reserve Data',
        'Income and Employment',
        'Interest Rates',
        'Leading Indicators',
        'Money and Banking',
        'National Accounts-Based Variables',
        'New England Textile Industry, 1815-1860',
        'Openness',
        'Population',
        'Price Levels of GDP, Consumption, Government, and Investment',
        'Price Levels, Expenditure Categories and Capital',
        'Prices',
        'Production of Commodities',
        'Purchasing Power Parity',
        'Purchasing Power Parity Converted GDP',
        'Ratio of GNP to GDP',
        'Real GDP per Capita (Constant Prices)',
        'Real GDP per Capita Relative to U.S.',
        'Real GDP per Equivalent Adult',
        'Real GDP per Hour Worked by Employees',
        'Real GDP per Person Counted in Total Employment',
        'Real GDP per Person Engaged',
        'Real GDP per Worker',
        'Real GDP, Employment and Population Levels',
        'Recession Probabilities',
        'Savings and Investment',
        'Section 1. General Statistics of All Banks in the United States',
        'Section 2. Assets and Liabilities of All Member Banks',
        'Security Markets',
        'Shares in Output-side Real GDP at Current Purchasing Power Parities',
        'Sticky Wages and Comovement',
        'Stocks of Commodities',
        'The Effects of the 1930s HOLC "Redlining" Maps',
        'Transportation and Public Utilities',
        'U.S. Survey of Working Arrangements and Attitudes',
        'Volume of Transactions',
        'Weekly U.S. and State Bond Prices, 1855-1865'.
        Only set when the user names a specific FRED category matching one of the above.
        Return None otherwise.
        """,
    )
    series_id: Optional[str] = Field(
        None,
        description="""
        Exact FRED series identifier in uppercase (e.g. 'UNRATE', 'GDP', 'CPIAUCSL').
        Only set when the user provides an exact series ID verbatim. Return None otherwise.
        """,
    )
    frequency: Optional[str] = Field(
        None,
        description="""
        Data release frequency as stored in the database. Must be one of these exact strings:
        'Annual', 'Annual, As of January 1', 'Annual, As of July 1', 'Annual, End of Period',
        'Annual, End of Year', 'Daily', 'Daily, 7-Day', 'Monthly',
        'Monthly, As of 15th of the Month', 'Monthly, Beginning of Month',
        'Monthly, End of Month', 'Monthly, End of Period',
        'Monthly, Middle and End of the Month', 'Monthly, Middle of Month',
        "Monthly, Saturday Nearest Month's End", 'Quarterly',
        'Quarterly, Beginning of Period', 'Quarterly, End of Quarter',
        'Semiannual, End of Period', 'Weekly', 'Weekly, As of Wednesday',
        'Weekly, Ending Wednesday', '10 Year'.
        Map user language: 'daily' → 'Daily', 'weekly' → 'Weekly',
        'monthly' → 'Monthly', 'quarterly' → 'Quarterly', 'annual'/'yearly' → 'Annual'.
        Only set when the user explicitly asks about a specific frequency. Return None otherwise.
        """,
    )
    seasonal_adjustment: Optional[str] = Field(
        None,
        description="""
        Seasonal adjustment status. Must be exactly one of:
        'Seasonally Adjusted', 'Not Seasonally Adjusted'.
        Map 'SA'/'seasonally adjusted' → 'Seasonally Adjusted';
        'NSA'/'not seasonally adjusted'/'unadjusted' → 'Not Seasonally Adjusted'.
        Return None if not mentioned.
        """,
    )
    popularity_op: Optional[str] = Field(
        None,
        description="""
        Comparison operator for popularity filter: '$gt', '$gte', '$lt', '$lte'.
        Only set when the user mentions a popularity threshold. Return None otherwise.
        """,
    )
    popularity_value: Optional[int] = Field(
        None,
        description="""
        Integer popularity threshold paired with popularity_op.
        Popularity ranges from 0 to 87 in this database.
        Return None if popularity is not mentioned.
        """,
    )
    last_updated: Optional[str] = Field(
        None,
        description="ISO date string YYYY-MM-DD. Return None if not mentioned.",
    )
    last_updated_op: Optional[str] = Field(
        None,
        description="'$gte' for 'after', '$lte' for 'before'. Paired with last_updated.",
    )
    observation_end: Optional[str] = Field(
        None,
        description="""
        Absolute ISO date (YYYY-MM-DD) for filtering series by how recent their latest
        observation is. Set this when the user constrains data recency — e.g. 'observations
        within 1 year from today', 'series still being updated', 'data ending after 2020'.
        Resolve relative phrases against the current date given in the system prompt (e.g.
        'within 1 year from today' -> today minus one year). Return None when the user does
        not constrain observation recency.
        """,
    )
    observation_end_op: Optional[str] = Field(
        None,
        description="""
        Operator paired with observation_end: '$gte' for 'within / after / since / still
        updated' (latest observation on or after the date), '$lte' for 'ended before'.
        Default to '$gte' for recency phrases. Return None when observation_end is None.
        """,
    )
    cleaned_query: str = Field(
        ...,
        description="User question with FRED entity mentions removed.",
    )


class CodeRepoFilters(BaseModel):
    account: Optional[str] = Field(
        None,
        description="""
        GitHub account name. Must be exactly one of: 'troystribling', 'glyfish'.
        Only set when the user explicitly names an account. Return None otherwise.
        """,
    )
    repo: Optional[str] = Field(
        None,
        description="""
        GitHub repository name as stored in the database. Must be one of these exact strings:
        'BAP3', 'BLEBond', 'BlueBeacon', 'BlueCap', 'BlueCap-ObjC',
        'CBPeripheralManager-Demo', 'DetectPencil', 'Financial-Models-Numerical-Methods',
        'FutureLocation', 'GPUImage', 'HueSwitch-ObjC', 'LRResty', 'LocationTest',
        'MCMC', 'MailCore', 'MemoryMappedFileObjC', 'MemoryMappedFileSwift',
        'NN', 'NestPWN', 'PID', 'PracticeSessions', 'Principia', 'PyMC',
        'Robinhood', 'RobinhoodShell', 'Rpi_StartKit', 'Rpi_StartKit_Swift',
        'Sano', 'SimpleFutures', 'Stochastic.jl', 'Studium', 'Studium-ObjC',
        'Swift-Errors', 'WaitTime', 'acts_as_aln', 'aethyr', 'aethyr_agent',
        'agent_linux', 'agent_xmpp', 'agent_xmpp_orig', 'agentic', 'alef',
        'alpaca', 'alpaca-backtrader-api', 'alpaca-trade-api-python',
        'arduino-examples', 'autobahn-python', 'backtrader', 'bluecap-arduino',
        'bluecap-arduino-examples', 'cpp-ethereum', 'cryptocoins', 'data_examples',
        'data_sink', 'dotfiles', 'ejabberd', 'enstrophy', 'entropy',
        'ep-chan-book-algo-trading', 'evma_xmlpushparser', 'exempli', 'fbm',
        'gnosus-xmpp', 'hackerrank', 'has_ancestor', 'hue-switch-arduino', 'huebi',
        'iCircuitModels', 'iOSPorts', 'imaginaryProducts', 'imaginaryProductsSite',
        'ios-alethzero', 'ios-etherium', 'kinect_machine', 'libetpan', 'meida',
        'navi', 'neural_net', 'nordic-ble-sdk-examples', 'nordic-nrf8001', 'photio',
        'planb_site', 'prime_challenge', 'pyalgotrade', 'pylivetrader', 'route-me',
        'ruby-freenect', 'seeker1', 'shade', 'solidity_examples', 'streethak',
        'studium_ruby', 'troystribling.github.io', 'truffle_examples',
        'twitter_analysis', 'utils-arduino', 'virtadm', 'web3_examples',
        'website', 'zgomot', 'zipline'.
        Only set when the user names a specific repository. Return None otherwise.
        """,
    )
    ext: Optional[str] = Field(
        None,
        description="""
        File extension including leading dot as stored in the database.
        Map programming language names to extensions:
        'Python' → '.py', 'Ruby' → '.rb', 'JavaScript' → '.js',
        'Swift' → '.swift', 'C' → '.c', 'C++' → '.cpp',
        'Objective-C' → '.m', 'Erlang' → '.erl', 'Scala' → '.scala',
        'Lua' → '.lua', 'Julia' → '.jl', 'Solidity' → '.sol',
        'Shell'/'Bash' → '.sh', 'Perl' → '.pl', 'LaTeX' → '.tex',
        'SQL' → '.sql', 'Jupyter'/'notebook' → '.ipynb',
        'YAML' → '.yaml', 'JSON' → '.json', 'Markdown' → '.md',
        'HTML' → '.html', 'CSS' → '.css'.
        Other common stored values: '.h', '.hpp', '.mm', '.rb', '.rake', '.gemspec',
        '.erl', '.hrl', '.yml', '.xml', '.txt', '.sh', '.zsh', '.rst', '.svg'.
        Only set when the user mentions a specific language or file type. Return None otherwise.
        """,
    )
    cleaned_query: str = Field(
        ...,
        description="User question with account/repo/language mentions removed.",
    )


class ResearchLibraryFilters(BaseModel):
    shelf: Optional[str] = Field(
        None,
        description="""
        Library shelf identifier. Must be exactly one of:
        'jaynes' (papers by E. T. Jaynes),
        'notes' (research notes by Troy Stribling),
        'posts' (blog posts by Troy Stribling),
        'publications' (published academic papers by Troy Stribling),
        'reading_list' (papers by various external authors).
        Map user language: 'Jaynes' → 'jaynes', 'notes'/'research notes' → 'notes',
        'blog'/'posts' → 'posts', 'publications'/'papers'/'academic' → 'publications',
        'reading list'/'external' → 'reading_list'.
        Only set when the user explicitly names a shelf or collection. Return None otherwise.
        """,
    )
    title: Optional[str] = Field(
        None,
        description="""
        Document title with spelling corrected.
        Only set when the user names a specific document title.
        Correct obvious misspellings but otherwise preserve the user's phrasing.
        Return None if the user is not referring to a specific document.
        """,
    )
    authors: Optional[str] = Field(
        None,
        description="""
        Author name with spelling corrected.
        Only set when the user explicitly names an author.
        Correct obvious misspellings (e.g. 'Janes' → 'E. T. Jaynes',
        'Troy Stripling' → 'Troy Stribling').
        Return None if no author is mentioned.
        """,
    )
    cleaned_query: str = Field(
        ...,
        description="User question with shelf/title/author mentions removed.",
    )


# ---------- where-dict converters ----------

def _in_filter(key: str, val: str | list[str] | None) -> dict | None:
    """Return a ChromaDB equality or $in filter for a field, or None if val is empty."""
    if not val:
        return None
    if isinstance(val, list):
        val = [v for v in val if v]
        if not val:
            return None
        if len(val) == 1:
            return {key: val[0]}
        return {key: {"$in": val}}
    return {key: val}


def etf_filters_to_where(f: ETFFilters) -> Optional[dict]:
    parts = [
        _in_filter("family", f.family),
        _in_filter("category_group", f.category_group),
        _in_filter("category", f.category),
        _in_filter("exchange", f.exchange),
    ]
    conditions = [p for p in parts if p is not None]
    if not conditions:
        return None
    if len(conditions) == 1:
        return conditions[0]
    return {"$and": conditions}


def fred_filters_to_where(f: FredFilters) -> Optional[dict]:
    conditions: dict = {}
    if f.category_name:
        conditions["category_name"] = f.category_name
    if f.series_id:
        conditions["series_id"] = f.series_id
    if f.frequency:
        conditions["frequency"] = f.frequency
    if f.seasonal_adjustment:
        conditions["seasonal_adjustment"] = f.seasonal_adjustment
    if f.popularity_op and f.popularity_value is not None:
        conditions["popularity"] = {f.popularity_op: f.popularity_value}
    if f.observation_end and f.observation_end_op:
        end_int = _iso_to_yyyymmdd(f.observation_end)
        if end_int is not None:
            conditions["observation_end_int"] = {f.observation_end_op: end_int}
    if f.last_updated:
        # Range comparisons in Chroma require the numeric YYYYMMDD field, not the
        # raw string (a string operand raises ValueError at query time).
        updated_int = _iso_to_yyyymmdd(f.last_updated)
        if updated_int is not None:
            conditions["last_updated_int"] = {f.last_updated_op or "$gte": updated_int}
    return conditions or None


def code_repo_filters_to_where(f: CodeRepoFilters) -> Optional[dict]:
    conditions: dict = {}
    if f.account:
        conditions["account"] = f.account
    if f.repo:
        conditions["repo"] = f.repo
    if f.ext:
        conditions["ext"] = f.ext
    return conditions or None


def research_library_filters_to_where(f: ResearchLibraryFilters) -> Optional[dict]:
    conditions: dict = {}
    if f.shelf:
        conditions["shelf"] = f.shelf
    if f.title:
        conditions["title"] = f.title
    if f.authors:
        conditions["authors"] = f.authors
    return conditions or None


# ---------- extraction prompts ----------

_ETF_SYSTEM = """
You extract structured metadata filters from ETF search queries.
Your output drives a ChromaDB metadata filter and a semantic vector search.

Rules:
- Only extract a field when the user clearly mentions that entity.
- For fund family names, always use the full canonical form (see field descriptions).
- For category_group and category, you MUST use only the exact strings listed in the field
  descriptions — any other value will produce zero results. If no listed value matches what
  the user said, return null for that field and let the vector search handle it.
- 'Dividend Growth' is NOT a valid category value — never set category='Dividend Growth'.
- All filter fields accept either a single string or a list of strings (SQL IN equivalent).
  Use a list when the user names multiple values or a named group (e.g. 'US exchanges').
  US exchanges are: ASE, NCM, NIM, NMS, NYQ, PCX, PNK.
- If uncertain about any value, return null and let the vector search handle it.
- cleaned_query must retain enough content for a meaningful vector search (at least 3 words).
"""

_FRED_SYSTEM = """
You extract structured metadata filters from FRED economic data search queries.
Your output drives a ChromaDB metadata filter and a semantic vector search.

Rules:
- Only extract series_id when the user states an exact FRED ID (e.g. UNRATE, GDP).
- Only extract category_name when the user names a specific FRED category matching the valid list.
- Only extract frequency when the user explicitly mentions a release frequency (daily, monthly, etc.).
- Only extract seasonal_adjustment when the user mentions SA/NSA or seasonal adjustment status.
- For popularity, only extract when the user explicitly mentions a threshold number (max 87).
- Only extract observation_end / observation_end_op when the user constrains data recency
  (e.g. 'observations within 1 year from today', 'series still being updated', 'data ending
  after 2020'). observation_end is an absolute ISO date (YYYY-MM-DD); resolve relative phrases
  against today's date, provided below. Use '$gte' for 'within / after / since / still updated'
  and '$lte' for 'ended before'.
- If uncertain about any value, return null and let the vector search handle it.
- cleaned_query must retain enough content for a meaningful vector search.

Examples (resolve relative dates against today's date, provided below):
- "US GDP series with observations within 1 year from today"
    → observation_end = (today − 1 year), observation_end_op = "$gte",
      cleaned_query = "US GDP series"
- "unemployment data that is still being updated"
    → observation_end = (today − 1 year), observation_end_op = "$gte",
      cleaned_query = "unemployment data"
- "inflation series with data ending after 2020"
    → observation_end = "2020-01-01", observation_end_op = "$gte",
      cleaned_query = "inflation series"
- "discontinued indicators that ended before 1990"
    → observation_end = "1990-01-01", observation_end_op = "$lte",
      cleaned_query = "discontinued indicators"
- "monthly CPI for all urban consumers"
    → no observation_end (no recency constraint), frequency = "Monthly",
      cleaned_query = "CPI for all urban consumers"
"""

_CODE_SYSTEM = """
You extract structured metadata filters from code repository search queries.
Your output drives a ChromaDB metadata filter and a semantic vector search.

Rules:
- Only extract account/repo when the user explicitly names them.
- Map programming language names to file extensions.
- cleaned_query must retain enough content for a meaningful vector search.
"""

_RESEARCH_SYSTEM = """
You extract structured metadata filters from research library search queries.
Your output drives a ChromaDB metadata filter and a semantic vector search.

Rules:
- Only extract shelf when the user names a collection or shelf — use exact stored identifiers.
- Only extract title when the user names a specific document — correct misspellings.
- Only extract authors when the user explicitly names an author — correct misspellings.
- Do NOT extract topic or tags — those are not supported filter fields.
- If uncertain about any value, return null and let the vector search handle it.
- cleaned_query must retain enough content for a meaningful vector search.
"""


def _make_prompt(system: str) -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", "{request}"),
    ])


# ---------- async extraction functions ----------
@traceable(run_type="chain", name="extract_etf_filters")
async def extract_etf_filters(request: str) -> tuple[Optional[dict], str]:
    cleaned, where = build_filter_and_query(request)
    if where is not None:
        logger.info(f"ETF filters (regex): where={where} query={cleaned!r}")
        return where, cleaned

    try:
        llm = filter_llm_model().with_structured_output(ETFFilters)
        prompt = _make_prompt(_ETF_SYSTEM)
        result = cast(ETFFilters, await (prompt | llm).ainvoke({"request": request}))
        where = etf_filters_to_where(result)
        logger.info(f"ETF filters (llm): where={where} query={result.cleaned_query!r}")
        return where, result.cleaned_query
    except Exception as e:
        logger.warning(f"extract_etf_filters failed: {e}")
        return None, request


@traceable(run_type="chain", name="extract_fred_filters")
async def extract_fred_filters(request: str) -> tuple[Optional[dict], str]:
    cleaned, where = build_filter_and_query(request)
    if where is not None:
        logger.info(f"FRED filters (regex): where={where} query={cleaned!r}")
        return where, cleaned

    try:
        llm = filter_llm_model().with_structured_output(FredFilters)
        system = f"{_FRED_SYSTEM}\nToday's date is {date.today().isoformat()}."
        prompt = _make_prompt(system)
        result = cast(FredFilters, await (prompt | llm).ainvoke({"request": request}))
        where = fred_filters_to_where(result)
        logger.info(f"FRED filters (llm): where={where} query={result.cleaned_query!r}")
        return where, result.cleaned_query
    except Exception as e:
        logger.warning(f"extract_fred_filters failed: {e}")
        return None, request


@traceable(run_type="chain", name="extract_code_repo_filters")
async def extract_code_repo_filters(request: str) -> tuple[Optional[dict], str]:
    cleaned, where = build_filter_and_query(request)
    if where is not None:
        logger.info(f"Code repo filters (regex): where={where} query={cleaned!r}")
        return where, cleaned

    try:
        llm = filter_llm_model().with_structured_output(CodeRepoFilters)
        prompt = _make_prompt(_CODE_SYSTEM)
        result = cast(CodeRepoFilters, await (prompt | llm).ainvoke({"request": request}))
        where = code_repo_filters_to_where(result)
        logger.info(f"Code repo filters (llm): where={where} query={result.cleaned_query!r}")
        return where, result.cleaned_query
    except Exception as e:
        logger.warning(f"extract_code_repo_filters failed: {e}")
        return None, request


@traceable(run_type="chain", name="extract_research_library_filters")
async def extract_research_library_filters(request: str) -> tuple[Optional[dict], str]:
    cleaned, where = build_filter_and_query(request)
    if where is not None:
        logger.info(f"Research library filters (regex): where={where} query={cleaned!r}")
        return where, cleaned

    try:
        llm = filter_llm_model().with_structured_output(ResearchLibraryFilters)
        prompt = _make_prompt(_RESEARCH_SYSTEM)
        result = cast(ResearchLibraryFilters, await (prompt | llm).ainvoke({"request": request}))
        where = research_library_filters_to_where(result)
        logger.info(f"Research library filters (llm): where={where} query={result.cleaned_query!r}")
        return where, result.cleaned_query
    except Exception as e:
        logger.warning(f"extract_research_library_filters failed: {e}")
        return None, request
