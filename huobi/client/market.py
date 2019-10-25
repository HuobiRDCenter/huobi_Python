
from huobi.constant import *
from huobi.service.market import *
from huobi.serialize.market import *
from huobi.model.market import *
from huobi.utils import *


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

    def get_candlestick(self, symbol, interval, size):
        """
        Get the candlestick/kline for the specified symbol. The data number is 150 as default.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The start time of of requested candlestick/kline data. (optional)
        :return: The list of candlestick/kline data.
        """
        check_symbol(symbol)
        check_should_not_none(interval, "interval")
        check_range(size, 1, 2000, "size")

        params = {
            "symbol": symbol,
            "interval": interval,
            "size": size
        }

        return GetCandleStickService(params).request(**self.__kwargs)

    def sub_candlestick(self, symbols: 'str', interval: 'CandlestickInterval', callback, error_handler):

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
        check_symbol_list(symbol_list)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
            "interval" : interval,
        }

        SubCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_candlestick(self, symbols: 'str', interval: 'CandlestickInterval', callback,
                                    from_ts_second = None, end_ts_second = None, error_handler=None):
        """
        Subscribe candlestick/kline event. If the candlestick/kline is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(candlestick_event: 'CandlestickEvent'):
                        pass
        :param from_ts_second : data from timestamp [it's second]
        :param end_ts_second : data util timestamp [it's second]
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return: No return
        """

        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
            "interval" : interval,
            "from_ts_second" : from_ts_second,
            "end_ts_second" : end_ts_second
        }

        ReqCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)

    def get_pricedepth(self, symbol: 'str', size: 'int' = 20) -> PriceDepth:
        """
        Get the Market Depth of a symbol.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param size: The maximum number of Market Depth requested. range [1 - 150], default is 20. (optional)
        :return: Market Depth data.
        """

        check_symbol(symbol)
        check_range(size, 1, 150, "size")

        params = {
            "symbol": symbol,
            "type": "step0",
            "size": size
        }

        return GetPriceDepthService(params).request(**self.__kwargs)

    def sub_pricedepth(self, symbols: 'str', depth_step: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param depth_step: The depth precision, string from step0 to step5.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event: 'PriceDepthEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass

        :return:  No return
        """
        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        new_step = PriceDepthSerial.get_valid_depth_step(value=depth_step, defalut_value=DepthStep.STEP0)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
            "step" : new_step,
        }

        SubPriceDepthService(params).subscribe(callback, error_handler, **self.__kwargs)

    def sub_pricedepth_bbo(self, symbols: 'str', callback, error_handler=None):
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
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
        }

        SubPriceDepthBboService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_pricedepth(self, symbols: 'str', depth_step: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param depth_step: The depth precision, string from step0 to step5.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event: 'PriceDepthEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass

        :return:  No return
        """
        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        new_step = PriceDepthSerial.get_valid_depth_step(value=depth_step, defalut_value=DepthStep.STEP0)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list": symbol_list,
            "step": new_step,
        }

        ReqPriceDepthService(params).subscribe(callback, error_handler, **self.__kwargs)

    def get_market_detail(self, symbol: 'str') -> MarketDetail:
        """
        Get trade statistics in 24 hours.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: Trade statistics.
        """

        check_symbol(symbol)

        params = {
            "symbol": symbol,
        }

        return GetMarketDetailService(params).request(**self.__kwargs)

    def sub_market_detail(self, symbols: 'str', callback, error_handler=None):
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
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
        }

        SubMarketDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_market_detail(self, symbols: 'str', callback, error_handler=None):
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
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list": symbol_list,
        }

        ReqMarketDetailService(params).subscribe(callback, error_handler, **self.__kwargs)


    def get_market_trade(self, symbol: 'str') -> list:
        """
        Get the most recent trades with their price, volume and direction.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :return: The list of trade.
        """

        check_symbol(symbol)

        params = {
            "symbol": symbol,
        }

        return GetMarketTradeService(params).request(**self.__kwargs)

    def get_history_trade(self, symbol: 'str', size: 'int' = None) -> list:
        """
        Get the most recent trades with their price, volume and direction.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param size: The number of historical trade requested, range [1 - 2000] (optional)
        :return: The list of trade.
        """

        check_symbol(symbol)
        check_range(size, 1, 2000, "size")

        params = {
            "symbol": symbol,
            "size" : size
        }

        return GetHistoryTradeService(params).request(**self.__kwargs)

    def sub_trade_detail(self, symbols: 'str', callback, error_handler=None):
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
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")


        params = {
            "symbol_list" : symbol_list,
        }

        SubTradeDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_trade_detail(self, symbols: 'str', callback, error_handler=None):
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
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
        }

        ReqTradeDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def get_market_detail_merged(self, symbol):
        check_symbol(symbol)
        params = {
            "symbol": symbol
        }

        return GetMarketDetailMergedService(params).request(**self.__kwargs)