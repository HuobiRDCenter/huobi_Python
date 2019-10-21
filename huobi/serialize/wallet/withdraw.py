from huobi.utils.time_service import convert_cst_in_millisecond_to_utc
from huobi.constant import *


class WithdrawSerial:


    @staticmethod
    def json_parse(json_data):
        withdraw = Withdraw()
        withdraw.id = json_data.get_int("id")
        withdraw.currency = json_data.get_string("currency")
        withdraw.tx_hash = json_data.get_string("tx-hash")
        withdraw.amount = json_data.get_float("amount")
        withdraw.address = json_data.get_string("address")
        withdraw.address_tag = json_data.get_string("address-tag")
        withdraw.fee = json_data.get_float("fee")
        withdraw.withdraw_state = json_data.get_string("state")
        withdraw.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        withdraw.updated_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("updated-at"))
        return withdraw

    @staticmethod
    def json_parse_list(json_wrapper):
        withdraws = list()
        data_array = json_wrapper.get_array("data")
        for item in data_array.get_items():
            withdraw = Withdraw.json_parse(item)
            withdraws.append(withdraw)
        return withdraws






    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()