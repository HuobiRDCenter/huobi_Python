from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.serialize.market import *



class GetPriceDepthService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/market/depth"

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, PriceDepthSerial.json_parse)






