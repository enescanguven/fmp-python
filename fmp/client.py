"""Main FMP API client."""

from typing import Any, Dict, Optional
import httpx
from fmp.exceptions import FMPAPIError, FMPAuthError
from fmp.endpoints.company import CompanyEndpoints
from fmp.endpoints.market import MarketEndpoints
from fmp.endpoints.crypto import CryptoEndpoints
from fmp.endpoints.financials import FinancialsEndpoints


class FMPClient(CompanyEndpoints, MarketEndpoints, CryptoEndpoints, FinancialsEndpoints):
    """
    Main client for interacting with the Financial Modeling Prep API.

    Args:
        api_key: Your FMP API key
        base_url: Base URL for the API (default: https://financialmodelingprep.com/api/v3)
        timeout: Request timeout in seconds (default: 30.0)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://financialmodelingprep.com/api/v3",
        timeout: float = 30.0,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close the HTTP client."""
        self._client.close()

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make a request to the FMP API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters

        Returns:
            JSON response data

        Raises:
            FMPAuthError: If authentication fails
            FMPAPIError: If API returns an error
        """
        if params is None:
            params = {}

        params["apikey"] = self.api_key
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self._client.request(method, url, params=params)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict) and "Error Message" in data:
                raise FMPAPIError(data["Error Message"], response.status_code)

            return data

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise FMPAuthError("Invalid API key", 401)
            elif e.response.status_code == 403:
                raise FMPAuthError("Access forbidden - check your API key permissions", 403)
            else:
                raise FMPAPIError(
                    f"API request failed: {e.response.text}",
                    e.response.status_code,
                )
        except httpx.RequestError as e:
            raise FMPAPIError(f"Request failed: {str(e)}")

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request to the API."""
        return self._request("GET", endpoint, params)
