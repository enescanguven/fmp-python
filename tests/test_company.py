"""Tests for company endpoints."""

from fmp.models import CompanyProfile, SearchResult, StockScreenerResult, StockNews


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


def test_search_stock_news(client):
    """Test searching stock news."""
    results = client.search_stock_news("AAPL", limit=5)
    assert isinstance(results, list)
    assert len(results) > 0
    assert isinstance(results[0], StockNews)
    assert results[0].symbol == "AAPL"
    assert results[0].title is not None
    assert results[0].published_date is not None
    assert results[0].url is not None
    assert results[0].site is not None


def test_get_general_news_latest(client):
    """Test getting latest general news."""
    results = client.get_general_news_latest(limit=5)
    assert isinstance(results, list)
    assert len(results) > 0
    assert isinstance(results[0], StockNews)
    assert results[0].title is not None
    assert results[0].url is not None


def test_get_stock_news_latest(client):
    """Test getting latest stock news."""
    results = client.get_stock_news_latest(limit=5)
    assert isinstance(results, list)
    assert len(results) > 0
    assert isinstance(results[0], StockNews)
    assert results[0].title is not None
    assert results[0].url is not None
