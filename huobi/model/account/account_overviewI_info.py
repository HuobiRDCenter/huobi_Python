class AccountOverviewInfoResult:
    def __init__(self):
        self.currency = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "currency")
