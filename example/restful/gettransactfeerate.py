from huobi import RequestClient
from huobi.constant.test import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, url="https://api.huobi.pro")
result_list = request_client.get_reference_transact_fee_rate("btcusdt,ethusdt,eosusdt")
if result_list and len(result_list):
    for rate_item in result_list:
        rate_item.print_object()
        print()


