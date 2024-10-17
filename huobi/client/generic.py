from huobi.model.generic import *


class GenericClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """
        self.__kwargs = kwargs

    # 获取当前系统时间戳
    def get_exchange_timestamp(self) -> int:
        """
        Get the timestamp from Huobi server. The timestamp is the Unix timestamp in millisecond.
        The count shows how many milliseconds passed from Jan 1st 1970, 00:00:00.000 at UTC.
        e.g. 1546300800000 is Thu, 1st Jan 2019 00:00:00.000 UTC.

        :return: The timestamp in UTC
        """

        params = {}

        from huobi.service.generic.get_exchange_timestamp import GetExchangeTimestampService
        return GetExchangeTimestampService(params).request(**self.__kwargs)

    def get_exchange_currencies(self) -> list:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading currencies.
        """

        params = {}

        from huobi.service.generic.get_exchange_currencies import GetExchangeCurrenciesService
        return GetExchangeCurrenciesService(params).request(**self.__kwargs)

    def get_exchange_symbols(self) -> list:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument etc.

        :return: The information of trading instrument.
        """

        params = {}

        from huobi.service.generic.get_exchange_symbols import GetExchangeSymbolsService
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

    # APIv2币链参考信息
    def get_reference_currencies(self, currency: 'str' = None, is_authorized_user: 'bool' = None) -> list:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :param currency: btc, ltc, bch, eth, etc ...(available currencies in Huobi Global)
        :param is_authorized_user: is Authorized user? True or False
        :return: The information of trading instrument and currencies.
        """

        params = {
            "currency": currency,
            "authorizedUser": is_authorized_user
        }

        from huobi.service.generic.get_reference_currencies import GetReferenceCurrenciesService
        return GetReferenceCurrenciesService(params).request(**self.__kwargs)

    # 获取当前系统状态
    def get_system_status(self) -> str:
        """
        get system status

        :return: system status.
        """

        from huobi.service.generic.get_system_status import GetSystemStatusService
        return GetSystemStatusService({}).request(**self.__kwargs)

    # 获取当前市场状态
    def get_market_status(self):
        from huobi.service.generic.get_market_status import GetMarketStatusService
        return GetMarketStatusService({}).request(**self.__kwargs)

    # 获取所有交易对(V2)
    def get_common_symbols(self, ts: 'int' = None):
        params = {
            "ts": ts
        }

        from huobi.service.generic.get_common_symbols import GetCommonSymbolsService
        return GetCommonSymbolsService(params).request(**self.__kwargs)

    # 获取所有币种(V2)
    def get_common_currencies(self, ts: 'int' = None):
        params = {
            "ts": ts
        }

        from huobi.service.generic.get_common_currencies import GetCommonCurrenciesService
        return GetCommonCurrenciesService(params).request(**self.__kwargs)

    # 获取币种配置
    def get_common_currencys(self, ts: 'int' = None):
        params = {
            "ts": ts
        }

        from huobi.service.generic.get_common_currencys import GetCommonCurrencysService
        return GetCommonCurrencysService(params).request(**self.__kwargs)

    # 获取交易对配置
    def get_common_symbols_v1(self, ts: 'int' = None):
        params = {
            "ts": ts
        }

        from huobi.service.generic.get_common_symbols_v1 import GetCommonSymbolsV1Service
        return GetCommonSymbolsV1Service(params).request(**self.__kwargs)

    # 获取市场交易对配置
    def get_market_symbols(self, symbols: 'str' = None, ts: 'int' = None):
        params = {
            "symbols": symbols,
            "ts": ts
        }

        from huobi.service.generic.get_market_symbols import GetMarketSymbolsService
        return GetMarketSymbolsService(params).request(**self.__kwargs)

    # 查询链信息
    def get_common_chains(self, show_desc: 'str' = None, currency: 'str' = None, ts: 'int' = None):
        params = {
            "show-desc": show_desc,
            "currency": currency,
            "ts": ts
        }

        from huobi.service.generic.get_common_chains import GetCommonChainsService
        return GetCommonChainsService(params).request(**self.__kwargs)
