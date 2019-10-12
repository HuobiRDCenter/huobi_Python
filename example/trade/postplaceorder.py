from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *

request_client = RequestClient(api_key=g_api_key,
                               secret_key=g_secret_key)
symbol_test = "eosusdt"
order_id = request_client.create_order(symbol_test, AccountType.SPOT, OrderType.SELL_LIMIT, amount=1.0, price=100.0)
print(order_id)
request_client.cancel_order(symbol_test, order_id)
