from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *

request_client = RequestClient(api_key=g_api_key,
                               secret_key=g_secret_key)


symbol_test = "eosusdt"
order_id = request_client.create_order(symbol_test, AccountType.SPOT, OrderType.BUY_LIMIT, amount=1, price=1.011)
print(order_id)
request_client.cancel_order(symbol_test, order_id)



symbol_test = "xrpusdt"
order_id = request_client.create_order(symbol_test, AccountType.MARGIN, OrderType.BUY_LIMIT, amount=101, price=0.01)
print(order_id)
request_client.cancel_order(symbol_test, order_id)



symbol_test = "xrpusdt"
order_id = request_client.create_order(symbol_test, AccountType.SUPER_MARGIN, OrderType.BUY_LIMIT, amount=101, price=0.011)
print(order_id)
order_id = request_client.create_order(symbol_test, AccountType.SUPER_MARGIN, OrderType.BUY_LIMIT, amount=101, price=0.012)
print(order_id)
request_client.cancel_order(symbol_test, order_id)
