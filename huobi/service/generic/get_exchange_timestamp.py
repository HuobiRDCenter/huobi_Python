from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.utils import *



class GetExchangeTimestampService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/common/timestamp"

        def parse(dict_data):
            ts = dict_data.get("data", 0)
            return convert_cst_in_millisecond_to_utc(ts)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






