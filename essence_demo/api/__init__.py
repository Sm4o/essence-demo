from alpaca_trade_api.rest import REST, TimeFrame 

# typing only
from essence_demo.core import MarketService
import pandas as pd


class APIService:
    def __init__(self):
        self.api = REST()

    def get_bars(self, market: MarketService) -> pd.DataFrame:
        return self.api.get_crypto_bars(
            f"{market.coin}{market.currency}", 
            TimeFrame.Hour, 
            exchanges=[market.exchange]
        ).df.reset_index()

