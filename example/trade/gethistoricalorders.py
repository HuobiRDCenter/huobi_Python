from huobi import RequestClient
from huobi.constant.test import *
from huobi.impl.accountinfomap import account_info_map
from huobi.model import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

orders = request_client.get_historical_orders(symbol="nodeusdt", order_state=OrderState.FILLED,
                                              order_type=None, start_date=None, end_date=None, start_id=None, size=None)
counts = len(orders)
print(str(counts) + " found ")
if len(orders):
    for order in orders:
        order.print_object()
        print()

