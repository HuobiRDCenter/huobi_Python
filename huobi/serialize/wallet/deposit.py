from huobi.utils.time_service import convert_cst_in_millisecond_to_utc
from huobi.constant import *


class DepositSerial:


    @staticmethod
    def json_parse(json_data):
        deposit = Deposit()
        deposit.id = json_data.get_int("id")
        deposit.currency = json_data.get_string("currency")
        deposit.tx_hash = json_data.get_string("tx-hash")
        deposit.amount = json_data.get_float("amount")
        deposit.address = json_data.get_string("address")
        deposit.address_tag = json_data.get_string("address-tag")
        deposit.fee = json_data.get_float("fee")
        deposit.withdraw_state = json_data.get_string("state")
        deposit.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        deposit.updated_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("updated-at"))
        return deposit

    @staticmethod
    def json_parse_list(json_data):
        deposits = list()
        data_array = json_data.get_array("data")
        for item in data_array.get_items():
            deposit = Deposit.json_parse(item)
            deposits.append(deposit)
        return deposits



    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()