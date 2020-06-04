import time
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)

client_order_id_header = str(int(time.time()))

symbol_eosusdt = "eosusdt"

client_order_id_eos_01 = client_order_id_header + symbol_eosusdt + "01"
client_order_id_eos_02 = client_order_id_header + symbol_eosusdt + "02"
client_order_id_eos_03 = client_order_id_header + symbol_eosusdt + "03"

buy_limit_eos_01 = {
    "account_id":g_account_id,
    "symbol":symbol_eosusdt,
    "order_type":OrderType.BUY_LIMIT,
    "source":OrderSource.API,
    "amount":50,
    "price": 0.12,
    "client_order_id" : client_order_id_eos_01
 }

buy_limit_eos_02 = {
    "account_id":g_account_id,
    "symbol":symbol_eosusdt,
    "order_type":OrderType.BUY_LIMIT,
    "source": OrderSource.API,
    "amount":7,
    "price": 0.80,
    "client_order_id" : client_order_id_eos_02
 }

buy_limit_eos_03 = {
    "account_id":g_account_id,
    "symbol":symbol_eosusdt,
    "order_type":OrderType.BUY_LIMIT,
    "source": OrderSource.API,
    "amount":20,
    "price": 0.252,
    "client_order_id" : client_order_id_eos_03
 }

order_config_list = [
    buy_limit_eos_01,
    buy_limit_eos_02,
    buy_limit_eos_03
]

create_result = trade_client.batch_create_order(order_config_list=order_config_list)
LogInfo.output_list(create_result)

order_id_list = []
if create_result and len(create_result):
    for item in create_result:
        order_id_list.append(item.order_id)

    result = trade_client.cancel_orders(symbol_eosusdt, order_id_list)
    result.print_object()




