import threading
import websocket
import gzip
import ssl
import logging
import urllib.parse

from huobi.utils import *
from huobi.exception.huobi_api_exception import HuobiApiException

# Key: ws, Value: connection
websocket_connection_handler = dict()


def on_message(ws, message):
    print("on_message start")
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_message(message)
    print("on_message end")
    return


def on_error(ws, error):
    print("on_error start")
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_failure(error)
    print("on_error end")


def on_close(ws):
    print("on_close start")
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_close()
    print("on_close end")


def on_open(ws):
    print("on_open start")
    websocket_connection = websocket_connection_handler[ws]
    websocket_connection.on_open(ws)
    print("on_open end")


connection_id = 0


class ConnectionState:
    IDLE = 0
    CONNECTED = 1
    CLOSED_ON_ERROR = 2


def websocket_func(*args):
    try:
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
        if connection_instance.state == ConnectionState.CONNECTED:
            connection_instance.state = ConnectionState.IDLE
    except Exception as ee:
        print(ee)


class WebsocketConnection:

    def __init__(self, api_key, secret_key, uri, watch_dog, request):
        print("### __init__ ###")
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

    def in_delay_connection(self):
        print("### in_delay_connection ###")
        return self.delay_in_second != -1

    def re_connect_in_delay(self, delay_in_second):
        print("### re_connect_in_delay ###")
        if self.ws is not None:
            self.ws.close()
            self.ws = None
        self.delay_in_second = delay_in_second
        self.logger.warning("[Sub][" + str(self.id) + "] Reconnecting after "
                            + str(self.delay_in_second) + " seconds later")

    def re_connect(self):
        print("### re_connect ###")
        if self.delay_in_second != 0:
            self.delay_in_second -= 1
            self.logger.warning("In delay connection: " + str(self.delay_in_second))
        else:
            self.connect()

    def connect(self):
        print("### connect ###")
        if self.state == ConnectionState.CONNECTED:
            self.logger.info("[Sub][" + str(self.id) + "] Already connected")
        else:
            print("### connect prepare thread###")
            self.__thread = threading.Thread(target=websocket_func, args=[self])
            print("connect thread start " , self.url, self.__market_url, self.__trading_url)
            self.__thread.start()

    def send(self, data):
        print("send data : " + data)
        self.ws.send(data)

    def close(self):
        print("### close ###")
        self.ws.close()
        del websocket_connection_handler[self.ws]
        self.__watch_dog.on_connection_closed(self)
        self.logger.error("[Sub][" + str(self.id) + "] Closing normally")

    def on_open(self, ws):
        print("### open ###")
        self.logger.info("[Sub][" + str(self.id) + "] Connected to server")
        self.ws = ws
        self.last_receive_time = get_current_timestamp()
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
        print("### on_error ###")
        if self.request.error_handler is not None:
            exception = HuobiApiException(HuobiApiException.SUBSCRIPTION_ERROR, error_message)
            self.request.error_handler(exception)
        self.logger.error("[Sub][" + str(self.id) + "] " + str(error_message))

    def on_failure(self, error):
        print("### on_failure ###")
        self.on_error("Unexpected error: " + str(error))
        self.close_on_error()

    def on_message(self, message):
        print("### on_message ###")
        self.last_receive_time = get_current_timestamp()
        #print("origin message", message)
        dict_data = json.loads(gzip.decompress(message).decode("utf-8"), encoding="utf-8")
        print("dict data", dict_data)

        #print("RX: " + gzip.decompress(message).decode("utf-8"))

        status_outer = dict_data.get("status", "")
        err_code_outer = dict_data.get("err-code", 0)
        op_outer = dict_data.get("op", "")
        ch_outer = dict_data.get("ch", "")
        rep_outer = dict_data.get("rep", "")
        ping_outer = dict_data.get("ping", "")
        if status_outer and len(status_outer) and status_outer != "ok":
            error_code = dict_data.get("err-code", "Unknown error")
            error_msg = dict_data.get("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif err_code_outer and int(err_code_outer) != 0:
            error_code = dict_data.get("err-code", "Unknown error")
            error_msg = dict_data.get("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif op_outer and len(op_outer):
            if op_outer == "notify":
                self.__on_receive(dict_data)
            elif op_outer == "ping":
                ping_ts = dict_data.get("ts", 0)
                self.__process_ping_on_trading_line(ping_ts)
            elif op_outer == "auth":
                if self.request.subscription_handler is not None:
                    self.request.subscription_handler(self)
            elif op_outer == "req":
                self.__on_receive(dict_data)
        elif ch_outer and len(ch_outer):
            self.__on_receive(dict_data)
        elif rep_outer and len(rep_outer):
            self.__on_receive(dict_data)
        elif ping_outer and len(ping_outer):
            ping_ts = ping_outer
            self.__process_ping_on_market_line(ping_ts)
        else:
            print("unknown data process, RX: " + gzip.decompress(message).decode("utf-8"))

    def __on_receive(self, dict_data):
        print("### __on_receive ###")
        res = None
        try:
            if self.request.json_parser is not None:
                res = self.request.json_parser(dict_data)
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
        print("### __process_ping_on_trading_line ###")
        #self.send("{\"op\":\"pong\",\"ts\":" + str(get_current_timestamp()) + "}")
        PrintBasic.print_basic(ping_ts, "response time")
        self.send("{\"op\":\"pong\",\"ts\":" + str(ping_ts) + "}")
        return

    def __process_ping_on_market_line(self, ping_ts):
        print("### __process_ping_on_market_line ###")
        #self.send("{\"pong\":" + str(get_current_timestamp()) + "}")
        PrintBasic.print_basic(ping_ts, "response time")
        self.send("{\"pong\":" + str(ping_ts) + "}")
        return

    def close_on_error(self):
        print("### close_on_error ###")
        if self.ws is not None:
            self.ws.close()
            self.state = ConnectionState.CLOSED_ON_ERROR
            self.logger.error("[Sub][" + str(self.id) + "] Connection is closing due to error")
