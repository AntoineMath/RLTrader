import datetime


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
