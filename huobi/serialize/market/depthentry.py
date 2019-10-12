class DepthEntrySerial:


    @staticmethod
    def json_parse(float_data_arr):
        entry = DepthEntry()
        entry.price = float_data_arr.get_float_at(0)
        entry.amount = float_data_arr.get_float_at(1)
        return entry


