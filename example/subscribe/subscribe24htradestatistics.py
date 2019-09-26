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
    trade_statistics_event.print_object()
    print()


sub_client.subscribe_24h_trade_statistics_event("btcusdt", callback)
