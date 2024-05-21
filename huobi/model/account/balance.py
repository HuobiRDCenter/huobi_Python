from huobi.constant import *
from huobi.utils import default_parse_list_dict


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
        self.type = AccountBalanceUpdateType.INVALID
        self.balance = 0.0
        self.seq_num = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.type, format_data + "Balance Type")
        PrintBasic.print_basic(self.balance, format_data + "Balance")
        PrintBasic.print_basic(self.seq_num, format_data + "Sequence Number")
