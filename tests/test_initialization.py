"""Tests for client initialization."""

from fmp import FMPClient


def test_client_initialization(api_key):
    """Test client can be initialized with API key."""
    client = FMPClient(api_key=api_key)
    assert client.api_key == api_key
    assert client.base_url == "https://financialmodelingprep.com/api/v3"
    assert client.timeout == 30.0
    client.close()


def test_client_custom_base_url(api_key):
    """Test client with custom base URL."""
    client = FMPClient(api_key=api_key, base_url="https://custom.api.com/v1")
    assert client.base_url == "https://custom.api.com/v1"
    client.close()


def test_client_custom_timeout(api_key):
    """Test client with custom timeout."""
    client = FMPClient(api_key=api_key, timeout=60.0)
    assert client.timeout == 60.0
    client.close()


def test_context_manager(api_key):
    """Test client works as context manager."""
    with FMPClient(api_key=api_key) as client:
        assert client.api_key == api_key
