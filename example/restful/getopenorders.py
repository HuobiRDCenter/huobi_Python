from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

client_order_id_tmp = "open_orders_09090"

symbol_test = "eosusdt"
order_id = request_client.create_order(symbol_test, AccountType.SPOT, OrderType.BUY_LIMIT, amount=5, price=1.01, client_order_id=client_order_id_tmp)
print(order_id)


print("\n==============test case 1===============\n")
order_list = request_client.get_open_orders(symbol="btcusdt", account_type=AccountType.SPOT, direct="next")
if order_list and len(order_list):
    for order_item in order_list:
        order_item.print_object()
        print("\n")

print("\n==============test case 2===============\n")
order_list = request_client.get_open_orders(symbol="xrpusdt", account_type=AccountType.MARGIN, direct="prev")
if order_list and len(order_list):
    for order_item in order_list:
        order_item.print_object()
        print("\n")

print("\n==============test case 3===============\n")
order_list = request_client.get_open_orders(symbol="xrpusdt", account_type=AccountType.SUPER_MARGIN, direct="prev")
if order_list and len(order_list):
    for order_item in order_list:
        order_item.print_object()
        print("\n")

print("\n==============test case 4===============\n")
order_list = request_client.get_open_orders(symbol="eosusdt", account_type=AccountType.SPOT, direct="prev")
if order_list and len(order_list):
    for order_item in order_list:
        order_item.print_object()
        print("\n")

