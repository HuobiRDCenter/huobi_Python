from huobi.connection import RestApiSyncClient
from huobi.constant import *

class PostBatchCancelOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/batchcancel"

        def parse(dict_data):
            return

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






