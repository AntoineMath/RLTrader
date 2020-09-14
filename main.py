import dash
import dash_core_components as dcc
import dash_html_components as html
from binance.client import Client
from dash.dependencies import Input, Output

from rl_trader.data_processing import build_candlestick_graph, klines_to_ohcl

INTERVAL = 1000

client = Client()

dash_app = dash.Dash(title="RLTrader", update_title=None)
app = dash_app.server

dash_app.layout = html.Div(
    [dcc.Graph(id="live-graph"), dcc.Interval(id="graph-update", interval=INTERVAL)]
)


@dash_app.callback(
    Output("live-graph", component_property="figure"),
    [Input("graph-update", "n_intervals")],
)
def update_graph(n):
    klines = client.get_historical_klines(
        symbol="BTCUSDT", interval="1m", start_str="1H ago UTC"
    )
    graph = build_candlestick_graph(klines)
    return graph


if __name__ == "__main__":
    dash_app.run_server(debug=True)
