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

    @staticmethod
    def json_parse(json_data):
        balance = Balance()
        balance.balance = json_data.get_string("balance")
        balance.currency = json_data.get_string("currency")
        balance.balance_type = json_data.get_string("type")
        return balance

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.balance_type, format_data + "Balance Type")
        PrintBasic.print_basic(self.balance, format_data + "Balance")