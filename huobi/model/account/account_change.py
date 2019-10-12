from huobi.constant import *


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

    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.account_type, format_data + "Account Type")
        PrintBasic.print_basic(self.balance_type, format_data + "Balance Type")
        PrintBasic.print_basic(self.balance, format_data + "Balance")