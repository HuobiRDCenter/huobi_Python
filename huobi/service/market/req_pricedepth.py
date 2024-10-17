import time

from huobi.connection.websocket_req_client import *
from huobi.utils.channels_request import *
from huobi.model.market import *


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

        def parse(dict_data):
            price_depth_event = PriceDepthReq()
            price_depth_event.id = dict_data.get("id")
            price_depth_event.rep = dict_data.get("rep")
            data = dict_data.get("data", {})
            price_depth_obj = PriceDepth.json_parse(data)
            price_depth_event.data = price_depth_obj
            return price_depth_event

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler)



