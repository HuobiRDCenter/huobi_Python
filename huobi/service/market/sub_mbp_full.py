import time

from huobi.model.market import *
from huobi.utils import *
from huobi.connection.subscribe_client import SubscribeClient


class SubMbpFullService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]
        level = self.params["levels"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(mbp_full_channel(symbol, level))
                time.sleep(0.01)

        def parse(dict_data):
            return MbpFullEvent.json_parse(dict_data)

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                                       parse,
                                                       callback,
                                                       error_handler)
