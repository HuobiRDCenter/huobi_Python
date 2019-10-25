from huobi.client import TradeClient
from huobi.constant import *
from huobi.constant.test import *


# cancel all the open orders under account
trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
result  = trade_client.cancel_open_orders(account_id=g_account_id)
result.print_object()
