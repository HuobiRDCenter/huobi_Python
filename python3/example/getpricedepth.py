from huobi import RequestClient


request_client = RequestClient()
depth = request_client.get_price_depth("btcusdt", 5)
print("---- Top 5 bids ----")
i = 0
for entry in depth.bids:
    i = i + 1
    print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))

print("---- Top 5 asks ----")
i = 0
for entry in depth.asks:
    i = i + 1
    print(str(i) + ": price: " + str(entry.price) + ", amount: " + str(entry.amount))
