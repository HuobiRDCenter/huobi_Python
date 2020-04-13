

class AccountLedger:
    """
    The account ledger information.

    :member
        accountId: Account ID.
        currency: Cryptocurrency.
        transactAmt: Transaction amount (income positive, expenditure negative).
        transactType: Transaction type.
        transferType: Transfer type (only valid for transactType=transfer).
        transactId: Transaction ID.
        transactTime: Transaction time.
        transferer: Transferer’s account ID.
        transferee: Transferee’s account ID.
    """

    def __init__(self):
        self.accountId = 0
        self.currency = ""
        self.transactAmt = 0.0
        self.transactType = ""
        self.transferType = ""
        self.transactId = 0
        self.transactTime = 0
        self.transferer = 0
        self.transferee = 0

    @staticmethod
    def json_parse(json_data):
        account_ledger = AccountLedger()
        account_ledger.accountId = json_data.get_int("accountId")
        account_ledger.currency = json_data.get_string("currency")
        account_ledger.transactAmt = json_data.get_float("transactAmt")
        account_ledger.transactType = json_data.get_string("transactType")
        account_ledger.transferType = json_data.get_string_or_default("transferType", "")
        account_ledger.transactId = json_data.get_int("transactId")
        account_ledger.transactTime = json_data.get_int("transactTime")
        account_ledger.transferer = json_data.get_int_or_default("transferer", 0)
        account_ledger.transferee = json_data.get_int_or_default("transferee", 0)
        return account_ledger

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.accountId, format_data + "Account ID")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.transactAmt, format_data + "Transaction Amount")
        PrintBasic.print_basic(self.transactType, format_data + "Transaction Type")
        PrintBasic.print_basic(self.transferType, format_data + "Transfer Type")
        PrintBasic.print_basic(self.transactId, format_data + "Transaction ID")
        PrintBasic.print_basic(self.transactTime, format_data + "Transaction Time")
        PrintBasic.print_basic(self.transferer, format_data + "Transferer’s Account ID")
        PrintBasic.print_basic(self.transferee, format_data + "Transferee’s Account ID")
