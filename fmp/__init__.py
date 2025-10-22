"""FMP Python SDK - A Python wrapper for the Financial Modeling Prep API."""

from fmp.client import FMPClient
from fmp.exceptions import FMPError, FMPAPIError, FMPAuthError
from fmp.models import (
    CompanyProfile,
    Quote,
    HistoricalPrice,
    SearchResult,
    StockScreenerResult,
    CryptoQuote,
    CryptoInfo,
    CryptoHistoricalPrice,
    CryptoNews,
    IncomeStatement,
    BalanceSheet,
    CashFlowStatement,
    FinancialGrowth,
)

__version__ = "0.1.0"
__all__ = [
    "FMPClient",
    "FMPError",
    "FMPAPIError",
    "FMPAuthError",
    "CompanyProfile",
    "Quote",
    "HistoricalPrice",
    "SearchResult",
    "StockScreenerResult",
    "CryptoQuote",
    "CryptoInfo",
    "CryptoHistoricalPrice",
    "CryptoNews",
    "IncomeStatement",
    "BalanceSheet",
    "CashFlowStatement",
    "FinancialGrowth",
]
