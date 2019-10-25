import requests
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.utils.etf_result import etf_result_check
from huobi.utils import *


def check_response(dict_data):
    status = dict_data.get("status", None)
    code = dict_data.get("code", None)
    success = dict_data.get("success", None)
    if status and len(status):
        if status == "error":
            err_code = dict_data.get("err-code", "")
            err_msg = dict_data.get("err-msg", "")
            raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                    "[Executing] " + err_code + ": " + err_msg)
        elif status != "ok":
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Response is not expected: " + status)
    elif code:
        code_int = int(code)
        if code_int != 200:
            err_code = dict_data.get("code", "")
            err_msg = dict_data.get("message", "")
            raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                    "[Executing] " + err_code + ": " + err_msg)
    elif success is not None:
        if bool(success) is False:
            err_code = etf_result_check(dict_data.get("code"))
            err_msg = dict_data.get("message", "")
            if err_code == "":
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + err_msg)
            else:
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + err_code + ": " + err_msg)
    else:
        raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Status cannot be found in response.")


def call_sync(request):
    if request.method == "GET":
        print("=========host=========", request.host)
        print("=========url=========", request.url)
        print("=========header=========", request.header)
        response = requests.get(request.host + request.url, headers=request.header)
        dict_data = json.loads(response.text, encoding="utf-8")
        print("call_sync  === recv data : ", dict_data)
        return request.json_parser(dict_data)


    elif request.method == "POST":
        response = requests.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        dict_data = json.loads(response.text, encoding="utf-8")
        print("call_sync  === recv data : ", dict_data)
        check_response(dict_data)
        return request.json_parser(dict_data)

