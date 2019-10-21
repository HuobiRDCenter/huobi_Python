import time

from huobi.model.market import *
from huobi.serialize.market import *
from huobi.utils import *
from huobi.connection import SubscribeClient


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
            trade_detail_event = TradeDetailEvent()
            tick = dict_data.get("tick", {})
            trade_detail_event.ch = dict_data.get("ch", "")
            trade_detail_event.id = tick.get("id", 0)
            trade_detail_event.ts = tick.get("ts", 0)
            data_list_json = tick.get("data", [])
            if (len(data_list_json)):
                for row in data_list_json:
                    trade_detail_obj = TradeDetailSerial.json_parse(row)
                    trade_detail_event.data.append(trade_detail_obj)

            return trade_detail_event

        SubscribeClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler)



