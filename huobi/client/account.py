from huobi.constant import *
from huobi.service.account import *
from huobi.model.account import *
from huobi.utils import *


class AccountClient(object):
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

    def get_accounts(self):
        """
        Get the account list.
        :return: The list of accounts data.
        """

        return GetAccountsService({}).request(**self.__kwargs)

    def get_balance(self, account_id:'int'):
        """
        Get the account list.
        :return: The list of accounts data.
        """
        check_should_not_none(account_id, "account-id")
        params = {
            "account-id" : account_id
        }
        return GetBalanceService(params).request(**self.__kwargs)

    def get_account_balance(self):
        account_balance_list = []
        accounts = self.get_accounts()
        if accounts and len(accounts):
            for account_obj in accounts:
                account_balance_obj = AccountBalance()
                account_balance_obj.id = account_obj.id
                account_balance_obj.type = account_obj.type
                account_balance_obj.state = account_obj.state
                balance_list = self.get_balance(account_obj.id)
                account_balance_obj.list = balance_list
                account_balance_list.append(account_balance_obj)
        return account_balance_list

    def get_account_balance_by_subuid(self, sub_uid):
        """
        Get account balance of a sub-account.

        :param sub_uid: the specified sub account id to get balance for.
        :return: the balance of a sub-account specified by sub-account uid.
        """
        check_should_not_none(sub_uid, "sub-uid")
        params = {
            "sub-uid" : sub_uid
        }
        return GetAccountBalanceBySubUidService(params).request(**self.__kwargs)

    def get_aggregated_subuser_balance(self):
        """
        Get the aggregated balance of all sub-accounts of the current user.

        :return: The balance of all the sub-account aggregated.
        """
        params={}
        return GetAggregateSubUserBalanceService(params).request(**self.__kwargs)

    def transfer_between_parent_and_subuser(self, sub_uid: 'int', currency: 'str', amount: 'float',
                                        transfer_type: 'TransferMasterType'):
        """
        Transfer Asset between Parent and Sub Account.

        :param sub_uid: The target sub account uid to transfer to or from. (mandatory)
        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, see {@link TransferMasterType} (mandatory)
        :return: The order id.
        """
        check_currency(currency)
        check_should_not_none(sub_uid, "sub-uid")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "type")

        params = {
            "sub-uid" : sub_uid,
            "currency" : currency,
            "amount" : amount,
            "type" : transfer_type
        }
        return PostSubaccountTransferService(params).request(**self.__kwargs)

    def sub_account_change(self, model: 'BalanceMode', callback, error_handler=None):
        """
        Subscribe account changing event. If the balance is updated, server will send the data to client and onReceive in callback will be called.

        :param model: when model is AVAILABLE, balance refers to available balance; when model is TOTAL, balance refers to TOTAL balance for trade sub account (available+frozen).
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(account_event: 'AccountEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """

        check_should_not_none(model, "model")
        check_should_not_none(callback, "callback")

        params = {
            "model" : model,
        }

        SubAccountChangeService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_account_balance(self, callback, client_req_id=None, error_handler=None):
        """
        Subscribe account changing event. If the balance is updated, server will send the data to client and onReceive in callback will be called.

        :param client_req_id: client request ID
        :param auto_close : close websocket connection after get data
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(account_event: 'AccountEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """

        check_should_not_none(callback, "callback")
        params = {
            "client_req_id" : client_req_id
        }

        ReqAccountBalanceService(params).subscribe(callback, error_handler, **self.__kwargs)
