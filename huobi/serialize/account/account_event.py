from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc
from huobi.model import *


class AccountEventSerial:


    @staticmethod
    def json_parse(json_data, account_type = None):
        account_event = AccountEvent()
        account_event.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        data = json_data.get_object("data")
        account_event.change_type = data.get_string("event")
        list_array = data.get_array("list")
        account_change_list = list()
        for item in list_array.get_items():
            account_change = AccountChange.json_parse(item)
            account_change_list.append(account_change)

        account_event.account_change_list = account_change_list
        return account_event

