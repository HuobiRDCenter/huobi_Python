import time
from huobi.impl.websocketrequest import WebsocketRequest
from huobi.impl.utils.channels import *
from huobi.impl.utils.channelparser import ChannelParser
from huobi.impl.accountinfomap import account_info_map
from huobi.impl.utils.timeservice import *
from huobi.impl.utils.inputchecker import *
from huobi.model import *
from huobi.model.orderupdatenew import OrderUpdateNew
from huobi.model.orderupdatenewevent import OrderUpdateNewEvent


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
            ch = json_wrapper.get_string("ch")
            parse = ChannelParser(ch)
            candlestick_event = CandlestickEvent()
            candlestick_event.symbol = parse.symbol
            candlestick_event.interval = interval
            candlestick_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            tick = json_wrapper.get_object("tick")
            data = Candlestick()
            data.timestamp = convert_cst_in_second_to_utc(tick.get_int("id"))
            data.open = tick.get_float("open")
            data.close = tick.get_float("close")
            data.low = tick.get_float("low")
            data.high = tick.get_float("high")
            data.amount = tick.get_float("amount")
            data.count = tick.get_int("count")
            data.volume = tick.get_float("vol")
            candlestick_event.data = data
            return candlestick_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
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

        def json_parse(json_wrapper):
            ch = json_wrapper.get_string("ch")
            parse = ChannelParser(ch)
            trade_statistics_event = TradeStatisticsEvent()
            trade_statistics_event.symbol = parse.symbol
            ts = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            trade_statistics_event.timestamp = ts
            tick = json_wrapper.get_object("tick")
            statistics = TradeStatistics()
            statistics.amount = tick.get_float("amount")
            statistics.open = tick.get_float("open")
            statistics.close = tick.get_float("close")
            statistics.high = tick.get_float("high")
            statistics.timestamp = ts
            statistics.count = tick.get_int("count")
            statistics.low = tick.get_float("low")
            statistics.volume = tick.get_float("vol")
            trade_statistics_event.trade_statistics = statistics
            return trade_statistics_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = json_parse
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
            trade_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            tick = json_wrapper.get_object("tick")
            data_array = tick.get_array("data")
            trade_list = list()
            for item in data_array.get_items():
                trade = Trade()
                trade.amount = item.get_float("amount")
                trade.price = item.get_float("price")
                trade.trade_id = item.get_string("id")
                trade.direction = item.get_string("direction")
                trade.timestamp = convert_cst_in_millisecond_to_utc(item.get_int("ts"))
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

    def subscribe_price_depth_event(self, symbols, callback, error_handler=None):
        check_symbol_list(symbols)
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            for val in symbols:
                connection.send(price_depth_channel(val))
                time.sleep(0.01)

        def json_parse(json_wrapper):
            ch = json_wrapper.get_string("ch")
            parse = ChannelParser(ch)
            price_depth_event = PriceDepthEvent()
            price_depth_event.symbol = parse.symbol
            price_depth_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            price_depth = PriceDepth()
            tick = json_wrapper.get_object("tick")
            bid_list = list()
            bids_array = tick.get_array("bids")
            for item in bids_array.get_items_as_array():
                depth_entry = DepthEntry()
                depth_entry.price = item.get_float_at(0)
                depth_entry.amount = item.get_float_at(1)
                bid_list.append(depth_entry)
            ask_list = list()
            asks_array = tick.get_array("asks")
            for item in asks_array.get_items_as_array():
                depth_entry = DepthEntry()
                depth_entry.price = item.get_float_at(0)
                depth_entry.amount = item.get_float_at(1)
                ask_list.append(depth_entry)
            price_depth.bids = bid_list
            price_depth.asks = ask_list
            price_depth_event.data = price_depth
            return price_depth_event

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.is_trading = False
        request.json_parser = json_parse
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
            order_update_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            data = json_wrapper.get_object("data")
            order = Order()
            order.order_id = data.get_int("order-id")
            order.symbol = parse.symbol
            order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                    data.get_int("account-id")).account_type
            order.amount = data.get_float("order-amount")
            order.price = data.get_float("order-price")
            order.created_timestamp = convert_cst_in_millisecond_to_utc(data.get_int("created-at"))
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
            order_update_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            data = json_wrapper.get_object("data")
            order = OrderUpdateNew()

            order.match_id = data.get_int("match-id")
            order.order_id = data.get_int("order-id")
            order.symbol = parse.symbol
            order.state = data.get_string("order-state")
            order.role = data.get_string("role")
            order.price = data.get_float("price")
            order.filled_amount = data.get_float("filled-amount")
            order.filled_cash_amount = data.get_float("filled-cash-amount")
            order.unfilled_amount = data.get_float("unfilled-amount")
            order.client_order_id = data.get_string("client-order-id")

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
            account_event.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
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
