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
    print("Symbol: ", candlestick_event.symbol)
    print("Subscribe Receive Time: ", candlestick_event.timestamp)
    print("Interval: ", candlestick_event.interval)
    candlestick_event.data.print_object()
    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client.subscribe_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, error)
