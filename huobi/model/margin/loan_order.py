from huobi.constant import *


class LoanOrder:
    """
    The margin order information.

    :member
        id: The order id.
        user_id: The user id.
        account_type: The account type which created the loan order.
        currency: The currency name.
        loan_amount: The amount of the origin loan.
        loan_balance: The amount of the loan left.
        interest_rate: The loan interest rate.
        interest_amount: The accumulated loan interest.
        interest_balance: The amount of loan interest left.
        state: The loan stats, possible values: created, accrual, cleared, invalid.
        created_at: The UNIX formatted timestamp in UTC when the order was created.
        accrued_at: The UNIX formatted timestamp in UTC when the last accrue happened.
    """

    def __init__(self):
        self.currency = ""
        self.deduct_rate = 0
        self.paid_point = 0.0
        self.deduct_currency = ""
        self.user_id = 0
        self.created_at = 0
        self.account_id = 0
        self.paid_coin = 0.0
        self.loan_amount = 0.0
        self.interest_amount = 0.0
        self.deduct_amount = 0.0
        self.loan_balance = 0.0
        self.interest_balance = 0.0
        self.updated_at = 0
        self.accrued_at = 0
        self.interest_rate = 0.0
        self.id = 0
        self.state = LoanOrderState.INVALID

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.deduct_rate, format_data + "Deduct Rate")
        PrintBasic.print_basic(self.paid_point, format_data + "Paid Point")
        PrintBasic.print_basic(self.deduct_currency, format_data + "Deduct Currency")
        PrintBasic.print_basic(self.user_id, format_data + "User Id")
        PrintBasic.print_basic(self.created_at, format_data + "Create Time")
        PrintBasic.print_basic(self.account_id, format_data + "Account Id")
        PrintBasic.print_basic(self.paid_coin, format_data + "Paid Coin")
        PrintBasic.print_basic(self.loan_amount, format_data + "Load Amount")
        PrintBasic.print_basic(self.interest_amount, format_data + "Interest Amount")
        PrintBasic.print_basic(self.deduct_amount, format_data + "Deduct Amount")
        PrintBasic.print_basic(self.loan_balance, format_data + "Loan Balance")
        PrintBasic.print_basic(self.interest_balance, format_data + "Interest Balance")
        PrintBasic.print_basic(self.updated_at, format_data + "Update Time")
        PrintBasic.print_basic(self.accrued_at, format_data + "Accrued Time")
        PrintBasic.print_basic(self.interest_rate, format_data + "Interest Rate")
        PrintBasic.print_basic(self.id, format_data + "ID")
        PrintBasic.print_basic(self.state, format_data + "Loan Order State")
