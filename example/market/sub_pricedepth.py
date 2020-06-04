
from huobi.client.market import MarketClient
from huobi.constant import *



def callback(price_depth_event: 'PriceDepthEvent'):
    price_depth_event.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


market_client = MarketClient()
market_client.sub_pricedepth("btcusdt", DepthStep.STEP0, callback, error)
market_client.sub_pricedepth("eosusdt", DepthStep.STEP0, callback, error)
market_client.sub_pricedepth("ethusdt", DepthStep.STEP0, callback, error)
