from huobi.constant import *
from huobi.model.account.account_point_group import AccountPointGroup
from huobi.utils import default_parse, default_parse_list_dict


class AccountPointResult:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        list: The balance list of the specified currency. The content is Balance class

    """

    def __init__(self):
        self.accountId = ""
        self.accountStatus = AccountPointState.INVALID
        self.groupIds = list()
        self.acctBalance = ""

    @staticmethod
    def json_parse(data_dict):
        if data_dict and len(data_dict):
            group_ids = data_dict.get("groupIds")
            data_dict.pop("groupIds")
            account_point_obj = default_parse(data_dict, AccountPointResult, AccountPointGroup)
            account_point_obj.subtype = data_dict.get("subtype", data_dict.get("symbol"))
            account_point_obj.list = default_parse_list_dict(group_ids, AccountPointGroup, [])
            return account_point_obj

        return None

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.accountId, format_data + "Account ID")
        PrintBasic.print_basic(self.accountStatus, format_data + "Account Status")
        PrintBasic.print_basic(self.acctBalance, format_data + "Account Balance")

        print()
        if len(self.groupIds):
            for row in self.groupIds:
                row.print_object(format_data + "\t")
                print()
