from huobi import RequestClient
from huobi.constant.test import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
market_ticker_list = request_client.get_market_tickers()
if market_ticker_list and len(market_ticker_list):
    for market_ticker in market_ticker_list:
        market_ticker.print_object()
        print()
