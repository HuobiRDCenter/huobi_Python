from huobi.client.market import MarketClient
from huobi.constant import *



def callback(trade_req: 'TradeDetailReq'):
    print("---- trade_event:  ----")
    trade_req.print_object()
    print()



market_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN)
market_client.req_trade_detail("btcusdt,eosusdt", callback)


