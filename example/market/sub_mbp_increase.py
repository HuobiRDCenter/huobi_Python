from huobi.client.market import MarketClient
from huobi.constant import *


def callback(mbp_event: 'MbpIncreaseEvent'):
    mbp_event.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


market_client = MarketClient(init_log=True)
market_client.sub_mbp_increase("btcusdt,eosusdt", MbpLevel.MBP5, callback, error)
