from huobi.client import TradeClient
from huobi.constant import *

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = trade_client.get_orders(symbol="htusdt", order_state=OrderState.FILLED,
                                    order_type=OrderType.BUY_LIMIT, start_date=None, end_date=None,
                                   start_id=None, size=None, direct=QueryDirection.PREV)

counts = len(list_obj)
print(str(counts) + " found ")
if len(list_obj):
    for order in list_obj:
        order.print_object()
        print()

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = trade_client.get_orders(symbol="eosusdt", order_state=OrderState.FILLED,
                                    order_type=OrderType.BUY_LIMIT, start_date="2019-09-30", end_date=None,
                                   start_id=None, size=None, direct=QueryDirection.PREV)

counts = len(list_obj)
print(str(counts) + " found ")
if len(list_obj):
    for order in list_obj:
        order.print_object()
        print()

list_obj = trade_client.get_orders(symbol="trxusdt", order_state=OrderState.FILLED,
                                    order_type=None, start_date=None, end_date=None,
                                   start_id=None, size=None, direct=QueryDirection.PREV)

counts = len(list_obj)
print(str(counts) + " found ")
if len(list_obj):
    for order in list_obj:
        order.print_object()
        print()
