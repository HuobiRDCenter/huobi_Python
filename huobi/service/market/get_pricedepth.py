from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import PriceDepth


class GetPriceDepthService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/depth"

        def parse(dict_data):
            tick = dict_data.get("tick", {})
            return PriceDepth.json_parse(tick)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






