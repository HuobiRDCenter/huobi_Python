from huobi.constant import *


class AccountPointGroup:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        list: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.groupId = ""
        self.expiryDate = ""
        self.remainAmt = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.groupId, format_data + "Group Id")
        PrintBasic.print_basic(self.expiryDate, format_data + "Expiration date")
        PrintBasic.print_basic(self.remainAmt, format_data + "Remain Amount")
