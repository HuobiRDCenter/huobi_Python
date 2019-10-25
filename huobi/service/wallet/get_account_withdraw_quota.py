from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.wallet import *
from huobi.utils import *


class GetAccountWithdrawQuotaService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/account/withdraw/quota"

        def parse(dict_data):
            data = dict_data.get("data", {})
            chains = data.get("chains", [])
            return default_parse_list_dict(chains, WithdrawQuota)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






