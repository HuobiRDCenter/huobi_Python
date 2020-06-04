import time

from huobi.model.market import *
from huobi.utils import *
from huobi.connection.websocket_req_client import *


class ReqTradeDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(request_trade_detail_channel(symbol))
                time.sleep(0.01)

        def parse(dict_data):
            return default_parse(dict_data, TradeDetailReq, TradeDetail)

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler)



