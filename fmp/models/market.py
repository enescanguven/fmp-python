"""Market data response models."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class Quote(BaseModel):
    """Real-time quote response model."""

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
    volume: Optional[int] = None
    avg_volume: Optional[int] = Field(None, alias="avgVolume")
    open: Optional[float] = None
    previous_close: Optional[float] = Field(None, alias="previousClose")
    eps: Optional[float] = None
    pe: Optional[float] = None
    earnings_announcement: Optional[str] = Field(None, alias="earningsAnnouncement")
    shares_outstanding: Optional[int] = Field(None, alias="sharesOutstanding")
    timestamp: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class HistoricalPrice(BaseModel):
    """Historical price data point."""

    date: str
    open: float
    high: float
    low: float
    close: float
    adj_close: Optional[float] = Field(None, alias="adjClose")
    volume: int
    unadjusted_volume: Optional[int] = Field(None, alias="unadjustedVolume")
    change: Optional[float] = None
    change_percent: Optional[float] = Field(None, alias="changePercent")
    vwap: Optional[float] = None
    label: Optional[str] = None
    change_over_time: Optional[float] = Field(None, alias="changeOverTime")

    model_config = ConfigDict(populate_by_name=True)
