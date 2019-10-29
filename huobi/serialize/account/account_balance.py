

from huobi.model.account import *
from huobi.utils import *


class AccountBalanceSerial:
    @staticmethod
    def json_parse(json_data_account_balance):
        return default_parse(json_data_account_balance, AccountBalance, Balance)


