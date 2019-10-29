
from huobi.model.balance import Balance
from huobi.model.constant import *


class CrossMarginAccountBalance:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        type: The type of this account, possible value: spot, margin, otc, point.
        state: The account state, possible value: working, lock.
        list: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.id = 0
        self.type = AccountType.INVALID
        self.state = AccountState.INVALID
        self.risk_rate = 0
        self.acct_balance_sum = 0.0
        self.debt_balance_sum = 0.0
        self.list = list()

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Account ID")
        PrintBasic.print_basic(self.type, format_data + "Account Type")
        PrintBasic.print_basic(self.state, format_data + "Account State")
        PrintBasic.print_basic(self.risk_rate, format_data + "Risk Rate")
        PrintBasic.print_basic(self.acct_balance_sum, format_data + "Total Balance")
        PrintBasic.print_basic(self.debt_balance_sum, format_data + "Debt Balance")
        if self.list and len(self.list):
            for balance in self.list:
                balance.print_object()
                print()

