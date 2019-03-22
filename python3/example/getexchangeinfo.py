from huobi import RequestClient


request_client = RequestClient()
exchange_info = request_client.get_exchange_info()
print("---- Supported symbols ----")
for symbol in exchange_info.symbol_list:
    print(symbol.symbol)

print("---- Supported currencies ----");
for currency in exchange_info.currencies:
    print(currency)
