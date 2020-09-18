from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.generic import *
from huobi.utils import *


class GetMarketStatusService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/market-status"

        def parse(dict_data):
            return default_parse(dict_data.get("data", {}), MarketStatus)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)
