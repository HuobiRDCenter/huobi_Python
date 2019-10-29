from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostTransferFuturesProService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/futures/transfer"

        def parse(dict_data):
            transfer_id = int(dict_data.get("data", 0))
            return transfer_id     # transfer ID

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






