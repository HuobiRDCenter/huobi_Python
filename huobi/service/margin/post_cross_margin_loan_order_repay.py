from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod


class PostCrossMarginLoanOrderRepayService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/cross-margin/orders/{order_id}/repay".format(order_id=self.params.get("order-id"))

        def parse(dict_data):
            return dict_data.get("status", None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)






