import base64
import hashlib
import hmac
import datetime
from urllib import parse
import urllib.parse
from huobi.exception.huobi_api_exception import HuobiApiException


def create_signature(api_key, secret_key, method, url, builder):
    if api_key is None or secret_key is None or api_key == "" or secret_key == "":
        raise HuobiApiException(HuobiApiException.KEY_MISSING,  "API key and secret key are required")

    timestamp = utc_now()
    builder.put_url("AccessKeyId", api_key)
    builder.put_url("SignatureVersion", "2")
    builder.put_url("SignatureMethod", "HmacSHA256")
    builder.put_url("Timestamp", timestamp)

    host = urllib.parse.urlparse(url).hostname
    path = urllib.parse.urlparse(url).path

    # 对参数进行排序:
    keys = sorted(builder.param_map.keys())
    # 加入&
    qs0 = '&'.join(['%s=%s' % (key, parse.quote(builder.param_map[key], safe='')) for key in keys])
    # 请求方法，域名，路径，参数 后加入`\n`
    payload0 = '%s\n%s\n%s\n%s' % (method, host, path, qs0)
    dig = hmac.new(secret_key.encode('utf-8'), msg=payload0.encode('utf-8'), digestmod=hashlib.sha256).digest()
    # 进行base64编码
    s = base64.b64encode(dig).decode()
    builder.put_url("Signature", s)


def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
