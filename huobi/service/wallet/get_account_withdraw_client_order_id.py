from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.wallet import *
from huobi.model.wallet.get_account_withdraw_client_order_id import AccountWithdrawClientOrderId
from huobi.utils import *


class GetAccountWithdrawClientOrderIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/query/withdraw/client-order-id"

        def parse(dict_data):
            return default_parse(dict_data.get("data", {}), AccountWithdrawClientOrderId)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






