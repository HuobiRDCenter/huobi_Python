from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *


class PostTransferInMarginService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/dw/transfer-in/margin"

        def parse(dict_data):
            transfer_id = int(dict_data.get("data", 0))
            return transfer_id

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






