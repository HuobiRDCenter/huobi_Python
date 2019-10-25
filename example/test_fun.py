
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market.candlestick_event import CandlestickEvent


def callback_candlestick(candlestick_event: 'CandlestickEvent'):
    print("====callback_candlestick ====")


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


def callback_pricedepth(price_depth_event: 'PriceDepthEvent'):
    print("====callback_pricedepth ====")


market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN, init_log=True)
#market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN5, callback_candlestick, error)
market_client.sub_pricedepth("btcusdt", DepthStep.STEP5, callback_pricedepth, error)