from huobi.model.constant import *


class AccountsUpdate:
    """
    The detail order information.

    :member
        account_type: The account type which created this order.
        currency: The currency for this account.
        accountId: account id
        balance: balance of account.
        available: available balance.
        changeType: balance change event. detail to see AccountChangeType
        changeTime: UNIX timestamp for change time
    """

    def __init__(self):
        self.currency = ""
        self.accountId = 0
        self.balance = ""
        self.available = ""
        self.changeType = AccountChangeType.INVALID
        self.accountType = BalanceType.INVALID
        self.changeTime = 0


    @staticmethod
    def json_parse(json_data):
        upd = AccountsUpdate()
        if json_data and json_data.contain_key("accountId"):
            upd.currency = json_data.get_string("currency")
            upd.accountId = json_data.get_int_or_default("accountId", 0)
            upd.balance = json_data.get_string_or_default("balance", "0")
            upd.available = json_data.get_string_or_default("available", "0")
            upd.changeType = json_data.get_string_or_default("changeType", "")
            upd.accountType = json_data.get_string_or_default("accountType", "")
            upd.changeTime = json_data.get_int_or_default("changeTime", 0)
        return upd

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.accountId, format_data + "Account Id")
        PrintBasic.print_basic(self.balance, format_data + "Balance")
        PrintBasic.print_basic(self.available, format_data + "Available")
        PrintBasic.print_basic(self.changeType, format_data + "Change Type")
        PrintBasic.print_basic(self.accountType, format_data + "Account Type")
        PrintBasic.print_basic(self.changeTime, format_data + "Change Time")



