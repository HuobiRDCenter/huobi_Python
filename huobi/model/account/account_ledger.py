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

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accountId, format_data + "Account ID")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.transactAmt, format_data + "Transaction Amount")
        PrintBasic.print_basic(self.transactType, format_data + "Transaction Type")
        PrintBasic.print_basic(self.transferType, format_data + "Transfer Type")
        PrintBasic.print_basic(self.transactId, format_data + "Transaction ID")
        PrintBasic.print_basic(self.transactTime, format_data + "Transaction Time")
        PrintBasic.print_basic(self.transferer, format_data + "Transferer’s Account ID")
        PrintBasic.print_basic(self.transferee, format_data + "Transferee’s Account ID")