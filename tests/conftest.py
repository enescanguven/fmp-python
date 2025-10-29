"""Shared pytest fixtures."""

import os
from pathlib import Path
import pytest
from dotenv import load_dotenv
from fmp import FMPClient

# Load .env from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


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
