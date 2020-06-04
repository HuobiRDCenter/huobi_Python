from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import *


margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)

# no filter
list_obj = margin_client.get_cross_margin_loan_orders()
LogInfo.output_list(list_obj)

# filter by state
list_obj = margin_client.get_cross_margin_loan_orders(state=LoanOrderState.ACCRUAL)
LogInfo.output_list(list_obj)


