import base64
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

import huobi
from unittest import mock
from huobi.utils import *
from huobi.utils.api_signature_ED25519 import create_signatureED25519


class TestApi(unittest.TestCase):
    def test_request(self):
        builder = UrlParamsBuilder()
        huobi.utils.api_signature.utc_now = mock.Mock(return_value="123")
        create_signature("123", "456", "GET", "http://host/url", builder)
        self.assertEqual(
            "?AccessKeyId=123&SignatureVersion=2&SignatureMethod=HmacSHA256&Timestamp=123&Signature=Hhiaq8xYQPiBZOyWV37MdQutLo4f0ZOHiJtG3p%2BnILc%3D",
            builder.build_url())
        return

    def test_request3(self):
        builder = UrlParamsBuilder()
        # Mock utc_now() 方法返回固定时间
        huobi.utils.api_signature_ED25519.utc_now = mock.Mock(return_value="123")
        # Base64 编码
        private_key_b64 = (
            "Ed25519私钥"
        )
        # 调用 create_signature3 方法
        create_signatureED25519("123", private_key_b64, "GET", "http://host/url", builder)
        # 使用从上一步捕获的实际签名
        expected_signature = "69h62vchDx8Nml8bPgBHLZY2GiVesY4ayKau6FOXKWz9QMLfE1l869XyX0d4T%2BGmOBkRfE43almvByRamG50Cw%3D%3D"  # 请替换为实际的签名
        expected_url = f"?AccessKeyId=123&SignatureVersion=2&SignatureMethod=ED25519&Timestamp=123&Signature={expected_signature}"
        # 检查生成的 URL 是否符合预期
        self.assertEqual(expected_url, builder.build_url())


if __name__ == "__main__":
    unittest.main()
