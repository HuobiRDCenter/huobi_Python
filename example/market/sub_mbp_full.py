from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market import MbpFullEvent


def callback(mbp_event: 'MbpFullEvent'):
    mbp_event.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


market_client = MarketClient(init_log=True)
market_client.sub_mbp_full("btcusdt,eosusdt", MbpLevel.MBP5, callback, error)
