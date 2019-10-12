from huobi.utils.timeservice import convert_cst_in_millisecond_to_utc


class BestQuoteSerial:


    @staticmethod
    def json_parse(json_data):
        best_quote = BestQuote()
        best_quote.timestamp = convert_cst_in_millisecond_to_utc(json_data.get_int("ts"))
        tick = json_data.get_object("tick")
        ask_array = tick.get_array("ask")
        best_quote.ask_price = ask_array.get_float_at(0)
        best_quote.ask_amount = ask_array.get_float_at(1)
        bid_array = tick.get_array("bid")
        best_quote.bid_price = bid_array.get_float_at(0)
        best_quote.bid_amount = bid_array.get_float_at(1)
        return best_quote

