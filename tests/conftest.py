"""Shared pytest fixtures."""

import os
import pytest
from dotenv import load_dotenv
from fmp import FMPClient

load_dotenv()


@pytest.fixture
def api_key():
    """Get API key from environment."""
    key = os.getenv("FMP_API_KEY")
    if not key:
        pytest.skip("FMP_API_KEY not set in environment")
    return key


@pytest.fixture
def client(api_key):
    """Create FMP client for tests."""
    client = FMPClient(api_key=api_key)
    yield client
    client.close()
