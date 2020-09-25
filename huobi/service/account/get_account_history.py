from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *


class GetAccountHistoryService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/account/history"

        def parse(dict_data):
            response = dict()
            data_list = dict_data.get("data", [])
            response['data'] = default_parse_list_dict(data_list, AccountHistory, [])
            response['next_id'] = dict_data.get("next-id", 0)
            return response

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
