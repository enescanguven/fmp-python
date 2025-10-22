"""Cryptocurrency response models."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class CryptoQuote(BaseModel):
    """Cryptocurrency quote response model."""

    symbol: str
    name: Optional[str] = None
    price: float
    changes_percentage: Optional[float] = Field(None, alias="changesPercentage")
    change: Optional[float] = None
    day_low: Optional[float] = Field(None, alias="dayLow")
    day_high: Optional[float] = Field(None, alias="dayHigh")
    year_high: Optional[float] = Field(None, alias="yearHigh")
    year_low: Optional[float] = Field(None, alias="yearLow")
    market_cap: Optional[float] = Field(None, alias="marketCap")
    price_avg50: Optional[float] = Field(None, alias="priceAvg50")
    price_avg200: Optional[float] = Field(None, alias="priceAvg200")
    exchange: Optional[str] = None
    volume: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = Field(None, alias="previousClose")
    timestamp: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class CryptoInfo(BaseModel):
    """Cryptocurrency information model."""

    symbol: str
    name: str
    exchange: Optional[str] = None
    ico_date: Optional[str] = Field(None, alias="icoDate")
    circulating_supply: Optional[float] = Field(None, alias="circulatingSupply")
    total_supply: Optional[float] = Field(None, alias="totalSupply")

    model_config = ConfigDict(populate_by_name=True)


class CryptoHistoricalPrice(BaseModel):
    """Cryptocurrency historical price model."""

    symbol: str
    date: str
    price: float
    volume: Optional[float] = None

    model_config = ConfigDict(populate_by_name=True)


class CryptoNews(BaseModel):
    """Cryptocurrency news article model."""

    symbol: str
    published_date: str = Field(alias="publishedDate")
    publisher: str
    title: str
    image: Optional[str] = None
    site: str
    text: str
    url: str

    model_config = ConfigDict(populate_by_name=True)
