import time

from huobi.utils import *

from huobi.connection.websocket_req_client import *
from huobi.model.market import *
from huobi.utils.channels_request import *


class ReqCandleStickService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]
        interval = self.params["interval"]
        from_ts_second = self.params.get("from_ts_second", None)
        end_ts_second = self.params.get("end_ts_second", None)

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(request_kline_channel(symbol, interval, from_ts_second, end_ts_second))
                time.sleep(0.01)

        def parse(dict_data):
            return default_parse(dict_data, CandlestickReq, Candlestick)

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler)



