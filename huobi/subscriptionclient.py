import urllib.parse
from huobi.impl.websocketrequestimpl import WebsocketRequestImpl
from huobi.impl.websocketconnection import WebsocketConnection
from huobi.impl.websocketwatchdog import WebSocketWatchDog
from huobi.impl.restapirequestimpl import RestApiRequestImpl
from huobi.impl.accountinfomap import account_info_map
from huobi.model import *

class SubscriptionClient(object):

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
        self.websocket_request_impl = WebsocketRequestImpl(self.__api_key)
        self.connections = list()
        self.uri = "wss://api.huobi.pro/"
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

        try:
            host = urllib.parse.urlparse(uri).hostname
            impl = RestApiRequestImpl(api_key, secret_key, "https://" + host)
            account_info_map.update_user_info(api_key, impl)
        except Exception:
            pass

    def __create_connection(self, request):
        connection = WebsocketConnection(self.__api_key, self.__secret_key, self.uri, self.__watch_dog, request)
        self.connections.append(connection)
        connection.connect()

    def subscribe_candlestick_event(self, symbols: 'str', interval: 'CandlestickInterval', callback, error_handler=None):
        """
        Subscribe candlestick/kline event. If the candlestick/kline is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(candlestick_event: 'CandlestickEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return: No return
        """
        symbol_list = symbols.split(",")
        request = self.websocket_request_impl.subscribe_candlestick_event(symbol_list, interval, callback, error_handler)
        self.__create_connection(request)

    def subscribe_price_depth_event(self, symbols: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event: 'PriceDepthEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        symbol_list = symbols.split(",")
        request = self.websocket_request_impl.subscribe_price_depth_event(symbol_list, callback, error_handler)
        self.__create_connection(request)

    def subscribe_order_update_event(self, symbols: 'str', callback, error_handler=None):
        """
        Subscribe order changing event. If a order is created, canceled etc, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(order_update_event: 'OrderUpdateEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        symbol_list = symbols.split(",")
        request = self.websocket_request_impl.subscribe_order_update(symbol_list, callback, error_handler)
        self.__create_connection(request)

    def subscribe_trade_event(self, symbols: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_event: 'TradeEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        symbol_list = symbols.split(",")
        request = self.websocket_request_impl.subscribe_trade_event(symbol_list, callback, error_handler)
        self.__create_connection(request)

    def subscribe_24h_trade_statistics_event(self, symbols: 'str', callback, error_handler=None):
        """
        Subscribe 24 hours trade statistics event. If statistics is generated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_statistics_event: 'TradeStatisticsEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        symbol_list = symbols.split(",")
        request = self.websocket_request_impl.subscribe_24h_trade_statistics_event(symbol_list, callback, error_handler)
        self.__create_connection(request)

    def subscribe_account_event(self, mode: 'BalanceMode', callback, error_handler=None):
        """
        Subscribe account changing event. If the balance is updated, server will send the data to client and onReceive in callback will be called.

        :param mode: when mode is AVAILABLE, balance refers to available balance; when mode is TOTAL, balance refers to TOTAL balance for trade sub account (available+frozen).
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(account_event: 'AccountEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        request = self.websocket_request_impl.subscribe_account_event(mode, callback, error_handler)
        self.__create_connection(request)

    def unsubscribe_all(self):
        for conn in self.connections:
            conn.close()
        self.connections.clear()
