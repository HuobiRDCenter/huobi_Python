from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import LogInfo

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)

currency_test = "trx"
trans_id_one = trade_client.transfer_between_futures_and_pro(amount=400, currency=currency_test,
                                                               transfer_type=TransferFuturesPro.TO_FUTURES)
LogInfo.output(trans_id_one)



trans_id_two = trade_client.transfer_between_futures_and_pro(amount=400, currency=currency_test,
                                                               transfer_type=TransferFuturesPro.TO_PRO)
LogInfo.output(trans_id_two)
