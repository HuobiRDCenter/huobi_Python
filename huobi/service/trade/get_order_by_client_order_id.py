from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *


class GetOrderByClientOrderIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/order/orders/getClientOrder"

        def parse(dict_data):
            data_dict = dict_data.get("data", {})
            return Order.json_parse(data_dict)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






