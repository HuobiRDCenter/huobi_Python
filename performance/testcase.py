
from huobi.model import *
import time

from performance.requsttest import RequestTest
import sys
from huobi.constant.test import *

class RunStatus:
    SUCCESS = "OK"
    FAILED = "Fail"

ROUND_SIZE = 3
TRANSFER_TRX_MIN_AMOUNT = 100

time_cost_detail_list = []
count_offset = 0

class TimeCost:
    sdk_api_start_time = 0.0  # SDK call start time
    server_req_cost = 0.0 # time cost from response.elapsed.total_seconds(), cost is from sending request to receive response
    server_api_cost = 0.0   # manually statistics time before/after requests.get  (server_api_cost >= server_req_cost)
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
            "sdk_api_cost" : round(sdk_api_cost, ROUND_SIZE),
            "server_api_cost" : round(self.server_api_cost, ROUND_SIZE + 1),
            "server_req_cost" : round(self.server_req_cost, ROUND_SIZE + 1),
            "sdk_api_delay" : round(sdk_cost_manual, ROUND_SIZE),
            "sdk_req_delay" : round(sdk_cost_req, ROUND_SIZE),
            "sdk_func_name" : self.function_name,
            "run_status" : self.run_status,
            "sdk_test_start_time" : self.sdk_api_start_time
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

        if only_brief == True:
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

        sdk_api_delay_desc ="{sdk_api_delay}({server_api_cost}){format_str}".format(
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


        if only_brief == True:
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

        if is_sorted == True:
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
        sum_key_list = ["sdk_api_cost", "server_api_cost", "server_req_cost", "sdk_api_delay", "sdk_req_delay"]
        if len(time_cost_detail_list):
            average_count = len(time_cost_detail_list) + count_offset
            for key_name in sum_key_list:
                sum_final[key_name] = sum(row[key_name] for row in time_cost_detail_list)
                average_final[key_name] = round(sum_final[key_name] / average_count, ROUND_SIZE)

        print("api counts :", average_count, count_offset)
        #TimeCost.output_sdk_cost_list(data_list=[sum_final], only_brief=True)
        TimeCost.output_sdk_cost_list(data_list=[average_final], only_brief=True)


class RestfulTestCaseSeq:

    def __init__(self):
        from huobi.constant.test import g_api_key, g_secret_key
        self.test_client = RequestTest(api_key=g_api_key, secret_key=g_secret_key)

    def test_common_market(self):
        common_market_symbol = "btcusdt"

        #case get_latest_candlestick
        tc = TimeCost(function_name = self.test_client.get_latest_candlestick.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_latest_candlestick(symbol=common_market_symbol,
                                                                                       interval=CandlestickInterval.MIN1,
                                                                                       size=150)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        #case get_candlestick
        tc = TimeCost(function_name=self.test_client.get_candlestick.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_candlestick(symbol=common_market_symbol,
                                                                                       interval=CandlestickInterval.MIN1,
                                                                                       size=150)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_price_depth
        tc = TimeCost(function_name=self.test_client.get_price_depth.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_price_depth(symbol=common_market_symbol, size=20)
        tc.run_status = RunStatus.SUCCESS if result and len(result.bids) else RunStatus.FAILED
        tc.add_record()

        # case get_market_trade
        tc = TimeCost(function_name=self.test_client.get_market_trade.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_market_trade(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_historical_trade
        tc = TimeCost(function_name = self.test_client.get_historical_trade.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_historical_trade(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()


        # case get_24h_trade_statistics
        tc = TimeCost(function_name=self.test_client.get_24h_trade_statistics.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_24h_trade_statistics(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and result.count else RunStatus.FAILED
        tc.add_record()

        # case get_exchange_symbol_list
        tc = TimeCost(function_name=self.test_client.get_exchange_symbol_list.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_exchange_symbol_list()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()


        # case get_exchange_currencies
        tc = TimeCost(function_name=self.test_client.get_exchange_currencies.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_exchange_currencies()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_best_quote
        tc = TimeCost(function_name=self.test_client.get_best_quote.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_best_quote(symbol=common_market_symbol)
        tc.run_status = RunStatus.SUCCESS if result and result.bid_amount else RunStatus.FAILED
        tc.add_record()

        # case get_order_in_recent_48hour
        tc = TimeCost(function_name=self.test_client.get_order_in_recent_48hour.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_order_in_recent_48hour()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_reference_currencies
        tc = TimeCost(function_name=self.test_client.get_reference_currencies.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_reference_currencies()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()



    def test_deposit_withdraw(self):
        #withdraw
        #cancel_withdraw
        #post_create_withdraw
        #post_cancel_withdraw

        # case get_withdraw_history
        tc = TimeCost(function_name=self.test_client.get_withdraw_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_withdraw_history(currency="usdt", from_id=0,
                                                                                           size=10)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_deposit_history
        tc = TimeCost(function_name=self.test_client.get_deposit_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_deposit_history(currency=None, from_id=0,
                                                                                          size=10,
                                                                                          direct=QueryDirection.PREV)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_deposit_withdraw
        tc = TimeCost(function_name=self.test_client.get_deposit_withdraw.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_deposit_withdraw(op_type=DepositWithdraw.WITHDRAW)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_transfer(self):

        # case transfer from spot to margin
        transfer_symbol = "trxusdt"
        transfer_currency = "trx"
        tranfer_amount = 13
        tc = TimeCost(function_name=self.test_client.transfer.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.transfer(symbol=transfer_symbol,
                                                                               from_account=AccountType.SPOT,
                                                                               to_account=AccountType.MARGIN,
                                                                               currency=transfer_currency,
                                                                               amount=tranfer_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case transfer from margin to spot
        tc = TimeCost(function_name=self.test_client.transfer.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.transfer(symbol=transfer_symbol,
                                                                               from_account=AccountType.MARGIN,
                                                                               to_account=AccountType.SPOT,
                                                                               currency=transfer_currency,
                                                                               amount=tranfer_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case transfer_between_futures_and_pro
        transfer_trx_amount = TRANSFER_TRX_MIN_AMOUNT  # 100 TRX as min amount
        tc = TimeCost(function_name=self.test_client.transfer_between_futures_and_pro.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.transfer_between_futures_and_pro(
            currency="trx",
            amount=transfer_trx_amount,
            transfer_type=TransferFuturesPro.TO_FUTURES)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case transfer_between_futures_and_pro
        transfer_trx_amount = TRANSFER_TRX_MIN_AMOUNT
        tc = TimeCost(function_name=self.test_client.transfer_between_futures_and_pro.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.transfer_between_futures_and_pro(
            currency="trx",
            amount=transfer_trx_amount,
            transfer_type=TransferFuturesPro.TO_PRO)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_cross_margin(self):
        # post_cross_margin_loan_order_repay

        # case post_cross_margin_transfer_in
        transfer_usdt_currency = "usdt"
        transfer_usdt_amount = 2
        tc = TimeCost(function_name=self.test_client.post_cross_margin_transfer_in.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.post_cross_margin_transfer_in(
            currency=transfer_usdt_currency,
            amount=transfer_usdt_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case post_cross_margin_transfer_out
        transfer_trx_amount = TRANSFER_TRX_MIN_AMOUNT
        tc = TimeCost(function_name=self.test_client.post_cross_margin_transfer_out.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.post_cross_margin_transfer_out(
            currency=transfer_usdt_currency,
            amount=transfer_usdt_amount)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_cross_margin_loan_orders
        tc = TimeCost(function_name=self.test_client.get_cross_margin_loan_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_cross_margin_loan_orders()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_cross_margin_account_balance
        tc = TimeCost(function_name=self.test_client.get_cross_margin_account_balance.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_cross_margin_account_balance()
        tc.run_status = RunStatus.SUCCESS if result and len(result.list) else RunStatus.FAILED
        tc.add_record()


    def test_load_repay(self):
        #case apply_loan
        #case repay_loan

        # case get_loan_history
        load_symbol_test = "trxusdt"
        tc = TimeCost(function_name=self.test_client.get_loan_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_loan_history(symbol=load_symbol_test)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_create_cancel_order(self):
        # case create_order
        create_order_symbol_test = "trxusdt"
        trx_sell_price = 1122
        tc = TimeCost(function_name=self.test_client.create_order.__name__)
        created_order_id, tc.server_req_cost, tc.server_api_cost = self.test_client.create_order(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT,
            order_type=OrderType.SELL_LIMIT,
            amount=1,
            price=trx_sell_price)
        tc.run_status = RunStatus.SUCCESS if created_order_id else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case create_order & get_order check status
        tc = TimeCost(function_name=self.test_client.get_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_order(
            symbol=create_order_symbol_test,
            order_id=created_order_id)
        tc.run_status = RunStatus.SUCCESS if result and result.state in [OrderState.SUBMITTING,
                                                                         OrderState.SUBMITTED] else RunStatus.FAILED
        tc.add_record()

        # case cancel_order
        tc = TimeCost(function_name=self.test_client.cancel_order.__name__)
        _, tc.server_req_cost, tc.server_api_cost = self.test_client.cancel_order(symbol=create_order_symbol_test,
                                                                              order_id=created_order_id)
        tc.run_status = RunStatus.SUCCESS
        tc.add_record()

        time.sleep(1)  # need wait

        # case cancel_order & get_order check status
        tc = TimeCost(function_name=self.test_client.get_order.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_order(
            symbol=create_order_symbol_test,
            order_id=created_order_id)
        tc.run_status = RunStatus.SUCCESS if result and (
                    result.state in [OrderState.CANCELLING, OrderState.CANCELED]) else RunStatus.FAILED
        tc.add_record()

    def test_batch_create_cancel_order(self):

        client_order_id_header = str(int(time.time()))

        symbol_eosusdt = "eosusdt"
        symbol_btcusdt = "btcusdt"

        client_order_id_eos = client_order_id_header + symbol_eosusdt
        client_order_id_btc = client_order_id_header + symbol_btcusdt

        buy_limit_eos = {
            "account_type": AccountType.SPOT,
            "symbol": symbol_eosusdt,
            "order_type": OrderType.BUY_LIMIT,
            "amount": 1,
            "price": 0.12,
            "client_order_id": client_order_id_eos
        }

        buy_limit_btc = {
            "account_type": AccountType.SPOT,
            "symbol": symbol_btcusdt,
            "order_type": OrderType.BUY_LIMIT,
            "amount": 1,
            "price": 1.12,
            "client_order_id": client_order_id_btc
        }

        order_config_list = [
            buy_limit_eos,
            buy_limit_btc
        ]

        # case batch create orders
        tc = TimeCost(function_name=self.test_client.batch_create_order.__name__)
        create_result, tc.server_req_cost, tc.server_api_cost = self.test_client.batch_create_order(order_config_list=order_config_list)
        tc.run_status = RunStatus.SUCCESS if len(create_result) else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case batch cancel orders
        tc = TimeCost(function_name=self.test_client.cancel_orders.__name__)
        cancel_result, tc.server_req_cost, tc.server_api_cost = self.test_client.cancel_orders(order_id_list=[],
                                                     client_order_id_list=[client_order_id_eos, client_order_id_btc])
        tc.run_status = RunStatus.SUCCESS if (len(cancel_result.success) and len(cancel_result.failed) ==0) else RunStatus.FAILED
        tc.add_record()

    def test_batch_cancel_get_orders(self):
        # case create orders
        create_order_symbol_test = "trxusdt"
        trx_sell_price = 1122  # 高价不成交
        order_counts = 10
        first_batch_cancel_count = 3

        i = 0
        order_id_list = []
        while(i<order_counts):
            tc = TimeCost(function_name=self.test_client.create_order.__name__)
            created_order_id, tc.server_req_cost, tc.server_api_cost = self.test_client.create_order(
                symbol=create_order_symbol_test,
                account_type=AccountType.SPOT,
                order_type=OrderType.SELL_LIMIT,
                amount=1,
                price=(trx_sell_price+i))
            tc.run_status = RunStatus.SUCCESS if created_order_id else RunStatus.FAILED
            tc.add_record()
            i = i+1
            order_id_list.append(created_order_id)

        print("batch created order count : ", len(order_id_list))
        print(order_id_list)

        time.sleep(1)  # need wait

        # case get_open_orders
        tc = TimeCost(function_name=self.test_client.get_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_open_orders(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT)
        print("case 1 : get open orders counts : ", len(result))
        tc.run_status = RunStatus.SUCCESS if result and (len(result) >= order_counts) else RunStatus.FAILED
        tc.add_record()

        # case cancel_orders
        tc = TimeCost(function_name=self.test_client.cancel_orders.__name__)
        _, tc.server_req_cost, tc.server_api_cost = self.test_client.cancel_orders(
            order_id_list=order_id_list[0:first_batch_cancel_count],
            client_order_id_list=[]
        )
        tc.run_status = RunStatus.SUCCESS
        tc.add_record()

        time.sleep(1)  # need wait

        # case get_open_orders
        tc = TimeCost(function_name=self.test_client.get_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_open_orders(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT)
        print("case 2 : get open orders counts : ", len(result))
        tc.run_status = RunStatus.SUCCESS if result and (len(result) >= order_counts - first_batch_cancel_count) else RunStatus.FAILED
        tc.add_record()

        # case cancel_open_orders & get_order check status
        tc = TimeCost(function_name=self.test_client.cancel_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.cancel_open_orders(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT)
        tc.run_status = RunStatus.SUCCESS if result and result.success_count >= 0 and result.failed_count == 0 else RunStatus.FAILED
        tc.add_record()

        time.sleep(1)  # need wait

        # case get_open_orders
        tc = TimeCost(function_name=self.test_client.get_open_orders.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_open_orders(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT)
        print("case 3 : get open orders counts : ", len(result))
        tc.run_status = RunStatus.SUCCESS if (len(result) == 0) else RunStatus.FAILED
        tc.add_record()


    def test_match_result(self):
        create_order_symbol_test = "trxusdt"
        tc = TimeCost(function_name=self.test_client.create_order.__name__)
        created_order_id, tc.server_req_cost, tc.server_api_cost = self.test_client.create_order(
            symbol=create_order_symbol_test,
            account_type=AccountType.SPOT,
            order_type=OrderType.SELL_MARKET,
            amount=1,
            price=None)
        print("create order id for match result: ", created_order_id)
        tc.run_status = RunStatus.SUCCESS if created_order_id else RunStatus.FAILED
        tc.add_record()
        time.sleep(1)  # match result is not ready, need sleep a time

        # case get_match_results_by_order_id
        tc = TimeCost(function_name=self.test_client.get_match_results_by_order_id.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_match_results_by_order_id(order_id=created_order_id)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_match_result
        tc = TimeCost(function_name=self.test_client.get_match_result.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_match_result(
            symbol=create_order_symbol_test)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_account(self):
        spot_account_id = 0

        # case get_account_balance
        tc = TimeCost(function_name="(" + self.test_client.get_accounts.__name__ + " GET request call once)")
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_accounts()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()
        for row in result:
            if row.account_type == AccountType.SPOT:
                spot_account_id = row.id
                break
        print("test_account spot account id : ", spot_account_id)

        # case get_account_balance
        tc = TimeCost(function_name="(" + self.test_client.get_account_balance.__name__ + " GET request call once)")
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_balance()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()
        spot_account_id = 0
        for row in result:
            if row.account_type == AccountType.SPOT:
                spot_account_id = row.id
                break
        print("test_account spot account id : ", spot_account_id)

        # case get_current_user_aggregated_balance
        tc = TimeCost(function_name=self.test_client.get_current_user_aggregated_balance.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_current_user_aggregated_balance()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        #get_specify_account_balance


        # case get_margin_balance_detail
        tc = TimeCost(function_name=self.test_client.get_margin_balance_detail.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_margin_balance_detail()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_deposit_address
        tc = TimeCost(function_name=self.test_client.get_account_deposit_address.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_deposit_address(currency="usdt")
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_withdraw_quota
        tc = TimeCost(function_name=self.test_client.get_account_withdraw_quota.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_withdraw_quota(currency="usdt")
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        # case get_account_history
        tc = TimeCost(function_name=self.test_client.get_account_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_history(account_id=spot_account_id)
        tc.run_status = RunStatus.SUCCESS
        tc.add_record()

        # case get_account_ledger
        tc = TimeCost(function_name=self.test_client.get_account_ledger.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_ledger(account_id=spot_account_id)
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_etf(self):

        # case get_etf_swap_config
        tc = TimeCost(function_name=self.test_client.get_etf_swap_config.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_etf_swap_config(etf_symbol="hb10")
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

        # case get_etf_swap_history
        tc = TimeCost(function_name=self.test_client.get_etf_swap_history.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_etf_swap_history(etf_symbol="hb10", offset=0, size=10)
        tc.run_status = RunStatus.SUCCESS if len(result) >= 0 else RunStatus.FAILED
        tc.add_record()

    def test_trade(self):
        # case get_fee_rate
        tc = TimeCost(function_name=self.test_client.get_fee_rate.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_fee_rate(symbols="btcusdt,trxusdt,eosusdt")
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_sub_uid_management(self):
        # case sub_uid_management
        tc = TimeCost(function_name=self.test_client.sub_uid_management.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.sub_uid_management(sub_uid=g_sub_uid, action=SubUidState.LOCK)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

        tc = TimeCost(function_name=self.test_client.sub_uid_management.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.sub_uid_management(sub_uid=g_sub_uid,
                                                                                             action=SubUidState.UNLOCK)
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()

    def test_get_market_tickers(self):
        # case get_market_tickers
        tc = TimeCost(function_name=self.test_client.get_market_tickers.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_market_tickers()
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_get_system_status(self):
        # case get_system_status
        tc = TimeCost(function_name=self.test_client.get_system_status.__name__)
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_system_status()
        tc.run_status = RunStatus.SUCCESS if result else RunStatus.FAILED
        tc.add_record()

    def test_account_balance_performance(self):

        # case get_account_balance
        tc = TimeCost(function_name="(" + self.test_client.get_account_balance.__name__ + " GET request call once)")
        result, tc.server_req_cost, tc.server_api_cost = self.test_client.get_account_balance()
        tc.run_status = RunStatus.SUCCESS if result and len(result) else RunStatus.FAILED
        tc.add_record()
        spot_account_id = 0
        for row in result:
            if row.account_type == AccountType.SPOT:
                spot_account_id = row.id
                break
        print("test_account spot account id : ", spot_account_id)

if __name__ == "__main__":
    test_case = RestfulTestCaseSeq()
    test_case.test_common_market()
    test_case.test_deposit_withdraw()
    test_case.test_transfer()
    test_case.test_load_repay()
    test_case.test_create_cancel_order()
    test_case.test_batch_create_cancel_order()
    test_case.test_batch_cancel_get_orders()
    test_case.test_match_result()
    test_case.test_account()
    test_case.test_account_balance_performance()
    test_case.test_etf()
    test_case.test_trade()
    test_case.test_cross_margin()
    test_case.test_sub_uid_management()
    test_case.test_get_market_tickers()
    test_case.test_get_system_status()


    print("\n\n==================api execute sequence=========================")
    TimeCost.output_sort_cost(by_key_name="", is_sorted=False)

    print("\n\n======================order by api delay time desc=====================")
    TimeCost.output_sort_cost(by_key_name="sdk_api_delay", is_sorted=True)

    print("\n\n======================average cost/delay time=====================")
    TimeCost.output_average_cost()

    """
    row_dict = {
        "sdk_api_cost": 100.11111,
        "server_api_cost": 90.103,
        "server_req_cost": 80.2938,
        "sdk_api_delay": 10.998,
        "sdk_req_delay": 9.09889,
        "sdk_func_name": "aaaaaaaa",
        "run_status": "OK",
        "sdk_test_start_time": 8878373773.09889
    }

    row_dict2 = {
        "sdk_api_cost": 90.11111,
        "server_api_cost": 190.103,
        "server_req_cost": 180.2938,
        "sdk_api_delay": 18.998,
        "sdk_req_delay": 8.09889,
        "sdk_func_name": "bbbbbbb",
        "run_status": "OK",
        "sdk_test_start_time": 8878373773.09889
    }

    time_cost_detail_list.append(row_dict)
    time_cost_detail_list.append(row_dict2)

    #TimeCost.output_sdk_header(format_str="\t", only_brief=False)
    #TimeCost.output_sdk_header(format_str="\t", only_brief=True)
    #TimeCost.output_sdk_cost(dict_data=row_dict, format_str="\t", only_brief=False)
    #TimeCost.output_sdk_cost(dict_data=row_dict, format_str="\t", only_brief=True)

    TimeCost.output_sort_cost(by_key_name="", is_sorted=False)
    print()
    TimeCost.output_sort_cost(by_key_name="sdk_api_delay", is_sorted=True)
    print()
    TimeCost.output_sort_cost(by_key_name="sdk_req_delay", is_sorted=True)
    print()

    TimeCost.output_average_cost()
    """












