from huobi.constant import *


class AccountUpdate:
    """
    The account change information received by subscription of account.

    :member
        currency: The currency of the change.
        accountId: The account id.
        balance: Account balance (only exists when account balance changed)
        available:	Available balance (only exists when available balance changed)
        changeType:	Change type see AccountChangeType, valid value: order-place,order-match,order-refund,order-cancel,order-fee-refund,margin-transfer,margin-loan,margin-interest,margin-repay,other,
        accountType: Account type see AccountBalanceUpdateType, valid value: trade, frozen, loan, interest
        changeTime:	Change time, unix time in millisecond
    """

    def __init__(self):
        self.currency = ""
        self.accountId = 0
        self.balance = ""
        self.available = ""
        self.changeType = AccountChangeType.INVALID
        self.accountType = AccountBalanceUpdateType.INVALID
        self.changeTime = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.accountId, format_data + "Account ID")
        PrintBasic.print_basic(self.balance, format_data + "Balance")
        PrintBasic.print_basic(self.available, format_data + "Available")
        PrintBasic.print_basic(self.changeType, format_data + "Account Change Type")
        PrintBasic.print_basic(self.accountType, format_data + "Account Balance Change Type")
        PrintBasic.print_basic(self.changeTime, format_data + "Account Timestamp")
