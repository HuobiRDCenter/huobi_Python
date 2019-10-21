from huobi.connection import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostCreateWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/dw/withdraw/api/create"

        def parse(dict_data):
            return dict_data.get("data", 0)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






