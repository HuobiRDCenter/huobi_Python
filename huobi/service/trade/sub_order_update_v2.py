import time


from huobi.connection.subscribe_client import SubscribeClient
from huobi.model.trade import *
from huobi.utils import *


class SubOrderUpdateV2Service:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for val in symbol_list:
                connection.send(orders_update_channel(val))
                time.sleep(0.01)

        def parse(dict_data):
            return default_parse(dict_data, OrderUpdateEvent, OrderUpdate)

        SubscribeClient(**kwargs).execute_subscribe_v2(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)







