import threading
import websocket
import gzip
import ssl
import logging
from urllib import parse
import urllib.parse

from huobi.base.printtime import PrintDate
from huobi.impl.utils.timeservice import get_current_timestamp
from huobi.impl.utils.urlparamsbuilder import UrlParamsBuilder
from huobi.impl.utils.apisignature import create_signature
from huobi.exception.huobiapiexception import HuobiApiException
from huobi.impl.utils import *

# Key: ws, Value: connection
websocket_connection_handler = dict()


def on_message(ws, message):
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_message(message)
    return


def on_error(ws, error):
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_failure(error)


def on_close(ws):
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_close()


def on_open(ws):
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_open(ws)


connection_id = 0


class ConnectionState:
    """
    IDLE -> CONNECTING -> CONNECTED(call on_open from WebSocketApp) -> CLOSED_ON_ERROR(websocket_func)
                ^                                                   |
                |                                                   |
                |                                                   |
    DELAY_CONNECTING(call re_connect_in_delay from watch_dog_job) <-|
    """
    IDLE = 0
    CONNECTED = 1
    DELAY_CONNECTING = 2
    CONNECTING = 3
    CLOSED_ON_ERROR = 4


def websocket_func(*args):
    connection_instance = args[0]
    connection_instance.ws = websocket.WebSocketApp(connection_instance.url,
                                                    on_message=on_message,
                                                    on_error=on_error,
                                                    on_close=on_close)
    global websocket_connection_handler
    websocket_connection_handler[connection_instance.ws] = connection_instance
    connection_instance.logger.info("[Sub][" + str(connection_instance.id) + "] Connecting...")
    connection_instance.delay_in_second = -1
    connection_instance.ws.on_open = on_open
    connection_instance.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    connection_instance.logger.info("[Sub][" + str(connection_instance.id) + "] Connection event loop down")
    with connection_instance.state_lock:
        if connection_instance.state == ConnectionState.CONNECTED:
            connection_instance.state = ConnectionState.IDLE


