from dataclasses import dataclass


@dataclass
class MarketService:
    coin: str = "BTC"
    currency: str = "USD"
    exchange: str = "CBSE"

    def __post_init__(self):
        if self.currency is None:
            self.currency = 'USD'  # Only USD supported via the Alpaca API
        if self.exchange is None:
            self.exchange = 'CBSE'
        if self.coin is None:
            self.coin = 'BTC'
