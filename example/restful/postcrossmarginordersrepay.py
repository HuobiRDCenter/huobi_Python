from huobi import RequestClient
from huobi.constant.test import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
request_client.post_cross_margin_loan_order_repay(order_id=9430, amount=0.00416667)















