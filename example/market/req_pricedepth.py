
from huobi.client.market import MarketClient
from huobi.constant import DepthStep
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market import PriceDepthReq


def callback(price_depth_req: 'PriceDepthReq'):
    price_depth_req.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client = MarketClient()
sub_client.req_pricedepth("btcusdt", DepthStep.STEP0, callback, error)
