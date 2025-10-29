"""Tests for cryptocurrency endpoints."""

import pytest
from fmp.models import CryptoQuote, CryptoInfo, CryptoHistoricalPrice, CryptoNews


def test_get_crypto_quote(client):
    """Test getting cryptocurrency quote."""
    quote = client.get_crypto_quote("BTCUSD")
    assert isinstance(quote, list)
    assert len(quote) > 0
    assert isinstance(quote[0], CryptoQuote)
    assert quote[0].symbol == "BTCUSD"
    assert quote[0].price is not None


@pytest.mark.skip(reason="Endpoint not available in v4 API")
def test_get_crypto_list(client):
    """Test getting cryptocurrency list."""
    cryptos = client.get_crypto_list()
    assert isinstance(cryptos, list)
    assert len(cryptos) > 0
    assert isinstance(cryptos[0], CryptoInfo)
    assert cryptos[0].symbol is not None
    assert cryptos[0].name is not None


def test_get_crypto_intraday(client):
    """Test getting intraday crypto data."""
    data = client.get_crypto_intraday("BTCUSD", interval="5min")
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], CryptoHistoricalPrice)
    assert data[0].price is not None


def test_get_crypto_news_latest(client):
    """Test getting latest crypto news."""
    news = client.get_crypto_news_latest(limit=5)
    assert isinstance(news, list)
    assert len(news) > 0
    assert isinstance(news[0], CryptoNews)
    assert news[0].title is not None
    assert news[0].url is not None


def test_search_crypto_news(client):
    """Test searching crypto news by symbol."""
    news = client.search_crypto_news("BTCUSD", limit=5)
    assert isinstance(news, list)
    assert len(news) > 0
    assert isinstance(news[0], CryptoNews)
    assert news[0].title is not None
