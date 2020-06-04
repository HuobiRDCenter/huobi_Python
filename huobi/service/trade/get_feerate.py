from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.trade import *
from huobi.utils import *


class GetFeeRateService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/fee/fee-rate/get"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, FeeRate, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






