import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl



data = '''
{
	"status": "ok",
	"data": [{
		"base-currency": "btc",
		"quote-currency": "usdt",
		"price-precision": 2,
		"amount-precision": 4,
		"symbol-partition": "main",
		"symbol": "btcusdt",
		"state":"online",
		"value-precision":12,
		"min-order-amt":10,
		"max-order-amt":200,
		"min-order-value":1,
		"leverage-ratio":2
	}, {
		"base-currency": "bch",
		"quote-currency": "usdt",
		"price-precision": 3,
		"amount-precision": 5,
		"symbol-partition": "main",
		"symbol": "bchusdt",
		"state":"online",
		"value-precision":12,
		"min-order-amt":10,
		"max-order-amt":200,
		"min-order-value":1,
		"leverage-ratio":2
	}]
}'''

class TestGetSymbols(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_symbols()
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/common/symbols") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_symbols()
        symbol_list = request.json_parser(parse_json_from_string(data))
        self.assertEqual(2, len(symbol_list))
        self.assertEqual("btcusdt", symbol_list[0].symbol)
        self.assertEqual("btc", symbol_list[0].base_currency)
        self.assertEqual("usdt", symbol_list[0].quote_currency)
        self.assertEqual(2, symbol_list[0].price_precision)
        self.assertEqual(4, symbol_list[0].amount_precision)
        self.assertEqual("main", symbol_list[0].symbol_partition)

        self.assertEqual("bchusdt", symbol_list[1].symbol)
        self.assertEqual("bch", symbol_list[1].base_currency)
        self.assertEqual("usdt", symbol_list[1].quote_currency)
        self.assertEqual(3, symbol_list[1].price_precision)
        self.assertEqual(5, symbol_list[1].amount_precision)
        self.assertEqual("main", symbol_list[1].symbol_partition)
