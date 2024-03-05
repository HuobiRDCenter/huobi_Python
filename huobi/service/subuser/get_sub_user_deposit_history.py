from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.wallet import *
from huobi.utils import *


class GetSubUserDepositHistoryService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/query-deposit"

        def parse(dict_data):
            deposit_history = DepositHistory()
            deposit_history.nextId = dict_data.get("nextId", 0)
            json_data_list = dict_data.get("data", [])
            deposit_history_item_list = default_parse_list_dict(json_data_list, DepositHistoryItem)
            deposit_history.data = deposit_history_item_list
            return deposit_history

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)



