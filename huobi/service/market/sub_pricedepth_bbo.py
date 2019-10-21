import time

from huobi.serialize.market import *
from huobi.utils import *
from huobi.connection import SubscribeClient


class SubPriceDepthBboService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(price_depth_bbo_channel(symbol))
                time.sleep(0.01)

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            PriceDepthBboEventSerial.json_parse,
                                            callback,
                                            error_handler)



