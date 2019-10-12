from huobi.constant import *


class Account:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        balances: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.id = 0
        self.account_type = AccountType.INVALID
        self.account_state = AccountState.INVALID



    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.account_type, format_data + "Account Type")
        PrintBasic.print_basic(self.account_state, format_data + "Account State")
        print()
        if len(self.balances):
            for row in self.balances:
                row.print_object()
                print()


