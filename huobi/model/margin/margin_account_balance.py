from huobi.constant import *


class MarginAccountBalance:
    """
    The margin order information.

    :member
        id: Inner id.
        type: The account type.
        state: The account state.
        symbol: The symbol, like "btcusdt".
        fl_price: The trigger price.
        fl_type: The trigger type.
        risk_rate: The risk rate.
        list:Balance Object list
    """

    def __init__(self):
        self.id = 0
        self.type = AccountType.INVALID
        self.state = AccountState.INVALID
        self.symbol = ""
        self.fl_price = 0.0
        self.fl_type = 0.0
        self.risk_rate = 0.0
        self.list = []

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.type, format_data + "Account Type")
        PrintBasic.print_basic(self.state, format_data + "Account State")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.fl_price, format_data + "Trigger Price")
        PrintBasic.print_basic(self.fl_type, format_data + "Trigger Type")
        PrintBasic.print_basic(self.risk_rate, format_data + "Risk Rate")
        if self.list and len(self.list):
            for balance_obj in self.list:
                balance_obj.print_object("\t")
                print()