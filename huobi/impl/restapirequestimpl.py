from huobi.impl import RestApiRequest
from huobi.impl.utils.urlparamsbuilder import UrlParamsBuilder
from huobi.impl.utils.apisignature import create_signature
from huobi.impl.accountinfomap import account_info_map
from huobi.impl.utils.inputchecker import *
from huobi.impl.utils.timeservice import *
from huobi.model import *


class RestApiRequestImpl(object):
    # __MARKET_URL = "https://api.huobi.pro:443"
    # __TRADING_URL = "https://api.huobi.pro:443"

    def __init__(self, api_key, secret_key, server_url="https://api.huobi.pro"):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__server_url = server_url

    def __create_request_by_get(self, url, builder=UrlParamsBuilder()):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({'Content-Type': 'application/json'})
        request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder=UrlParamsBuilder()):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        create_signature(self.__api_key, self.__secret_key, request.method, request.host + url, builder)
        request.header.update({"Content-Type": "application/x-www-form-urlencoded"})
        request.url = url + builder.build_url()
        return request

    def get_exchange_timestamp(self):
        request = self.__create_request_by_get("/v1/common/timestamp")

        def parse(json_wrapper):
            return convert_cst_in_millisecond_to_utc(json_wrapper.get_int("data"))

        request.json_parser = parse
        return request

    def get_candlestick(self, symbol, interval, size, start_time=None, end_time=None):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")

        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("period", interval)
        builder.put_url("size", size)
        builder.put_url("start_time", start_time)
        builder.put_url("end_time", end_time)

        request = self.__create_request_by_get("/market/history/kline", builder)

        def parse(json_wrapper):
            candlestick_list = list()
            data_list = json_wrapper.get_array("data")
            for item in data_list.get_items():
                candlestick = Candlestick()
                candlestick.timestamp = convert_cst_in_second_to_utc(item.get_int("id"))
                candlestick.low = item.get_float("low")
                candlestick.high = item.get_float("high")
                candlestick.amount = item.get_float("amount")
                candlestick.open = item.get_float("open")
                candlestick.close = item.get_float("close")
                candlestick.volume = item.get_float("vol")
                candlestick.count = item.get_int("count")
                candlestick_list.append(candlestick)
            return candlestick_list

        request.json_parser = parse
        return request

    def get_price_depth(self, symbol, size=None):
        check_symbol(symbol)
        check_range(size, 1, 150, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("type", "step0")
        request = self.__create_request_by_get("/market/depth", builder)

        def parse(json_wrapper):
            tick = json_wrapper.get_object("tick")
            dp = PriceDepth()
            dp.timestamp = convert_cst_in_millisecond_to_utc(tick.get_int("ts"))
            bid_array = tick.get_array("bids")
            ask_array = tick.get_array("asks")
            bids = list()
            asks = list()
            for i in range(0, size):
                bid_entry = bid_array.get_array_at(i)
                entry = DepthEntry()
                entry.price = bid_entry.get_float_at(0)
                entry.amount = bid_entry.get_float_at(1)
                bids.append(entry)
            for i in range(0, size):
                ask_entry = ask_array.get_array_at(i)
                entry = DepthEntry()
                entry.price = ask_entry.get_float_at(0)
                entry.amount = ask_entry.get_float_at(1)
                asks.append(entry)
            dp.bids = bids
            dp.asks = asks
            return dp

        request.json_parser = parse
        return request

    def get_historical_trade(self, symbol, form_id, size):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("size", size)
        request = self.__create_request_by_get("/market/history/trade", builder)

        def parse(json_wrapper):
            data_array = json_wrapper.get_array("data")
            trade_list = list()
            for item in data_array.get_items():
                data_array_in = item.get_array("data")
                for item_in in data_array_in.get_items():
                    local_trade = Trade()
                    local_trade.price = item_in.get_float("price")
                    local_trade.amount = item_in.get_float("amount")
                    local_trade.trade_id = item_in.get_int("id")
                    local_trade.timestamp = convert_cst_in_millisecond_to_utc(item_in.get_int("ts"))
                    local_trade.direction = item_in.get_string("direction")
                    trade_list.append(local_trade)
            return trade_list

        request.json_parser = parse
        return request

    def get_24h_trade_statistics(self, symbol):
        check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        request = self.__create_request_by_get("/market/detail", builder)

        def parse(json_wrapper):
            tick = json_wrapper.get_object("tick")
            trade_statistics = TradeStatistics()
            trade_statistics.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            trade_statistics.amount = tick.get_float("amount")
            trade_statistics.open = tick.get_float("open")
            trade_statistics.close = tick.get_float("close")
            trade_statistics.high = tick.get_float("high")
            trade_statistics.low = tick.get_float("low")
            trade_statistics.count = tick.get_int("count")
            trade_statistics.volume = tick.get_float("vol")
            return trade_statistics

        request.json_parser = parse
        return request

    def get_symbols(self):
        request = self.__create_request_by_get("/v1/common/symbols", UrlParamsBuilder())

        def parse(json_wrapper):
            symbols = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                local_symbol = Symbol()
                local_symbol.base_currency = item.get_string("base-currency")
                local_symbol.quote_currency = item.get_string("quote-currency")
                local_symbol.price_precision = item.get_int("price-precision")
                local_symbol.amount_precision = item.get_int("amount-precision")
                local_symbol.symbol_partition = item.get_string("symbol-partition")
                local_symbol.symbol = item.get_string("symbol")
                symbols.append(local_symbol)
            return symbols

        request.json_parser = parse
        return request

    def get_currencies(self):
        request = self.__create_request_by_get("/v1/common/currencys", UrlParamsBuilder())

        def parse(json_wrapper):
            return json_wrapper.get_array("data").get_items_as_string()

        request.json_parser = parse
        return request

    def get_best_quote(self, symbol):
        check_symbol(symbol)
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        request = self.__create_request_by_get("/market/detail/merged", builder)

        def parse(json_wrapper):
            best_quote = BestQuote()
            best_quote.timestamp = convert_cst_in_millisecond_to_utc(json_wrapper.get_int("ts"))
            tick = json_wrapper.get_object("tick")
            ask_array = tick.get_array("ask")
            best_quote.ask_price = ask_array.get_float_at(0)
            best_quote.ask_amount = ask_array.get_float_at(1)
            bid_array = tick.get_array("bid")
            best_quote.bid_price = bid_array.get_float_at(0)
            best_quote.bid_amount = bid_array.get_float_at(1)
            return best_quote

        request.json_parser = parse
        return request

    def get_accounts(self):
        request = self.__create_request_by_get_with_signature("/v1/account/accounts")

        def parse(json_wrapper):
            account_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                account = Account()
                account.id = item.get_int("id")
                account.account_type = item.get_string("type")
                account.account_state = item.get_string("state")
                account_list.append(account)
            return account_list

        request.json_parser = parse
        return request

    def get_withdraw_history(self, currency, from_id, size):
        check_currency(currency)
        check_should_not_none(from_id, "from_id")
        check_should_not_none(size, "size")

        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("type", "withdraw")
        builder.put_url("from", from_id)
        builder.put_url("size", size);
        request = self.__create_request_by_get_with_signature("/v1/query/deposit-withdraw", builder)

        def parse(json_wrapper):
            withdraws = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                withdraw = Withdraw()
                withdraw.id = item.get_int("id")
                withdraw.currency = item.get_string("currency")
                withdraw.tx_hash = item.get_string("tx-hash")
                withdraw.amount = item.get_float("amount")
                withdraw.address = item.get_string("address")
                withdraw.address_tag = item.get_string("address-tag")
                withdraw.fee = item.get_float("fee")
                withdraw.withdraw_state = item.get_string("state")
                withdraw.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                withdraw.updated_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("updated-at"))
                withdraws.append(withdraw)
            return withdraws

        request.json_parser = parse
        return request

    def get_deposit_history(self, currency, from_id, size):
        check_symbol(currency)
        check_should_not_none(from_id, "from_id")
        check_should_not_none(size, "size")

        builder = UrlParamsBuilder()
        builder.put_url("currency", currency)
        builder.put_url("type", "deposit")
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/query/deposit-withdraw", builder)

        def parse(json_wrapper):
            deposits = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                deposit = Deposit()
                deposit.id = item.get_int("id")
                deposit.currency = item.get_string("currency")
                deposit.tx_hash = item.get_string("tx-hash")
                deposit.amount = item.get_float("amount")
                deposit.address = item.get_string("address")
                deposit.address_tag = item.get_string("address-tag")
                deposit.fee = item.get_float("fee")
                deposit.withdraw_state = item.get_string("state")
                deposit.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                deposit.updated_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("updated-at"))
                deposits.append(deposit)
            return deposits

        request.json_parser = parse
        return request

    def get_balance(self, account):
        path = "/v1/account/accounts/{}/balance"
        path = path.format(account.id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            balances = list()
            data = json_wrapper.get_object("data")
            list_array = data.get_array("list")
            for item in list_array.get_items():
                balance = Balance()
                balance.balance = item.get_float("balance")
                balance.currency = item.get_string("currency")
                balance.balance_type = item.get_string("type")
                balances.append(balance)
            return balances

        request.json_parser = parse;
        return request

    def transfer(self, symbol, from_account, to_account, currency, amount):
        check_symbol(symbol)
        check_should_not_none(from_account, "from_account")
        check_should_not_none(to_account, "to_account")
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        if from_account == AccountType.SPOT and to_account == AccountType.MARGIN:
            address = "/v1/dw/transfer-in/margin"
        elif from_account == AccountType.MARGIN and AccountType.SPOT:
            address = "/v1/dw/transfer-out/margin"
        else:
            raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] incorrect transfer type")
        builder = UrlParamsBuilder()
        builder.put_post("currency", currency)
        builder.put_post("symbol", symbol)
        builder.put_post("amount", amount)
        request = self.__create_request_by_post_with_signature(address, builder)

        def parse(json_wrapper):
            if json_wrapper.get_string("status") == "ok":
                return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def apply_loan(self, symbol, currency, amount):
        check_symbol(symbol)
        check_should_not_none(currency, "currency")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("currency", currency)
        builder.put_post("symbol", symbol)
        builder.put_post("amount", amount)
        request = self.__create_request_by_post_with_signature("/v1/margin/orders", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def repay_loan(self, load_id, amount):
        check_should_not_none(load_id, "load_id")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("amount", amount)
        path = "/v1/margin/orders/{}/repay"
        path = path.format(load_id)
        request = self.__create_request_by_post_with_signature(path, builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_loan(self, symbol, start_date=None, end_date=None, states=None, from_id=None, size=None):
        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("states", states)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/margin/loan-orders", builder)

        def parse(json_wrapper):
            loan_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                loan = Loan()
                loan.loan_balance = item.get_float("loan-balance")
                loan.interest_balance = item.get_float("interest-balance")
                loan.interest_rate = item.get_float("interest-rate")
                loan.loan_amount = item.get_float("loan-amount")
                loan.interest_amount = item.get_float("interest-amount")
                loan.symbol = item.get_string("symbol")
                loan.currency = item.get_string("currency")
                loan.id = item.get_int("id")
                loan.state = item.get_string("state")
                loan.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                       item.get_int("account-id")).account_type
                loan.user_id = item.get_int("user-id")
                loan.accrued_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("accrued-at"))
                loan.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                loan_list.append(loan)
            return loan_list

        request.json_parser = parse
        return request

    def create_order(self, symbol, account_type, order_type, amount, price):
        check_symbol(symbol)
        check_should_not_none(account_type, "account_type")
        check_should_not_none(order_type, "order_type")
        check_should_not_none(amount, "amount")
        if order_type == OrderType.SELL_LIMIT \
                or order_type == OrderType.BUY_LIMIT \
                or order_type == OrderType.BUY_LIMIT_MAKER \
                or order_type == OrderType.SELL_LIMIT_MAKER:
            check_should_not_none(price, "price")
        if order_type == OrderType.SELL_MARKET or order_type == OrderType.BUY_MARKET:
            check_should_none(price, "price")
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type)
        source = "api"
        if account_type == AccountType.MARGIN:
            source = "margin-api"
        builder = UrlParamsBuilder()
        builder.put_post("account-id", account.id)
        builder.put_post("amount", amount)
        builder.put_post("price", price)
        builder.put_post("symbol", symbol)
        builder.put_post("type", order_type)
        builder.put_post("source", source)
        request = self.__create_request_by_post_with_signature("/v1/order/orders/place", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_open_orders(self, symbol, account_type, size=None, side=None):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")
        check_should_not_none(account_type, "account_type")
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type)
        builder = UrlParamsBuilder()
        builder.put_url("account-id", account.id)
        builder.put_url("symbol", symbol)
        builder.put_url("side", side)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/order/openOrders", builder)

        def parse(json_wrapper):
            order_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                order = Order()
                order.order_id = item.get_int("id")
                order.symbol = item.get_string("symbol")
                order.price = item.get_float("price")
                order.amount = item.get_float("amount")
                order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                        item.get_int("account-id")).account_type
                order.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                order.order_type = item.get_string("type")
                order.filled_amount = item.get_float("filled-amount")
                order.filled_cash_amount = item.get_float("filled-cash-amount")
                order.filled_fees = item.get_float("filled-fees")
                order.source = item.get_string("source")
                order.state = item.get_string("state")
                order_list.append(order)
            return order_list

        request.json_parser = parse
        return request

    def cancel_order(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/{}/submitcancel"
        path = path.format(order_id)
        request = self.__create_request_by_post_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def cancel_orders(self, symbol, order_id_list):
        check_symbol(symbol)
        check_should_not_none(order_id_list, "order_id_list")
        check_list(order_id_list, 1, 50, "order_id_list")
        string_list = list()
        for order_id in order_id_list:
            string_list.append(str(order_id))
        builder = UrlParamsBuilder()
        builder.put_post("order-ids", string_list)
        request = self.__create_request_by_post_with_signature("/v1/order/orders/batchcancel", builder)

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def cancel_open_orders(self, symbol, account_type, side=None, size=None):
        check_symbol(symbol)
        check_should_not_none(account_type, "account_type")
        global account_info_map
        user = account_info_map.get_user(self.__api_key)
        account = user.get_account_by_type(account_type)
        builder = UrlParamsBuilder()
        builder.put_url("account-id", account.id)
        builder.put_url("symbol", symbol)
        builder.put_url("side", side)
        builder.put_url("size", size)
        request = self.__create_request_by_post_with_signature("/v1/order/orders/batchCancelOpenOrders", builder)

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            batch_cancel_result = BatchCancelResult()
            batch_cancel_result.success_count = data.get_int("success-count")
            batch_cancel_result.failed_count = data.get_int("failed-count")
            return batch_cancel_result

        request.json_parser = parse
        return request

    def get_order(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/()"
        path = path.format(order_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            order = Order()
            order.order_id = data.get_int("id")
            order.symbol = data.get_string("symbol")
            order.price = data.get_float("price")
            order.amount = data.get_float("amount")
            order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                    data.get_int("account-id")).account_type
            order.created_timestamp = convert_cst_in_millisecond_to_utc(data.get_int("created-at"))
            order.canceled_timestamp = convert_cst_in_millisecond_to_utc(data.get_int("canceled-at"))
            order.finished_timestamp = convert_cst_in_millisecond_to_utc(data.get_int("finished-at"))
            order.order_type = data.get_string("type")
            order.filled_amount = data.get_float("field-amount")
            order.filled_cash_amount = data.get_float("field-cash-amount")
            order.filled_fees = data.get_float("field-fees")
            order.source = data.get_string("source")
            order.state = data.get_string("state")
            return order

        request.json_parser = parse
        return request

    def get_match_results_by_order_id(self, symbol, order_id):
        check_symbol(symbol)
        check_should_not_none(order_id, "order_id")
        path = "/v1/order/orders/{}/matchresults"
        path = path.format(order_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            match_result_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                match_result = MatchResult()
                match_result.id = item.get_int("id")
                match_result.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                match_result.filled_amount = item.get_float("filled-amount")
                match_result.filled_fees = item.get_float("filled-fees")
                match_result.match_id = item.get_int("match-id")
                match_result.order_id = item.get_int("order-id")
                match_result.price = item.get_float("price")
                match_result.source = item.get_string("source")
                match_result.symbol = item.get_string("symbol")
                match_result.order_type = item.get_string("type")
                match_result_list.append(match_result)
            return match_result_list

        request.json_parser = parse
        return request

    def get_match_results(self, symbol, order_type=None, start_date=None, end_date=None, size=None, from_id=None):
        check_symbol(symbol)
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        check_range(size, 1, 100, "size")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("types", order_type)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("from", from_id)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/order/matchresults", builder)

        def parse(json_wrapper):
            match_result_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                match_result = MatchResult()
                match_result.id = item.get_int("id")
                match_result.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                match_result.filled_amount = item.get_float("filled-amount")
                match_result.filled_fees = item.get_float("filled-fees")
                match_result.match_id = item.get_int("match-id")
                match_result.order_id = item.get_int("order-id")
                match_result.price = item.get_float("price")
                match_result.source = item.get_string("source")
                match_result.symbol = item.get_string("symbol")
                match_result.order_type = item.get_string("type")
                match_result_list.append(match_result)
            return match_result_list

        request.json_parser = parse
        return request

    def withdraw(self, address, amount, currency, fee=None, address_tag=None):
        check_symbol(currency)
        check_should_not_none(address, "address")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_post("address", address)
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("fee", fee)
        builder.put_post("addr-tag", address_tag)

        request = self.__create_request_by_post_with_signature("/v1/dw/withdraw/api/create", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def cancel_withdraw(self, currency, withdraw_id):
        check_symbol(currency)
        check_should_not_none(withdraw_id, "withdraw_id")
        path = "/v1/dw/withdraw-virtual/{}/cancel"
        path = path.format(withdraw_id)
        request = self.__create_request_by_post_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            return

        request.json_parser = parse
        return request

    def get_historical_orders(self, symbol, order_state, order_type=None, start_date=None, end_date=None, start_id=None,
                              size=None):
        check_symbol(symbol),
        check_should_not_none(order_state, "order_state")
        start_date = format_date(start_date, "start_date")
        end_date = format_date(end_date, "end_date")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("types", order_type)
        builder.put_url("start-date", start_date)
        builder.put_url("end-date", end_date)
        builder.put_url("from", start_id)
        builder.put_url("states", order_state)
        builder.put_url("size", size)
        request = self.__create_request_by_get_with_signature("/v1/order/orders", builder)

        def parse(json_wrapper):
            order_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                order = Order()
                order.account_type = account_info_map.get_account_by_id(self.__api_key,
                                                                        item.get_int("account-id")).account_type
                order.amount = item.get_float("amount")
                order.canceled_timestamp = convert_cst_in_millisecond_to_utc(item.get_int_or_default("canceled-at", 0))
                order.finished_timestamp = convert_cst_in_millisecond_to_utc(item.get_int_or_default("finished-at", 0))
                order.order_id = item.get_int("id")
                order.symbol = item.get_string("symbol")
                order.price = item.get_float("price")
                order.created_timestamp = convert_cst_in_millisecond_to_utc(item.get_int("created-at"))
                order.order_type = item.get_string("type")
                order.filled_amount = item.get_float("field-amount")
                order.filled_cash_amount = item.get_float("field-cash-amount")
                order.filled_fees = item.get_float("field-fees")
                order.source = item.get_string("source")
                order.state = item.get_string("state")
                order_list.append(order)
            return order_list

        request.json_parser = parse
        return request

    def transfer_between_parent_and_sub(self, sub_uid, currency, amount, transfer_type):
        check_currency(currency)
        check_should_not_none(sub_uid, "sub_uid")
        check_should_not_none(amount, "amount")
        check_should_not_none(transfer_type, "transfer_type")
        builder = UrlParamsBuilder()
        builder.put_post("sub-uid", sub_uid)
        builder.put_post("amount", amount)
        builder.put_post("currency", currency)
        builder.put_post("type", transfer_type)
        request = self.__create_request_by_post_with_signature("/v1/subuser/transfer", builder)

        def parse(json_wrapper):
            return json_wrapper.get_int("data")

        request.json_parser = parse
        return request

    def get_current_user_aggregated_balance(self):
        request = self.__create_request_by_get_with_signature("/v1/subuser/aggregate-balance", UrlParamsBuilder())

        def parse(json_wrapper):
            balances = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items:
                balance = Balance()
                balance.currency = item.get_string("currency")
                balance.balance = item.get_float("balance")
                balances.append(balance)
            return balances

        request.json_parser = parse
        return request

    def get_specify_account_balance(self, sub_id):
        path = "/v1/account/accounts/{}"
        path = path.format(sub_id)
        request = self.__create_request_by_get_with_signature(path, UrlParamsBuilder())

        def parse(json_wrapper):
            complete_sub_account_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                complete_sub_account = CompleteSubAccountInfo()
                complete_sub_account.id = item.get_int("id")
                complete_sub_account.account_type = item.get_string("type")
                balances = list()
                data_array_in = item.get_array("list")
                for item_in in data_array_in.get_items():
                    balance = Balance()
                    balance.currency = item_in.get_string("currency")
                    balance.type = item_in.get_string("type")
                    balance.balance = item_in.get_float("balance")
                    balances.append(balance)
                complete_sub_account.balances = balances
                complete_sub_account_list.append(complete_sub_account)
            return complete_sub_account_list

        request.json_parser = parse
        return request

    def get_etf_candlestick(self, symbol, interval, size=None):
        check_symbol(symbol)
        check_range(size, 1, 2000, "size")
        check_should_not_none(interval, "interval")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("period", interval)
        builder.put_url("limit", size)
        request = self.__create_request_by_get("/quotation/market/history/kline", builder)

        def parse(json_wrapper):
            candlestick_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                candlestick = Candlestick()
                candlestick.open = item.get_float("open")
                candlestick.close = item.get_float("close")
                candlestick.low = item.get_float("low")
                candlestick.high = item.get_float("high")
                candlestick.amount = item.get_float("amount")
                candlestick.count = 0
                candlestick.volume = item.get_float("vol")
                candlestick_list.append(candlestick)
            return candlestick_list

        request.json_parser = parse
        return request

    def get_etf_swap_config(self, etf_symbol):
        check_symbol(etf_symbol)
        builder = UrlParamsBuilder()
        builder.put_url("etf_name", etf_symbol)
        request = self.__create_request_by_get("/etf/swap/config", builder)

        def parse(json_wrapper):
            data = json_wrapper.get_object("data")
            etf_swap_config = EtfSwapConfig()
            etf_swap_config.purchase_max_amount = data.get_int("purchase_max_amount")
            etf_swap_config.purchase_min_amount = data.get_int("purchase_min_amount")
            etf_swap_config.redemption_max_amount = data.get_int("redemption_max_amount")
            etf_swap_config.redemption_min_amount = data.get_int("redemption_min_amount")
            etf_swap_config.purchase_fee_rate = data.get_float("purchase_fee_rate")
            etf_swap_config.redemption_fee_rate = data.get_float("redemption_fee_rate")
            etf_swap_config.status = data.get_string("etf_status")
            unit_price_data_array = data.get_array("unit_price")
            unit_price_list = list()
            for item in unit_price_data_array.get_items():
                unit_price = UnitPrice()
                unit_price.currency = item.get_string("currency")
                unit_price.amount = item.get_float("amount")
                unit_price_list.append(unit_price)
            etf_swap_config.unit_price_list = unit_price_list
            return etf_swap_config

        request.json_parser = parse
        return request

    def etf_swap(self, etf_symbol, amount, swap_type):
        check_symbol(etf_symbol)
        check_should_not_none(amount, "amount")
        check_should_not_none(swap_type, "swap_type")
        builder = UrlParamsBuilder()
        builder.put_post("etf_name", etf_symbol)
        builder.put_post("amount", amount)
        if swap_type == EtfSwapType.IN:
            request = self.__create_request_by_post_with_signature("/etf/swap/in", builder)
        else:
            request = self.__create_request_by_post_with_signature("/etf/swap/out", builder)

        def parse():
            return

        request.json_parser = parse
        return request

    def get_etf_swap_history(self, etf_symbol, offset, size):
        check_symbol(etf_symbol)
        check_range(size, 1, 100, "size")
        greater_or_equal(offset, 0, "offset")
        builder = UrlParamsBuilder()
        builder.put_url("etf_name", etf_symbol)
        builder.put_url("offset", offset)
        builder.put_url("limit", size)
        request = self.__create_request_by_get_with_signature("/etf/swap/list", builder)

        def parse(json_wrapper):
            etf_swap_history_list = list()
            data_array = json_wrapper.get_array("data")
            for item in data_array.get_items():
                etf_swap_history = EtfSwapHistory()
                etf_swap_history.created_timestamp = item.get_int("gmt_created")
                etf_swap_history.currency = item.get_string("currency")
                etf_swap_history.amount = item.get_float("amount")
                etf_swap_history.type = item.get_string("type")
                etf_swap_history.status = item.get_int("status")
                detail = item.get_object("detail")
                etf_swap_history.rate = detail.get_float("rate")
                etf_swap_history.fee = detail.get_float("fee")
                etf_swap_history.point_card_amount = detail.get_float("point_card_amount")
                used_currency_array = detail.get_array("used_currency_list")
                used_currency_list = list()
                for currency in used_currency_array.get_items():
                    unit_price = UnitPrice()
                    unit_price.amount = currency.get_float("amount")
                    unit_price.currency = currency.get_string("currency")
                    used_currency_list.append(unit_price)
                etf_swap_history.used_currency_list = used_currency_list
                obtain_currency_array = detail.get_array("obtain_currency_list")
                obtain_currency_list = list()
                for currency in obtain_currency_array.get_items():
                    unit_price = UnitPrice()
                    unit_price.amount = currency.get_float("amount")
                    unit_price.currency = currency.get_string("currency")
                    obtain_currency_list.append(unit_price)
                etf_swap_history.obtain_currency_list = obtain_currency_list
                etf_swap_history_list.append(etf_swap_history)
            return etf_swap_history_list

        request.json_parser = parse
        return request
