import json
from huobi.utils.time_service import get_current_timestamp

def dict_add_new(old_dict, new_dict):
    if old_dict  is None:
        old_dict = {}

    if new_dict and len(new_dict):
        for key_val, val in new_dict.items():
            if val:
                exist_val = old_dict.get(key_val, None)
                if exist_val and len(str(exist_val)):
                    pass
                else:
                    old_dict[key_val] = str(val)

    return old_dict

def request_kline_channel(symbol, interval, from_ts_second = None, to_ts_second = None):
    channel = dict()
    channel["req"] = "market." + symbol + ".kline." + interval
    channel["id"] = str(get_current_timestamp())
    if from_ts_second:
        channel["from"] = int(from_ts_second)
    if to_ts_second:
        channel["to"] = int(to_ts_second)
    return json.dumps(channel)


def request_trade_detail_channel(symbol):
    channel = dict()
    channel["req"] = "market." + symbol + ".trade.detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def request_price_depth_channel(symbol, step_type = "step0"):
    channel = dict()
    channel["req"] = "market." + symbol + ".depth." + step_type
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def request_market_detail_channel(symbol):
    channel = dict()
    channel["req"] = "market." + symbol + ".detail"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def request_account_list_channel(client_req_id = None):
    channel = dict()
    channel["op"] = "req"
    channel["topic"] = "accounts.list"
    channel["cid"] = str(client_req_id) if client_req_id else str(get_current_timestamp())
    return json.dumps(channel)

def request_order_list_channel(symbol, account_id, states_str= None, client_req_id = None, more_key={}):
    channel = dict()
    try:
        channel["op"] = "req"
        channel["account-id"] = account_id
        channel["topic"] = "orders.list"
        channel["symbol"] = symbol
        if states_str and len(states_str):
            channel["states"] = str(states_str)
        channel["cid"] = str(client_req_id) if client_req_id else str(get_current_timestamp())
        channel = dict_add_new(channel, more_key)

    except Exception as e:
        print(e)
    return json.dumps(channel)

def request_order_detail_channel(order_id, client_req_id = None):
    channel = dict()
    channel["op"] = "req"
    channel["topic"] = "orders.detail"
    channel["order-id"] = str(order_id)
    channel["cid"] = str(client_req_id) if client_req_id else str(get_current_timestamp())
    return json.dumps(channel)


def request_ticker_channel(symbol):
    channel = dict()
    channel["req"] = "market." + symbol + ".ticker"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)
