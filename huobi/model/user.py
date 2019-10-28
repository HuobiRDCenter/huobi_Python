from huobi.exception.huobiapiexception import HuobiApiException
from huobi.model import AccountType


class User:
    """
    The user's account information, consisting of account and balance etc.

    :member
        accounts: The account list. The content is Account class.
    """

    def __init__(self):
        self.accounts = list()

    def get_account_by_type(self, account_type, subtype:'str'=None):
        """
        Get account by account type.

        :param account_type: The specified account type.
        :param subtype: for margin trade
        :return: The account.
        """
        margin_account_type_list = [AccountType.MARGIN]
        if account_type in margin_account_type_list and subtype is None or len(subtype) == 0:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] subtype for margin account error")
        for account in self.accounts:
            if account.account_type == account_type:
                if account_type in margin_account_type_list:
                    if account.subtype == subtype:
                        return account
                else:
                    return account
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] No such account")

    def get_account_by_id(self, account_id):
        """
        Get account by account id.

        :param account_id: The specified account id.
        :return: The account.
        """
        for account in self.accounts:
            if account.id == account_id:
                return account
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] No such account")
