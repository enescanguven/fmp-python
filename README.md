# fmp-python

A Python SDK for the Financial Modeling Prep API with full type safety via Pydantic models.

## Installation

```bash
# From PyPI (when published)
pip install fmp-python

# Or install from source
pip install -e .

# With dev dependencies
pip install -e ".[dev]"
```

## Quick Start

```python
import os
from fmp import FMPClient

client = FMPClient(api_key=os.getenv("FMP_API_KEY"))

# Company data
profile = client.get_profile("AAPL")
print(f"{profile[0].company_name}: ${profile[0].price}")

# Market data
quote = client.get_quote("AAPL")
print(f"Volume: {quote[0].volume:,}")

# Crypto
btc = client.get_crypto_quote("BTCUSD")
print(f"Bitcoin: ${btc[0].price:,.2f}")

# Financials
income = client.get_income_statement("AAPL", period="annual", limit=1)
print(f"Revenue: ${income[0].revenue:,.0f}")
```

## Features

**Company Data**
- Company profiles, search, screening
- CIK/CUSIP/ISIN lookup

**Market Data**
- Real-time quotes, historical prices
- Industry/sector performance & P/E ratios

**Cryptocurrency**
- Real-time quotes, historical data
- Crypto news

**Financial Statements**
- Income statement, balance sheet, cash flow
- Financial growth metrics

## API Methods

### Company
```python
client.get_profile(symbol)
client.search_symbol(query)
client.search_by_cik(cik)
client.screen_stocks(sector="Technology", market_cap_more_than=1e9, limit=10)
client.get_stock_list()
```

### Market
```python
client.get_quote(symbol)
client.get_historical_chart(symbol, interval="5min", from_date="2024-01-01")
client.get_historical_price(symbol, timeseries=30)
client.get_industry_pe(date="2024-10-01", exchange="NASDAQ")
```

### Crypto
```python
client.get_crypto_quote("BTCUSD")
client.get_crypto_list()
client.get_crypto_intraday("BTCUSD", interval="5min")
client.get_crypto_news_latest(limit=10)
```

### Financials
```python
client.get_income_statement(symbol, period="annual", limit=5)
client.get_balance_sheet(symbol, period="annual", limit=5)
client.get_cash_flow_statement(symbol, period="annual", limit=5)
client.get_financial_growth(symbol, period="annual", limit=5)
```

## Type Safety

All responses are Pydantic models with full type hints:

```python
from fmp.models import CompanyProfile, Quote, IncomeStatement

profile: list[CompanyProfile] = client.get_profile("AAPL")
print(profile[0].company_name)  # ✅ IDE autocomplete
print(profile[0].market_cap)     # ✅ Type checked
print(profile[0].sector)         # ✅ Validated
```

## Error Handling

```python
from fmp import FMPClient, FMPAPIError, FMPAuthError

try:
    profile = client.get_profile("AAPL")
except FMPAuthError:
    print("Invalid API key")
except FMPAPIError as e:
    print(f"API error: {e}")
```

## Requirements

- Python 3.8+
- httpx >= 0.27.0
- pydantic >= 2.0.0

## Links

- [FMP API Documentation](https://site.financialmodelingprep.com/developer/docs)
- [Get API Key](https://site.financialmodelingprep.com/developer/docs/pricing)
- [API Dashboard](https://site.financialmodelingprep.com/developer/docs/dashboard)

## TODO

- [ ] Publish to PyPI
- [ ] Add async support (httpx already supports it)
- [ ] Add rate limiting handling
- [ ] Add retry logic for failed requests
- [ ] Add more endpoint coverage (earnings, dividends, etc.)
- [ ] Add caching layer
- [ ] Add pagination support for large datasets
- [ ] Create comprehensive documentation site
- [ ] Add usage examples for all endpoints
- [ ] Add GitHub Actions CI/CD pipeline

## License

MIT
