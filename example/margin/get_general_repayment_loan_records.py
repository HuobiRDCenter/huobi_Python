from huobi.client.margin import MarginClient
from huobi.constant import *
from huobi.utils import LogInfo

margin_client = MarginClient(api_key=g_api_key, secret_key=g_secret_key)

list_result = margin_client.get_general_repayment_loan_records(limit=10)
LogInfo.output_list(list_result)




