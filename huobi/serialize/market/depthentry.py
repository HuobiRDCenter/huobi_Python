from huobi.model.market import *

class DepthEntrySerial:

    @staticmethod
    def json_parse(float_data_arr):
        entry = DepthEntry()
        entry.price = float_data_arr[0]
        entry.amount = float_data_arr[1]
        return entry


