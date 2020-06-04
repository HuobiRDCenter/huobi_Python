from huobi.client.market import MarketClient


def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()
    print()



market_client = MarketClient(init_log=True)
market_client.sub_trade_detail("btcusdt,eosusdt", callback)

