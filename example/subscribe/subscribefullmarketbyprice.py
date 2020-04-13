import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(mbp_event: 'MbpEvent'):
    print("Timestamp: " + str(mbp_event.ts))
    print("Channel : " + mbp_event.ch)
    mbp = mbp_event.data
    print("seqNum : ", mbp.seqNum)
    for entry in mbp.bids:
        print("Bids: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

    for entry in mbp.asks:
        print("Asks: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_full_mbp_event("btcusdt", MbpLevel.MBP20, callback, error)
