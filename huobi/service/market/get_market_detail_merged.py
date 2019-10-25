from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import *
from huobi.utils import *



class GetMarketDetailMergedService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/detail/merged"

        def parse(dict_data):
            tick = dict_data.get("tick", {})
            return default_parse_fill_directly(tick, MarketDetailMerged)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






