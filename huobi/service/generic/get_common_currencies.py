from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.generic.common_currencies import CommonCurrencies
from huobi.utils import default_parse_list_dict


class GetCommonCurrenciesService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/settings/common/currencies"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, CommonCurrencies, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






