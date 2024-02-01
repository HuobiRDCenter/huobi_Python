from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import Balance
from huobi.model.margin import *
from huobi.utils import *
from huobi.utils.json_parser import default_parse_data_as_long


class PostCrossMarginRepayService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order-id"]
        def get_channel():
            path = "/v1/cross-margin/orders/{order-id}/repay"
            return path.format(order_id)

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






