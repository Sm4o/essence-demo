import json

from flask import Blueprint
from flask import (
    render_template, 
    request,
)
from flask_login import (
    current_user,
    login_required,
)
from alpaca_trade_api.rest import REST, TimeFrame 
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder
from dotenv import load_dotenv

# from essence_demo.views.views import ViewModel

dash = Blueprint('dash', __name__)


@dash.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@dash.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    coin = request.form.get("coin")
    if not coin:
        coin = "BTC"
    currency = "USD" 
    exchange = request.form.get("exchange")
    if not exchange:
        exchange = "CBSE"
    symbol = f"{coin}{currency}"
    api = REST()
    df = api.get_crypto_bars(symbol, TimeFrame.Hour, exchanges=[exchange]).df
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.index, 
            open=df['open'], 
            high=df['high'], 
            low=df['low'], 
            close=df['close'],
        )
    ])
    fig.update_layout(
        title=f"Candlestick chart for ${symbol}",
        xaxis_title="Date",
        yaxis_title=f"Price (${currency})",
    )
    graph = json.dumps(fig, cls=PlotlyJSONEncoder)
    return render_template('dashboard.html', 
                           current_user=current_user, 
                           graph=graph, 
                           column_names=df.columns.values,
                           row_data=df.values.tolist(),
                           )
