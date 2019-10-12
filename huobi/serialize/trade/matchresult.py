from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.constant import *


class MatchResultSerial:
    @staticmethod
    def json_parse(json_data):
        match_result = MatchResult()
        match_result.id = json_data.get_int("id")
        match_result.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        match_result.filled_amount = json_data.get_float("filled-amount")
        match_result.filled_fees = json_data.get_float("filled-fees")
        match_result.match_id = json_data.get_int("match-id")
        match_result.order_id = json_data.get_int("order-id")
        match_result.price = json_data.get_float("price")
        match_result.source = json_data.get_string("source")
        match_result.symbol = json_data.get_string("symbol")
        match_result.order_type = json_data.get_string("type")
        match_result.role = json_data.get_string("role")
        match_result.filled_points = json_data.get_string("filled-points")
        match_result.fee_deduct_currency = json_data.get_string("fee-deduct-currency")
        return match_result

    @staticmethod
    def json_parse_list(json_data):
        match_result_list = list()
        data_array = json_data.get_array("data")
        for item in data_array.get_json_datas():
            match_result = MatchResult.json_parse(item)
            match_result_list.append(match_result)
        return match_result_list



    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()