import unittest
import json
from huobi.model import *
from huobi.impl.utils import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.impl.restapiinvoker import check_response
from huobi.exception.huobiapiexception import HuobiApiException


data = '''
{
    "code": 200,
    "data": null,
    "message": null,
    "success": true
}
'''

class TestEtfSwap(unittest.TestCase):
    def test_request_in(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.etf_swap("hb10", 123, EtfSwapType.IN)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("/etf/swap/in") != -1)
        self.assertEqual("hb10", request.post_body["etf_name"])
        self.assertEqual("123", request.post_body["amount"])

    def test_request_out(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.etf_swap("hb10", 345, EtfSwapType.OUT)
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find("/etf/swap/out") != -1)
        self.assertEqual("hb10", request.post_body["etf_name"])
        self.assertEqual("345", request.post_body["amount"])
