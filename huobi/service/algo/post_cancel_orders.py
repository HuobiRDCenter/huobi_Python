from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import default_parse_fill_directly
from huobi.model.algo import *


class PostCancelOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/algo-orders/cancellation"

        # {'code': 200, 'data': {'accepted': [], 'rejected': ['test001', 'test002']}}
        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse_fill_directly(data, CancelOrderResult)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
