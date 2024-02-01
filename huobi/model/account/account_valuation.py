from huobi.constant import *
from huobi.model.account.updated import Updated


class AccountValuation:

    def __init__(self):
        self.totalBalance = ""
        self.todayProfit = ""
        self.todayProfitRate = ""
        self.profitAccountBalanceList = []
        self.updated = Updated()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.totalBalance, format_data + "totalBalance")
        PrintBasic.print_basic(self.todayProfit, format_data + "todayProfit")
        PrintBasic.print_basic(self.todayProfitRate, format_data + "todayProfitRate")
        if self.profitAccountBalanceList and len(self.profitAccountBalanceList):
            for profitAccountBalanceList_obj in self.profitAccountBalanceList:
                profitAccountBalanceList_obj.print_object("\t")
                print()
        self.updated.print_object()


