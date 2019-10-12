from huobi.model.account import *
from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc



class AccountBalanceReqSerial:
    @staticmethod
    def json_parse(json_data):
        account_balance = AccountBalanceReq()
        account_balance.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        account_balance.client_req_id = json_data.get_string("cid")
        account_balance.topic = json_data.get_string("topic")
        subaccount_list = json_data.get_array("data")

        account_list = list()
        for subaccount in subaccount_list.get_items():
            account = Account.json_parse(subaccount)
            account_list.append(account)
        account_balance.account_list = account_list
        return account_balance

