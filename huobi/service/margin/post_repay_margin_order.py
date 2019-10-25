from huobi.connection import RestApiSyncClient
from huobi.constant import *


class PostRepayMarginOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        load_id = self.params["load_id"]
        def get_channel():
            path = "/v1/margin/orders/{}/repay"
            return path.format(load_id)

        def parse(dict_data):
            margin_order_id = int(dict_data.get("data", 0))
            return margin_order_id

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






