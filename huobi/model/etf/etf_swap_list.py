from huobi.constant import *
from huobi.model.etf.unitprice import UnitPrice
from huobi.utils import default_parse_list_dict


class EtfSwapList:
    """
    The past creation and redemption.

    :member
        id: the operation Id.
        gmt_created: The UNIX formatted timestamp in UTC of the operation.
        currency: The ETF name.
        amount: Creation or redemption amount.
        type: The swap type. Creation or redemption.
        status: The operation result
        rate: The fee rate.
        fee: The actual fee amount

        point_card_amount: Discount from point card.
        used_currency_list: For creation this is the list and amount of underlying assets used for ETF creation.
            For redemption this is the amount of ETF used for redemption. The content is UnitPrice class.
        obtain_currency_list: For creation this is the amount for ETF created.
            For redemption this is the list and amount of underlying assets obtained. The content is UnitPrice class
    """

    def __init__(self):
        self.id = 0
        self.gmt_created = 0
        self.currency = ""
        self.amount = 0.0
        self.type = EtfSwapType.INVALID
        self.status = 0
        self.rate = 0.0
        self.fee = 0.0
        self.point_card_amount = 0.0
        self.used_currency_list = list()
        self.obtain_currency_list = list()

    @staticmethod
    def json_parse(dict_data):
        if dict_data and len(dict_data):
            detail = dict_data.get("detail", {})
            dict_data.pop("detail")
            etf_swap_obj = default_parse_list_dict(dict_data, EtfSwapList)
            if detail and len(detail):
                etf_swap_obj.rate = detail.get("rate", 0)
                etf_swap_obj.fee = detail.get("fee", 0)
                etf_swap_obj.point_card_amount = detail.get("point_card_amount", 0)
                etf_swap_obj.used_currency_list = default_parse_list_dict(detail.get("used_currency_list"), UnitPrice, [])
                etf_swap_obj.obtain_currency_list = default_parse_list_dict(detail.get("obtain_currency_list"), UnitPrice, [])
            return etf_swap_obj

        return None

    @staticmethod
    def json_parse_list(dict_data):
        ret_list = list()
        for item in dict_data:
            item_obj = EtfSwapList.json_parse(item)
            if item_obj is not None:
                ret_list.append(item_obj)

        return ret_list


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.id, format_data + "Operater Id")
        PrintBasic.print_basic(self.gmt_created, format_data + "GMT Create Time")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.type, format_data + "Type")
        PrintBasic.print_basic(self.amount, format_data + "Amount")
        PrintBasic.print_basic(self.rate, format_data + "Rate")
        PrintBasic.print_basic(self.fee, format_data + "Fee")
        PrintBasic.print_basic(self.status, format_data + "Status")
        PrintBasic.print_basic(self.point_card_amount, format_data + "Point Card Amount")

        if len(self.used_currency_list):
            PrintBasic.print_basic("used_currency_list as below:")
            for row in self.used_currency_list:
                row.print_object(format_data + "\t")

        if len(self.obtain_currency_list):
            PrintBasic.print_basic("obtain_currency_list as below:")
            for row in self.obtain_currency_list:
                row.print_object(format_data + "\t")

