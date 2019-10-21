import time

from huobi.serialize.market import *
from huobi.connection import *
from huobi.utils.channels_request import *


class ReqPriceDepthService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]
        step = self.params["step"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(request_price_depth_channel(symbol, step))
                time.sleep(0.01)

        WebSocketReqClient(**kwargs).execute_subscribe(subscription,
                                            PriceDepthReqSerial.json_parse,
                                            callback,
                                            error_handler)



