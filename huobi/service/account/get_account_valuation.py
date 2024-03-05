from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.model.account.account_valuation import AccountValuation
from huobi.model.account.profit_account_balance_list import ProfitAccountBalanceList
from huobi.utils import *


class GetAccountValuationService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/account/valuation"

        def parse(dict_data):
            data_list = dict_data.get("data", {})
            ret_list = default_parse(data_list, AccountValuation, ProfitAccountBalanceList)
            return ret_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
