
class LoanInfo:
    """
    The margin rate define.

    :member
        currency: The currency name.
        interest_rate: all interest rate
        min_loan_amt: min loan amount.
        max_loan_amt: max loan amount.
        loanable_amt: loanable amount.
        actual_rate: rate after deduction.
    """

    def __init__(self):
        self.currency = ""
        self.interest_rate = ""
        self.min_loan_amt = ""
        self.max_loan_amt = ""
        self.loanable_amt = ""
        self.actual_rate = ""

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.interest_rate, format_data + "Interest Rate")
        PrintBasic.print_basic(self.min_loan_amt, format_data + "Min Loan Amount")
        PrintBasic.print_basic(self.max_loan_amt, format_data + "Max Loan Amount")
        PrintBasic.print_basic(self.loanable_amt, format_data + "Loanable Amount")
        PrintBasic.print_basic(self.actual_rate, format_data + "Actual Rate")
