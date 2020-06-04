from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
transfer_id = margin_client.post_repay_margin_order(loan_id=7440184, amount=100.004083)
LogInfo.output("transfer id : {id}".format(id=transfer_id))

