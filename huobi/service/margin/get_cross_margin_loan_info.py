from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.margin import *
from huobi.utils import *



class GetCrossMarginLoanInfoService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/cross-margin/loan-info"

        def parse(dict_data):
            return default_parse_list_dict(dict_data.get("data", []), CrossMarginLoanInfo, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






