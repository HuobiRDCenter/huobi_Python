from huobi.model.crossmarginloaninfo import CrossMarginLoanInfo


class MarginLoanInfo:
    """
    The margin loan info.

    :member
        symbol: symbol like "btcusdt"
        currencies: loan info for currency in symbol
    """

    def __init__(self):
        self.symbol = ""
        self.currencies = list()

    @staticmethod
    def json_parse(json_data):
        margin_loan_obj = MarginLoanInfo()
        margin_loan_obj.symbol = json_data.get_string_or_default("symbol", "")


        currencies_array_data = json_data.get_array("currencies")
        result_list = list()
        for item_in_data in currencies_array_data.get_items():
            loan_base = CrossMarginLoanInfo.json_parse(item_in_data)
            result_list.append(loan_base)

        margin_loan_obj.currencies = result_list

        return margin_loan_obj

    def print_object(self, format_data=""):
        from huobi.base.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        if self.currencies and len(self.currencies):
            for currency_item in self.currencies:
                currency_item.print_object()
                print()