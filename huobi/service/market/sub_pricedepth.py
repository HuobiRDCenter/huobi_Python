import time

from huobi.model.market import *
from huobi.utils import *
from huobi.connection.subscribe_client import SubscribeClient


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

        def parse(dict_data):
            price_depth_event_obj = PriceDepthEvent()
            price_depth_event_obj.ch = dict_data.get("ch", "")
            tick = dict_data.get("tick", "")
            price_depth_event_obj.tick = PriceDepth.json_parse(tick)
            return price_depth_event_obj

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler)



