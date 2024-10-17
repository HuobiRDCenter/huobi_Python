
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.model.trade import OrderUpdateEvent


def callback(upd_event: 'OrderUpdateEvent'):
    print("---- order update : ----")
    upd_event.print_object()
    print()


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, init_log=True)
trade_client.sub_order_update("eosusdt", callback)
