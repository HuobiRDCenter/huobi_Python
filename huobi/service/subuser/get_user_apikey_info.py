from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.subuser import *


class GetUserApikeyInfoService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/user/api-key"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", {}), UserApikeyInfo)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
