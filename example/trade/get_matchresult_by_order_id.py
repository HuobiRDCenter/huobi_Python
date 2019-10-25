from huobi.client import TradeClient
from huobi.constant import *



order_id_test = 123456789

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
list_obj = trade_client.get_match_results_by_order_id(order_id=order_id_test)
if list_obj and len(list_obj):
    for obj in list_obj:
        obj.print_object()
        print()
