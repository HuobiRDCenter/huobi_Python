from huobi.exception.huobi_api_exception import HuobiApiException


class User:
    """
    The user's account information, consisting of account and balance etc.

    :member
        accounts: The account list. The content is Account class.
    """

    def __init__(self):
        self.accounts = list()

    def get_account_by_type(self, account_type):
        """
        Get account by account type.

        :param account_type: The specified account type.
        :return: The account.
        """
        for account in self.accounts:
            if account.account_type == account_type:
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
