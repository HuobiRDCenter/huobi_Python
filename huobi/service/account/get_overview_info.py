from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account.account_overviewI_info import AccountOverviewInfoResult
from huobi.utils import *


class GetAccountOverviewInfoService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/account/overview/info"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountOverviewInfoResult, {})

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
