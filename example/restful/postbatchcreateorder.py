from huobi import RequestClient
from huobi.constant.test import *
from huobi.model import *

import time

request_client = RequestClient(api_key=g_api_key,
                               secret_key=g_secret_key)


client_order_id_header = str(int(time.time()))

symbol_eosusdt = "eosusdt"
symbol_btcusdt = "btcusdt"

client_order_id_eos = client_order_id_header + symbol_eosusdt
client_order_id_btc = client_order_id_header + symbol_btcusdt


buy_limit_eos = {
    "account_type":AccountType.SPOT,
    "symbol":symbol_eosusdt,
    "order_type":OrderType.BUY_LIMIT,
    "amount":1,
    "price": 0.12,
    "client_order_id" : client_order_id_eos
 }

buy_limit_btc = {
    "account_type":AccountType.SPOT,
    "symbol":symbol_btcusdt,
    "order_type":OrderType.BUY_LIMIT,
    "amount":1,
    "price": 1.12,
    "client_order_id" : client_order_id_btc
 }

order_config_list = [
    buy_limit_eos,
    buy_limit_btc
]


create_result = request_client.batch_create_order(order_config_list=order_config_list)
if len(create_result):
    for item in create_result:
        item.print_object()
        print()

cancel_result = request_client.cancel_orders(order_id_list=[], client_order_id_list=[client_order_id_eos, client_order_id_btc])
cancel_result.print_object()







