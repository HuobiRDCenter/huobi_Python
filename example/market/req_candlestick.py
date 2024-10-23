from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market import CandlestickReq


def callback(candlestick_req: 'CandlestickReq'):
    candlestick_req.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client = MarketClient(init_log=True)
# sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=None, end_ts_second=None, error_handler=None)
# sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1571124360, end_ts_second=1571129820)
# sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1569361140, end_ts_second=0)
# sub_client.request_candlestick_event("btcusdt", CandlestickInterval.MIN1, callback, from_ts_second=1569379980)
sub_client.req_candlestick("btcusdt", CandlestickInterval.MIN1, callback)
