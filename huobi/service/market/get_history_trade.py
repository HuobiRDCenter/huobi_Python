from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import *
from huobi.utils import *


class GetHistoryTradeService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/history/trade"

        def parse(dict_data):
            trade_list_ret = []  # two level list, list item is list too
            data_list_outer = dict_data.get("data", [])
            if len(data_list_outer):
                for row in data_list_outer:
                    data_list_inner = row.get("data", [])
                    if len(data_list_inner):
                        for trade_info in data_list_inner:
                            trade_obj = default_parse_list_dict(trade_info, Trade, None)  # return a list
                            if trade_obj:
                                trade_list_ret.append(trade_obj)

            return trade_list_ret

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






