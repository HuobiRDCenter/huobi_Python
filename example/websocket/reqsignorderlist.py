import logging
from huobi import SubscriptionClient, RequestClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix, PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def callback(order_req_obj: 'OrderListRequest'):
    print("---- order list:  ----")
    order_req_obj.print_object()
    print()

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, url = "https://api.huobi.vn")
sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key, uri = "https://api.huobi.vn")
data = request_client.get_account_balance()
if len(data):
    for account in data:
        print("============= account info =============")
        PrintBasic.print_basic(account.id, "Account ID")
        sub_client.request_order_list_event(symbol="nodeusdt", account_id=account.id, callback=callback, order_states = OrderState.FILLED, client_req_id = None, auto_close = True)
        break # for frequence limit


