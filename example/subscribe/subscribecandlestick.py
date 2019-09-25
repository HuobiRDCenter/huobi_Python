import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.exception.huobiapiexception import HuobiApiException

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(candlestick_event: 'CandlestickEvent'):
    print("Symbol: " + candlestick_event.symbol)
    print("High: " + str(candlestick_event.data.high))
    print("Low: " + str(candlestick_event.data.low))
    print("Open: " + str(candlestick_event.data.open))
    print("Close: " + str(candlestick_event.data.close))
    print("Volume: " + str(candlestick_event.data.volume))
    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, error)
