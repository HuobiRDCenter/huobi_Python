import logging
from huobi import SubscriptionClient
from huobi.model import *

logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(trade_statistics_event: 'TradeStatisticsEvent'):
    print("Timestamp: " + str(trade_statistics_event.trade_statistics.timestamp))
    print("High: " + str(trade_statistics_event.trade_statistics.high))
    print("Low: " + str(trade_statistics_event.trade_statistics.low))
    print("Open: " + str(trade_statistics_event.trade_statistics.open))
    print("Close: " + str(trade_statistics_event.trade_statistics.close))
    print("Volume: " + str(trade_statistics_event.trade_statistics.volume))


sub_client.subscribe_24h_trade_statistics_event("btcusdt", callback)
