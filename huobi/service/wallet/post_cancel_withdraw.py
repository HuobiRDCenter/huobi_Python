from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class PostCancelWithdrawService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        withdraw_id_params = self.params["withdraw-id"]
        def get_channel():
            path = "/v1/dw/withdraw-virtual/{}/cancel"
            return path.format(withdraw_id_params)

        def parse(dict_data):
            withdraw_id_ret = int(dict_data.get("data", -1))
            return withdraw_id_ret

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, get_channel(), self.params, parse)






