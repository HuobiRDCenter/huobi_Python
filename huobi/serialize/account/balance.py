from huobi.constant import *


class BalanceSerial:

    @staticmethod
    def json_parse(json_data):
        balance = Balance()
        balance.balance = json_data.get_string("balance")
        balance.currency = json_data.get_string("currency")
        balance.balance_type = json_data.get_string_or_default("type", BalanceType.INVALID)
        return balance

