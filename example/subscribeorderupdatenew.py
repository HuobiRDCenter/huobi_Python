import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.base.printobject import PrintMix,PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key="xxxxxx", secret_key="xxxxxx")


def callback(upd_event: 'OrderUpdateNewEvent'):
    print("---- order update : ")
    PrintBasic.print_basic(upd_event.symbol, "Symbol")
    PrintBasic.print_basic(upd_event.timestamp, "Timestamp")
    PrintMix.print_data(upd_event.data)

sub_client.subscribe_order_update_new_event("eosht", callback)
