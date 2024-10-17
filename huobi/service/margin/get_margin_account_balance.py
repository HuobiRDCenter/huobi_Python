from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import Balance
from huobi.model.margin import *
from huobi.utils import *



class GetMarginAccountBalanceService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/margin/accounts/balance"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            account_balance_list = []
            if data_list and len(data_list):
                for row in data_list:
                    account_balance = default_parse(row, MarginAccountBalance, Balance)
                    account_balance_list.append(account_balance)
            return account_balance_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






