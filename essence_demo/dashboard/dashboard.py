from flask import Blueprint
from flask import (
    render_template, 
    request,
)
from flask_login import (
    current_user,
    login_required,
)

from essence_demo.core import MarketService
from essence_demo.api import APIService
from essence_demo.graphs import GraphService

dash = Blueprint('dash', __name__)


@dash.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@dash.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    coin = request.form.get("coin")
    exchange = request.form.get("exchange")

    market = MarketService(coin=coin, exchange=exchange)

    api = APIService()
    df = api.get_bars(market)

    graph = GraphService()
    graph = graph.generate_graph(df, market)
    return render_template('dashboard.html', 
                           current_user=current_user, 
                           graph=graph, 
                           column_names=df.columns.values,
                           row_data=df.values.tolist(),
                           )
