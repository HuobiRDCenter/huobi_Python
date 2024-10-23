import logging

from huobi.connection.impl.websocket_watchdog import WebSocketWatchDog
from huobi.connection.impl.websocket_manage import WebsocketManage
from huobi.connection.impl.websocket_request import WebsocketRequest
from huobi.constant.system import WebSocketDefine, ApiVersion


class SubscribeClient(object):
    # static property
    subscribe_watch_dog = WebSocketWatchDog()

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

        self.__websocket_manage_list = list()

    def __create_websocket_manage(self, request):
        manager = WebsocketManage(self.__api_key, self.__secret_key, self.__uri, request)
        self.__websocket_manage_list.append(manager)
        manager.connect()
        SubscribeClient.subscribe_watch_dog.on_connection_created(manager)

    def create_request(self, subscription_handler, parse, callback, error_handler, is_trade, is_mbp_feed=False):
        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = is_trade
        request.is_mbp_feed = is_mbp_feed
        request.auto_close = False  # subscribe need connection. websocket request need close request.
        request.json_parser = parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def create_request_v1(self, subscription_handler, parse, callback, error_handler, is_trade=False):
        request = self.create_request(subscription_handler=subscription_handler, parse=parse, callback=callback,
                                      error_handler=error_handler, is_trade=is_trade)
        request.api_version = ApiVersion.VERSION_V1
        return request

    def create_request_v2(self, subscription_handler, parse, callback, error_handler, is_trade=False):
        request = self.create_request(subscription_handler=subscription_handler, parse=parse, callback=callback,
                                      error_handler=error_handler, is_trade=is_trade)
        request.api_version = ApiVersion.VERSION_V2
        return request

    def execute_subscribe_v1(self, subscription_handler, parse, callback, error_handler, is_trade=False):
        request = self.create_request_v1(subscription_handler, parse, callback, error_handler, is_trade)
        self.__create_websocket_manage(request)

    def execute_subscribe_v2(self, subscription_handler, parse, callback, error_handler, is_trade=False):
        request = self.create_request_v2(subscription_handler, parse, callback, error_handler, is_trade)
        self.__create_websocket_manage(request)

    def execute_subscribe_mbp(self, subscription_handler, parse, callback, error_handler, is_trade=False,
                              is_mbp_feed=True):
        request = self.create_request(subscription_handler, parse, callback, error_handler, is_trade, is_mbp_feed)
        self.__create_websocket_manage(request)

    def unsubscribe_all(self):
        for websocket_manage in self.__websocket_manage_list:
            SubscribeClient.subscribe_watch_dog.on_connection_closed(websocket_manage)
            websocket_manage.close()
        self.__websocket_manage_list.clear()
