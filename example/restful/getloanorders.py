from huobi import RequestClient
from huobi.constant.test import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

obj_list = request_client.get_loan_history(symbol="trxusdt")
if obj_list and len(obj_list):
    for loan in obj_list:
        loan.print_object()
        print()


