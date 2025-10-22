"""Tests for company endpoints."""

from fmp.models import CompanyProfile, SearchResult, StockScreenerResult


def test_get_profile(client):
    """Test getting company profile."""
    profile = client.get_profile("AAPL")
    assert isinstance(profile, list)
    assert len(profile) > 0
    assert isinstance(profile[0], CompanyProfile)
    assert profile[0].symbol == "AAPL"
    assert profile[0].company_name is not None
    assert profile[0].sector is not None


def test_search_symbol(client):
    """Test searching by symbol."""
    results = client.search_symbol("Apple")
    assert isinstance(results, list)
    assert len(results) > 0
    assert isinstance(results[0], SearchResult)
    assert results[0].symbol is not None
    assert results[0].name is not None


def test_screen_stocks(client):
    """Test stock screener."""
    results = client.screen_stocks(
        sector="Technology",
        market_cap_more_than=1_000_000_000,
        limit=5
    )
    assert isinstance(results, list)
    assert len(results) <= 5
    if len(results) > 0:
        assert isinstance(results[0], StockScreenerResult)
