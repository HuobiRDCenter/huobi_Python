from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *


class PostPointTransferService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/point/transfer"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountPointTransferResult, {})

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
