from huobi.client.market import MarketClient
from huobi.constant import DepthStep
from huobi.model.market import PriceDepth
from huobi.utils.input_checker import *


class MarketClientPerformance(MarketClient):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """

        self.__kwargs = kwargs
        self.__kwargs["performance_test"] = True
        super(MarketClientPerformance, self).__init__(**self.__kwargs)

    def get_pricedepth(self, symbol: 'str', depth_type: 'str', depth_size: 'int' = None) -> PriceDepth:
        """
        Get the Market Depth of a symbol.

        :param symbol: The symbol, like "btcusdt". (mandatory)
        :param depth_type: The tpye, like "step0" to "step5". (mandatory)
        :param depth_size(optional): The maximum number of Market Depth step0 requested. range [1 - 150], default is 150
                           The maximum number of Market Depth step1,step2,step3,step4,step5 requested. size is in [5, 10, 20], default is 20.
        :return: Market Depth data.
        """

        check_symbol(symbol)
        check_in_list(depth_type, [DepthStep.STEP0, DepthStep.STEP1, DepthStep.STEP2, DepthStep.STEP3, DepthStep.STEP4,
                                   DepthStep.STEP5], "depth_type")
        params = {
            "symbol": symbol,
            "type": depth_type,
            # "depth": depth_size
        }

        from huobi.service.market.get_pricedepth import GetPriceDepthService
        ret_data, req_cost, cost_manual = GetPriceDepthService(params).request(**self.__kwargs)

        if depth_size is not None:
            if (ret_data.bids is not None) and (len(ret_data.bids) > depth_size):
                ret_data.bids = ret_data.bids[0:depth_size]

            if (ret_data.asks is not None) and (len(ret_data.asks) > depth_size):
                ret_data.asks = ret_data.asks[0:depth_size]

        return ret_data, req_cost, cost_manual

