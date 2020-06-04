from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *


amount = 100
currency = "usdt"


margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)
# order_id = margin_client.post_cross_margin_create_loan_orders(currency=currency, amount=amount)
# LogInfo.output("step 1: create loan order {id}".format(id=order_id))

# to check not clearing loan orders
list_obj = margin_client.get_cross_margin_loan_orders(currency=currency, state=LoanOrderState.ACCRUAL)
LogInfo.output("step 2: loaning order information ")
LogInfo.output_list(list_obj)

if list_obj and len(list_obj):
    for loan_order in list_obj:
        # pay attention to Scientific Notation
        repay_amount = float(loan_order.loan_balance) + float(loan_order.interest_balance)
        LogInfo.output("repay loan order {id}, repay amount : {amount}".format(id=loan_order.id, amount=repay_amount))
        result = margin_client.post_cross_margin_loan_order_repay(order_id=loan_order.id, amount=repay_amount)
        LogInfo.output("step 3: repay loan order {id}, status : {status}, repay amount : {amount}".format(id=loan_order.id, status=result, amount=repay_amount))

list_obj = margin_client.get_cross_margin_loan_orders(currency=currency, state=LoanOrderState.ACCRUAL)
LogInfo.output("step 4: loaning order history ")
LogInfo.output_list(list_obj)
