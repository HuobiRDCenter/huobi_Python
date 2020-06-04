from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod


class GetSystemStatusService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/api/v2/summary.json"
        kwargs["url"] = "https://status.huobigroup.com"

        def parse(dict_data):
            return dict_data

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)






