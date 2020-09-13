import datetime
import plotly
import plotly.graph_objs as go


def timestamp_to_time(timestamp_ms) -> datetime.date:
    timestamp_s = timestamp_ms / 1000.0
    time = datetime.datetime.fromtimestamp(timestamp_s)
    return time


def klines_to_ohcl(klines_list: list) -> dict:
    ohcl_dict = {
        "t": [timestamp_to_time(kline[0]) for kline in klines_list],
        "o": [kline[1] for kline in klines_list],
        "h": [kline[2] for kline in klines_list],
        "l": [kline[3] for kline in klines_list],
        "c": [kline[4] for kline in klines_list],
    }
    return ohcl_dict


def build_candlestick_graph(klines_list: dict) -> plotly.graph_objs:
    """Transform klines Binance API payload into a plotly graph

    Args:
        klines_list (dict): klines payload from the Binance API

    Returns:
        plotly.graph_objs: updated plotly candlestick graph
    """

    ohcl_dict = klines_to_ohcl(klines_list)
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=ohcl_dict["t"],
                open=ohcl_dict["o"],
                high=ohcl_dict["h"],
                low=ohcl_dict["l"],
                close=ohcl_dict["c"],
            )
        ]
    )
    return fig