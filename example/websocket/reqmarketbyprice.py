import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(event: 'MbpRequest'):
    print("Timestamp: " , str(event.id))
    print("Channel : " , event.rep)
    mbp = event.data
    print("seqNum : ", mbp.seqNum)
    print("prevSeqNum : ", mbp.prevSeqNum)
    for entry in mbp.bids:
        print("Bids: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

    for entry in mbp.asks:
        print("Asks: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.request_mbp_event("btcusdt", MbpLevel.MBP150, callback, error)
