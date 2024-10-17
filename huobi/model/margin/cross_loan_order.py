from huobi.constant import *


class CrossLoanOrder:

    def __init__(self):
        self.currency = ""
        self.id = 0
        self.user_id = 0
        self.account_id = 0
        self.loan_amount = 0.0
        self.loan_balance = 0.0
        self.interest_amount = 0.0
        self.interest_balance = 0.0
        self.filled_points = 0.0
        self.filled_ht = 0.0
        self.created_at = 0
        self.accrued_at = 0
        self.state = LoanOrderState.INVALID

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.id, format_data + "Id")
        PrintBasic.print_basic(self.user_id, format_data + "User Id")
        PrintBasic.print_basic(self.account_id, format_data + "Account Id")
        PrintBasic.print_basic(self.loan_amount, format_data + "Loan Amount")
        PrintBasic.print_basic(self.loan_balance, format_data + "Loan Balance")
        PrintBasic.print_basic(self.interest_amount, format_data + "Interest Amount")
        PrintBasic.print_basic(self.interest_balance, format_data + "Interest Balance")
        PrintBasic.print_basic(self.filled_points, format_data + "Filled Points")
        PrintBasic.print_basic(self.filled_ht, format_data + "Filled Ht")
        PrintBasic.print_basic(self.created_at, format_data + "Created At")
        PrintBasic.print_basic(self.accrued_at, format_data + "Accrued At")
        PrintBasic.print_basic(self.state, format_data + "State")
