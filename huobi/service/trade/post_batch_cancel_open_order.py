from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostBatchCancelOpenOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/batchCancelOpenOrders"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, BatchCancelCount)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






