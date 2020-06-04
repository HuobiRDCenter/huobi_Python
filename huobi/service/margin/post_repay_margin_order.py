from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import default_parse_data_as_long


class PostRepayMarginOrderService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        loan_id = self.params["loan_id"]
        def get_channel():
            path = "/v1/margin/orders/{}/repay"
            return path.format(loan_id)

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






