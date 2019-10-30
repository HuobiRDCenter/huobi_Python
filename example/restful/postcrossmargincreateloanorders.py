from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
loan_order_id = request_client.post_cross_margin_create_loan_orders(currency="usdt", amount=100)
PrintBasic.print_basic(loan_order_id, "Loan Order Id")















