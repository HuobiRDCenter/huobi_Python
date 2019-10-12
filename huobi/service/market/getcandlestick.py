from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import *
from huobi.serialize.market import *


class GetCandleStickService:

    def __init__(self, params):
        self.params = params

    """
    @staticmethod
    def to_string(obj_list):
        if len(obj_list):
            for row_obj in obj_list:
                row_obj.print_object()
                print()
    """

    def request(self, **kwargs):
        channel = "/market/history/kline"

        def parse(json_wrapper):
            candlestick_list = list()
            data_list = json_wrapper.get_array("data")
            for item in data_list.get_items():
                candlestick = CandlestickSerial.json_parse(item)
                candlestick_list.append(candlestick)
            return candlestick_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






