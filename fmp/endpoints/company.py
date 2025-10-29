"""Company-related API endpoints."""

from typing import Any, Dict, List, Optional
from fmp.models.company import (
    CompanyProfile,
    SearchResult,
    StockScreenerResult,
    StockNews,
)


class CompanyEndpoints:
    """Company profile, search, and screening endpoints."""

    def get_profile(self, symbol: str) -> List[CompanyProfile]:
        """
        Get detailed company profile information.

        Retrieves comprehensive company data including stock price, market cap,
        business description, and fundamental metrics.

        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL')

        Returns:
            List of CompanyProfile objects
        """
        data = self._get("profile", params={"symbol": symbol})
        return [CompanyProfile(**item) for item in data]

    def search_symbol(self, query: str) -> List[SearchResult]:
        """
        Search for stocks by company name or symbol.

        Args:
            query: Company name or symbol to search for

        Returns:
            List of SearchResult objects
        """
        data = self._get("search-name", params={"query": query})
        return [SearchResult(**item) for item in data]

    def search_by_name(self, query: str) -> List[SearchResult]:
        """
        Search for ticker symbols by full or partial company name.

        Args:
            query: Full or partial company or asset name

        Returns:
            List of SearchResult objects
        """
        data = self._get("search-name", params={"query": query})
        return [SearchResult(**item) for item in data]

    def search_by_cik(self, cik: str) -> List[Dict[str, Any]]:
        """
        Retrieve company information by Central Index Key (CIK).

        Args:
            cik: Central Index Key of the company

        Returns:
            List containing company data associated with the CIK
        """
        return self._get("cik_search/" + cik)

    def search_by_cusip(self, cusip: str) -> List[Dict[str, Any]]:
        """
        Search for securities by CUSIP number.

        Args:
            cusip: CUSIP number of the financial security

        Returns:
            List containing company details associated with the CUSIP
        """
        return self._get("cusip", params={"cusip": cusip})

    def search_by_isin(self, isin: str) -> List[Dict[str, Any]]:
        """
        Search for securities by International Securities Identification Number (ISIN).

        Args:
            isin: ISIN of the financial security

        Returns:
            List containing company details associated with the ISIN
        """
        return self._get("search-isin", params={"isin": isin})

    def get_stock_list(self) -> List[Dict[str, Any]]:
        """
        Retrieve a comprehensive list of all available financial symbols.

        Returns:
            List of all stocks with symbol, name, price, exchange, and country information
        """
        return self._get("stock/list")

    def screen_stocks(
        self,
        market_cap_more_than: Optional[int] = None,
        market_cap_lower_than: Optional[int] = None,
        price_more_than: Optional[float] = None,
        price_lower_than: Optional[float] = None,
        beta_more_than: Optional[float] = None,
        beta_lower_than: Optional[float] = None,
        volume_more_than: Optional[int] = None,
        volume_lower_than: Optional[int] = None,
        dividend_more_than: Optional[float] = None,
        dividend_lower_than: Optional[float] = None,
        sector: Optional[str] = None,
        industry: Optional[str] = None,
        country: Optional[str] = None,
        exchange: Optional[str] = None,
        is_etf: Optional[bool] = None,
        is_fund: Optional[bool] = None,
        is_actively_trading: Optional[bool] = None,
        limit: Optional[int] = None,
    ) -> List[StockScreenerResult]:
        """
        Screen stocks based on various financial and market criteria.

        Args:
            market_cap_more_than: Minimum market capitalization
            market_cap_lower_than: Maximum market capitalization
            price_more_than: Minimum stock price
            price_lower_than: Maximum stock price
            beta_more_than: Minimum beta value
            beta_lower_than: Maximum beta value
            volume_more_than: Minimum trading volume
            volume_lower_than: Maximum trading volume
            dividend_more_than: Minimum dividend yield
            dividend_lower_than: Maximum dividend yield
            sector: Filter by sector (e.g., 'Technology')
            industry: Filter by industry (e.g., 'Consumer Electronics')
            country: Filter by country (e.g., 'US')
            exchange: Filter by exchange (e.g., 'NASDAQ')
            is_etf: Filter for ETFs
            is_fund: Filter for mutual funds
            is_actively_trading: Filter for actively trading stocks
            limit: Maximum number of results

        Returns:
            List of StockScreenerResult objects
        """
        params = {}

        if market_cap_more_than is not None:
            params["marketCapMoreThan"] = market_cap_more_than
        if market_cap_lower_than is not None:
            params["marketCapLowerThan"] = market_cap_lower_than
        if price_more_than is not None:
            params["priceMoreThan"] = price_more_than
        if price_lower_than is not None:
            params["priceLowerThan"] = price_lower_than
        if beta_more_than is not None:
            params["betaMoreThan"] = beta_more_than
        if beta_lower_than is not None:
            params["betaLowerThan"] = beta_lower_than
        if volume_more_than is not None:
            params["volumeMoreThan"] = volume_more_than
        if volume_lower_than is not None:
            params["volumeLowerThan"] = volume_lower_than
        if dividend_more_than is not None:
            params["dividendMoreThan"] = dividend_more_than
        if dividend_lower_than is not None:
            params["dividendLowerThan"] = dividend_lower_than
        if sector is not None:
            params["sector"] = sector
        if industry is not None:
            params["industry"] = industry
        if country is not None:
            params["country"] = country
        if exchange is not None:
            params["exchange"] = exchange
        if is_etf is not None:
            params["isEtf"] = str(is_etf).lower()
        if is_fund is not None:
            params["isFund"] = str(is_fund).lower()
        if is_actively_trading is not None:
            params["isActivelyTrading"] = str(is_actively_trading).lower()
        if limit is not None:
            params["limit"] = limit

        data = self._get("company-screener", params=params)
        return [StockScreenerResult(**item) for item in data]

    def search_stock_news(
        self,
        symbols: str,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[StockNews]:
        """
        Search for news articles related to specific stock symbols.

        Find specific stock news by entering a ticker symbol to track the latest
        developments and news coverage.

        Args:
            symbols: Stock ticker symbol(s) to search for news (e.g., 'AAPL')
            page: Page number for pagination (default: 0)
            limit: Number of results per page (default: 20)

        Returns:
            List of StockNews objects containing news articles
        """
        params = {"symbols": symbols}

        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        data = self._get("news/stock", params=params)
        return [StockNews(**item) for item in data]
