from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *


class PostCreateOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/place"

        def parse(dict_data):
            return int(dict_data.get("data", 0))

        print("params in PostCreateOrderService", self.params)
        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






