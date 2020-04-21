import json
from huobi.impl.utils.timeservice import get_current_timestamp
from huobi.model import DepthStep, MbpLevel


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


def price_depth_channel(symbol, step_type = DepthStep.STEP0):
    channel = dict()
    channel["sub"] = "market." + symbol + ".depth." + step_type
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def mbp_channel(symbol, levels):
    channel = dict()
    channel["sub"] = "market.{symbol}.mbp.{levels}".format(symbol=symbol, levels=levels)
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def full_mbp_channel(symbol, levels):
    channel = dict()
    channel["sub"] = "market.{symbol}.mbp.refresh.{levels}".format(symbol=symbol, levels=levels)
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def orders_update_channel(symbol):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "orders#{symbol}".format(symbol=symbol)
    return json.dumps(channel)

def price_depth_bbo_channel(symbol):
    channel = dict()
    channel["sub"] = "market." + symbol + ".bbo"
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
    channel["model"] = mode
    return json.dumps(channel)

def trade_clearing_channel(symbol="*"):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "trade.clearing#" + symbol
    return json.dumps(channel)

def accounts_update_channel(mode=0):
    channel = dict()
    channel["action"] = "sub"
    if mode is None:
        channel["ch"] = "accounts.update"
    else:
        channel["ch"] = "accounts.update#{mode}".format(mode=mode)
    return json.dumps(channel)

