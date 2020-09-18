from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *


class PostCreateOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/algo-orders"

        # {'code': 200, 'data': {'clientOrderId': 'test001'}}
        def parse(dict_data):
            data = dict_data.get('data')
            return data.get('clientOrderId')

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
