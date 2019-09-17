import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.base.printobject import PrintMix, PrintBasic

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key="xxxxxx",
                                secret_key="xxxxxx")


def callback(trade_event: 'TradeEvent'):
    print("---- trade_event:  ----")
    PrintBasic.print_basic(trade_event.symbol, "Symbol")
    PrintBasic.print_basic(trade_event.timestamp, "Timestamp")
    PrintMix.print_data(trade_event.trade_list)



sub_client.subscribe_trade_event("btcusdt,eosusdt", callback)
