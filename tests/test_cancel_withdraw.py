import unittest
from huobi.impl.utils import *
from huobi.model import *
from huobi.impl.restapirequestimpl import RestApiRequestImpl

from huobi.impl.restapirequestimpl import account_info_map
from huobi.exception.huobiapiexception import HuobiApiException


class TestCancelWithdraw(unittest.TestCase):
    def test_request(self):
        impl = RestApiRequestImpl("12345", "67890")
        request = impl.cancel_withdraw("htbtc", 12345)
        path = "/v1/dw/withdraw-virtual/{}/cancel"
        path = path.format("12345")
        self.assertEqual("POST", request.method)
        self.assertTrue(request.url.find(path) != -1)
        self.assertTrue(request.url.find("Signature") != -1)
