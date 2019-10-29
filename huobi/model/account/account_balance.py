from huobi.constant import *


class AccountBalance:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        list: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.id = 0
        self.type = AccountType.INVALID
        self.state = AccountState.INVALID
        self.list = list()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Account ID")
        PrintBasic.print_basic(self.type, format_data + "Account Type")
        PrintBasic.print_basic(self.state, format_data + "Account State")
        print()
        if len(self.list):
            for row in self.list:
                row.print_object(format_data+"\t")
                print()
