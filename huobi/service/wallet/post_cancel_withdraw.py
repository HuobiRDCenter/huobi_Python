from huobi.connection import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostCancelWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        withdraw_id = self.params["withdraw_id"]
        def get_channel():
            path = "/v1/dw/withdraw-virtual/{}/cancel"
            return path.format(withdraw_id)

        def parse(dict_data):
            return

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






