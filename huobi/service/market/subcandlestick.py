import time

from huobi.constant import OutputKey
from huobi.model.market import Candlestick
from huobi.utils.channelparser import ChannelParser
from huobi.utils.channels import kline_channel

from huobi.connection import SubscribeClient
from huobi.model.market import CandlestickEvent
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc


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

        def parse(json_wrapper):
            ch = json_wrapper.get_string(OutputKey.KeyChannelCh)
            parse = ChannelParser(ch)
            candlestick_event = CandlestickEvent()
            candlestick_event.symbol = parse.symbol
            candlestick_event.interval = ""
            candlestick_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            tick = json_wrapper.get_object(OutputKey.KeyTick)
            data = Candlestick.json_parse(tick)
            candlestick_event.data = data
            candlestick_event.interval = interval
            return candlestick_event

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler)
    """
    @staticmethod
    def to_string(obj):
        if obj:
            obj.print_object()
            print()
    """



