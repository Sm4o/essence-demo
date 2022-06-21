from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketService:
    coin: Optional[str] = "BTC"
    currency: Optional[str] = "USD"
    exchange: Optional[str] = "CBSE"

    def __post_init__(self) -> None:
        if self.currency is None:
            self.currency = "USD"  # Only USD supported via the Alpaca API
        if self.exchange is None:
            self.exchange = "CBSE"
        if self.coin is None:
            self.coin = "BTC"
