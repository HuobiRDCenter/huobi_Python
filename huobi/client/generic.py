from huobi.constant import *
from huobi.model.generic import *
from huobi.service.generic import *
from huobi.utils import *


class GenericClient(object):
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

    def get_exchange_currencies(self) -> list():
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading currencies.
        """

        params = {}

        return GetExchangeCurrenciesService(params).request(**self.__kwargs)

    def get_exchange_symbols(self) -> list():
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument etc.

        :return: The information of trading instrument.
        """

        params = {}

        return GetExchangeSymbolsService(params).request(**self.__kwargs)

    def get_exchange_info(self) -> ExchangeInfo:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading instrument and currencies.
        """

        ret = ExchangeInfo()
        ret.symbol_list = self.get_exchange_symbols()
        ret.currencies = self.get_exchange_currencies()
        return ret
