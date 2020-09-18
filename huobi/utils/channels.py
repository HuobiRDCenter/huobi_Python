import json
from huobi.utils.time_service import get_current_timestamp
from huobi.constant import DepthStep


def kline_channel(symbol, interval):
    channel = dict()
    channel["sub"] = "market." + symbol + ".kline." + interval
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def trade_detail_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".trade.detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def price_depth_channel(symbol, step_type=DepthStep.STEP0):
    channel = dict()
    channel["sub"] = "market." + symbol + ".depth." + step_type
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def price_depth_bbo_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".bbo"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def orders_update_channel(symbol):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "orders#{symbol}".format(symbol=symbol)
    return json.dumps(channel)


def market_detail_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def accounts_update_channel(mode=0):
    channel = dict()
    channel["action"] = "sub"
    if mode is None:
        channel["ch"] = "accounts.update"
    else:
        channel["ch"] = "accounts.update#{mode}".format(mode=mode)
    return json.dumps(channel)


def mbp_increase_channel(symbol, levels):
    channel = dict()
    channel["sub"] = "market.{symbol}.mbp.{levels}".format(symbol=symbol, levels=levels)
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def mbp_full_channel(symbol, levels):
    channel = dict()
    channel["sub"] = "market.{symbol}.mbp.refresh.{levels}".format(symbol=symbol, levels=levels)
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def request_mbp_channel(symbol, levels):
    channel = dict()
    channel["req"] = "market.{symbol}.mbp.{levels}".format(symbol=symbol, levels=levels)
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def trade_clearing_channel(symbol="*"):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "trade.clearing#" + symbol
    return json.dumps(channel)
