from huobi import RequestClient
from huobi.constant.test import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result_list = request_client.get_cross_margin_loan_info()
if result_list and len(result_list):
    for loan_item in result_list:
        loan_item.print_object()
        print()

