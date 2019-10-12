from huobi import RequestClient
from huobi.model import *

from huobi.base.printobject import PrintMix

request_client = RequestClient()
trades = request_client.get_market_trade(symbol="btcusdt")
if len(trades):
    for trade in trades:
        trade.print_object()
        print()















