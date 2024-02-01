from huobi.constant import *
from huobi.utils import default_parse_list_dict


class ProfitAccountBalanceList:

    def __init__(self):
        self.distributionType = ""
        self.balance = 0.0
        self.success = None
        self.accountBalance = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.distributionType, format_data + "distributionType")
        PrintBasic.print_basic(self.balance, format_data + "balance")
        PrintBasic.print_basic(self.success, format_data + "success")
        PrintBasic.print_basic(self.accountBalance, format_data + "accountBalance")





