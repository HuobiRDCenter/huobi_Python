from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc


class TradeSerial:

    @staticmethod
    def json_parse(json_data):
        trade = Trade()
        trade.amount = json_data.get_float("amount")
        trade.price = json_data.get_float("price")
        trade.trade_id = json_data.get_string("id")
        trade.direction = json_data.get_string("direction")
        trade.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        return trade

