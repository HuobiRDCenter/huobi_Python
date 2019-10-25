from huobi.client import TradeClient
from huobi.constant import *

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = trade_client.get_match_result(symbol="trxusdt", size=5, direct=QueryDirection.NEXT)
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()

list_obj = trade_client.get_match_result(symbol="htusdt", size=5, direct=QueryDirection.NEXT)
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()