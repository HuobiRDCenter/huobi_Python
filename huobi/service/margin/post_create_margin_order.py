from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *


class PostCreateMarginOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/margin/orders"

        def parse(dict_data):
            margin_order_id = int(dict_data.get("data", 0))
            return margin_order_id

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






