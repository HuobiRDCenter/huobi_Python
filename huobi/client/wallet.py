"""
from huobi.constant.system import RestApiDefine, HttpMethod
from huobi.utils import RestApiRequest
from huobi.utils.restapirequestimpl import RestApiRequestImpl
from huobi.utils.restapiinvoker import call_sync
from huobi.utils.account_info_map import account_info_map
from huobi.utils.api_signature.py import create_signature
from huobi.utils.input_checker import *
from huobi.utils.url_params_builder import urlParamsBuilder
from huobi.model import *
"""
from huobi.constant.system import RestApiDefine
from huobi.utils.input_checker import *


class WalletClient(object):
    __server_url = RestApiDefine.Url
    args_config = {}

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        self.args_config = kwargs

        """
        if "api_key" in kwargs:
            self.__api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            self.__secret_key = kwargs["secret_key"]
        if "url" in kwargs:
            self.__server_url = kwargs["url"]
        """

        """   
        for request has bind subscription_handler and parse_handler to connection, so connection can't be reused
        if "reuse_sub_connection" in kwargs:
            self.__reuse_sub_connection = kwargs["reuse_sub_connection"]
            if self.__reuse_sub_connection and self.__reuse_sub_connection == True:
                self.__reuse_sub_connection = True
        """


    def get_candlestick(self, symbol, interval, size, startTime=None, endTime=None):
        """
        Get the candlestick/kline for the specified symbol. The data number is 150 as default.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The start time of of requested candlestick/kline data. (optional)
        :param start_time: The start time of of requested candlestick/kline data. (optional)
        :param end_time: The end time of of requested candlestick/kline data. (optional)
        :return: The list of candlestick/kline data.
        """
        check_symbol(symbol)
        check_should_not_none(interval, "interval")

        params = {
            "symbol": symbol,
            "interval": interval,
            "size": size
        }
        if startTime:
            params["start_time"] = startTime
        if endTime:
            params["end_time"] = endTime

        return CandleStickServiceGet(params).request(self.args_config)

    def sub_candlestick(self, symbols: 'str', interval: 'CandlestickInterval', callback, error_handler):
        """
        Get the candlestick/kline for the specified symbol. The data number is 150 as default.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :return: The list of candlestick/kline data.
        """
        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
            "interval" : interval
        }

        CandleStickServiceSub(params).subscribe(self.args_config, callback, error_handler)