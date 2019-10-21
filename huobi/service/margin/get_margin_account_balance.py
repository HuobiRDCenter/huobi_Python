from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *



class GetMarginAccountBalanceService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/margin/accounts/balance"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, Balance, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






