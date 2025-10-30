"""Market data API endpoints."""

from typing import Any, Dict, List, Optional
from fmp.models.market import Quote, HistoricalPrice


class MarketEndpoints:
    """Market data, historical prices, and industry performance endpoints."""

    def get_quote(self, symbol: str) -> List[Quote]:
        """
        Get real-time stock quote.

        Args:
            symbol: Stock ticker symbol

        Returns:
            List of Quote objects
        """
        data = self._get("quote", params={"symbol": symbol})
        return [Quote(**item) for item in data]

    def get_historical_chart(
        self,
        symbol: str,
        interval: str = "1day",
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> List[HistoricalPrice]:
        """
        Get historical price data for a symbol.

        Args:
            symbol: Stock ticker symbol
            interval: Time interval - '1min', '5min', '15min', '30min', '1hour', '4hour', '1day'
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)

        Returns:
            List of HistoricalPrice objects
        """
        params = {"symbol": symbol}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self._get(f"historical-chart/{interval}", params=params)
        return [HistoricalPrice(**item) for item in data]

    def get_historical_price(
        self,
        symbol: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        timeseries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get daily historical price data.

        Args:
            symbol: Stock ticker symbol
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)
            timeseries: Number of days to retrieve

        Returns:
            Dictionary containing symbol and historical price data
        """
        params = {"symbol": symbol}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if timeseries:
            params["timeseries"] = timeseries

        return self._get("historical-price-eod/light", params=params)

    def get_industry_pe(
        self,
        date: str,
        exchange: Optional[str] = None,
        industry: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get price-to-earnings ratios for industries.

        Args:
            date: Date in YYYY-MM-DD format
            exchange: Stock exchange (e.g., 'NASDAQ', 'NYSE')
            industry: Specific industry to filter by

        Returns:
            List of industries with their P/E ratios
        """
        params = {"date": date}
        if exchange:
            params["exchange"] = exchange
        if industry:
            params["industry"] = industry

        return self._get("industry_pe", params=params)

    def get_sector_pe(
        self,
        date: str,
        exchange: Optional[str] = None,
        sector: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get price-to-earnings ratios for sectors.

        Args:
            date: Date in YYYY-MM-DD format
            exchange: Stock exchange (e.g., 'NASDAQ', 'NYSE')
            sector: Specific sector to filter by

        Returns:
            List of sectors with their P/E ratios
        """
        params = {"date": date}
        if exchange:
            params["exchange"] = exchange
        if sector:
            params["sector"] = sector

        return self._get("sector_pe", params=params)

    def get_industry_performance(
        self,
        date: str,
        exchange: Optional[str] = None,
        industry: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get daily performance data for industries.

        Args:
            date: Date in YYYY-MM-DD format
            exchange: Stock exchange to filter by
            industry: Specific industry to filter by

        Returns:
            List of industries with average percentage changes
        """
        params = {"date": date}
        if exchange:
            params["exchange"] = exchange
        if industry:
            params["industry"] = industry

        return self._get("sector-performance", params=params)

    def get_historical_sector_pe(
        self,
        sector: str,
        exchange: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get historical price-to-earnings ratios for a sector.

        Args:
            sector: Sector name (e.g., 'Energy', 'Technology')
            exchange: Stock exchange to filter by
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)

        Returns:
            List of historical P/E ratios for the sector
        """
        params = {"sector": sector}
        if exchange:
            params["exchange"] = exchange
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._get("historical-sector-performance", params=params)
