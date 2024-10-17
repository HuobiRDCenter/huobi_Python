from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.etf import *
from huobi.utils import *



class GetEtfSwapConfigService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/etf/swap/config"

        def parse(dict_data):
            data_info = dict_data.get("data", {})
            return default_parse(data_info, EtfSwapConfig, UnitPrice)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






