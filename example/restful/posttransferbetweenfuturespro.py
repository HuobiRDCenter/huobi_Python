from huobi import RequestClient
from huobi.model import *


request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")

trans_id_one = request_client.transfer_between_futures_and_pro(amount=0.35, currency="eos",
                                                               transfer_type=TransferFuturesPro.TO_FUTURES)
print (trans_id_one)
trans_id_two = request_client.transfer_between_futures_and_pro(amount=0.35, currency="eos",
                                                               transfer_type=TransferFuturesPro.TO_PRO)
print (trans_id_two)
