from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)
list_obj = trade_client.get_match_result(symbol="trxusdt", size=5, direct=QueryDirection.NEXT)
LogInfo.output_list(list_obj)

list_obj = trade_client.get_match_result(symbol="eosusdt", size=5)
LogInfo.output_list(list_obj)