from huobi.client.generic import GenericClient

generic_client = GenericClient()
market_status = generic_client.get_market_status()
print(market_status)



