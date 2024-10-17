from huobi.model.algo import *
from huobi.utils.input_checker import *


class AlgoClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """
        self.__kwargs = kwargs

    # 策略委托下单
    def create_order(self, account_id: 'int', symbol: 'str', order_side: 'OrderSide', order_type: 'OrderType',
                     client_order_id: 'str', stop_price: 'str', order_price: 'str' = None, order_size: 'str' = None,
                     order_value: 'str' = None, time_in_force: 'str' = None, trailing_rate: 'str' = None) -> int:
        """
        Make an algo order in huobi.
        :param account_id: Account id. (mandatory)
        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_side: the Order side, possible values: buy,sell. (mandatory)
        :param order_type: The order type, possible values: limit, market. (mandatory)
        :param stop_price: The stop price. (mandatory)
        :param order_price: The limit price of limit order, only needed for limit order. (mandatory for buy-limit, sell-limit, buy-limit-maker and sell-limit-maker)
        :param order_size: The amount of market order only
        :param order_value: for market buy order only
        :param stop_price: Price for auto sell to get the max benefit
        :param time_in_force: gtc(invalid for orderType=market), boc(invalid orderType=market),ioc,fok(invalid for orderType=market)
        :param trailing_rate: for trailing orders only
        :param client_order_id: unique Id which is user defined and must be unique in recent 24 hours
        """

        params = self.create_order_param_check(symbol, account_id, order_side, order_type, stop_price, order_price,
                                               order_size, order_value, time_in_force, trailing_rate, client_order_id)
        from huobi.service.algo.post_create_order import PostCreateOrderService
        return PostCreateOrderService(params).request(**self.__kwargs)

    # 策略委托（触发前）撤单
    def cancel_orders(self, client_order_ids) -> CancelOrderResult:
        check_should_not_none(client_order_ids, "clientOrderIds")

        params = {
            "clientOrderIds": client_order_ids
        }
        from huobi.service.algo.post_cancel_orders import PostCancelOrderService
        return PostCancelOrderService(params).request(**self.__kwargs)

    # 查询未触发OPEN策略委托
    def get_open_orders(self, account_id: 'str' = None, symbol: 'str' = None, order_side: 'OrderSide' = None,
                        order_type: 'AlgoOrderType' = None, sort: 'SortDesc' = None, limit: 'int' = 100,
                        from_id: 'int' = None):

        params = {
            "accountId": account_id,
            "symbol": symbol,
            "orderSide": order_side,
            "orderType": order_type,
            "sort": sort,
            "limit": limit,
            "fromId": from_id
        }
        from huobi.service.algo.get_open_orders import GetOpenOrdersService
        return GetOpenOrdersService(params).request(**self.__kwargs)

    # 查询策略委托历史
    def get_order_history(self, symbol: 'str', order_status: 'AlgoOrderStatus', account_id: 'str' = None,
                          order_side: 'OrderSide' = None, order_type: 'AlgoOrderType' = None, start_time: 'int' = None,
                          end_time: 'int' = None, sort: 'SortDesc' = SortDesc.DESC, limit: 'int' = 100,
                          from_id: 'int' = None):

        params = {
            "symbol": symbol,
            "accountId": account_id,
            "orderSide": order_side,
            "orderType": order_type,
            "orderStatus": order_status,
            "startTime": start_time,
            "endTime": end_time,
            "sort": sort,
            "limit": limit,
            "fromId": from_id
        }
        from huobi.service.algo.get_order_history import GetOrderHistoryService
        return GetOrderHistoryService(params).request(**self.__kwargs)

    # 查询特定策略委托
    def get_order(self, client_order_id: 'str'):
        params = {
            "clientOrderId": client_order_id
        }
        from huobi.service.algo.get_order_by_cid import GetOrderByClientOrderIdService
        return GetOrderByClientOrderIdService(params).request(**self.__kwargs)

    # 自动撤销订单
    def post_cancel_all_after(self, timeout: 'int'):
        check_should_not_none(timeout, "timeout")
        params = {
            "timeout": timeout
        }
        from huobi.service.algo.post_cancel_all_after import PostCancelAllAfterService
        return PostCancelAllAfterService(params).request(**self.__kwargs)

    def create_order_param_check(self, symbol, account_id, order_side, order_type, stop_price, order_price,
                                 order_size, order_value, time_in_force, trailing_rate, client_order_id):
        check_symbol(symbol)
        check_should_not_none(account_id, "accountId")
        check_should_not_none(order_type, "orderType")
        check_should_not_none(order_side, "orderSide")

        if order_type == OrderType.SELL_LIMIT \
                or order_type == OrderType.BUY_LIMIT \
                or order_type == OrderType.BUY_LIMIT_MAKER \
                or order_type == OrderType.SELL_LIMIT_MAKER:
            check_should_not_none(order_price, "orderPrice")

        if time_in_force is not None:
            check_time_in_force(time_in_force, order_type)

        if order_type in [OrderType.SELL_MARKET, OrderType.BUY_MARKET]:
            order_price = None

        params = {
            "accountId": account_id,
            "symbol": symbol,
            "orderPrice": order_price,
            "orderSide": order_side,
            "orderSize": order_size,
            "orderValue": order_value,
            "timeInForce": time_in_force,
            "orderType": order_type,
            "clientOrderId": client_order_id,
            "stopPrice": stop_price,
            "trailingRate": trailing_rate
        }

        return params
