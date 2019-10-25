
from huobi.client import MarketClient
from huobi.constant import *



def callback(price_depth_event: 'PriceDepthEvent'):
    price_depth_event.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN)
market_client.sub_pricedepth("btcusdt", DepthStep.STEP0, callback, error)
