from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.subuser import *
from huobi.utils.json_parser import default_parse_data_as_long



class GetUidService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/user/uid"

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
