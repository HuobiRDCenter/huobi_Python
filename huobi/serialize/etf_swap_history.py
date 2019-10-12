from huobi.model import UnitPrice
from huobi.constant import *


class EtfSwapHistorySerial:



    @staticmethod
    def json_parse(json_data):
        etf_swap_history = EtfSwapHistory()
        etf_swap_history.created_timestamp = json_data.get_int("gmt_created")
        etf_swap_history.currency = json_data.get_string("currency")
        etf_swap_history.amount = json_data.get_float("amount")
        etf_swap_history.type = json_data.get_string("type")
        etf_swap_history.status = json_data.get_int("status")
        detail = json_data.get_object("detail")
        etf_swap_history.rate = detail.get_float("rate")
        etf_swap_history.fee = detail.get_float("fee")
        etf_swap_history.point_card_amount = detail.get_float("point_card_amount")
        used_currency_array = detail.get_array("used_currency_list")
        used_currency_list = list()
        for currency in used_currency_array.get_items():
            unit_price = UnitPrice.json_parse(currency)
            used_currency_list.append(unit_price)
        etf_swap_history.used_currency_list = used_currency_list
        obtain_currency_array = detail.get_array("obtain_currency_list")
        obtain_currency_list = list()
        for currency in obtain_currency_array.get_items():
            unit_price = UnitPrice.json_parse(currency)
            obtain_currency_list.append(unit_price)
        etf_swap_history.obtain_currency_list = obtain_currency_list
        return etf_swap_history

    @staticmethod
    def json_parse_list(json_data):
        etf_swap_history_list = list()
        data_array = json_data.get_array("data")
        for item in data_array.get_items():
            etf_swap_history = EtfSwapHistory.json_parse(item)
            etf_swap_history_list.append(etf_swap_history)
        return etf_swap_history_list





    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()