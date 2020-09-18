from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod


class PostSubuserApikeyDeletionService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/sub-user/api-key-deletion"

        # {'code': 200, 'data': None, 'ok': True}
        def parse(dict_data):
            return dict_data

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
