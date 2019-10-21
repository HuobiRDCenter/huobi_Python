import time

from huobi.serialize.market import *
from huobi.utils import *
from huobi.connection import SubscribeClient


class SubPriceDepthService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]
        step = self.params["step"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(price_depth_channel(symbol, step))
                time.sleep(0.01)

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            PriceDepthSerial.json_parse,
                                            callback,
                                            error_handler)



