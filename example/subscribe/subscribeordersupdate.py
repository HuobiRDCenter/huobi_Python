import logging
from huobi import SubscriptionClient
from huobi.constant.test import *
from huobi.model.ordersupdateevent import OrdersUpdateEvent

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(orders_update_event: 'OrdersUpdateEvent'):
    print("---- orders update : ----")
    orders_update_event.print_object()
    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_orders_update_event("hthusd", callback, error)
