from huobi import RequestClient


request_client = RequestClient()
trade_list = request_client.get_historical_trade("btcusdt", 5)
for trade in trade_list:
    print("Trade at: " + str(trade.timestamp))
    print("Id: " + str(trade.trade_id))
    print("Price: " + str(trade.price))
    print("Amount: " + str(trade.amount))
    print("Direction: " + trade.direction)
    print()
