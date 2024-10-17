from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade.order_auto_place import OrderAutoPlace
from huobi.utils.json_parser import default_parse_data_as_long, default_parse


class PostOrderAutoPlaceService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):

        channel = "/v1/order/auto/place"

        def parse(dict_data):
            return default_parse(dict_data.get("data", {}), OrderAutoPlace)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






