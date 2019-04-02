from huobi.model.constant import *


class MarginBalanceDetail:
    def __init__(self):
        self.id = 0
        self.symbol = 0
        self.state = AccountState.INVALID
        self.type = AccountType.INVALID
        self.risk_rate = 0.0
        self.fl_price = 0.0
        self.fl_type = ""
        self.sub_account_balance_list = list()

