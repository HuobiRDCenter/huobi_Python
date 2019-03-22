from huobi.model.constant import *


class Balance:
    """
    The balance of specified account.

    :member
        currency: The currency of this balance.
        balance_type: The balance type, trade or frozen.
        balance: The balance in the main currency unit.

    """

    def __init__(self):
        self.currency = ""
        self.balance_type = BalanceType.INVALID
        self.balance = 0.0
