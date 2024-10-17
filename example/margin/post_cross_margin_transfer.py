from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
transfer_id = margin_client.post_cross_margin_transfer_in(currency="eos", amount=5)
LogInfo.output(transfer_id)

transfer_id = margin_client.post_cross_margin_transfer_out(currency="eos", amount=5)
LogInfo.output(transfer_id)


