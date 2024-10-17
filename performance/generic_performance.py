from huobi.client.generic import GenericClient
from huobi.model.generic import ExchangeInfo


class GenericClientPerformance(GenericClient):

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
        super(GenericClientPerformance, self).__init__(**self.__kwargs)

    def get_exchange_info(self) -> ExchangeInfo:
        """
        Get all the trading assets and currencies supported in huobi.
        The information of trading instrument, including base currency, quote precision, etc.

        :return: The information of trading instrument and currencies.
        """

        ret = ExchangeInfo()
        ret.symbol_list, req_cost_1, cost_manual_1  = self.get_exchange_symbols()
        ret.currencies, req_cost_2, cost_manual_2 = self.get_exchange_currencies()
        return ret, req_cost_1 + req_cost_2, cost_manual_1 + cost_manual_2


if __name__ == "__main__":
    generic_client = GenericClientPerformance()
    list_obj, req_cost, cost_manual = generic_client.get_exchange_info()

    print(len(list_obj.symbol_list), req_cost, cost_manual)

    # generic_client = GenericClient(performance_test=True)
    # list_obj, req_cost, cost_manual = generic_client.get_exchange_symbols()
    #
    # print(len(list_obj), req_cost, cost_manual)

