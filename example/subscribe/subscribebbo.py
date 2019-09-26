import logging
from huobi import SubscriptionClient
from huobi.base.printobject import PrintBasic
from huobi.model import *
from huobi.model.pricedepthbboevent import PriceDepthBboEvent

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(price_depth_event: 'PriceDepthBboEvent'):
    PrintBasic.print_basic(price_depth_event.timestamp, "Timestamp")
    PrintBasic.print_basic(price_depth_event.symbol, "Symbol")
    PrintBasic.print_basic(price_depth_event.ch, "Channel")
    bbo_obj = price_depth_event.data
    PrintBasic.print_basic(bbo_obj.quote_time, "\t Quote Time")
    PrintBasic.print_basic(bbo_obj.ask, "\t Ask")
    PrintBasic.print_basic(bbo_obj.ask_size, "\t Ask Size")
    PrintBasic.print_basic(bbo_obj.bid, "\t Bid")
    PrintBasic.print_basic(bbo_obj.bid_size, "\t Bid Size")
    print()



def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_price_depth_bbo_event("btcusdt", callback, error)
