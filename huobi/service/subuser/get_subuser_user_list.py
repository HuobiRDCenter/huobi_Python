from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.subuser.subuser_user_list import SubuserUserList
from huobi.utils import *
from huobi.model.subuser import *
from huobi.utils.json_parser import default_parse_data_as_long



class GetSubuserUserListService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/user-list"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, SubuserUserList, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)
