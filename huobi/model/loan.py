from huobi.model.constant import *


class Loan:
    """
    The margin order information.

    :member
        id: The order id.
        user_id: The user id.
        account_type: The account type which created the loan order.
        symbol: The symbol, like "btcusdt".
        currency: The currency name.
        loan_amount: The amount of the origin loan.
        loan_balance: The amount of the loan left.
        interest_rate: The loan interest rate.
        interest_amount: The accumulated loan interest.
        interest_balance: The amount of loan interest left.
        state: The loan stats, possible values: created, accrual, cleared, invalid.
        created_timestamp: The UNIX formatted timestamp in UTC when the order was created.
        accrued_timestamp: The UNIX formatted timestamp in UTC when the last accrue happened.
    """

    def __init__(self):
        self.id = 0
        self.user_id = 0
        self.account_type = AccountType.INVALID
        self.symbol = ""
        self.currency = ""
        self.loan_amount = 0.0
        self.loan_balance = 0.0
        self.interest_rate = 0.0
        self.interest_amount = 0.0
        self.interest_balance = 0.0
        self.state = LoanOrderState.INVALID
        self.created_timestamp = 0
        self.accrued_timestamp = 0
