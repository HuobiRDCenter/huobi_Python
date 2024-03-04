from huobi.client.market import MarketClient
from huobi.model.market import TradeDetailReq


def callback(trade_req: 'TradeDetailReq'):
    print("---- trade_event:  ----")
    trade_req.print_object()
    print()


market_client = MarketClient()
market_client.req_trade_detail("btcusdt,eosusdt", callback)
