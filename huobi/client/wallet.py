
from huobi.constant.system import RestApiDefine
from huobi.utils.input_checker import *
from huobi.service.wallet import *
from huobi.model.wallet import *


class WalletClient(object):
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

    def get_deposit_withdraw(self, op_type:'str', currency: 'str'=None, from_id: 'int'=None, size: 'int'=None, direct:'str'=None) -> list:
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

        return GetDepositWithdrawService(params).request(**self.__kwargs)

    def post_create_withdraw(self, address: 'str', amount: 'float', currency: 'str', fee: 'float',
                 chain:'str' =None, address_tag: 'str' = None) -> int:
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
            "addr-tag" : address_tag
        }

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

        return PostCancelWithdrawService(params).request(**self.__kwargs)

    def get_account_deposit_address(self, currency: 'str'):
        """
        Get deposit address of corresponding chain, for a specific crypto currency (except IOTA)

        :param currency: The currency, like "btc". (optional)
        :return:
        """
        check_should_not_none(currency, "currency")

        params = {
            "currency": currency
        }

        return GetAccountDepositAddressService(params).request(**self.__kwargs)

    def get_account_withdraw_quota(self, currency: 'str'):
        """
        Get the withdraw quota for currencies

        :param currency: The currency, like "btc". (mandatory)
        :return:
        """
        check_should_not_none(currency, "currency")

        params = {
            "currency": currency,
        }

        return GetAccountWithdrawQuotaService(params).request(**self.__kwargs)

