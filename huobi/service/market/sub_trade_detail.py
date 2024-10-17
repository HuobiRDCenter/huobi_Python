import time

from huobi.model.market import *
from huobi.utils import *
from huobi.connection.subscribe_client import SubscribeClient


class SubTradeDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(trade_detail_channel(symbol))
                time.sleep(0.01)

        def parse(dict_data):
            tick = dict_data.get("tick", {})
            trade_detail_event = default_parse(tick, TradeDetailEvent, TradeDetail)
            trade_detail_event.ch = dict_data.get("ch", "")
            return trade_detail_event

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                            parse,
                                            callback,
                                            error_handler)



