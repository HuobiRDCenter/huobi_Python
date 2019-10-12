from huobi.connection.impl.restapi_invoker import call_sync
from huobi.connection.impl.restapi_request import RestApiRequest
from huobi.constant.system import RestApiDefine, HttpMethod
from huobi.utils.apisignature import create_signature
from huobi.utils.urlparamsbuilder import UrlParamsBuilder

from huobi.exception.huobiapiexception import HuobiApiException


class RestApiSyncClient(object):
    __server_url = RestApiDefine.Url

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        if "api_key" in kwargs:
            self.__api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            self.__secret_key = kwargs["secret_key"]
        if "url" in kwargs:
            self.__server_url = kwargs["url"]
        if "method" in kwargs:
            self.__method = kwargs["method"]

        """
        try:
            account_info_map.update_user_info(self.__api_key, self.request_impl)
        except Exception:
            pass
        """

    def __create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({'Content-Type': 'application/json'})
        request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({"Content-Type": "application/x-www-form-urlencoded"})
        request.url = url + builder.build_url()
        return request

    def create_request(self, method, url, params, parse):
        builder = UrlParamsBuilder()
        for key, value in params.items():
            builder.put_url(key, value)

        if method == HttpMethod.GET:
            request = self.__create_request_by_get(url, builder)
        elif method == HttpMethod.GET_SIGN:
            request = self.__create_request_by_get_with_signature(url, builder)
        elif method == HttpMethod.POST_SIGN:
            request = self.__create_request_by_post_with_signature(url, builder)
        elif method == HttpMethod.POST:
            request = self.__create_request_by_post_with_signature(url, builder)
        else:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + str(self.__method) + "  is invalid http method")

        request.json_parser = parse

        return request

    def request_process(self, method, url, params, parse):
        request = self.create_request(method, url, params, parse)
        if request:
            return call_sync(request)

        return None

