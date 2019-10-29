import unittest
import huobi
from unittest import mock
from huobi.utils import *



class TestApi(unittest.TestCase):
    def test_request(self):
        builder = UrlParamsBuilder()
        huobi.utils.api_signature.utc_now = mock.Mock(return_value="123")
        create_signature("123", "456", "GET",  "http://host/url", builder)
        self.assertEqual("?AccessKeyId=123&SignatureVersion=2&SignatureMethod=HmacSHA256&Timestamp=123&Signature=Hhiaq8xYQPiBZOyWV37MdQutLo4f0ZOHiJtG3p%2BnILc%3D", builder.build_url())
        return


if __name__ == "__main__":
    unittest.main()