from huobi.model import Balance
from huobi.constant import *


class CompleteSubAccountSerial:


    @staticmethod
    def json_parse(json_data):
        complete_sub_account = CompleteSubAccountInfo()
        complete_sub_account.id = json_data.get_int("id")
        complete_sub_account.account_type = json_data.get_string("type")
        balances = list()
        data_array_in = json_data.get_array("list")
        for item_in in data_array_in.get_items():
            balance = Balance.json_parse(item_in)
            balances.append(balance)
        complete_sub_account.balances = balances

        return complete_sub_account

    @staticmethod
    def json_parse_list(json_wrapper):
        complete_sub_account_list = list()
        data_array = json_wrapper.get_array("data")
        for item in data_array.get_items():
            complete_sub_account = CompleteSubAccountInfo.json_parse(item)
            complete_sub_account_list.append(complete_sub_account)
        return complete_sub_account_list



    @staticmethod
    def print_object_list(data_list, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()