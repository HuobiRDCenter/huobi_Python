- Python signature code and demo

```
import base64
import hashlib
import hmac
import datetime
from urllib import parse
import urllib.parse
import json


def print_builder(builder):
    print("params in builder", builder.param_map)
    print("params in builder build_urls", builder.build_url())


class UrlParamsBuilder(object):

    def __init__(self):
        self.param_map = dict()
        self.post_map = dict()

    def put_url(self, name, value):
        if value is not None:
            if isinstance(value, list):
                self.param_map[name] = value
            else:
                self.param_map[name] = str(value)

    def put_post(self, name, value):
        if value is not None:
            if isinstance(value, list):
                self.post_map[name] = value
            else:
                self.post_map[name] = str(value)

    def build_url(self):
        if len(self.param_map) == 0:
            return ""
        encoded_param = urllib.parse.urlencode(self.param_map)
        return "?" + encoded_param

    def build_url_to_json(self):
        return json.dumps(self.param_map)

def create_signature(api_key, secret_key, method, url, builder):
    ret = {
        "code" : 0,
        "message" : ""
    }
    if api_key is None or secret_key is None or api_key == "" or secret_key == "":
        ret["code"] = -1
        ret["message"] = "API key and secret key are required"
        return ret

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
    return ret


def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')


if __name__ == "__main__":
    api_key_test = "api_key_xxxxxxx"
    secret_key_test = "secret_key_xxxxxxx"
    method_test = "GET"
    url_test = "www.huobi.pro"

    builder = UrlParamsBuilder()
    builder.put_url("symbol", "usdtbtc")
    builder.put_url("types", "market,limit,margin")
    create_signature(api_key=api_key_test, secret_key=secret_key_test, method=method_test, url=url_test, builder=builder)
    print_builder(builder)
```