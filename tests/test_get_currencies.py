import unittest
from huobi.impl.utils import *
from huobi.model.constant import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl


data = '''
{
    "status": "ok",
    "data": ["hb10", "usdt", "btc", "bch"]
}
'''

class TestGetCurrencies(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_currencies()
        self.assertEqual("GET", request.method)
        self.assertTrue(request.url.find("/v1/common/currencys") != -1)

    def test_result(self):
        impl = RestApiRequestImpl("", "")
        request = impl.get_currencies()
        currencies = request.json_parser(parse_json_from_string(data))
        self.assertEqual(4, len(currencies))
        self.assertEqual("hb10", currencies[0])
        self.assertEqual("usdt", currencies[1])
        self.assertEqual("btc", currencies[2])
