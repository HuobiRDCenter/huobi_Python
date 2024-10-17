from huobi.client.etf import EtfClient
from huobi.client.generic import GenericClient
import time

from huobi.client.margin import MarginClient
from huobi.client.trade import TradeClient
from huobi.client.wallet import WalletClient
from huobi.constant import *
from performance.account_performance import AccountClientPerformance
from performance.market_performance import MarketClientPerformance


class RunStatus:
    SUCCESS = "OK"
    FAILED = "Fail"


ROUND_SIZE = 3
TRANSFER_TRX_MIN_AMOUNT = 100

time_cost_detail_list = []
count_offset = 0
from huobi.constant.test import g_api_key, g_secret_key

# prepare list
withdraw_address = "TRec1vonZcbcXHs5TZLuH2WTa8ejXvnTm8"
loan_amount = 100
loan_currency = "usdt"
loan_symbol = "eosusdt"
trade_symbol = "eosusdt"


class TimeCost:
    sdk_api_start_time = 0.0  # SDK call start time
    server_req_cost = 0.0  # time cost from response.elapsed.total_seconds(), cost is from sending request to receive response
    server_api_cost = 0.0  # manually statistics time before/after requests.get  (server_api_cost >= server_req_cost)
    function_name = ""
    run_status = ""

    def __init__(self, function_name=""):
        self.sdk_api_start_time = round(time.time(), ROUND_SIZE + 1)
        self.function_name = function_name

    def add_record(self):
        sdk_api_end_time = round(time.time(), ROUND_SIZE + 1)
        sdk_api_cost = sdk_api_end_time - self.sdk_api_start_time
        sdk_cost_req = sdk_api_cost - self.server_req_cost
        sdk_cost_manual = sdk_api_cost - self.server_api_cost

        row_dict = {
            "sdk_api_cost": round(sdk_api_cost, ROUND_SIZE),
            "server_api_cost": round(self.server_api_cost, ROUND_SIZE + 1),
            "server_req_cost": round(self.server_req_cost, ROUND_SIZE + 1),
            "sdk_api_delay": round(sdk_cost_manual, ROUND_SIZE),
            "sdk_req_delay": round(sdk_cost_req, ROUND_SIZE),
            "sdk_func_name": self.function_name,
            "run_status": self.run_status,
            "sdk_test_start_time": self.sdk_api_start_time
        }
        global time_cost_detail_list
        time_cost_detail_list.append(row_dict)

    @staticmethod
    def output_sdk_cost_list(data_list, format_str="", only_brief=False):

        TimeCost.output_sdk_header(format_str, only_brief)

        for dict_data in data_list:
            TimeCost.output_sdk_cost(dict_data, format_str, only_brief)

    @staticmethod
    def output_sdk_header(format_str, only_brief):
        delay_server_api_cost = "delay(server_api_cost){format_str}".format(format_str=format_str)
        delay_server_req_cost = "delay(server_req_cost){format_str}".format(format_str=format_str)
        sdk_api_cost = "sdk_api_cost{format_str}".format(format_str=format_str)

        sdk_test_start_time = "sdk_test_start_time{format_str}".format(format_str=format_str)
        sdk_func_name = "sdk_func_name{format_str}".format(format_str=format_str)
        run_status = "run_status{format_str}".format(format_str=format_str)

        if only_brief:
            print(delay_server_api_cost,
                  delay_server_req_cost,
                  sdk_api_cost)
        else:
            print(
                delay_server_api_cost,
                delay_server_req_cost,
                sdk_api_cost,
                sdk_test_start_time,
                sdk_func_name,
                run_status)

    @staticmethod
    def output_sdk_cost(dict_data, format_str, only_brief):
        sdk_test_start_time = dict_data.get("sdk_test_start_time", "")
        if sdk_test_start_time:
            sdk_test_start_time_desc = "{sdk_test_start_time}{format_str}".format(
                sdk_test_start_time=dict_data["sdk_test_start_time"],
                format_str=format_str)
        else:
            sdk_test_start_time_desc = ""

        sdk_api_delay_desc = "{sdk_api_delay}({server_api_cost}){format_str}".format(
            sdk_api_delay=dict_data["sdk_api_delay"],
            server_api_cost=dict_data["server_api_cost"],
            format_str=format_str)

        sdk_req_delay_desc = "{sdk_req_delay}({server_req_cost}){format_str}".format(
            sdk_req_delay=dict_data["sdk_req_delay"],
            server_req_cost=dict_data["server_req_cost"],
            format_str=format_str)

        sdk_api_cost_desc = "{sdk_api_cost}{format_str}".format(
            sdk_api_cost=dict_data["sdk_api_cost"],
            format_str=format_str)

        sdk_func_name = dict_data.get("sdk_func_name", None)
        if sdk_func_name:
            sdk_func_name_desc = "{sdk_func_name}{format_str}".format(
                sdk_func_name=dict_data["sdk_func_name"],
                format_str=format_str)
        else:
            sdk_func_name_desc = ""

        run_status = dict_data.get("run_status", None)
        if run_status:
            run_status_desc = "{run_status}{format_str}".format(
                run_status=dict_data["run_status"],
                format_str=format_str)
        else:
            run_status_desc = ""

        if only_brief:
            print(
                sdk_api_delay_desc,
                sdk_req_delay_desc,
                sdk_api_cost_desc,
            )
        else:
            print(
                sdk_api_delay_desc,
                sdk_req_delay_desc,
                sdk_api_cost_desc,
                sdk_test_start_time_desc,
                sdk_func_name_desc,
                run_status_desc
            )

    @staticmethod
    def output_sort_cost(by_key_name, is_sorted=False):
        global time_cost_detail_list

        if is_sorted:
            output_list = sorted(time_cost_detail_list, key=lambda e: e.__getitem__(by_key_name), reverse=True)
        else:
            output_list = time_cost_detail_list

        TimeCost.output_sdk_cost_list(data_list=output_list, format_str="\t", only_brief=False)

    @staticmethod
    def output_average_cost():
        global time_cost_detail_list
        global count_offset
        sum_final = {}
        average_final = {}
        average_count = 0
        sum_key_list = ["sdk_api_cost", "server_api_cost", "server_req_cost", "sdk_api_delay", "sdk_req_delay"]
        if len(time_cost_detail_list):
            average_count = len(time_cost_detail_list) + count_offset
            for key_name in sum_key_list:
                sum_final[key_name] = sum(row[key_name] for row in time_cost_detail_list)
                average_final[key_name] = round(sum_final[key_name] / average_count, ROUND_SIZE)

        print("api counts :", average_count, count_offset)
        # TimeCost.output_sdk_cost_list(data_list=[sum_final], only_brief=True)
        TimeCost.output_sdk_cost_list(data_list=[average_final], only_brief=True)


