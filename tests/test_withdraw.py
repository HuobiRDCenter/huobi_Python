import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.exception.huobiapiexception import HuobiApiException

data = '''
{
"status": "ok",
"data": 1000
}
'''

class TestWithdraw(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.withdraw("0xde709f2102306220921060314715629080e2fb77", 0.05, "eth", 1.0, "aaa")
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("Signature") != -1)
        self.assertEqual("0xde709f2102306220921060314715629080e2fb77", request.post_body["address"])
        self.assertEqual("eth", request.post_body["currency"])
        self.assertEqual("0.05", request.post_body["amount"])
        self.assertEqual("1.0", request.post_body["fee"])
        self.assertEqual("aaa", request.post_body["addr-tag"])

    def test_result(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.withdraw("0xde709f2102306220921060314715629080e2fb77", 0.05, "eth", 1.0, "aaa")
        id = request.json_parser(parse_json_from_string(data))
        self.assertEqual(1000, id)
