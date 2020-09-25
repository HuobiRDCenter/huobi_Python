from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import *
from huobi.model.algo import *


class GetOpenOrdersService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/algo-orders/opening"

        # {
        #     "code": 200,
        #     "data": [
        #         {
        #             "accountId": 3684354,
        #             "clientOrderId": "test004",
        #             "lastActTime": 1600141535221,
        #             "orderOrigTime": 1600141535137,
        #             "orderPrice": "0.08",
        #             "orderSide": "buy",
        #             "orderSize": "65",
        #             "orderStatus": "created",
        #             "orderType": "limit",
        #             "source": "api",
        #             "stopPrice": "0.085",
        #             "symbol": "adausdt",
        #             "trailingRate": 0.001,
        #             "timeInForce": "gtc"
        #         }
        #     ]
        # }

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse_list_dict(data, OrderListItem)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
