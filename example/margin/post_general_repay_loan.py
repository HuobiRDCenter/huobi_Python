from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import LogInfo

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)

list_result = margin_client.post_general_repay_loan(account_id=g_account_id, currency="usdt", amount=1)
LogInfo.output_list(list_result)
