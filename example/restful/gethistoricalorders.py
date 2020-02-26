from huobi import RequestClient
from huobi.model import *
from huobi.constant.test import *

from huobi.base.printobject import PrintMix

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
orders = request_client.get_historical_orders(symbol="xrpusdt", order_state=OrderState.CANCELED, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None)
if orders and len(orders):
    for order_item in orders:
        order_item.print_object()
        print()


orders = request_client.get_historical_orders(symbol="eosusdt", order_state=OrderState.CANCELED, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None, start_time=1582608293237, end_time=1582628393237)
if orders and len(orders):
    for order_item in orders:
        order_item.print_object()
        print()

