import time

from huobi.utils import *

from huobi.connection import SubscribeClient
from huobi.model.market import *



class SubCandleStickService:
    def __init__(self, params):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]
        interval = self.params["interval"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(kline_channel(symbol, interval))
                time.sleep(0.01)

        def parse(dict_data):
            return default_parse(dict_data, CandlestickEvent, Candlestick)

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler)



