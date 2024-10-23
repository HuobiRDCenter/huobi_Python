from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import HttpMethod


class PostSubuserApikeyGenerationService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v1/trust/user/active/credit"

        def parse(dict_data):
            return dict_data.get("data", bool)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
