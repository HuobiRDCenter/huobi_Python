from huobi.constant import *
from huobi.model.account.balance import Balance
from huobi.utils import default_parse, default_parse_list_dict


class AccountBalance:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        list: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.id = 0
        self.type = AccountType.INVALID
        self.state = AccountState.INVALID
        self.subtype = ""
        self.list = list()

    @staticmethod
    def json_parse(data_dict):
        if data_dict and len(data_dict):
            balance_list = data_dict.get("list")
            data_dict.pop("list")
            account_balance_obj = default_parse(data_dict, AccountBalance, Balance)
            account_balance_obj.subtype = data_dict.get("subtype", data_dict.get("symbol"))
            account_balance_obj.list = default_parse_list_dict(balance_list, Balance, [])
            return account_balance_obj

        return None

    @staticmethod
    def json_parse_list(data_list):
        account_balance_list = []
        if data_list and len(data_list):
            for item in data_list:
                item_obj = AccountBalance.json_parse(item)
                if item_obj:
                    account_balance_list.append(item_obj)
        return account_balance_list

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Account ID")
        PrintBasic.print_basic(self.type, format_data + "Account Type")
        PrintBasic.print_basic(self.state, format_data + "Account State")
        PrintBasic.print_basic(self.subtype, format_data + "Subtype")

        print()
        if len(self.list):
            for row in self.list:
                row.print_object(format_data+"\t")
                print()
