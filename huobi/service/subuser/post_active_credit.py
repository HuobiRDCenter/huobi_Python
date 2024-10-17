from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.subuser import *


class PostActiveCreditService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/trust/user/active/credit"

        def parse(dict_data):
            return dict_data.get("data")

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
