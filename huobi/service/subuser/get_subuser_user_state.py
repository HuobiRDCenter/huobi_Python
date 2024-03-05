from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.subuser.subuser_user_state import SubuserUserState
from huobi.utils import *
from huobi.model.subuser import *
from huobi.utils.json_parser import default_parse_data_as_long



class GetSubuserUserStateService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/user-state"

        def parse(dict_data):
            return default_parse(dict_data.get("data", {}), SubuserUserState)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
