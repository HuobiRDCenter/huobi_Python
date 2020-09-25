from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account.account_asset_valuation import AccountAssetValuationResult
from huobi.utils import *


class GetAccountAssetValuationService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/account/asset-valuation"

        def parse(dict_data):
            data = dict_data.get("data", {})
            return default_parse(data, AccountAssetValuationResult, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
