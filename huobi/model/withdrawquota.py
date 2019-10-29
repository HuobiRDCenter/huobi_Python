
class WithdrawQuota:
    """
    Withdraw Quota info.

    :member
        chain: Block chain name.
        maxWithdrawAmt: Maximum withdraw amount in each request.
        withdrawQuotaPerDay: Maximum withdraw amount in a day
        remainWithdrawQuotaPerDay: Remaining withdraw quota in the day
        withdrawQuotaPerYear: Maximum withdraw amount in a year
        remainWithdrawQuotaPerYear: Remaining withdraw quota in the year
        withdrawQuotaTotal: Maximum withdraw amount in total
        remainWithdrawQuotaTotal: Remaining withdraw quota in total
    """
    def __init__(self):
        self.chain = ""
        self.maxWithdrawAmt = ""
        self.withdrawQuotaPerDay = ""
        self.remainWithdrawQuotaPerDay = ""
        self.withdrawQuotaPerYear = ""
        self.remainWithdrawQuotaPerYear = ""
        self.withdrawQuotaTotal = ""
        self.remainWithdrawQuotaTotal = ""



    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.chain, format_data + "Chain")
        PrintBasic.print_basic(self.maxWithdrawAmt, format_data + "maxWithdrawAmt")
        PrintBasic.print_basic(self.withdrawQuotaPerDay, format_data + "withdrawQuotaPerDay")
        PrintBasic.print_basic(self.remainWithdrawQuotaPerDay, format_data + "remainWithdrawQuotaPerDay")
        PrintBasic.print_basic(self.withdrawQuotaPerYear, format_data + "withdrawQuotaPerYear")
        PrintBasic.print_basic(self.remainWithdrawQuotaPerYear, format_data + "remainWithdrawQuotaPerYear")
        PrintBasic.print_basic(self.withdrawQuotaTotal, format_data + "withdrawQuotaTotal")
        PrintBasic.print_basic(self.remainWithdrawQuotaTotal, format_data + "remainWithdrawQuotaTotal")
