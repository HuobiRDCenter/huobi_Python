from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod


class GetExchangeCurrenciesService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/common/currencys"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return data_list if len(data_list) else []

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






