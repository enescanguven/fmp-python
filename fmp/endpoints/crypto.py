"""Cryptocurrency API endpoints."""

from typing import List, Optional
from fmp.models.crypto import CryptoQuote, CryptoInfo, CryptoHistoricalPrice, CryptoNews


class CryptoEndpoints:
    """Cryptocurrency quotes, historical data, and news endpoints."""

    def get_crypto_quote(self, symbol: str) -> List[CryptoQuote]:
        """
        Get real-time quote for a cryptocurrency.

        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTCUSD', 'ETHUSD')

        Returns:
            List of CryptoQuote objects
        """
        data = self._get("quote", params={"symbol": symbol})
        return [CryptoQuote(**item) for item in data]

    def get_crypto_list(self) -> List[CryptoInfo]:
        """
        Get comprehensive list of all available cryptocurrencies.

        Returns:
            List of CryptoInfo objects
        """
        data = self._get("symbol/available-cryptocurrencies")
        return [CryptoInfo(**item) for item in data]

    def get_crypto_historical_price(
        self,
        symbol: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> List[CryptoHistoricalPrice]:
        """
        Get historical end-of-day prices for a cryptocurrency.

        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTCUSD')
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)

        Returns:
            List of CryptoHistoricalPrice objects
        """
        params = {"symbol": symbol}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self._get("historical-price-eod/light", params=params)
        return [CryptoHistoricalPrice(**item) for item in data]

    def get_crypto_intraday(
        self,
        symbol: str,
        interval: str = "1min",
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> List[CryptoHistoricalPrice]:
        """
        Get intraday price data for a cryptocurrency.

        Args:
            symbol: Cryptocurrency symbol (e.g., 'BTCUSD')
            interval: Time interval - '1min', '5min', '15min', '30min', '1hour'
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)

        Returns:
            List of CryptoHistoricalPrice objects with intraday data
        """
        params = {"symbol": symbol}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self._get(f"historical-chart/{interval}", params=params)

        result = []
        for item in data:
            result.append(
                CryptoHistoricalPrice(symbol=symbol, date=item["date"], price=item["close"], volume=item.get("volume"))
            )
        return result

    def get_crypto_news_latest(
        self,
        page: int = 0,
        limit: int = 20,
    ) -> List[CryptoNews]:
        """
        Get latest cryptocurrency news.

        Args:
            page: Page number for pagination (default: 0)
            limit: Number of articles per page (default: 20, max: 250)

        Returns:
            List of CryptoNews objects
        """
        params = {"page": page, "limit": limit}
        data = self._get("news/crypto-latest", params=params)
        return [CryptoNews(**item) for item in data]

    def search_crypto_news(
        self,
        symbols: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: int = 0,
        limit: int = 20,
    ) -> List[CryptoNews]:
        """
        Search cryptocurrency news by symbol.

        Args:
            symbols: Cryptocurrency symbol(s) (e.g., 'BTCUSD')
            from_date: Start date (YYYY-MM-DD format)
            to_date: End date (YYYY-MM-DD format)
            page: Page number for pagination (default: 0)
            limit: Number of articles per page (default: 20, max: 250)

        Returns:
            List of CryptoNews objects
        """
        params = {
            "symbols": symbols,
            "page": page,
            "limit": limit,
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self._get("news/crypto", params=params)
        return [CryptoNews(**item) for item in data]
