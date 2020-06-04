from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import default_parse_data_as_long


class PostCancelOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]

        def get_channel():
            path = "/v1/order/orders/{}/submitcancel"
            return path.format(order_id)

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)
        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






