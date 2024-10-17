from huobi.model.etf import *
from huobi.utils import *


class EtfClient(object):

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

    def get_etf_swap_config(self, etf_name: 'str') -> EtfSwapConfig:
        """
        Get the basic information of ETF creation and redemption, as well as ETF constituents,
        including max amount of creation, min amount of creation, max amount of redemption, min amount
        of redemption, creation fee rate, redemption fee rate, eft create/redeem status.
        :return: The etf configuration information.
        """
        check_symbol(etf_name)
        params={
            "etf_name":etf_name
        }

        from huobi.service.etf.get_etf_swap_config import GetEtfSwapConfigService
        return GetEtfSwapConfigService(params).request(**self.__kwargs)

    def get_etf_swap_list(self, etf_name: 'str', offset: 'int', size: 'int') -> list:
        """
        Get past creation and redemption.(up to 100 records)
        :param offset: The offset of the records, set to 0 for the latest records. (mandatory)
        :param size: The number of records to return, the range is [1, 100]. (mandatory)
        :return: The swap history.
        """
        check_symbol(etf_name)
        params={
            "etf_name":etf_name,
            "offset" : offset,
            "limit" : size
        }

        from huobi.service.etf.get_etf_swap_list import GetEtfSwapListService
        return GetEtfSwapListService(params).request(**self.__kwargs)

    def post_etf_swap_in(self, etf_name: 'str', amount: 'int') -> None:
        """
        Order creation or redemption of ETF.

        :param etf_name: The symbol, currently only support hb10. (mandatory)
        :param amount: The amount to create or redemption. (mandatory)
        :return: No return
        """
        check_symbol(etf_name)
        check_should_not_none(amount, "amount")

        params = {
            "etf_name" : etf_name,
            "amount" : amount
        }

        from huobi.service.etf.post_etf_swap_in import PostEftSwapInService
        return PostEftSwapInService(params).request(**self.__kwargs)

    def post_etf_swap_out(self, etf_name: 'str', amount: 'int') -> None:
        """
        Order creation or redemption of ETF.

        :param etf_name: The symbol, currently only support hb10. (mandatory)
        :param amount: The amount to create or redemption. (mandatory)
        :return: No return
        """

        check_symbol(etf_name)
        check_should_not_none(amount, "amount")

        params = {
            "etf_name": etf_name,
            "amount": amount
        }

        from huobi.service.etf.post_etf_swap_out import PostEtfSwapOutService
        return PostEtfSwapOutService(params).request(**self.__kwargs)

