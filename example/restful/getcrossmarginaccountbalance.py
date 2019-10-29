from huobi import RequestClient
from huobi.constant.test import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
cross_margin_account_obj = request_client.get_cross_margin_account_balance()
cross_margin_account_obj.print_object()















