import logging

from huobi.connection.impl.websocket_manage import WebsocketManage
from huobi.connection.impl.websocket_request import WebsocketRequest
from huobi.constant.system import WebSocketDefine


class WebSocketReqClient(object):

    def __init__(self, **kwargs):
        """
        Create the subscription client to subscribe the update from server.

        :param kwargs: The option of subscription connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: Set the URI for subscription.
            init_log: to init logger
        """

        self.__api_key = kwargs.get("api_key", None)
        self.__secret_key = kwargs.get("secret_key", None)
        self.__uri = kwargs.get("url", WebSocketDefine.Uri)
        self.__init_log = kwargs.get("init_log", None)
        if self.__init_log and self.__init_log:
            logger = logging.getLogger("huobi-client")
            logger.setLevel(level=logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(handler)

    def __create_websocket_manage(self, request):
        manager = WebsocketManage(self.__api_key, self.__secret_key, self.__uri, request)
        manager.connect()

    def create_request(self, subscription_handler, parse, callback, error_handler, is_trade=False, is_mbp_feed=False):
        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = is_trade
        request.is_mbp_feed = is_mbp_feed
        request.auto_close = True  # for websocket request, auto close the connection after request.
        request.json_parser = parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def execute_subscribe_v1(self, subscription_handler, parse, callback, error_handler, is_trade=False):
        request = self.create_request(subscription_handler, parse, callback, error_handler, is_trade)
        self.__create_websocket_manage(request)

    def execute_subscribe_mbp(self, subscription_handler, parse, callback, error_handler, is_trade=False,
                              is_mbp_feed=True):
        request = self.create_request(subscription_handler, parse, callback, error_handler, is_trade, is_mbp_feed)
        self.__create_websocket_manage(request)
