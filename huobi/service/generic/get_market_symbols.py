from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.generic.market_symbols import MarketSymbols
from huobi.utils import *


class GetMarketSymbolsService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/settings/common/market-symbols"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            market_symbols = default_parse_list_dict(data_list, MarketSymbols, [])
            market_symbols.in_ = data_list['in']
            return market_symbols

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)
