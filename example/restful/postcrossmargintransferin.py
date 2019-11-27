from huobi import RequestClient
from huobi.constant.test import *
from huobi.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
transfer_id = request_client.post_cross_margin_transfer_in(currency="trx", amount=2)
PrintBasic.print_basic(transfer_id, "Transfer ID")















