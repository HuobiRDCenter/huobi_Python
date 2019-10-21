from huobi.connection import RestApiSyncClient
from huobi.constant import *



class PostCancelOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]

        def get_channel():
            path = "/v1/order/orders/{}/submitcancel"
            return path.format(order_id)

        def parse(dict_data):
            return int(dict_data.get("data", -1))  # order-id

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






