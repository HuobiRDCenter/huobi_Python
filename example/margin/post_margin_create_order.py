from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *
import time

loan_amount = 100
interest_amount = 0.004083

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
loan_id = margin_client.post_create_margin_order(symbol="eosusdt", currency="usdt", amount=loan_amount)
LogInfo.output("step 1: loan id : {id}".format(id=loan_id))

time.sleep(2)

repay_id = margin_client.post_repay_margin_order(loan_id=loan_id, amount=loan_amount + interest_amount)
LogInfo.output("step 2: repay id : {id}".format(id=repay_id))

list_obj = margin_client.get_margin_loan_orders(symbol="eosusdt", states=LoanOrderState.ACCRUAL)
LogInfo.output("step 3: loaning order information")
LogInfo.output_list(list_obj)


list_obj = margin_client.get_margin_loan_orders(symbol="eosusdt")
LogInfo.output("step 4: loan order history")
LogInfo.output_list(list_obj)