class WebsocketConnection:

    def __init__(self, api_key, secret_key, uri, watch_dog, request):
        # threading.Thread.__init__(self)
        self.__thread = None
        self.__market_url = "wss://api.huobi.pro/ws"
        self.__trading_url = "wss://api.huobi.pro/ws/v1"
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.request = request
        self.__watch_dog = watch_dog
        self.delay_in_second = -1
        self.ws = None
        self.last_receive_time = 0
        self.logger = logging.getLogger("huobi-client")
        self.state = ConnectionState.IDLE
        self.state_lock = threading.Lock()
        global connection_id
        connection_id += 1
        self.id = connection_id
        host = urllib.parse.urlparse(uri).hostname
        if host.find("api.") == 0:
            self.__market_url = "wss://" + host + "/ws"
            self.__trading_url = "wss://" + host + "/ws/v1"
        else:
            self.__market_url = "wss://" + host + "/api/ws"
            self.__trading_url = "wss://" + host + "/ws/v1"
        if request.is_trading:
            self.url = self.__trading_url
        else:
            self.url = self.__market_url

    def re_connect_in_delay(self, delay_in_second):
        if self.ws is not None:
            self.ws.close()
            self.ws = None
        self.delay_in_second = delay_in_second
        self.state = ConnectionState.DELAY_CONNECTING
        self.logger.warning("[Sub][" + str(self.id) + "] Reconnecting after "
                            + str(self.delay_in_second) + " seconds later")

    def re_connect(self):
        if self.delay_in_second != 0:
            self.delay_in_second -= 1
            self.logger.warning("In delay connection: " + str(self.delay_in_second))
        else:
            self.connect()

    def connect(self):
        if self.state == ConnectionState.CONNECTED:
            self.logger.info("[Sub][" + str(self.id) + "] Already connected")
        elif self.state != ConnectionState.CONNECTING:  # from IDLE/DELAY_CONNECTING, make sure only one new thread launch
            self.state = ConnectionState.CONNECTING
            self.__thread = threading.Thread(target=websocket_func, args=[self])
            self.__thread.start()

    def send(self, data):
        #print(data)
        self.ws.send(data)

    def close(self):
        self.ws.close()
        del websocket_connection_handler[self.ws]
        self.__watch_dog.on_connection_closed(self)
        self.logger.error("[Sub][" + str(self.id) + "] Closing normally")

    def on_close(self):
        del websocket_connection_handler[self.ws]
        self.logger.error("[Sub][" + str(self.id) + "] Closing requested from WebSocketApp")

    def on_open(self, ws):
        #print("### open ###")
        self.logger.info("[Sub][" + str(self.id) + "] Connected to server")
        self.ws = ws
        self.last_receive_time = get_current_timestamp()
        with self.state_lock:
            self.state = ConnectionState.CONNECTED
        self.__watch_dog.on_connection_created(self)
        if self.request.is_trading:
            try:
                builder = UrlParamsBuilder()
                create_signature(self.__api_key, self.__secret_key,
                                 "GET", self.url, builder)
                builder.put_url("op", "auth")
                self.send(builder.build_url_to_json())
            except Exception as e:
                self.on_error("Unexpected error when create the signature: " + str(e))
        else:
            if self.request.subscription_handler is not None:
                self.request.subscription_handler(self)
        return

    def on_error(self, error_message):
        if self.request.error_handler is not None:
            exception = HuobiApiException(HuobiApiException.SUBSCRIPTION_ERROR, error_message)
            self.request.error_handler(exception)
        self.logger.error("[Sub][" + str(self.id) + "] " + str(error_message))

    def on_failure(self, error):
        self.on_error("Unexpected error: " + str(error))
        self.close_on_error()

    def on_message(self, message):
        self.last_receive_time = get_current_timestamp()
        json_wrapper = parse_json_from_string(gzip.decompress(message).decode("utf-8"))
        #print("RX: " + gzip.decompress(message).decode("utf-8"))

        if json_wrapper.contain_key("status") and json_wrapper.get_string("status") != "ok":
            error_code = json_wrapper.get_string_or_default("err-code", "Unknown error")
            error_msg = json_wrapper.get_string_or_default("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif json_wrapper.contain_key("err-code") and json_wrapper.get_int("err-code") != 0:
            error_code = json_wrapper.get_string_or_default("err-code", "Unknown error")
            error_msg = json_wrapper.get_string_or_default("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif json_wrapper.contain_key("op"):
            op = json_wrapper.get_string("op")
            if op == "notify":
                self.__on_receive(json_wrapper)
            elif op == "ping":
                ping_ts = json_wrapper.get_string("ts")
                self.__process_ping_on_trading_line(ping_ts)
            elif op == "auth":
                if self.request.subscription_handler is not None:
                    self.request.subscription_handler(self)
            elif op == "req":
                self.__on_receive(json_wrapper)
        elif json_wrapper.contain_key("ch"):
            self.__on_receive(json_wrapper)
        elif json_wrapper.contain_key("rep"):
            self.__on_receive(json_wrapper)
        elif json_wrapper.contain_key("ping"):
            ping_ts = json_wrapper.get_string("ping")
            self.__process_ping_on_market_line(ping_ts)
        else:
            print("unknown data process, RX: " + gzip.decompress(message).decode("utf-8"))

    def __on_receive(self, json_wrapper):
        res = None
        try:
            if self.request.json_parser is not None:
                res = self.request.json_parser(json_wrapper)
        except Exception as e:
            self.on_error("Failed to parse server's response: " + str(e))

        try:
            if self.request.update_callback is not None:
                self.request.update_callback(res)
        except Exception as e:
            self.on_error("Process error: " + str(e)
                     + " You should capture the exception in your error handler")

        if self.request.auto_close:
            self.close()

    def __process_ping_on_trading_line(self, ping_ts):
        #self.send("{\"op\":\"pong\",\"ts\":" + str(get_current_timestamp()) + "}")
        #PrintDate.timestamp_to_date(ping_ts)
        self.send("{\"op\":\"pong\",\"ts\":" + str(ping_ts) + "}")
        return

    def __process_ping_on_market_line(self, ping_ts):
        #self.send("{\"pong\":" + str(get_current_timestamp()) + "}")
        #PrintDate.timestamp_to_date(ping_ts)
        self.send("{\"pong\":" + str(ping_ts) + "}")
        return

    def close_on_error(self):
        if self.ws is not None:
            with self.state_lock:
                self.ws.close()
                self.state = ConnectionState.CLOSED_ON_ERROR
                self.logger.error("[Sub][" + str(self.id) + "] Connection is closing due to error")
