
from huobi.constant import *


class CompleteSubAccount:
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

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.account_type, format_data + "Account Type")
        if len(self.balances):
            for row in self.balances:
                row.print_object()
                print()