import logging
from huobi import SubscriptionClient
from huobi.constant.test import *
from huobi.impl.accountinfomap import account_info_map
from huobi.model import *
from huobi.base.printobject import PrintMix, PrintBasic
from huobi.model.orderdetailrequest import OrderDetailRequest

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(order_req_obj: 'OrderDetailRequest'):
    print("---- order_detail:  ----")
    order_req_obj.print_object()
    print()

order_id = 100000000
sub_client.request_order_detail_event(order_id, callback, auto_close=True)



