from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.account import *


class PostSubUidManagementService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/management"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", {}), SubUidManagement)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






