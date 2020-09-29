import threading
import websocket
import gzip
import ssl
import logging
import urllib.parse

from huobi.constant import *
from huobi.utils import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.connection.impl.private_def import ConnectionState

# Key: original_connection, Value: connection
websocket_connection_handler = dict()


def on_message(original_connection, message):
    websocket_connection = websocket_connection_handler[original_connection]
    websocket_connection.on_message(message)
    return


def on_error(original_connection, error):
    websocket_connection = websocket_connection_handler[original_connection]
    websocket_connection.on_failure(error)


def on_close(original_connection):
    websocket_connection = websocket_connection_handler[original_connection]
    websocket_connection.on_close()


def on_open(original_connection):
    websocket_connection = websocket_connection_handler[original_connection]
    websocket_connection.on_open(original_connection)


connection_id = 0


def websocket_func(*args):
    try:
        websocket_manage = args[0]
        websocket_manage.original_connection = websocket.WebSocketApp(websocket_manage.url,
                                                        on_message=on_message,
                                                        on_error=on_error,
                                                        on_close=on_close)
        global websocket_connection_handler
        websocket_connection_handler[websocket_manage.original_connection] = websocket_manage
        websocket_manage.logger.info("[Sub][" + str(websocket_manage.id) + "] Connecting...")
        websocket_manage.original_connection.on_open = on_open
        websocket_manage.original_connection.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        websocket_manage.logger.info("[Sub][" + str(websocket_manage.id) + "] Connection event loop down")
        if websocket_manage.state == ConnectionState.CONNECTED:
            websocket_manage.state = ConnectionState.IDLE
    except Exception as ex:
        print(ex)

