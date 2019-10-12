from huobi.model import Balance
from huobi.constant import *


class MarginBalanceDetailSerial:


    @staticmethod
    def json_parse(json_data):
        margin_balance_detail = MarginBalanceDetail()
        margin_balance_detail.id = json_data.get_int("id")
        margin_balance_detail.type = json_data.get_string("type")
        margin_balance_detail.symbol = json_data.get_string("symbol")
        margin_balance_detail.state = json_data.get_string("state")
        margin_balance_detail.fl_price = json_data.get_float("fl-price")
        margin_balance_detail.fl_type = json_data.get_string("fl-type")
        margin_balance_detail.risk_rate = json_data.get_float("risk-rate")
        balance_list = list()
        list_array = json_data.get_array("list")
        for item_in_list in list_array.get_items():
            balance = Balance.json_parse(item_in_list)
            balance_list.append(balance)
        margin_balance_detail.sub_account_balance_list = balance_list
        return margin_balance_detail

    @staticmethod
    def json_parse_list(json_data):
        margin_balance_detail_list = list()
        data_array = json_data.get_array("data")
        for item_in_data in data_array.get_items():
            margin_balance_detail = MarginBalanceDetail.json_parse(item_in_data)
            margin_balance_detail_list.append(margin_balance_detail)
        return margin_balance_detail_list



    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()