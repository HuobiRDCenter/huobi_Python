from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *
from huobi.model.etf import *


class PostEtfSwapOutService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/etf/swap/out"

        def parse(dict_data):
            return default_parse_fill_directly(dict_data, EtfSwapInOut)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)







