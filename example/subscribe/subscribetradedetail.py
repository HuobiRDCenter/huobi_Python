import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.base.printobject import PrintMix, PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(trade_event: 'TradeEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()



sub_client.subscribe_trade_event("btcusdt,eosusdt", callback)
