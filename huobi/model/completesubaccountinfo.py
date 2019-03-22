from huobi.model.constant import *


class CompleteSubAccountInfo:
    """
    Sub-account completed info

    :member
        id: The sub-id.
        account_type: The sub account type.
        balances: The balance list, the content is Balance class.
    """

    def __init__(self):
        self.id = 0
        self.account_type = AccountType.INVALID
        self.balances = list()
