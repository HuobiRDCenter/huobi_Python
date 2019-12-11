import logging
from huobi import SubscriptionClient
from huobi.constant.test import *
from huobi.model import *
from huobi.base.printobject import PrintMix,PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(upd_event: 'TradeClearingEvent'):
    print("---- trade clearing : ----")
    upd_event.print_object()
    print()

sub_client.subscribe_trade_clearing_event("eosusdt,trxusdt,btcusdt", callback)
