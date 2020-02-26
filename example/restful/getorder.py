from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

client_order_id_tmp = "abc022602"

symbol_test = "eosusdt"
order_id = request_client.create_order(symbol_test, AccountType.SPOT, OrderType.BUY_LIMIT, amount=5, price=1.01, client_order_id=client_order_id_tmp)
print(order_id)

print("\n============== get open order ===============\n")
order_obj = request_client.get_order(symbol=symbol_test, order_id=order_id)
order_obj.print_object()

request_client.cancel_order(symbol_test, order_id)

print("\n============== get cancel order ===============\n")
order_obj = request_client.get_order(symbol=symbol_test, order_id=order_id)
order_obj.print_object()


