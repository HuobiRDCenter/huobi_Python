from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.subuser import *


class PostSetSubuserTransferability:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/transferability"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", {}), SubuserTransferability)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
