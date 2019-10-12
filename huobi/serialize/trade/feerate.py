from huobi.constant import *


class FeeRateSerial:

    @staticmethod
    def json_parse(json_data):
        fee_rate = FeeRate()
        fee_rate.symbol = json_data.get_string("symbol")
        fee_rate.maker_fee = json_data.get_string("maker-fee")
        fee_rate.taker_fee = json_data.get_string("taker-fee")
        return fee_rate

    @staticmethod
    def json_parse_list(json_data):
        fee_list = list()
        data_array = json_data.get_array("data")
        for item_in_data in data_array.get_items():
            fee_rate = FeeRate.json_parse(item_in_data)
            fee_list.append(fee_rate)
        return fee_list



    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()