from huobi.client import MarginClient
from huobi.constant import *
from huobi.constant.test import *


margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
obj_list = margin_client.get_margin_account_balance(symbol="trxusdt")
if obj_list and len(obj_list):
    for account_balance in obj_list:
        account_balance.print_object()

