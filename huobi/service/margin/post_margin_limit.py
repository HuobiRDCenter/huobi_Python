from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.margin.margin_limit import MarginLimit
from huobi.utils.json_parser import default_parse_data_as_long, default_parse_list_dict


class PostMarginLimitService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/margin/limit"

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, MarginLimit, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)






