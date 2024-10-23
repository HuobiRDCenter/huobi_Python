from huobi.model.margin.loan_ino import LoanInfo
from huobi.utils import default_parse_list_dict


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
        retList = []
        for idx, item in enumerate(json_data):
            margin_loan_obj = MarginLoanInfo()
            margin_loan_obj.symbol = item.get("symbol", "")

            currencies_json = item.get("currencies")
            result_list = default_parse_list_dict(currencies_json, LoanInfo, [])

            margin_loan_obj.currencies = result_list

            retList.append(margin_loan_obj)

        return retList

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        if self.currencies and len(self.currencies):
            for currency_item in self.currencies:
                currency_item.print_object("\t")
                print()
