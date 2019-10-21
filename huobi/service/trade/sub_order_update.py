import time


from huobi.connection import SubscribeClient
from huobi.model.trade import *
from huobi.utils import *


class SubOrderUpdateService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for val in symbol_list:
                connection.send(orders_update_channel(val))
                time.sleep(0.01)

        def parse(dict_data):
            #account_type = "" #AccountInfoMap.get_account_type(self.__api_key, account_id)  TODO
            order_update_event = default_parse(dict_data, OrderUpdateEvent, OrderUpdate)

            return order_update_event

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler,
                                            is_trade=True)







