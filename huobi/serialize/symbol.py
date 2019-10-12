class SymbolSerial:


    @staticmethod
    def json_parse(json_data):
        local_symbol = Symbol()
        local_symbol.base_currency = json_data.get_string("base-currency")
        local_symbol.quote_currency = json_data.get_string("quote-currency")
        local_symbol.price_precision = json_data.get_int("price-precision")
        local_symbol.amount_precision = json_data.get_int("amount-precision")
        local_symbol.symbol_partition = json_data.get_string("symbol-partition")
        local_symbol.symbol = json_data.get_string("symbol")
        local_symbol.state = json_data.get_string("state")
        local_symbol.value_precision = json_data.get_string("value-precision")
        local_symbol.min_order_amt = json_data.get_string("min-order-amt")
        local_symbol.max_order_amt = json_data.get_string("max-order-amt")
        local_symbol.min_order_value = json_data.get_string("min-order-value")
        local_symbol.leverage_ratio = json_data.get_string_or_default("leverage-ratio", 0)
        return local_symbol

    @staticmethod
    def json_parse_list(json_data):
        symbols = list()
        data_array = json_data.get_array("data")
        for item in data_array.get_items():
            local_symbol = Symbol.json_parse(item)
            symbols.append(local_symbol)
        return symbols



    @staticmethod
    def print_object_list(data_list, format_data=""):
        if len(data_list):
            for row in data_list:
                row.print_object(format_data)
                print()
