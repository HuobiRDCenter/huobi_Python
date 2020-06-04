
from huobi.client.market import MarketClient


def callback(price_depth_event: 'PriceDepthBboEvent'):
    price_depth_event.print_object()
    print()



def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_pricedepth_bbo("btcusdt", callback, error)
