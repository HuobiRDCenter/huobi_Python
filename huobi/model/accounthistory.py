
from huobi.model.balance import Balance
from huobi.model.constant import *


class AccountHistory:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        balances: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.account_id = 0
        self.currency = ""
        self.transact_amt = ""
        self.transact_type = ""
        self.avail_balance = ""
        self.acct_balance = ""
        self.transact_time = 0
        self.record_id  = ""

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.account_id, format_data + "Account Id")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.transact_amt, format_data + "Transact Amount")
        PrintBasic.print_basic(self.transact_type, format_data + "Transact Type")
        PrintBasic.print_basic(self.avail_balance, format_data + "Avail Balance")
        PrintBasic.print_basic(self.acct_balance, format_data + "Account Balance")
        PrintBasic.print_basic(self.transact_time, format_data + "Transact Time")
        PrintBasic.print_basic(self.record_id, format_data + "Record Id")


