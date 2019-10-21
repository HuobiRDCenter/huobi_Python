from huobi.constant import *
from huobi.service.account import *
from huobi.utils import *


class AccountClient(object):
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
        self.__kwargs = kwargs

    def get_accounts(self):
        """
        Get the account list.
        :return: The list of accounts data.
        """

        return GetAccountsService({}).request(**self.__kwargs)

    def sub_account_change(self, mode: 'BalanceMode', callback, error_handler=None):
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

        check_should_not_none(mode, "mode")
        check_should_not_none(callback, "callback")

        params = {
            "mode" : mode,
        }

        SubAccountChangeEventService(params).subscribe(callback, error_handler, **self.__kwargs)

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

        """
        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
            "interval" : interval
        }

        if from_ts_second:
            params["from_ts_second"] = from_ts_second

        if end_ts_second:
            params["end_ts_second"] = end_ts_second

        self.__kwargs = fill_auto_close(self.__kwargs)  # for websocket need set auto_close to True as default, with strict check in fill_auto_close

        ReqCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)
        """
        pass