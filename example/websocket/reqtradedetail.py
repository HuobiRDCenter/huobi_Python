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


def callback(trade_event: 'TradeRequest'):
    print("---- trade_event:  ----")
    trade_event.print_object()
    print()



sub_client.request_trade_event("btcusdt,eosusdt", callback, auto_close = True)


