from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *

margin_client = MarginClient(api_key=g_api_key,
                             secret_key=g_secret_key)

list_obj = margin_client.post_margin_limit(currency="btc")
LogInfo.output_list(list_obj)
