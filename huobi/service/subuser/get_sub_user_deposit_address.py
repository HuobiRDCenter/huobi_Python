from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.wallet import *
from huobi.utils import *


class GetSubUserDepositAddressService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/deposit-address"

        def parse(dict_data):
            json_data_list = dict_data.get("data", [])
            return default_parse_list_dict(json_data_list, ChainDepositAddress, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)



