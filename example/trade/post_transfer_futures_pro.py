from huobi.client import TradeClient
from huobi.constant import *


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, url=HUOBI_URL_VN)

currency_test = "trx"

trans_id_one = trade_client.transfer_between_futures_and_pro(amount=100, currency=currency_test,
                                                               transfer_type=TransferFuturesPro.TO_FETURES)
print (trans_id_one)
trans_id_two = trade_client.transfer_between_futures_and_pro(amount=100, currency=currency_test,
                                                               transfer_type=TransferFuturesPro.TO_PRO)
print (trans_id_two)
