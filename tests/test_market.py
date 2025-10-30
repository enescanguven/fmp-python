"""Tests for market endpoints."""

from fmp.models import Quote, HistoricalPrice


def test_get_quote(client):
    """Test getting real-time quote."""
    quote = client.get_quote("AAPL")
    assert isinstance(quote, list)
    assert len(quote) > 0
    assert isinstance(quote[0], Quote)
    assert quote[0].symbol == "AAPL"
    assert quote[0].price is not None
    assert quote[0].volume is not None


def test_get_historical_chart(client):
    """Test getting historical chart data."""
    data = client.get_historical_chart("AAPL", interval="5min")
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], HistoricalPrice)
    assert data[0].date is not None
    assert data[0].close is not None


def test_get_historical_price_full(client):
    """Test getting full historical price data."""
    data = client.get_historical_price("AAPL", price_type="full", timeseries=5)
    assert isinstance(data, list)
    assert len(data) > 0
    assert "symbol" in data[0]


def test_get_historical_price_light(client):
    """Test getting light historical price data."""
    data = client.get_historical_price("AAPL", price_type="light", timeseries=5)
    assert isinstance(data, list)
    assert len(data) > 0