class RestfulTestCaseSeq:

    def __init__(self):
        pass

    def test_generic(self):
        generic_client = GenericClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)
        # case get_exchange_symbol_list
        tc = TimeCost(function_name=generic_client.get_exchange_timestamp.__name__)
        result, tc.server_req_cost, tc.server_api_cost = generic_client.get_exchange_timestamp()
        tc.run_status = RunStatus.SUCCESS if result and result > 0 else RunStatus.FAILED
        tc.add_record()

        # case get_exchange_currencies
        tc = TimeCost(function_name=generic_client.get_exchange_currencies.__name__)
        result, tc.server_req_cost, tc.server_api_cost = generic_client.get_exchange_currencies()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_exchange_symbols
        tc = TimeCost(function_name=generic_client.get_exchange_symbols.__name__)
        result, tc.server_req_cost, tc.server_api_cost = generic_client.get_exchange_symbols()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_reference_currencies
        tc = TimeCost(function_name=generic_client.get_reference_currencies.__name__)
        result, tc.server_req_cost, tc.server_api_cost = generic_client.get_reference_currencies()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_system_status
        tc = TimeCost(function_name=generic_client.get_system_status.__name__)
        result, tc.server_req_cost, tc.server_api_cost = generic_client.get_system_status()
        tc.run_status = RunStatus.SUCCESS if result and result.get("page") and result.get(
            "components") else RunStatus.FAILED
        tc.add_record()

    def test_market(self):
        market_client = MarketClientPerformance(api_key=g_api_key, secret_key=g_secret_key)
        common_market_symbol = "btcusdt"

        # case get_candlestick
        tc = TimeCost(function_name=market_client.get_candlestick.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_candlestick(symbol=common_market_symbol,
                                                                                       period=CandlestickInterval.MIN1,
                                                                                       size=150)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_pricedepth
        tc = TimeCost(function_name=market_client.get_pricedepth.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_pricedepth(symbol=common_market_symbol,
                                                                                      depth_type=DepthStep.STEP0,
                                                                                      depth_size=20)
        tc.run_status = RunStatus.SUCCESS if result and len(result.bids) else RunStatus.FAILED
        tc.add_record()

        # case get_market_detail
        tc = TimeCost(function_name=market_client.get_market_trade.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_market_detail(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and result.id else RunStatus.FAILED
        tc.add_record()

        # case get_market_trade
        tc = TimeCost(function_name=market_client.get_market_trade.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_market_trade(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_history_trade
        tc = TimeCost(function_name=market_client.get_history_trade.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_history_trade(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and result.count else RunStatus.FAILED
        tc.add_record()

        # case get_market_detail_merged
        tc = TimeCost(function_name=market_client.get_market_detail_merged.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_market_detail_merged(
            symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result.bid) and len(result.ask) else RunStatus.FAILED
        tc.add_record()

        # case get_market_tickers
        tc = TimeCost(function_name=market_client.get_market_tickers.__name__)
        result, tc.server_req_cost, tc.server_api_cost = market_client.get_market_tickers()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_wallet(self):
        wallet_client = WalletClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        # case get_account_deposit_address
        tc = TimeCost(function_name=wallet_client.get_account_deposit_address.__name__)
        result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_account_deposit_address(currency="usdt")
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_withdraw_quota
        tc = TimeCost(function_name=wallet_client.get_account_withdraw_quota.__name__)
        result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_account_withdraw_quota(currency="usdt")
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_deposit_withdraw
        tc = TimeCost(function_name=wallet_client.get_deposit_withdraw.__name__)
        result, tc.server_req_cost, tc.server_api_cost = wallet_client.get_deposit_withdraw(
            op_type=DepositWithdraw.DEPOSIT, currency=None, from_id=1, size=10, direct=QueryDirection.PREV)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_create_withdraw
        tc = TimeCost(function_name=wallet_client.post_create_withdraw.__name__)
        record_id, tc.server_req_cost, tc.server_api_cost = wallet_client.post_create_withdraw(address=withdraw_address,
                                                                                               amount=2,
                                                                                               currency="usdt", fee=0,
                                                                                               chain="trc20usdt",
                                                                                               address_tag=None)
        tc.run_status = RunStatus.SUCCESS if record_id and record_id > 0 else RunStatus.FAILED
        tc.add_record()

        # case post_cancel_withdraw
        tc = TimeCost(function_name=wallet_client.post_cancel_withdraw.__name__)
        record_id, tc.server_req_cost, tc.server_api_cost = wallet_client.post_cancel_withdraw(withdraw_id=record_id)
        tc.run_status = RunStatus.SUCCESS if record_id and record_id > 0 else RunStatus.FAILED
        tc.add_record()

    def test_cross_margin(self):
        margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        # case post_cross_margin_transfer_in
        tc = TimeCost(function_name=margin_client.post_cross_margin_transfer_in.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_cross_margin_transfer_in(
            currency=loan_currency, amount=loan_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_cross_margin_account_balance
        tc = TimeCost(function_name=margin_client.get_cross_margin_account_balance.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_cross_margin_account_balance()
        tc.run_status = RunStatus.SUCCESS if result and result.id else RunStatus.FAILED
        tc.add_record()

        # case get_cross_margin_loan_info
        tc = TimeCost(function_name=margin_client.get_cross_margin_loan_info.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_cross_margin_loan_info()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_cross_margin_create_loan_orders
        tc = TimeCost(function_name=margin_client.post_cross_margin_create_loan_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_cross_margin_create_loan_orders(
            currency=loan_currency, amount=loan_amount)
        tc.run_status = RunStatus.SUCCESS if result and int(result) > 0 else RunStatus.FAILED
        tc.add_record()

        time.sleep(3)  # wait for interest amount
        # case get_cross_margin_loan_orders
        tc = TimeCost(function_name=margin_client.get_cross_margin_loan_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_cross_margin_loan_orders(
            currency=loan_currency, state=LoanOrderState.ACCRUAL)
        cross_loan_accrual_order_list = result
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_cross_margin_loan_order_repay
        interest_amount = 0.0
        if cross_loan_accrual_order_list and len(cross_loan_accrual_order_list):
            for loan_order in cross_loan_accrual_order_list:
                tc = TimeCost(function_name=margin_client.post_cross_margin_loan_order_repay.__name__)
                repay_amount = float(loan_order.loan_balance) + float(loan_order.interest_balance)
                interest_amount = interest_amount + float(loan_order.interest_balance)
                result, tc.server_req_cost, tc.server_api_cost = margin_client.post_cross_margin_loan_order_repay(
                    order_id=loan_order.id, amount=repay_amount)
                tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
                tc.add_record()

        time.sleep(2)  # wait for repay result
        # case post_cross_margin_transfer_out
        tc = TimeCost(function_name=margin_client.post_cross_margin_transfer_out.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_cross_margin_transfer_out(
            currency=loan_currency, amount=loan_amount - interest_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_margin(self):
        margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        # case post_transfer_in_margin
        tc = TimeCost(function_name=margin_client.post_transfer_in_margin.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_transfer_in_margin(symbol=loan_symbol,
                                                                                               currency=loan_currency,
                                                                                               amount=loan_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_margin_loan_info
        tc = TimeCost(function_name=margin_client.get_margin_loan_info.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_margin_loan_info(
            symbols="btcusdt,ethusdt,eosusdt," + loan_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_margin_loan_orders
        tc = TimeCost(function_name=margin_client.get_margin_loan_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_margin_loan_orders(symbol=loan_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_create_margin_order
        tc = TimeCost(function_name=margin_client.post_create_margin_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_create_margin_order(
            symbol=loan_symbol, currency=loan_currency, amount=loan_amount)
        tc.run_status = RunStatus.SUCCESS if result and int(result) > 0 else RunStatus.FAILED
        tc.add_record()

        time.sleep(3)  # wait for interest amount
        # case get_margin_loan_orders
        tc = TimeCost(function_name=margin_client.get_margin_loan_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.get_margin_loan_orders(
            symbol=loan_symbol, states=LoanOrderState.ACCRUAL)
        cross_loan_accrual_order_list = result
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case post_repay_margin_order
        interest_amount = 0.0
        if cross_loan_accrual_order_list and len(cross_loan_accrual_order_list):
            for loan_order in cross_loan_accrual_order_list:
                tc = TimeCost(function_name=margin_client.post_repay_margin_order.__name__)
                repay_amount = float(loan_order.loan_balance) + float(loan_order.interest_balance)
                interest_amount = interest_amount + float(loan_order.interest_balance)
                result, tc.server_req_cost, tc.server_api_cost = margin_client.post_repay_margin_order(
                    order_id=12345, amount=repay_amount)
                tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
                tc.add_record()

        time.sleep(2)  # wait for repay result

        # case post_transfer_out_margin
        tc = TimeCost(function_name=margin_client.post_transfer_out_margin.__name__)
        result, tc.server_req_cost, tc.server_api_cost = margin_client.post_transfer_out_margin(symbol=loan_symbol,
                                                                                                currency=loan_currency,
                                                                                                amount=loan_amount - interest_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_trade_fee(self):
        trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        # case get_feerate
        tc = TimeCost(function_name=trade_client.get_feerate.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_feerate(
            symbols="htusdt,btcusdt,eosusdt," + trade_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_transact_feerate
        tc = TimeCost(function_name=trade_client.get_transact_feerate.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_transact_feerate(
            symbols="htusdt,btcusdt,eosusdt," + trade_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_trade_order(self):
        trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        client_order_id = "test_" + str(round(time.time())) + "_id"
        print("client order id : ", client_order_id)
        # case create_order
        tc = TimeCost(function_name=trade_client.create_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.create_order(
            symbol=trade_symbol,
            account_id=g_account_id,
            order_type=OrderType.BUY_LIMIT,
            source=OrderSource.API,
            amount=55,
            price=0.1,
            client_order_id=client_order_id,
            stop_price=0.08,
            operator="gte")
        order_id_tmp = result
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_order
        tc = TimeCost(function_name=trade_client.get_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.get_order(
            order_id=order_id_tmp)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_order_by_client_order_id
        tc = TimeCost(function_name=trade_client.get_order_by_client_order_id.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.get_order_by_client_order_id(
            client_order_id=client_order_id)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_open_orders
        tc = TimeCost(function_name=trade_client.get_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.get_open_orders(
            symbol=trade_symbol, account_id=g_account_id)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_orders
        tc = TimeCost(function_name=trade_client.get_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.get_orders(
            symbol=trade_symbol, order_type=OrderType.BUY_LIMIT, order_state=OrderState.SUBMITTED)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case cancel_order
        tc = TimeCost(function_name=trade_client.cancel_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.order_id = trade_client.cancel_order(
            symbol=trade_symbol, order_id=order_id_tmp)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_trade_create_cancel_orders(self):
        trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)
        client_order_id_header = "test_" + str(round(time.time())) + "_id"
        client_order_id_eos_01 = client_order_id_header + "01"
        client_order_id_eos_02 = client_order_id_header + "02"
        client_order_id_eos_03 = client_order_id_header + "03"

        buy_limit_eos_01 = {
            "account_id": g_account_id,
            "symbol": trade_symbol,
            "order_type": OrderType.BUY_LIMIT,
            "source": OrderSource.API,
            "amount": 50,
            "price": 0.12,
            "client_order_id": client_order_id_eos_01
        }

        buy_limit_eos_02 = {
            "account_id": g_account_id,
            "symbol": trade_symbol,
            "order_type": OrderType.BUY_LIMIT,
            "source": OrderSource.API,
            "amount": 7,
            "price": 0.80,
            "client_order_id": client_order_id_eos_02
        }

        buy_limit_eos_03 = {
            "account_id": g_account_id,
            "symbol": trade_symbol,
            "order_type": OrderType.BUY_LIMIT,
            "source": OrderSource.API,
            "amount": 20,
            "price": 0.252,
            "client_order_id": client_order_id_eos_03
        }

        order_config_list = [
            buy_limit_eos_01,
            buy_limit_eos_02,
            buy_limit_eos_03
        ]

        # case batch_create_order
        tc = TimeCost(function_name=trade_client.batch_create_order.__name__)
        create_result, tc.server_req_cost, tc.server_api_cost = trade_client.batch_create_order(
            order_config_list=order_config_list)
        tc.run_status = RunStatus.SUCCESS if create_result else RunStatus.FAILED
        tc.add_record()

        # time.sleep(1)  # need wait

        order_id_list = []
        if create_result and len(create_result):
            for item in create_result:
                order_id_list.append(item.order_id)

            # case batch_create_order
            tc = TimeCost(function_name=trade_client.batch_create_order.__name__)
            result, tc.server_req_cost, tc.server_api_cost = trade_client.cancel_orders(order_id_list=order_id_list)
            tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
            tc.add_record()

    def test_trade_create_cancel_open_orders(self):
        trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)
        order_config_list = []
        for i in range(6):
            buy_limit_item = {
                "account_id": g_account_id,
                "symbol": trade_symbol,
                "order_type": OrderType.BUY_LIMIT,
                "source": OrderSource.API,
                "amount": 50,
                "price": 0.12 + round(i / 100, 3),
            }
            order_config_list.append(buy_limit_item)

        # case batch_create_order
        tc = TimeCost(function_name=trade_client.batch_create_order.__name__)
        create_result, tc.server_req_cost, tc.server_api_cost = trade_client.batch_create_order(
            order_config_list=order_config_list)
        print(type(create_result), type(tc.server_req_cost), type(tc.server_api_cost))
        tc.run_status = RunStatus.SUCCESS if create_result else RunStatus.FAILED
        tc.add_record()

        # case cancel_open_orders
        tc = TimeCost(function_name=trade_client.cancel_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.cancel_open_orders(account_id=g_account_id)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_trade_match_result(self):
        trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)

        tc = TimeCost(function_name=trade_client.create_order.__name__)
        created_order_id, tc.server_req_cost, tc.server_api_cost = trade_client.create_order(
            symbol=trade_symbol, account_id=g_account_id, order_type=OrderType.BUY_MARKET, source=OrderSource.API,
            amount=5.0, price=None)
        print("create order id for match result: ", created_order_id)
        tc.run_status = RunStatus.SUCCESS if created_order_id else RunStatus.FAILED
        tc.add_record()
        time.sleep(2)  # match result is not ready, need sleep a time

        # case get_match_results_by_order_id
        tc = TimeCost(function_name=trade_client.get_match_results_by_order_id.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_match_results_by_order_id(
            order_id=created_order_id)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_match_result
        tc = TimeCost(function_name=trade_client.get_match_result.__name__)
        result, tc.server_req_cost, tc.server_api_cost = trade_client.get_match_result(
            symbol=trade_symbol, size=10)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_account(self):
        account_client = AccountClientPerformance(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)
        # case get_accounts
        tc = TimeCost(function_name=account_client.get_accounts.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_accounts()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_balance
        tc = TimeCost(function_name=account_client.get_account_balance.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_account_balance()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_by_type_and_symbol
        tc = TimeCost(function_name=account_client.get_account_by_type_and_symbol.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_account_by_type_and_symbol(
            account_type=AccountType.SPOT, symbol=None)
        account_id_spot = result.id if result else None
        tc.run_status = RunStatus.SUCCESS if result and result.id and account_id_spot else RunStatus.FAILED
        tc.add_record()

        # case get_account_history
        tc = TimeCost(function_name=account_client.get_account_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_account_history(account_id=account_id_spot)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_ledger
        tc = TimeCost(function_name=account_client.get_account_ledger.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_account_ledger(account_id=account_id_spot)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_balance
        tc = TimeCost(function_name=account_client.get_balance.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.get_balance(account_id=account_id_spot)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case transfer_between_futures_and_pro
        tc = TimeCost(function_name=account_client.transfer_between_futures_and_pro.__name__)
        result, tc.server_req_cost, tc.server_api_cost = account_client.transfer_between_futures_and_pro(currency="trx",
                                                                                                         amount=200,
                                                                                                         transfer_type=TransferFuturesPro.TO_FUTURES)
        time.sleep(2)
        result, tc.server_req_cost, tc.server_api_cost = account_client.transfer_between_futures_and_pro(currency="trx",
                                                                                                         amount=200,
                                                                                                         transfer_type=TransferFuturesPro.TO_PRO)
        tc.run_status = RunStatus.SUCCESS if result and result > 0 else RunStatus.FAILED
        tc.add_record()

    def test_etf(self):
        etf_client = EtfClient(api_key=g_api_key, secret_key=g_secret_key, performance_test=True)
        # case get_etf_swap_config
        tc = TimeCost(function_name=etf_client.get_etf_swap_config.__name__)
        result, tc.server_req_cost, tc.server_api_cost = etf_client.get_etf_swap_config(etf_name="hb10")
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_etf_swap_list
        tc = TimeCost(function_name=etf_client.get_etf_swap_list.__name__)
        result, tc.server_req_cost, tc.server_api_cost = etf_client.get_etf_swap_list(etf_name="hb10", offset=0,
                                                                                      size=10)
        tc.run_status = RunStatus.SUCCESS if len(result) >= 0 else RunStatus.FAILED
        tc.add_record()


if __name__ == "__main__":
    test_case = RestfulTestCaseSeq()
    test_case.test_generic()
    test_case.test_market()
    test_case.test_wallet()
    test_case.test_cross_margin()
    test_case.test_margin()
    test_case.test_account()
    test_case.test_etf()
    test_case.test_cross_margin()
    test_case.test_trade_fee()
    test_case.test_trade_match_result()
    test_case.test_trade_order()
    test_case.test_trade_create_cancel_orders()
    test_case.test_trade_create_cancel_open_orders()

    print("\n\n==================api execute sequence=========================")
    TimeCost.output_sort_cost(by_key_name="", is_sorted=False)

    print("\n\n======================order by api delay time desc=====================")
    TimeCost.output_sort_cost(by_key_name="sdk_api_delay", is_sorted=True)

    print("\n\n======================average cost/delay time=====================")
    TimeCost.output_average_cost()
