from huobi.model.crossmarginloaninfo import CrossMarginLoanInfo


class TransactFeeRate:
    """
    The transact fee rate.

    :member
        symbol: symbol like "btcusdt"
        currencies: transact fee rate
    """

    def __init__(self):
        self.symbol = ""
        self.makerFeeRate = ""
        self.takerFeeRate = ""
        self.actualMakerRate = ""
        self.actualTakerRate = ""

    @staticmethod
    def json_parse(json_data):
        fee_rate_obj = TransactFeeRate()
        fee_rate_obj.symbol = json_data.get_string_or_default("symbol", "")
        fee_rate_obj.makerFeeRate = json_data.get_string_or_default("makerFeeRate", "")
        fee_rate_obj.takerFeeRate = json_data.get_string_or_default("takerFeeRate", "")
        fee_rate_obj.actualMakerRate = json_data.get_string_or_default("actualMakerRate", "")
        fee_rate_obj.actualTakerRate = json_data.get_string_or_default("actualTakerRate", "")

        return fee_rate_obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.makerFeeRate, format_data + "makerFeeRate")
        PrintBasic.print_basic(self.takerFeeRate, format_data + "takerFeeRate")
        PrintBasic.print_basic(self.actualMakerRate, format_data + "actualMakerRate")
        PrintBasic.print_basic(self.actualTakerRate, format_data + "actualTakerRate")
