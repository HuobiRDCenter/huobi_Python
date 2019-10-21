from huobi.connection import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostBatchCancelOpenOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]

        channel = "/v1/order/orders/batchCancelOpenOrders"

        def parse(dict_data):
            return

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






