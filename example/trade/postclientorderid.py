from huobi import RequestClient
from huobi.model import *
from huobi.base.printobject import PrintMix

symbol_test = "eosht"
client_order_id_test = "xxxxxx"  # unique id in 24hours

request_client = RequestClient(api_key="xxxxxx", secret_key="xxxxxx")

order_id = request_client.create_order(symbol=symbol_test,
                                       account_type=AccountType.SPOT,
                                       order_type=OrderType.SELL_LIMIT,
                                       amount=1.0,
                                       price=20.12,
                                       client_order_id=client_order_id_test,
                                       stop_price=12,
                                       operator="gte")
print ("create new order id : " + (str(order_id)) + " with client id " + client_order_id_test)
print("\n\n")


orderObj = request_client.get_order(symbol=symbol_test, order_id=order_id)
print ("get order by order id : " + (str(order_id)))
PrintMix.print_data(orderObj)
print("\n\n")

orderObj = request_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
print ("get order by client order id : " + client_order_id_test)
PrintMix.print_data(orderObj)
print("\n\n")

request_client.cancel_client_order(client_order_id=client_order_id_test)
print ("cancel order by client order id : " + client_order_id_test)
print("\n\n")

orderObj = request_client.get_order_by_client_order_id(client_order_id=client_order_id_test)
print ("get order by client order id : " + client_order_id_test + " after cancel")
PrintMix.print_data(orderObj)


