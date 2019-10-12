from huobi.connection.impl.websocket_connection import WebsocketConnection
from huobi.connection.impl.websocket_request import WebsocketRequest
from huobi.connection.impl.websocket_watchdog import WebSocketWatchDog
from huobi.constant.system import WebSocketDefine


class SubscribeClient(object):

    def __init__(self, **kwargs):
        """
        Create the subscription client to subscribe the update from server.

        :param kwargs: The option of subscription connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            uri: Set the URI for subscription.
            is_auto_connect: When the connection lost is happening on the subscription line, specify whether the client
                            reconnect to server automatically. The connection lost means:
                                Caused by network problem
                                The connection close triggered by server (happened every 24 hours)
                            No any message can be received from server within a specified time, see receive_limit_ms
            receive_limit_ms: Set the receive limit in millisecond. If no message is received within this limit time,
                            the connection will be disconnected.
            connection_delay_failure: If auto reconnect is enabled, specify the delay time before reconnect.
        """
        api_key = None
        secret_key = None
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            secret_key = kwargs["secret_key"]
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.connections = list()
        self.uri = WebSocketDefine.Uri
        is_auto_connect = True
        receive_limit_ms = 60000
        connection_delay_failure = 15
        if "uri" in kwargs:
            self.uri = kwargs["uri"]
        if "is_auto_connect" in kwargs:
            is_auto_connect = kwargs["is_auto_connect"]
        if "receive_limit_ms" in kwargs:
            receive_limit_ms = kwargs["receive_limit_ms"]
        if "connection_delay_failure" in kwargs:
            connection_delay_failure = kwargs["connection_delay_failure"]
        self.__watch_dog = WebSocketWatchDog(is_auto_connect, receive_limit_ms, connection_delay_failure)

        """
        try:
            if self.__api_key and self.__secret_key:
                host = urllib.parse.urlparse(self.uri).hostname
                impl = RestApiRequestImpl(api_key, secret_key, "https://" + host)
                account_info_map.update_user_info(api_key, impl)
        except Exception:
            pass
        """

    def __create_connection(self, request):
        connection = WebsocketConnection(self.__api_key, self.__secret_key, self.uri, self.__watch_dog, request)
        self.connections.append(connection)
        connection.connect()

    def create_request(self, subscription_handler, parse, callback, error_handler, isTrade = False):
        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = isTrade
        request.json_parser = parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def connection(self, request):
        connection = WebsocketConnection(self.__api_key, self.__secret_key, self.uri, self.__watch_dog, request)
        self.connections.append(connection)
        connection.connect()

    def execute_subscribe(self, subscription_handler, parse, callback, error_handler, isTrade = False):
        request = self.create_request(subscription_handler, parse, callback, error_handler, isTrade)
        self.connection(request)

    def unsubscribe_all(self):
        for conn in self.connections:
            conn.close()
        self.connections.clear()

