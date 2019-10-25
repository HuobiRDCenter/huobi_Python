from huobi.constant import *
from huobi.constant.system import RestApiDefine
from huobi.model.trade import *
from huobi.service.trade import *
from huobi.utils.input_checker import *


class TradeClient(object):
    __server_url = RestApiDefine.Url
    __kwargs = {}

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            server_url: The URL name like "https://api.huobi.pro".
        """
        self.__kwargs = kwargs

    def get_feerate(self, symbols: 'str') -> list:
        """
        Get the candlestick/kline for the specified symbol. The data number is 150 as default.

        :param symbol: The symbol, like "btcusdt". To query hb10, put "hb10" at here. (mandatory)
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc. (mandatory)
        :param size: The start time of of requested candlestick/kline data. (optional)
        :param start_time: The start time of of requested candlestick/kline data. (optional)
        :param end_time: The end time of of requested candlestick/kline data. (optional)
        :return: The list of candlestick/kline data.
        """
        check_symbol(symbols)

        params = {
            "symbols": symbols
        }

        return GetFeeRateService(params).request(**self.__kwargs)

    def sub_order_update(self, symbols: 'str', callback, error_handler=None):
        """
        Subscribe order changing event. If a order is created, canceled etc, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(order_update_event: 'OrderUpdateEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return:  No return
        """
        symbol_list = symbols.split(",")
        check_symbol_list(symbol_list)
        check_should_not_none(callback, "callback")

        params = {
            "symbol_list" : symbol_list,
        }

        SubOrderUpdateService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_order_list(self, symbol: 'str', account_id: int, callback, order_states:'str',
                       order_types:'str'=None, start_date:'str'=None, end_date:'str'=None, from_id=None,
                       direct=None, size=None, client_req_id:'str'=None, error_handler=None):
        """
        request order list.

        :param symbol: The symbol, like "btcusdt".
        :param order_states: order status, can be one state or many state sepearted by comma, such as "submitted,partial-filled,partial-canceled,filled,canceled,created"
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(candlestick_event: 'CandlestickEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return: No return
        """
        check_should_not_none(symbol, "symbol")
        check_should_not_none(order_states, "states")
        check_should_not_none(account_id, "account-d")
        check_should_not_none(callback, "callback")
        params = {
            "symbol": symbol,
            "account-id" : account_id,
            "states" : order_states,
            "types" : order_types,
            "start-date" : start_date,
            "end-date" : end_date,
            "from": from_id,
            "direct" : direct,
            "size" : size,
            "client-req-id" : client_req_id
        }

        ReqOrderListService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_order_detail(self, order_id: 'str', callback,
                                client_req_id:'str'=None, error_handler=None):
        """
        Subscribe candlestick/kline event. If the candlestick/kline is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(candlestick_event: 'CandlestickEvent'):
                        pass
        :param client_req_id: client request ID
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Huobi server
            example: def error_handler(exception: 'HuobiApiException')
                        pass
        :return: No return
        """
        check_should_not_none(order_id, "order_id")
        check_should_not_none(callback, "callback")
        params = {
            "order-id": order_id,
            "cid": client_req_id,
        }

        ReqOrderDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def get_order(self, order_id: 'int') -> Order:
        """
        Get the details of an order.

        :param order_id: The order id. (mandatory)
        :return: The information of order.
        """
        check_should_not_none(order_id, "order_id")

        params = {
            "order_id": order_id,
        }

        return GetOrderByIdService(params).request(**self.__kwargs)

    def get_order_by_client_order_id(self, client_order_id):
        check_should_not_none(client_order_id, "clientOrderId")

        params = {
            "clientOrderId": client_order_id,
        }

        return GetOrderByClientOrderIdService(params).request(**self.__kwargs)

    def get_orders(self, symbol: 'str', order_state: 'OrderState', order_type: 'OrderType' = None,
                              start_date: 'str' = None, end_date: 'str' = None, start_id: 'int' = None,
                              size: 'int' = None, direct=None) -> list:
        check_symbol(symbol)
        check_should_not_none(order_state, "order_state")
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")

        params = {
            "symbol" : symbol,
            "types" : order_type,
            "start-date" : start_date,
            "end-date" : end_date,
            "from" : start_id,
            "states" : order_state,
            "size" :  size,
            "direct" : direct
        }

        return GetOrdersService(params).request(**self.__kwargs)

    def get_open_orders(self, symbol: 'str', account_id: 'int', side: 'OrderSide' = None,
                        size: 'int' = None, from_id=None, direct=None) -> list:
        """
        The request of get open orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_id: The order side, buy or sell. If no side defined, will return all open orders of the account. (mandatory)
        :param side: The order side, buy or sell. If no side defined, will return all open orders of the account. (optional)
        :param size: The number of orders to return. Range is [1, 500]. (optional)
        :param direct: 1:prev  order by ID asc from from_id, 2:next order by ID desc from from_id
        :param from_id: start ID for search
        :return: The orders information.
        """
        check_symbol(symbol)
        check_range(size, 1, 500, "size")
        check_should_not_none(account_id, "account_id")
        params = {
            "symbol" : symbol,
            "account-id" : account_id,
            "side" : side,
            "size" : size,
            "from" : from_id,
            "direct" : direct
        }

        return GetOpenOrdersService(params).request(**self.__kwargs)

    def get_history_orders(self, symbol=None, start_time=None, end_time=None, size=None, direct=None)-> list:
        """
        Transfer Asset between Futures and Contract.

        :param direct:
        :param symbol: The target sub account uid to transfer to or from. (optional)
        :param start_time: The crypto currency to transfer. (optional)
        :param end_time: The amount of asset to transfer. (optional)
        :param size: The type of transfer, need be "futures-to-pro" or "pro-to-futures" (optional)
        :return: The Order list.
        """
        params = {
            "symbol" :symbol,
            "start-time" : start_time,
            "end-time" : end_time,
            "size" : size,
            "direct" : direct
        }


        return GetHistoryOrdersService(params).request(**self.__kwargs)

    def get_match_result(self, symbol: 'str', order_type: 'OrderSide' = None, start_date: 'str' = None,
                         end_date: 'str' = None,
                         size: 'int' = None,
                         from_id: 'int' = None,
                         direct:'str'=None):
        """
        Search for the trade records of an account.

        :param symbol: The symbol, like "btcusdt" (mandatory).
        :param order_type: The types of order to include in the search (optional).
        :param start_date: Search starts date in format yyyy-mm-dd. (optional).
        :param end_date: Search ends date in format yyyy-mm-dd. (optional).
        :param size: The number of orders to return, range [1-100]. (optional).
        :param from_id: Search order id to begin with. (optional).
        :return:
        """

        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        check_range(size, 1, 100, "size")

        params = {
            "symbol" : symbol,
            "start-date" : start_date,
            "end-date" : end_date,
            "types" : order_type,
            "size" : size,
            "from" : from_id,
            "direct" : direct
        }

        return GetMatchResultsService(params).request(**self.__kwargs)

    def get_match_results_by_order_id(self, order_id: 'int') -> list:
        """
        Get detail match results of an order.

        :param order_id: The order id. (mandatory)
        :return: The list of match result.
        """
        check_should_not_none(order_id, "order_id")

        params = {
            "order_id": order_id
        }

        return GetMatchResultsByOrderIdService(params).request(**self.__kwargs)

    def order_source_desc(self, account_type):
        default_source = "api"
        if account_type:
            if account_type == AccountType.MARGIN:
                return "margin-api"
        return default_source

    def create_order(self, symbol: 'str', account_id: 'int', order_type: 'OrderType', amount: 'float',
                     price: 'float', source:'str'=None, client_order_id=None, stop_price=None, operator=None) -> int:
        """
        Make an order in huobi.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param account_id: Account id. (mandatory)
        :param order_type: The order type. (mandatory)
        :param source: The order type. (optional)
        :param amount: The amount to buy (quote currency) or to sell (base currency). (mandatory)
        :param price: The limit price of limit order, only needed for limit order. (mandatory for buy-limit, sell-limit, buy-limit-maker and sell-limit-maker)
        :param client_order_id: unique Id which is user defined and must be unique in recent 24 hours
        :param stop_price: Price for auto sell to get the max benefit
        :param operator: the condition for stop_price, value can be "gte" or "lte",  gte – greater than and equal (>=), lte – less than and equal (<=)
        :return: The order id.
        """

        check_symbol(symbol)
        check_should_not_none(account_id, "account_id")
        check_should_not_none(order_type, "order_type")
        check_should_not_none(amount, "amount")
        if order_type == OrderType.SELL_LIMIT \
                or order_type == OrderType.BUY_LIMIT \
                or order_type == OrderType.BUY_LIMIT_MAKER \
                or order_type == OrderType.SELL_LIMIT_MAKER:
            check_should_not_none(price, "price")
        if order_type == OrderType.SELL_MARKET or order_type == OrderType.BUY_MARKET:
            price = None

        params = {
            "account-id" : account_id,
            "amount" : amount,
            "price": price,
            "symbol": symbol,
            "type": order_type,
            "source": source,
            "client-order-id": client_order_id,
            "stop-price": stop_price,
            "operator": operator
        }

        print("create order params :", params)

        return PostCreateOrderService(params).request(**self.__kwargs)

    def cancel_order(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")

        params = {
            "order_id" : order_id
        }

        return PostCancelOrderService(params).request(**self.__kwargs)

    def cancel_orders(self, symbol, order_id_list)->BatchCancelResult:
        """
        Submit cancel request for cancelling multiple orders.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param order_id_list: The list of order id. the max size is 50. (mandatory)
        :return: No return
        """
        check_symbol(symbol)
        check_should_not_none(order_id_list, "order_id_list")
        check_list(order_id_list, 1, 50, "order_id_list")

        string_list = list()
        for order_id in order_id_list:
            string_list.append(str(order_id))

        params = {
            "order-ids" : string_list
        }

        return PostBatchCancelOrderService(params).request(**self.__kwargs)

    def cancel_open_orders(self, account_id, symbols: 'str'=None , side=None, size=None)->BatchCancelCount:
        """
        Request to cancel open orders.

        :param symbols: The symbol, like "btcusdt".
        :param account_type: Account type. (mandatory)
        :param side: The order side, buy or sell. If no side defined, will cancel all open orders of the account. (optional)
        :param size: The number of orders to cancel. Range is [1, 100]. (optional)
        :return: Status of batch cancel result.
        """
        check_should_not_none(account_id, "account_id")

        params = {
            "account-id": account_id,
            "symbol" : symbols,
            "side" : side,
            "size" : size
        }

        return PostBatchCancelOpenOrderService(params).request(**self.__kwargs)

    def cancel_client_order(self, client_order_id)->int:
        """
        Request to cancel open orders.

        :param client_order_id: user defined unique order id
        """
        check_should_not_none(client_order_id, "client-order-id")

        params = {
            "client-order-id" : client_order_id
        }

        return PostCancelClientOrderService(params).request(**self.__kwargs)

    def transfer_between_futures_and_pro(self, currency: 'str', amount: 'float',
                                        transfer_type: 'TransferFuturesPro')-> int:
        """
        Transfer Asset between Futures and Contract.

        :param sub_uid: The target sub account uid to transfer to or from. (mandatory)
        :param currency: The crypto currency to transfer. (mandatory)
        :param amount: The amount of asset to transfer. (mandatory)
        :param transfer_type: The type of transfer, need be "futures-to-pro" or "pro-to-futures" (mandatory)
        :return: The order id.
        """
        check_currency(currency)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "transfer_type")
        params = {
            "currency" : currency,
            "amount" : amount,
            "type" : transfer_type

        }

        return PostTransferFuturesProService(params).request(**self.__kwargs)
