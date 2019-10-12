import unittest
import huobi
from unittest import mock
from huobi.impl.utils.apisignature import create_signature
from huobi.impl.utils.apisignature import utc_now
from huobi.impl.utils.urlparamsbuilder import UrlParamsBuilder



class TestApi(unittest.TestCase):
    def test_request(self):
        builder = UrlParamsBuilder()
        huobi.impl.utils.apisignature.utc_now = mock.Mock(return_value="123")
        create_signature("123", "456", "GET",  "http://host/url", builder)
        self.assertEqual("?AccessKeyId=123&SignatureVersion=2&SignatureMethod=HmacSHA256&Timestamp=123&Signature=Hhiaq8xYQPiBZOyWV37MdQutLo4f0ZOHiJtG3p%2BnILc%3D", builder.build_url())
        return
