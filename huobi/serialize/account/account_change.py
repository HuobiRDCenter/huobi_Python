from huobi.constant import *


class AccountChangeSerial:


    @staticmethod
    def json_parse(json_data, account_type = None):
        account_change = AccountChange()
        account_change.account_type = account_type
        account_change.currency = json_data.get_string("currency")
        account_change.balance = json_data.get_float("balance")
        account_change.balance_type = json_data.get_string("type")
        return account_change

