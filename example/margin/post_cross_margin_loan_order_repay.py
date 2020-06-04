from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)

# to check not clearing loan orders
list_obj = margin_client.get_cross_margin_loan_orders(currency="usdt", state=LoanOrderState.ACCRUAL)
LogInfo.output_list(list_obj)

if list_obj and len(list_obj):
    for loan_order in list_obj:
        repay_amount = float(loan_order.loan_balance) + float(loan_order.interest_balance)
        LogInfo.output("repay loan order {id} and amount {amount}".format(id=loan_order.id, amount=repay_amount))
        order_id = margin_client.post_cross_margin_loan_order_repay(order_id=loan_order.id, amount=repay_amount)

# to check not clearing loan orders
list_obj = margin_client.get_cross_margin_loan_orders(currency="usdt", state=LoanOrderState.ACCRUAL)
LogInfo.output_list(list_obj)