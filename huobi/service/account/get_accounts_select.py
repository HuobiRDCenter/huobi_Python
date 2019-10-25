from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *



class GetAccountsSelectService:

    def __init__(self, params):
        self.params = params
        self.__channel = "/v1/account/accounts"

    @staticmethod
    def parse(dict_data):
        data_list = dict_data.get("data", [])
        return default_parse_list_dict(data_list, Account, [])

    """
        return value is dict, and key is account id, value is account object
    """
    def get_accounts_key_id(self, **kwargs):

        def parse(dict_data):
            account_dict = {}
            account_obj_list = GetAccountsSelectService.parse(dict_data)
            if len(account_obj_list):
                for account_obj in account_obj_list:
                    account_dict[int(account_obj.id)] = account_obj
            return account_dict


        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, self.__channel, self.params, parse)

    """
        return value is dict, and key is account type, value is account object list
        for some account type has more than one account
    """
    def get_accounts_key_type(self, **kwargs):
        def parse(dict_data):
            account_list = GetAccountsSelectService.parse(dict_data)
            account_dict = {}
            if len(account_list):
                for account_obj in account_list:
                    account_dict[account_obj.type] = []
                for account_obj in account_list:
                    account_dict[account_obj.type].append(account_obj)
            return account_dict

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, self.__channel, self.params, parse)

    """
        get account id list by account type
        return value is account id list
    """
    def get_accounts_id_by_type(self, **kwargs):
        account_type_in = self.params["account_type"]

        def parse(dict_data):
            ret = []
            account_list = GetAccountsSelectService.parse(dict_data)
            if len(account_list):
                for account_obj in account_list:
                    if account_obj.type == account_type_in:
                        ret.append(int(account_obj.id))
            return ret

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, self.__channel, self.params, parse)






