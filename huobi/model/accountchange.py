from huobi.model.constant import *


class AccountChange:
    """
    The account change information received by subscription of account.

    :member
        currency: The currency of the change.
        account_type: The account of the change.
        balance: The balance value.
        balance_type: The balance type.

    """

    def __init__(self):
        self.currency = ""
        self.account_type = AccountType.INVALID
        self.balance = 0.0
        self.balance_type = BalanceType.INVALID
