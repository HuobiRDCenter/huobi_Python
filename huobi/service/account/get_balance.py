from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *


class GetBalanceService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        account_id = self.params["account-id"]

        def get_channel():
            path = "/v1/account/accounts/{}/balance"
            return path.format(account_id)

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountBalance, {})

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)

    def get_request(self, **kwargs):
        account_id = self.params["account-id"]

        def get_channel():
            path = "/v1/account/accounts/{}/balance"
            return path.format(account_id)

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountBalance, {})

        return RestApiSyncClient(**kwargs).create_request(HttpMethod.GET_SIGN, get_channel(), self.params, parse)
