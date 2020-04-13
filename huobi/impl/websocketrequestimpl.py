import time
from huobi.impl.websocketrequest import WebsocketRequest
from huobi.impl.utils.channels import *
from huobi.impl.utils.channelsrequest import *
from huobi.impl.utils.channelparser import ChannelParser
from huobi.impl.accountinfomap import account_info_map
from huobi.impl.utils.timeservice import *
from huobi.impl.utils.inputchecker import *
from huobi.model import *
from huobi.model.accountbalancerequest import AccountBalanceRequest
from huobi.model.candlestickrequest import CandlestickRequest
from huobi.model.orderdetailrequest import OrderDetailRequest
from huobi.model.orderlistrequest import OrderListRequest
from huobi.model.orderupdatenew import OrderUpdateNew
from huobi.model.orderupdatenewevent import OrderUpdateNewEvent
from huobi.model.pricedepthbboevent import PriceDepthBboEvent
from huobi.model.pricedepthrequest import PriceDepthRequest
from huobi.model.traderequest import TradeRequest
from huobi.model.tradestatisticsrequest import TradeStatisticsRequest


class WebsocketRequestImpl(object):

    def __init__(self, api_key):
        self.__api_key = api_key

    def subscribe_candlestick_event(self, symbols, interval, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(kline_channel(val, interval))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            candle_stick_event_obj = CandlestickEvent.json_parse(json_wrapper)
            candle_stick_event_obj.interval = interval
            return candle_stick_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_candlestick_event(self, symbols, interval, callback, from_ts_second, end_ts_second, auto_close, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(request_kline_channel(val, interval, from_ts_second, end_ts_second))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            candle_stick_event_obj = CandlestickRequest.json_parse(json_wrapper)
            candle_stick_event_obj.interval = interval
            return candle_stick_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = False
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_24h_trade_statistics_event(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(trade_statistics_channel(val))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = TradeStatisticsEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_24h_trade_statistics_event(self, symbols, callback, auto_close, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(request_trade_statistics_channel(val))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = False
        request.json_parser = TradeStatisticsRequest.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_trade_event(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(trade_channel(val))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            ch = json_wrapper.get_string("ch")
            parse = ChannelParser(ch)
            trade_event = TradeEvent()
            trade_event.symbol = parse.symbol
            trade_event.timestamp = json_wrapper.get_int("ts")
            tick = json_wrapper.get_object("tick")
            data_array = tick.get_array("data")
            trade_list = list()
            for item in data_array.get_items():
                trade = Trade.json_parse(item)
                trade_list.append(trade)
            trade_event.trade_list = trade_list
            return trade_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_trade_event(self, symbols, callback, auto_close, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(request_trade_channel(val))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = False
        request.json_parser = TradeRequest.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_price_depth_event(self, symbols, depth_step, callback, error_handler=None):
        check_symbol_list(symbols)
        new_step = PriceDepth.get_valid_depth_step(value=depth_step, defalut_value=DepthStep.STEP0)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(price_depth_channel(val, new_step))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = PriceDepthEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_mbp_event(self, symbols, level, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(mbp_channel(val, level))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = MbpEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_full_mbp_event(self, symbols, level, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(full_mbp_channel(val, level))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = MbpEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_price_depth_bbo_event(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(price_depth_bbo_channel(val))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = PriceDepthBboEvent.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_price_depth_event(self, symbols, depth_step, callback, auto_close, error_handler=None):
        check_symbol_list(symbols)
        new_step = PriceDepth.get_valid_depth_step(value=depth_step, defalut_value=DepthStep.STEP0)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(request_price_depth_channel(val, new_step))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = False
        request.json_parser = PriceDepthRequest.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_mbp_event(self, symbols, level, callback, auto_close, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(request_mbp_channel(val, level))
                time.sleep(0.01)

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = False
        request.json_parser = MbpRequest.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_order_update(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(orders_channel(val))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            ch = json_wrapper.get_string("topic")
            parse = ChannelParser(ch)
            order_update_event = OrderUpdateEvent()
            order_update_event.symbol = parse.symbol
            order_update_event.timestamp = json_wrapper.get_int("ts")
            data = json_wrapper.get_object("data")
            order = Order()
            order.order_id = data.get_int("order-id")
            order.symbol = parse.symbol
            order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                    data.get_int("account-id")).account_type
            order.amount = data.get_float("order-amount")
            order.price = data.get_float("order-price")
            order.created_timestamp = data.get_int("created-at")
            order.order_type = data.get_string("order-type")
            order.filled_amount = data.get_float("filled-amount")
            order.filled_cash_amount = data.get_float("filled-cash-amount")
            order.filled_fees = data.get_float("filled-fees")
            order.state = data.get_string("order-state")
            order.source = data.get_string("order-source")
            order_update_event.data = order
            return order_update_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = True
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_order_update_new(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(orders_update_new_channel(val))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            ch = json_wrapper.get_string("topic")
            parse = ChannelParser(ch)
            order_update_event = OrderUpdateNewEvent()
            order_update_event.symbol = parse.symbol
            order_update_event.timestamp = json_wrapper.get_int("ts")
            data = json_wrapper.get_object("data")
            order = OrderUpdateNew.json_parse(data)

            order_update_event.data = order
            return order_update_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = True
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def subscribe_account_event(self, mode, callback, error_handler=None):
        check_should_not_none(mode, "mode")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(account_channel(mode))

        def json_parse(json_wrapper):
            account_event = AccountEvent()
            account_event.timestamp = json_wrapper.get_int("ts")
            data = json_wrapper.get_object("data")
            account_event.change_type = data.get_string("event")
            list_array = data.get_array("list")
            account_change_list = list()
            for item in list_array.get_items():
                account_change = AccountChange()
                account_change.account_type = account_info_map.get_account_by_id(self.__api_key, item.get_int(
                    "account-id")).account_type
                account_change.currency = item.get_string("currency")
                account_change.balance = item.get_float("balance")
                account_change.balance_type = item.get_string("type")
                account_change_list.append(account_change)
            account_event.account_change_list = account_change_list
            return account_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = True
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request


    def request_account_balance_event(self, callback, client_req_id, auto_close, error_handler=None):
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(request_account_list_channel(client_req_id))

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = True
        request.json_parser = AccountBalanceRequest.json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_order_list_event(self, symbol, account_id, callback, order_states, client_req_id, auto_close, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(request_order_list_channel(symbol=symbol, account_id=account_id, states_str=order_states, client_req_id=client_req_id))

        def get_account_type_map(json_wrapper):
            #get account type mapping
            account_id_type_map = {}
            error_code = json_wrapper.get_int("err-code")
            if error_code == 0:
                order_list_json = json_wrapper.get_array("data")
                for order_json in order_list_json.get_items():
                    account_id = order_json.get_int("account-id")
                    account_type = account_info_map.get_account_by_id(self.__api_key, account_id).account_type
                    account_id_type_map[account_id] = account_type
            return account_id_type_map

        def json_parse(json_wrapper):
            account_type_map = get_account_type_map(json_wrapper)
            req_obj = OrderListRequest.json_parse(json_wrapper, account_type_map)
            req_obj = OrderListRequest.update_symbol(req_obj)
            return req_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = True
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request

    def request_order_detail_event(self, order_id, callback, client_req_id, auto_close, error_handler=None):
        check_should_not_none(order_id, "order_id")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(request_order_detail_channel(order_id, client_req_id))

        def get_account_type_map(json_wrapper):
            #get account type mapping
            account_id_type_map = {}
            data = json_wrapper.get_object("data")
            account_id = data.get_int("account-id")
            account_type = account_info_map.get_account_by_id(self.__api_key, account_id).account_type
            account_id_type_map[account_id] = account_type
            return account_id_type_map

        def json_parse(json_wrapper):
            account_type_map = get_account_type_map(json_wrapper)
            req_obj = OrderDetailRequest.json_parse(json_wrapper, account_type_map)
            return req_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.auto_close = auto_close
        request.is_trading = True
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler
        return request
