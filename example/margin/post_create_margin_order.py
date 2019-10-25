from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.constant.test import *

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)
transfer_id = margin_client.post_create_margin_order(symbol="trxusdt", currency="usdt", amount=100)
print("transfer id :", transfer_id)

