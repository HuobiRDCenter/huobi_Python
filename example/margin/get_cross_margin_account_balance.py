from huobi.client.margin import MarginClient
from huobi.constant import *


margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
account_balance = margin_client.get_cross_margin_account_balance()
account_balance.print_object()


