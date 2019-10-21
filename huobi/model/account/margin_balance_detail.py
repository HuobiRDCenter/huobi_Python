
from huobi.constant import *


class MarginBalanceDetail:
    def __init__(self):
        self.id = 0
        self.symbol = 0
        self.state = AccountState.INVALID
        self.type = AccountType.INVALID
        self.risk_rate = 0.0
        self.fl_price = 0.0
        self.fl_type = ""
        self.sub_account_balance_list = list()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.type, format_data + "Account Type")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.state, format_data + "Account State")
        PrintBasic.print_basic(self.fl_price, format_data + "Burst Price")
        PrintBasic.print_basic(self.fl_type, format_data + "Burst Type")
        PrintBasic.print_basic(self.risk_rate, format_data + "Risk Rate")