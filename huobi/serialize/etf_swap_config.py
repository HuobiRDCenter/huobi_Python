from huobi.model.unitprice import UnitPrice
from huobi.constant import *


class EtfSwapConfigSerial:


    @staticmethod
    def json_parse(json_data):
        data = json_data.get_object("data")
        etf_swap_config = EtfSwapConfig()
        etf_swap_config.purchase_max_amount = data.get_int("purchase_max_amount")
        etf_swap_config.purchase_min_amount = data.get_int("purchase_min_amount")
        etf_swap_config.redemption_max_amount = data.get_int("redemption_max_amount")
        etf_swap_config.redemption_min_amount = data.get_int("redemption_min_amount")
        etf_swap_config.purchase_fee_rate = data.get_float("purchase_fee_rate")
        etf_swap_config.redemption_fee_rate = data.get_float("redemption_fee_rate")
        etf_swap_config.status = data.get_string("etf_status")
        unit_price_data_array = data.get_array("unit_price")
        unit_price_list = list()
        for item in unit_price_data_array.get_items():
            unit_price = UnitPrice.json_parse(item)
            unit_price_list.append(unit_price)
        etf_swap_config.unit_price_list = unit_price_list
        return etf_swap_config