class WebsocketManage:

    def __init__(self, api_key, secret_key, uri, request):
        self.__thread = None
        self.__market_url = HUOBI_WEBSOCKET_URI_PRO + "/ws"
        self.__trading_url = HUOBI_WEBSOCKET_URI_PRO + "/ws/" + request.api_version
        self.__mbp_feed_url = HUOBI_WEBSOCKET_URI_PRO + "/feed"
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.request = request
        self.reconnect_at = 0
        self.original_connection = None
        self.last_receive_time = 0
        self.logger = logging.getLogger("huobi-client")
        self.state = ConnectionState.IDLE
        global connection_id
        connection_id += 1
        self.id = connection_id
        host = urllib.parse.urlparse(uri).hostname
        if host.find("api") == 0:
            self.__market_url = "wss://" + host + "/ws"
            self.__mbp_feed_url = "wss://" + host + "/feed"
            self.__trading_url = "wss://" + host + "/ws/" + request.api_version
        else:
            self.__market_url = "wss://" + host + "/api/ws"
            self.__mbp_feed_url = "wss://" + host + "/feed"
            self.__trading_url = "wss://" + host + "/ws/" + request.api_version

        if request.is_trading:
            self.url = self.__trading_url
        elif request.is_mbp_feed:
            self.url = self.__mbp_feed_url
        else:
            self.url = self.__market_url

    def close_and_wait_reconnect(self, delay_in_ms):
        if self.original_connection is not None:
            self.original_connection.close()
            self.original_connection = None
            self.state = ConnectionState.WAIT_RECONNECT
            self.reconnect_at =  + delay_in_ms
        self.logger.warning("[Sub][%d] Lost connectiong for %d ms, will try reconnecting " % (self.id, self.reconnect_at))

    def re_connect(self):
        if get_current_timestamp() > self.reconnect_at:
            self.logger.info("[Sub][%d] Reconnecting ... " % self.id)
            self.connect()

    def connect(self):
        if self.state == ConnectionState.CONNECTED:
            self.logger.info("[Sub][" + str(self.id) + "] Already connected")
        else:
            self.__thread = threading.Thread(target=websocket_func, args=[self])
            self.__thread.start()

    def send(self, data):
        # print("Send Data : " + data)
        self.original_connection.send(data)

    def close(self):
        self.original_connection.close()
        del websocket_connection_handler[self.original_connection]
        self.state = ConnectionState.CLOSED
        self.logger.info("[Sub][" + str(self.id) + "] Closing normally")

    def on_open(self, original_connection):
        self.logger.info("[Sub][" + str(self.id) + "] Connected to server")
        self.original_connection = original_connection
        self.last_receive_time = get_current_timestamp()
        self.state = ConnectionState.CONNECTED
        if self.request.is_trading:
            try:
                if self.request.api_version == ApiVersion.VERSION_V1:
                    builder = UrlParamsBuilder()
                    create_signature(self.__api_key, self.__secret_key,
                                     "GET", self.url, builder)
                    builder.put_url("op", "auth")
                    self.send(builder.build_url_to_json())
                elif self.request.api_version == ApiVersion.VERSION_V2:
                    builder = UrlParamsBuilder()
                    create_signature_v2(self.__api_key, self.__secret_key,
                                     "GET", self.url, builder)
                    self.send(builder.build_url_to_json())
                else:
                    self.on_error("api version for create the signature fill failed")

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
        if isinstance(message, (str)): # V2
            # print("RX string : ", message)
            dict_data = json.loads(message)
        elif isinstance(message, (bytes)): # V1
            # print("RX bytes: " + gzip.decompress(message).decode("utf-8"))
            dict_data = json.loads(gzip.decompress(message).decode("utf-8"))
        else:
            print("RX unknow type : ", type(message))
            return

        status_outer = dict_data.get("status", "")
        err_code_outer = dict_data.get("err-code", 0)
        op_outer = dict_data.get("op", "")
        action_outer = dict_data.get("action", "")
        ch_outer = dict_data.get("ch", "")
        rep_outer = dict_data.get("rep", "")
        ping_market_outer = int(dict_data.get("ping", 0))
        if status_outer and len(status_outer) and status_outer != "ok":
            error_code = dict_data.get("err-code", "Unknown error")
            error_msg = dict_data.get("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif err_code_outer and int(err_code_outer) != 0:
            error_code = dict_data.get("err-code", "Unknown error")
            error_msg = dict_data.get("err-msg", "Unknown error")
            self.on_error(error_code + ": " + error_msg)
        elif op_outer and len(op_outer): # for V1
            if op_outer == "notify":
                self.__on_receive(dict_data)
            elif op_outer == "ping":
                #print("******** receive trade ping pong ********", dict_data)
                ping_ts = dict_data.get("ts", 0)
                self.__process_ping_on_trading_line(ping_ts)
            elif op_outer == "auth":
                if self.request.subscription_handler is not None:
                    self.request.subscription_handler(self)
            elif op_outer == "req":
                self.__on_receive(dict_data)
        elif action_outer and len(action_outer):  # for V2
            if action_outer == "ping":
                action_data = dict_data.get("data")
                ping_ts = action_data.get("ts")
                self.__process_ping_on_v2_trade(ping_ts)
            elif action_outer == "sub":
                action_code = dict_data.get("code", -1)
                if action_code == 200:
                    logging.info("subscribe ACK received")
                else:
                    logging.error("receive error data : " + message)
            elif action_outer == "req": #
                action_code = dict_data.get("code", -1)
                if action_code == 200:
                    logging.info("signature ACK received")
                    if self.request.subscription_handler is not None:
                        self.request.subscription_handler(self)
                else:
                    logging.error("receive error data : " + message)
            elif action_outer == "push":
                action_data = dict_data.get("data")
                if action_data:
                    self.__on_receive(dict_data)
                else:
                    logging.error("receive error push data : " + message)

        elif ch_outer and len(ch_outer):
            self.__on_receive(dict_data)
        elif rep_outer and len(rep_outer):
            self.__on_receive(dict_data)
        elif ping_market_outer:
            #print("******** receive market ping pong ********", dict_data)
            ping_ts = ping_market_outer
            self.__process_ping_on_market_line(ping_ts)
        else:
            #print("unknown data process, RX: ", gzip.decompress(message).decode("utf-8"))
            pass

    def __on_receive(self, dict_data):
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

        # websocket request will close the connection after receive
        if self.request.auto_close:
            self.close()

    def __process_ping_on_trading_line(self, ping_ts):
        #print("### __process_ping_on_trading_line ###")
        #self.send("{\"op\":\"pong\",\"ts\":" + str(get_current_timestamp()) + "}")
        PrintBasic.print_basic(ping_ts, "response time")
        self.send("{\"op\":\"pong\",\"ts\":" + str(ping_ts) + "}")
        return

    def __process_ping_on_market_line(self, ping_ts):
        #print("### __process_ping_on_market_line ###")
        #self.send("{\"pong\":" + str(get_current_timestamp()) + "}")
        PrintBasic.print_basic(ping_ts, "response time")
        self.send("{\"pong\":" + str(ping_ts) + "}")
        return

    def __process_ping_on_v2_trade(self, ping_ts):
        # PrintDate.timestamp_to_date(ping_ts)
        self.send("{\"action\": \"pong\",\"data\": {\"ts\": " + str(ping_ts) +"}}")
        return

    def close_on_error(self):
        if self.original_connection is not None:
            self.original_connection.close()
            self.state = ConnectionState.CLOSED_ON_ERROR
            self.logger.error("[Sub][" + str(self.id) + "] Connection is closing due to error")
