
from huobi.model.margin.loan_ino import LoanInfo

class CrossMarginLoanInfo(LoanInfo):
    def __init__(self):
        LoanInfo.__init__(self)

    def print_object(self, format_data=""):
        LoanInfo.print_object(self)
