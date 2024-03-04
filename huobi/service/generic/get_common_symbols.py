from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.generic.common_symbols import CommonSymbols
from huobi.model.generic.p import P
from huobi.utils import default_parse, default_parse_list_dict


class GetCommonSymbolsService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/settings/common/symbols"

        def parse(dict_data):
            ret_list = []
            data_list = dict_data.get("data", [])
            if data_list and len(data_list):
                for common_symbol in data_list:
                    common_symbol_obj = default_parse(common_symbol, CommonSymbols, P)
                    p_data = common_symbol.get("p", [])
                    common_symbol_obj.p = default_parse_list_dict(p_data, P, [])
                    ret_list.append(common_symbol_obj)
            return ret_list

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






