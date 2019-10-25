from huobi.client import TradeClient
from huobi.constant import *

#symbol_test_list = [None,"ethbtc","eosusdt"]
symbol_test_list = ["trxusdt"]
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
for symbol_test in symbol_test_list:
    list_obj = trade_client.get_history_orders(symbol=symbol_test, start_time=None, end_time=None, size=20, direct=None)
    if len(list_obj):
      for obj in list_obj:
            obj.print_object()















