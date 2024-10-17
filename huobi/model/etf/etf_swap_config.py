from huobi.constant import *


class EtfSwapConfig:
    """
    The basic information of ETF creation and redemption, as well as ETF constituents, including max
    amount of creation, min amount of creation, max amount of redemption, min amount of redemption,
    creation fee rate, redemption fee rate, eft create/redeem status.

    :member
        purchase_max_amount: The max creation amounts per request.
        purchase_min_amount: The minimum creation amounts per request.
        redemption_max_amount: The max redemption amounts per request.
        redemption_min_amount: The minimum redemption amounts per request.
        purchase_fee_rate: The creation fee rate.
        redemption_fee_rate: The redemption fee rate.
        status: The status of the ETF.
        unit_price_list: ETF constitution in format of amount and currency.

    """
    def __init__(self):
        self.etf_name = ""
        self.etf_status = EtfStatus.INVALID
        self.purchase_fee_rate = 0.0
        self.purchase_max_amount = 0
        self.purchase_min_amount = 0
        self.redemption_fee_rate = 0.0
        self.redemption_max_amount = 0
        self.redemption_min_amount = 0
        self.unit_price = list()

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.etf_name, format_data + "ETF Name")
        PrintBasic.print_basic(self.etf_status, format_data + "ETF Status")

        PrintBasic.print_basic(self.purchase_fee_rate, format_data + "Purchase Fee Rate")
        PrintBasic.print_basic(self.purchase_max_amount, format_data + "Purchase Max Amount")
        PrintBasic.print_basic(self.purchase_min_amount, format_data + "Purchase Min Amount")

        PrintBasic.print_basic(self.redemption_fee_rate, format_data + "Redemption Fee Rate")
        PrintBasic.print_basic(self.redemption_max_amount, format_data + "Redemption Max Amount")
        PrintBasic.print_basic(self.redemption_min_amount, format_data + "Redemption Min Amount")
        print()
        if len(self.unit_price):
            for row in self.unit_price:
                row.print_object(format_data)
                print()
