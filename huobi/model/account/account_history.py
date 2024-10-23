class AccountHistory:
    """
    The account information for spot account, margin account etc.

    :member
        account_id: Account Id.
        currency: Currency name
        transact_amt: Amount change (positive value if income, negative value if outcome)
        transact-type: Amount change type
        avail_balance: Available balance
        acct_balance: Account balance
        transact_time: Transaction time (database time)
        record_id: Unique record ID in the database

    """

    def __init__(self):
        self.account_id = 0
        self.currency = ""
        self.transact_amt = ""
        self.transact_type = ""
        self.avail_balance = ""
        self.acct_balance = ""
        self.transact_time = 0
        self.record_id = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.account_id, format_data + "Account Id")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.transact_amt, format_data + "Transact Amount")
        PrintBasic.print_basic(self.transact_type, format_data + "Transact Type")
        PrintBasic.print_basic(self.avail_balance, format_data + "Avail Balance")
        PrintBasic.print_basic(self.acct_balance, format_data + "Account Balance")
        PrintBasic.print_basic(self.transact_time, format_data + "Transact Time")
        PrintBasic.print_basic(self.record_id, format_data + "Record Id")
