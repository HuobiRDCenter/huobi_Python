import requests
from huobi.exception.huobiapiexception import HuobiApiException
from huobi.impl.utils.etfresult import etf_result_check
from huobi.impl.utils import *


def check_response(json_wrapper):
    if json_wrapper.contain_key("status"):
        status = json_wrapper.get_string("status")
        if status == "error":
            err_code = json_wrapper.get_string("err-code")
            err_msg = json_wrapper.get_string("err-msg")
            raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                    "[Executing] " + err_code + ": " + err_msg)
        elif status != "ok":
            raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Response is not expected: " + status)
    elif json_wrapper.contain_key("success"):
        success = json_wrapper.get_boolean("success")
        if success is False:
            err_code = etf_result_check(json_wrapper.get_int("code"))
            err_msg = json_wrapper.get_string("message")
            if err_code == "":
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + err_msg)
            else:
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + err_code + ": " + err_msg)
    else:
        raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Status cannot be found in response.")


def call_sync(request):
    if request.method == "GET":
        response = requests.get(request.host + request.url, headers=request.header)
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)
    elif request.method == "POST":
        response = requests.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)

