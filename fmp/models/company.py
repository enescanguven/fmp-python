"""Company-related response models."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CompanyProfile(BaseModel):
    """Company profile response model."""

    symbol: str
    price: float
    beta: Optional[float] = None
    vol_avg: Optional[int] = Field(None, alias="volAvg")
    mkt_cap: Optional[float] = Field(None, alias="mktCap")
    last_div: Optional[float] = Field(None, alias="lastDiv")
    range: Optional[str] = None
    changes: Optional[float] = None
    company_name: str = Field(alias="companyName")
    currency: Optional[str] = None
    cik: Optional[str] = None
    isin: Optional[str] = None
    cusip: Optional[str] = None
    exchange: Optional[str] = None
    exchange_short_name: Optional[str] = Field(None, alias="exchangeShortName")
    industry: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    ceo: Optional[str] = None
    sector: Optional[str] = None
    country: Optional[str] = None
    full_time_employees: Optional[str] = Field(None, alias="fullTimeEmployees")
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    dcf_diff: Optional[float] = Field(None, alias="dcfDiff")
    dcf: Optional[float] = None
    image: Optional[str] = None
    ipo_date: Optional[str] = Field(None, alias="ipoDate")
    default_image: Optional[bool] = Field(None, alias="defaultImage")
    is_etf: Optional[bool] = Field(None, alias="isEtf")
    is_actively_trading: Optional[bool] = Field(None, alias="isActivelyTrading")
    is_adr: Optional[bool] = Field(None, alias="isAdr")
    is_fund: Optional[bool] = Field(None, alias="isFund")

    model_config = ConfigDict(populate_by_name=True)


class SearchResult(BaseModel):
    """Company search result."""

    symbol: str
    name: str
    currency: Optional[str] = None
    stock_exchange: Optional[str] = Field(None, alias="stockExchange")
    exchange_short_name: Optional[str] = Field(None, alias="exchangeShortName")

    model_config = ConfigDict(populate_by_name=True)


class StockScreenerResult(BaseModel):
    """Stock screener result."""

    symbol: str
    company_name: str = Field(alias="companyName")
    market_cap: Optional[float] = Field(None, alias="marketCap")
    sector: Optional[str] = None
    industry: Optional[str] = None
    beta: Optional[float] = None
    price: Optional[float] = None
    last_annual_dividend: Optional[float] = Field(None, alias="lastAnnualDividend")
    volume: Optional[int] = None
    exchange: Optional[str] = None
    exchange_short_name: Optional[str] = Field(None, alias="exchangeShortName")
    country: Optional[str] = None
    is_etf: Optional[bool] = Field(None, alias="isEtf")
    is_actively_trading: Optional[bool] = Field(None, alias="isActivelyTrading")

    model_config = ConfigDict(populate_by_name=True)
