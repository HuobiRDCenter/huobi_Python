
from huobi.client.trade import TradeClient
from huobi.constant import *


def callback(obj_event: 'TradeClearingEvent'):
    obj_event.print_object()


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, init_log=True)
trade_client.sub_trade_clearing("eosusdt", callback)
