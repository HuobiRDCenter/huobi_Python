from huobi.constant.system import RestApiDefine
from huobi.service.market.getcandlestick import GetCandleStickService
from huobi.service.market.subcandlestick import SubCandleStickService
from huobi.utils.inputchecker import *


class MarketClient(object):
    __server_url = RestApiDefine.Url
    __kwargs = {}
    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        self.__kwargs = kwargs

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

        return GetCandleStickService(params).request(**self.__kwargs)

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

        SubCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)