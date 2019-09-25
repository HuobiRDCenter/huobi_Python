import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(price_depth_event: 'PriceDepthEvent'):
    print("Timestamp: " + str(price_depth_event.timestamp))
    print("Channel : " + price_depth_event.ch)
    depth = price_depth_event.data
    for entry in depth.bids:
        print("Bids: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

    for entry in depth.asks:
        print("Asks: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_price_depth_event("btcusdt", DepthStep.STEP0, callback, error)
