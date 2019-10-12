from huobi.utils.timeservice import convert_cst_in_second_to_utc


class CandlestickSerial:

    @staticmethod
    def json_parse(json_data):
        data_obj = Candlestick()
        if json_data.contain_key("id"):
            data_obj.id = json_data.get_int("id")
            data_obj.timestamp = convert_cst_in_second_to_utc(json_data.get_int("id"))
        data_obj.open = json_data.get_float("open")
        data_obj.close = json_data.get_float("close")
        data_obj.low = json_data.get_float("low")
        data_obj.high = json_data.get_float("high")
        data_obj.amount = json_data.get_float("amount")
        data_obj.count = json_data.get_int_or_default("count", 0)
        data_obj.volume = json_data.get_float("vol")
        return data_obj

