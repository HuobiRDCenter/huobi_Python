from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.algo.cancel_all_after import CancelAllAfter
from huobi.utils.json_parser import *
from huobi.model.algo import *


class PostCancelAllAfterService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/algo-orders/cancel-all-after"

        def parse(dict_data):
            return default_parse(dict_data.get("data", {}), CancelAllAfter)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
