from huobi.model.etf import *
from huobi.utils import *


class EtfSwapListSerial:

    @staticmethod
    def json_parse(dict_data):
        etf_swap_obj = default_parse(dict_data, EtfSwapList)
        detail = dict_data.get("detail", {})
        if detail and len(detail):
            etf_swap_obj.rate = detail.get("rate", 0)
            etf_swap_obj.fee = detail.get("fee", 0)
            etf_swap_obj.point_card_amount = detail.get("point_card_amount", 0)
            etf_swap_obj.used_currency_list = default_parse_list_dict(detail.get("used_currency_list", []), UnitPrice, [])
            etf_swap_obj.obtain_currency_list = default_parse_list_dict(detail.get("obtain_currency_list", []), UnitPrice, [])
        return etf_swap_obj
