from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.market import *
from huobi.utils import *



class PostSubaccountTransferService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/subuser/transfer"

        def parse(dict_data):
            return dict_data.get("data")

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






