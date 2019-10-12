import logging

from huobi.client.market import MarketClient
from huobi.constant.definition import CandlestickInterval
from huobi.exception.huobiapiexception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)




def callback(candlestick_event: 'CandlestickEvent'):
    print("Symbol: " + candlestick_event.symbol)
    candlestick_event.data.print_object()
    print()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient(api_key="123456", secret_key="abcdefg")
market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN1, callback, error)

