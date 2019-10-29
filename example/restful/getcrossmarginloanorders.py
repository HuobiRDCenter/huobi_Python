from huobi import RequestClient
from huobi.constant.test import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
obj_list = request_client.get_cross_margin_loan_orders()
if len(obj_list):
    for obj in obj_list:
        obj.print_object()
        print()















