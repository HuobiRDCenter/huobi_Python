from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account.account_user_info import AccountUserInfoResult
from huobi.utils import *


class GetAccountUserInfoService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/account/switch/user/info"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountUserInfoResult, {})

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
