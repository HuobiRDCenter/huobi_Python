import json
from huobi.impl.utils.timeservice import get_current_timestamp


def kline_channel(symbol, interval):
    channel = dict()
    channel["sub"] = "market." + symbol + ".kline." + interval
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def trade_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".trade.detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def price_depth_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".depth.step0"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def orders_channel(symbol):
    channel = dict()
    channel["op"] = "sub"
    channel["cid"] = str(get_current_timestamp())
    channel["topic"] = "orders." + symbol
    return json.dumps(channel)

def orders_update_new_channel(symbol):
    channel = dict()
    channel["op"] = "sub"
    channel["cid"] = str(get_current_timestamp())
    channel["topic"] = "orders." + symbol + ".update"
    print(channel)
    return json.dumps(channel)


def trade_statistics_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def account_channel(mode):
    channel = dict()
    channel["op"] = "sub"
    channel["cid"] = str(get_current_timestamp())
    channel["topic"] = "accounts"
    channel["mode"] = mode
    return json.dumps(channel)
