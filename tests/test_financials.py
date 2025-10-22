"""Tests for financial statements endpoints."""

from fmp.models import IncomeStatement, BalanceSheet, CashFlowStatement, FinancialGrowth


def test_get_income_statement(client):
    """Test getting income statement."""
    income_stmt = client.get_income_statement("AAPL", period="annual", limit=1)
    assert isinstance(income_stmt, list)
    assert len(income_stmt) > 0
    assert isinstance(income_stmt[0], IncomeStatement)
    assert income_stmt[0].symbol == "AAPL"
    assert income_stmt[0].revenue is not None
    assert income_stmt[0].net_income is not None


def test_get_balance_sheet(client):
    """Test getting balance sheet."""
    balance_sheet = client.get_balance_sheet("AAPL", period="annual", limit=1)
    assert isinstance(balance_sheet, list)
    assert len(balance_sheet) > 0
    assert isinstance(balance_sheet[0], BalanceSheet)
    assert balance_sheet[0].symbol == "AAPL"
    assert balance_sheet[0].total_assets is not None


def test_get_cash_flow_statement(client):
    """Test getting cash flow statement."""
    cash_flow = client.get_cash_flow_statement("AAPL", period="annual", limit=1)
    assert isinstance(cash_flow, list)
    assert len(cash_flow) > 0
    assert isinstance(cash_flow[0], CashFlowStatement)
    assert cash_flow[0].symbol == "AAPL"
    assert cash_flow[0].operating_cash_flow is not None


def test_get_financial_growth(client):
    """Test getting financial growth metrics."""
    growth = client.get_financial_growth("AAPL", period="annual", limit=1)
    assert isinstance(growth, list)
    assert len(growth) > 0
    assert isinstance(growth[0], FinancialGrowth)
    assert growth[0].symbol == "AAPL"
