import time

from huobi.model.market import *
from huobi.serialize.market import *
from huobi.utils import *
from huobi.connection import *


class ReqTradeDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol_list = self.params["symbol_list"]

        def subscription(connection):
            for symbol in symbol_list:
                connection.send(request_trade_detail_channel(symbol))
                time.sleep(0.01)

        def parse(dict_data):
            trade_detail_event = TradeDetailReq()
            data_list_json = dict_data.get("data", [])
            if (len(data_list_json)):
                for row in data_list_json:
                    trade_detail_obj = TradeDetailSerial.json_parse(row)
                    trade_detail_event.data.append(trade_detail_obj)

            return trade_detail_event

        WebSocketReqClient(**kwargs).execute_subscribe(subscription,
                                            parse,
                                            callback,
                                            error_handler)



