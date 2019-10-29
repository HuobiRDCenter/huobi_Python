
from huobi.client.trade import TradeClient
from huobi.constant import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = trade_client.get_feerate(symbols="htusdt,btcusdt")
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()