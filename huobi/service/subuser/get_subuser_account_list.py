from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.subuser.subuser_account_list import SubuserAccountList
from huobi.utils import *
from huobi.model.subuser.list import List



class GetSubuserAccountListService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/account-list"

        def parse(dict_data):
            data_list = dict_data.get("data", {})
            ret_list = default_parse(data_list, SubuserAccountList, List)
            ret_list.list.accountIds.accountId = data_list["list"]["accountIds"]["accountId"]
            ret_list.list.accountIds.subType = data_list["list"]["accountIds"]["subType"]
            ret_list.list.accountIds.accountStatus = data_list["list"]["accountIds"]["accountStatus"]
            return ret_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
