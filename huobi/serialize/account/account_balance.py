

from huobi.constant import *
from huobi.model.account import *


class AccountBalanceSerial:
    """
    The account information for spot account, margin account etc.

    :member
        id: The unique account id.
        account_type: The type of this account, possible value: spot, margin, otc, point.
        account_state: The account state, possible value: working, lock.
        balances: The balance list of the specified currency. The content is Balance class

    """

    @staticmethod
    def json_parse(json_data, account_type = None):
        account = AccountBalance()
        account.id = json_data.get_string("id")
        account.account_type = account_type if account_type else json_data.get_string("type")
        account.account_state = json_data.get_string("state")

        if json_data.contain_key("list"):
            list_array = json_data.get_array("list")
            balance_list = list()
            for item in list_array.get_items():
                balance = BalanceSerial.json_parse(item)
                balance_list.append(balance)

            account.balances = balance_list

        return account




