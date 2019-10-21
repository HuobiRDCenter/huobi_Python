from huobi.model.market import *


class TradeDetailSerial:

    @staticmethod
    def json_parse(dict_data):
        """
        self rewrite parse function to fill trade_id by tradeId, trade_id can auto filled by trade-id
        :param dict_data:
        :return:
        """
        trade_obj = TradeDetail()
        trade_obj.ts = dict_data.get("ts", 0)
        trade_obj.trade_id = dict_data.get("tradeId", 0)
        trade_obj.amount = dict_data.get("amount", 0)
        trade_obj.price = dict_data.get("price", 0)
        trade_obj.direction = dict_data.get("direction", 0)

        return trade_obj
