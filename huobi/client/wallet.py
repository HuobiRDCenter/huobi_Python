from huobi.utils.input_checker import *
from huobi.model.wallet import *


class WalletClient(object):

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

    def get_deposit_withdraw(self, op_type: 'str', currency: 'str' = None, from_id: 'int' = None, size: 'int' = None,
                             direct: 'str' = None) -> list:
        """
        Get the withdraw records of an account.

        :param currency: The currency, like "btc". (optional)
        :param from_id: The beginning withdraw record id. (optional)
        :param op_type: deposit or withdraw, see defination DepositWithdraw (mandatory)
        :param size: The size of record. (optional)
        :param direct: "prev" is order by asc, "next" is order by desc, default as "prev"(optional)
        :return: The list of withdraw records.
        """
        check_should_not_none(op_type, "operate type")

        params = {
            "currency": currency,
            "type": op_type,
            "from": from_id,
            "direct": direct,
            "size": size
        }

        from huobi.service.wallet.get_deposit_withdraw import GetDepositWithdrawService
        return GetDepositWithdrawService(params).request(**self.__kwargs)

    def post_create_withdraw(self, address: 'str', amount: 'float', currency: 'str', fee: 'float',
                             chain: 'str' = None, address_tag: 'str' = None) -> int:
        """
        Submit a request to withdraw some asset from an account.

        :param address: The destination address of this withdraw. (mandatory)
        :param amount: The amount of currency to withdraw. (mandatory)
        :param currency: The crypto currency to withdraw. (mandatory)
        :param fee: The fee to pay with this withdraw. (mandatory)
        :param address_tag: A tag specified for this address. (optional)
        :param chain: set as "usdt" to withdraw USDT to OMNI, set as "trc20usdt" to withdraw USDT to TRX. (optional)
        :return: Withdraw id
        """
        check_symbol(currency)
        check_should_not_none(address, "address")
        check_should_not_none(amount, "amount")
        check_should_not_none(fee, "fee")

        params = {
            "currency": currency,
            "address": address,
            "amount": amount,
            "fee": fee,
            "chain": chain,
            "addr-tag": address_tag
        }

        from huobi.service.wallet.post_create_withdraw import PostCreateWithdrawService
        return PostCreateWithdrawService(params).request(**self.__kwargs)

    def post_cancel_withdraw(self, withdraw_id: 'int') -> int:
        """
        Cancel an withdraw request.

        :param withdraw_id: withdraw id (mandatory)
        :return: No return.
        """
        params = {
            "withdraw-id": withdraw_id
        }

        from huobi.service.wallet.post_cancel_withdraw import PostCancelWithdrawService
        return PostCancelWithdrawService(params).request(**self.__kwargs)

    def get_account_deposit_address(self, currency: 'str') -> list:
        """
        Get deposit address of corresponding chain, for a specific crypto currency (except IOTA)

        :param currency: The currency, like "btc". (optional)
        :return:
        """
        check_should_not_none(currency, "currency")

        params = {
            "currency": currency
        }

        from huobi.service.wallet.get_account_deposit_address import GetAccountDepositAddressService
        return GetAccountDepositAddressService(params).request(**self.__kwargs)

    def get_account_withdraw_quota(self, currency: 'str') -> list:
        """
        Get the withdraw quota for currencies

        :param currency: The currency, like "btc". (mandatory)
        :return:
        """
        check_should_not_none(currency, "currency")

        params = {
            "currency": currency,
        }

        from huobi.service.wallet.get_account_withdraw_quota import GetAccountWithdrawQuotaService
        return GetAccountWithdrawQuotaService(params).request(**self.__kwargs)

    def get_sub_user_deposit_history(self, sub_uid: 'int', currency: 'str' = None,
                                     start_time: 'int' = None, end_time: 'int' = None,
                                     sort: 'str' = None, limit: 'int' = None, from_id: 'int' = None) -> DepositHistory:
        """
        Parent get sub user depoist history.

        :param sub_uid: Sub user id. (mandatory)
        :param currency: Cryptocurrency.
        :param start_time: Farthest time
        :param end_time: Nearest time
        :param sort: Sorting order
        :param limit: Maximum number of items in one page
        :param from_id: First record Id in this query
        """
        check_should_not_none(sub_uid, "sub_uid")

        params = {
            "subUid": sub_uid,
            "currency": currency,
            "startTime": start_time,
            "endTime": end_time,
            "sort": sort,
            "limit": limit,
            "fromId": from_id
        }

        from huobi.service.wallet.get_sub_user_deposit_history import GetSubUserDepositHistoryService
        return GetSubUserDepositHistoryService(params).request(**self.__kwargs)

    def get_sub_user_deposit_address(self, sub_uid: 'int', currency: 'str') -> list:
        """
        Parent get sub user deposit address

        :param sub_uid: Sub user id
        :param currency: Cryptocurrency, like "btc". (mandatory)
        :return:
        """

        check_should_not_none(sub_uid, "subUid")
        check_should_not_none(currency, "currency")
        params = {
            "subUid": sub_uid,
            "currency": currency
        }

        from huobi.service.wallet.get_sub_user_deposit_address import GetSubUserDepositAddressService
        return GetSubUserDepositAddressService(params).request(**self.__kwargs)

    def get_account_withdraw_address(self, currency: 'str', chain: 'str'=None, note: 'str'=None, limit: 'int' = 100,
                                     fromid: 'int' = None):
        check_should_not_none(currency, "currency")
        params = {
            "currency": currency,
            "chain": chain,
            "note": note,
            "limit": limit,
            "fromid": fromid
        }
        from huobi.service.wallet.get_account_withdraw_address import GetAccountWithdrawAddressService
        return GetAccountWithdrawAddressService(params).request(**self.__kwargs)

