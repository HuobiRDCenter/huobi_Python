from huobi import RequestClient

request_client = RequestClient()

trade_statistics = request_client.get_24h_trade_statistics("btcusdt")
trade_statistics.print_object()

