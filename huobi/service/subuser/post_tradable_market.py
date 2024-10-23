from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.subuser.trade_market import TradeMarket
from huobi.utils import *


class PostTradableMarketService:
    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/tradable-market"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", {}), TradeMarket)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
