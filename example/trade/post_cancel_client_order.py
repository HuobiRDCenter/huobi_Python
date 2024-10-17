from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *

client_order_id_test = "xxxxxx"
symbol_test = "eosusdt"

trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key)

order_id = trade_client.create_order(symbol=symbol_test, account_id=g_account_id,
                                     order_type=OrderType.BUY_LIMIT,
                                     source=OrderSource.API,
                                     amount=18.0,
                                     price=0.292, client_order_id=client_order_id_test)
LogInfo.output("created order id : {id}, {client_order_id}".format(id=order_id, client_order_id=client_order_id_test))
result = trade_client.cancel_client_order(client_order_id=client_order_id_test)
LogInfo.output("cancel result {id}".format(id=result))

