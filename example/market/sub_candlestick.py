
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent


def callback(candlestick_event: 'CandlestickEvent'):
    candlestick_event.print_object()
    print("\n")


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN1, callback, error)

