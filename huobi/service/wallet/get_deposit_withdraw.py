from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.wallet import *
from huobi.utils import *


class GetDepositWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/query/deposit-withdraw"

        def parse(dict_data):
            op_type = self.params["type"]
            data_list = dict_data.get("data", [])
            if op_type == DepositWithdraw.DEPOSIT:
                return default_parse_list_dict(data_list, Deposit)
            elif op_type == DepositWithdraw.WITHDRAW:
                return default_parse_list_dict(data_list, Withdraw)
            return []

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






