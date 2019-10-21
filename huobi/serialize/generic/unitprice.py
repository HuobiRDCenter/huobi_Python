class UnitPriceSerial:


    @staticmethod
    def json_parse(json_data):
        unit_price = UnitPrice()
        unit_price.currency = json_data.get_string("currency")
        unit_price.amount = json_data.get_float("amount")
        return unit_price

