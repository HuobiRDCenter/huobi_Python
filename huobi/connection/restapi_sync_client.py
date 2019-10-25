import logging

from huobi.connection.impl.restapi_invoker import call_sync
from huobi.connection.impl.restapi_request import RestApiRequest
from huobi.constant import *
from huobi.utils import *

from huobi.exception.huobi_api_exception import HuobiApiException



class RestApiSyncClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """
        self.__api_key = kwargs.get("api_key", None)
        self.__secret_key = kwargs.get("secret_key", None)
        self.__server_url = kwargs.get("url", RestApiDefine.Url)
        self.__init_log = kwargs.get("init_log", None)
        if self.__init_log and self.__init_log == True:
            logger = logging.getLogger("huobi-client")
            logger.setLevel(level=logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(handler)

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
        request.host = self.__server_url
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
        if params and len(params):
            if method in [HttpMethod.GET, HttpMethod.GET_SIGN]:
                for key, value in params.items():
                    builder.put_url(key, value)
            elif method in [HttpMethod.POST, HttpMethod.POST_SIGN]:
                for key, value in params.items():
                    builder.put_post(key, value)
            else:
                raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                        "[error] undefined HTTP method")

        if method == HttpMethod.GET:
            request = self.__create_request_by_get(url, builder)
        elif method == HttpMethod.GET_SIGN:
            request = self.__create_request_by_get_with_signature(url, builder)
        elif method == HttpMethod.POST_SIGN:
            request = self.__create_request_by_post_with_signature(url, builder)
        elif method == HttpMethod.POST:
            request = self.__create_request_by_post_with_signature(url, builder)
        else:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + method + "  is invalid http method")

        request.json_parser = parse

        return request

    def request_process(self, method, url, params, parse):
        request = self.create_request(method, url, params, parse)
        if request:
            return call_sync(request)

        return None

