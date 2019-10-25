from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod




class PostSubaccountTransferService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/subuser/transfer"

        def parse(dict_data):
            transfer_order_id = int(dict_data.get("data", -1))
            return transfer_order_id

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






