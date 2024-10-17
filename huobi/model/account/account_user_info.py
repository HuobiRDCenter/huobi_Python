class AccountUserInfoResult:
    def __init__(self):
        self.pointSwitch = 0
        self.currencySwitch = 0
        self.deductionCurrency = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.pointSwitch, format_data + "pointSwitch")
        PrintBasic.print_basic(self.currencySwitch, format_data + "currencySwitch")
        PrintBasic.print_basic(self.deductionCurrency, format_data + "deductionCurrency")
