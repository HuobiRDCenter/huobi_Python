from huobi.client.trade import TradeClient
from huobi.constant import *

trade_client = TradeClient(api_key=g_api_key,
                           secret_key=g_secret_key)

result = trade_client.post_order_auto_place(symbol="btcusdt", account_id="31253990", amount="0",
                                            source="super-margin-web", type_="buy-market", trade_purpose="2",
                                            market_amount="10")
result.print_object()
