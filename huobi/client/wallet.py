from huobi.utils.input_checker import *


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

    # 充提记录
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

    # 虚拟币提币
    def post_create_withdraw(self, address: 'str', amount: 'float', currency: 'str', fee: 'float',
                             chain: 'str' = None, address_tag: 'str' = None, client_order_id: 'str' = None) -> int:
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
            "addr-tag": address_tag,
            "client-order-id": client_order_id
        }

        from huobi.service.wallet.post_create_withdraw import PostCreateWithdrawService
        return PostCreateWithdrawService(params).request(**self.__kwargs)

    # 取消提币
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

    # 充币地址查询
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

    # 提币额度查询
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

    # 提币地址查询
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

    # 通过clientOrderId查询提币订单
    def get_account_withdraw_client_order_id(self, client_order_id: 'str'):
        check_should_not_none(client_order_id, "clientOrderId")
        params = {
            "clientOrderId": client_order_id
        }
        from huobi.service.wallet.get_account_withdraw_client_order_id import GetAccountWithdrawClientOrderIdService
        return GetAccountWithdrawClientOrderIdService(params).request(**self.__kwargs)



