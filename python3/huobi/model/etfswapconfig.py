from huobi.model.constant import *


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
        self.purchase_max_amount = 0
        self.purchase_min_amount = 0
        self.redemption_max_amount = 0
        self.redemption_min_amount = 0
        self.purchase_fee_rate = 0.0
        self.redemption_fee_rate = 0.0
        self.status = EtfStatus.INVALID
        self.unit_price_list = list()
