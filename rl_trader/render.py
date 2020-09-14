import plotly
import plotly.graph_objs as go

from rl_trader.data_processing import klines_to_ohcl


def build_candlestick_graph(klines_list: dict) -> plotly.graph_objs:
    """Transform klines Binance API payload into a plotly graph

    Args:
        klines_list (dict): klines payload from the Binance API

    Returns:
        plotly.graph_objs: updated plotly candlestick graph
    """

    ohcl_dict = klines_to_ohcl(klines_list)

    layout = {
        "title": "Reinforcement learning Trader",
        "xaxis": go.layout.XAxis(
            title=go.layout.xaxis.Title(text="Local time"),
            rangeslider={"visible": False},
        ),
        "yaxis": go.layout.YAxis(title=go.layout.yaxis.Title(text="BTC/USDT")),
        "width": 1000,
        "height": 800,
    }

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=ohcl_dict["t"],
                open=ohcl_dict["o"],
                high=ohcl_dict["h"],
                low=ohcl_dict["l"],
                close=ohcl_dict["c"],
            )
        ],
        layout=layout,
    )
    return fig
