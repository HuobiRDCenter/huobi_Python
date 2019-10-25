from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *



class GetAccountBalanceBySubUidService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        sub_uid = self.params["sub-uid"]

        def get_channel():
            path = "/v1/account/accounts/{}"
            return path.format(sub_uid)

        def parse(dict_data):
            ret = []
            data_list = dict_data.get("data", [])
            if data_list and len(data_list):
                for account_balance_dict in data_list:
                    account_balance_obj = default_parse(account_balance_dict, AccountBalance, Balance)
                    ret.append(account_balance_obj)
            return ret

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)






