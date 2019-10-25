from huobi.constant import *
from huobi.model.generic import *
from huobi.service.generic import *
from huobi.utils import *


class GenericClient(object):
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

    def get_exchange_timestamp(self) -> int:
        """
        Get the timestamp from Huobi server. The timestamp is the Unix timestamp in millisecond.
        The count shows how many milliseconds passed from Jan 1st 1970, 00:00:00.000 at UTC.
        e.g. 1546300800000 is Thu, 1st Jan 2019 00:00:00.000 UTC.

        :return: The timestamp in UTC
        """

        params = {}

        return GetExchangeTimestampService(params).request(**self.__kwargs)

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

    def get_reference_currencies(self, currency:'str'=None, is_authorized_user:'bool' =None) ->list:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :param currency: btc, ltc, bch, eth, etc ...(available currencies in Huobi Global)
        :param is_authorized_user: is Authorized user? True or False
        :return: The information of trading instrument and currencies.
        """

        params = {
            "currency" : currency,
            "authorizedUser" : is_authorized_user
        }

        return GetReferenceCurrenciesService(params).request(**self.__kwargs)
