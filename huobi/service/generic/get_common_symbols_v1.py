from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.generic.common_symbols_v1 import CommonSymbolsV1
from huobi.utils import default_parse_list_dict


class GetCommonSymbolsV1Service:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/settings/common/symbols"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, CommonSymbolsV1, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






