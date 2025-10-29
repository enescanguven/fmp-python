"""Financial statements API endpoints."""

from typing import List, Optional
from fmp.models.financials import (
    IncomeStatement,
    BalanceSheet,
    CashFlowStatement,
    FinancialGrowth,
)


class FinancialsEndpoints:
    """Financial statements, ratios, and growth metrics endpoints."""

    def get_income_statement(
        self,
        symbol: str,
        period: str = "annual",
        limit: Optional[int] = None,
    ) -> List[IncomeStatement]:
        """
        Get income statement for a company.

        Args:
            symbol: Stock ticker symbol
            period: 'annual' or 'quarter' (default: 'annual')
            limit: Number of statements to return

        Returns:
            List of IncomeStatement objects
        """
        params = {"symbol": symbol, "period": period}
        if limit:
            params["limit"] = limit

        data = self._get("income-statement", params=params)
        return [IncomeStatement(**item) for item in data]

    def get_balance_sheet(
        self,
        symbol: str,
        period: str = "annual",
        limit: Optional[int] = None,
    ) -> List[BalanceSheet]:
        """
        Get balance sheet for a company.

        Args:
            symbol: Stock ticker symbol
            period: 'annual' or 'quarter' (default: 'annual')
            limit: Number of statements to return

        Returns:
            List of BalanceSheet objects
        """
        params = {"symbol": symbol, "period": period}
        if limit:
            params["limit"] = limit

        data = self._get("balance-sheet-statement", params=params)
        return [BalanceSheet(**item) for item in data]

    def get_cash_flow_statement(
        self,
        symbol: str,
        period: str = "annual",
        limit: Optional[int] = None,
    ) -> List[CashFlowStatement]:
        """
        Get cash flow statement for a company.

        Args:
            symbol: Stock ticker symbol
            period: 'annual' or 'quarter' (default: 'annual')
            limit: Number of statements to return

        Returns:
            List of CashFlowStatement objects
        """
        params = {"symbol": symbol, "period": period}
        if limit:
            params["limit"] = limit

        data = self._get("cash-flow-statement", params=params)
        return [CashFlowStatement(**item) for item in data]

    def get_financial_growth(
        self,
        symbol: str,
        period: str = "annual",
        limit: Optional[int] = None,
    ) -> List[FinancialGrowth]:
        """
        Get financial growth metrics for a company.

        Args:
            symbol: Stock ticker symbol
            period: 'annual' or 'quarter' (default: 'annual')
            limit: Number of periods to return

        Returns:
            List of FinancialGrowth objects
        """
        params = {"symbol": symbol, "period": period}
        if limit:
            params["limit"] = limit

        data = self._get("financial-growth", params=params)
        return [FinancialGrowth(**item) for item in data]
