import json
from typing import Dict

import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder

# typing only
import pandas as pd
from essence_demo.core import MarketService


class GraphService:
    def generate_graph(
        self, df: pd.DataFrame, market: MarketService
    ) -> str:
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=df.index,
                    open=df["open"],
                    high=df["high"],
                    low=df["low"],
                    close=df["close"],
                )
            ]
        )
        fig.update_layout(
            title=f"Candlestick chart for ${market.coin}{market.currency} on Exchange {market.exchange}",
            xaxis_title="Date",
            yaxis_title=f"Price (${market.currency})",
        )
        return json.dumps(fig, cls=PlotlyJSONEncoder)
