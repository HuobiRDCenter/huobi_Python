import base64
import datetime
import urllib
from urllib import parse

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from huobi.exception.huobi_api_exception import HuobiApiException


def create_signatureED25519(api_key, secret_key, method, url, builder):
    if api_key is None or secret_key is None or api_key == "" or secret_key == "":
        raise HuobiApiException(HuobiApiException.KEY_MISSING, "API key and secret key are required")
    timestamp = utc_now()
    builder.put_url("AccessKeyId", api_key)

    builder.put_url("SignatureMethod", "Ed25519")
    builder.put_url("SignatureVersion", "2")
    builder.put_url("Timestamp", timestamp)
    host = urllib.parse.urlparse(url).hostname
    path = urllib.parse.urlparse(url).path
    # 对参数进行排序
    keys = sorted(builder.param_map.keys())
    # keys=['AccessKeyId','SignatureMethod','SignatureVersion','Timestamp']
    # 加入&
    qs0 = '&'.join(['%s=%s' % (key, parse.quote(builder.param_map[key], safe='')) for key in keys])
    # 请求方法，域名，路径，参数后加入`\n`
    payload0 = '%s\n%s\n%s\n%s' % (method, host, path, qs0)

    private_key_bytes = secret_key.encode('utf-8')
    private_key = load_pem_private_key(data=private_key_bytes, password=None, backend=default_backend())
    # 生成签名
    signature = private_key.sign(payload0.encode('ASCII'))
    # 进行 base64 编码
    s = base64.b64encode(signature).decode('utf-8')
    builder.put_url("Signature", s)


def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
