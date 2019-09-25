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


def callback(candlestick_event: 'CandlestickRequest'):

    print("Symbol: " + str(candlestick_event.symbol))
    print("Timestamp: " + str(candlestick_event.timestamp))
    print("Interval: " + str(candlestick_event.interval))

    if len(candlestick_event.data):
        for candlestick in candlestick_event.data:
            print("Timestamp: " + str(candlestick.timestamp))
            print("High: " + str(candlestick.high))
            print("Low: " + str(candlestick.low))
            print("Open: " + str(candlestick.open))
            print("Close: " + str(candlestick.close))
            print("Amount: " + str(candlestick.amount))
            print("Volume: " + str(candlestick.volume))
            print("Count: " + str(candlestick.count))
            print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


#sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=None, end_ts_second=None, auto_close=True, error_handler=None)
#sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1569361140, end_ts_second=1569366420)
#sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1569361140, end_ts_second=0)
#sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1569379980)
sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback)
