from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.constant import *


class LoanSerial:

    @staticmethod
    def json_parse(json_data, account_type):
        loan = Loan()
        loan.loan_balance = json_data.get_float("loan-balance")
        loan.interest_balance = json_data.get_float("interest-balance")
        loan.interest_rate = json_data.get_float("interest-rate")
        loan.loan_amount = json_data.get_float("loan-amount")
        loan.interest_amount = json_data.get_float("interest-amount")
        loan.symbol = json_data.get_string("symbol")
        loan.currency = json_data.get_string("currency")
        loan.id = json_data.get_int("id")
        loan.state = json_data.get_string("state")
        loan.account_type = account_type
        loan.user_id = json_data.get_int("user-id")
        loan.accrued_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("accrued-at"))
        loan.created_timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("created-at"))
        return loan

    @staticmethod
    def json_parse_list(json_data, account_type_map):
        loan_list = list()
        data_array = json_data.get_array("data")
        for json_data in data_array.get_json_datas():
            account_id = json_data.get_int("account-id")
            loan = Loan.json_parse(json_data, account_type_map[account_id])
            loan_list.append(loan)
        return loan_list




    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()