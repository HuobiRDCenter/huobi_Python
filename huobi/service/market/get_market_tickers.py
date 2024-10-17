from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import *
from huobi.utils import *



class GetMarketTickersService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/tickers"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", []), MarketTicker)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






