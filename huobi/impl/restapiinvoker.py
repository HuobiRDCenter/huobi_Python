import requests
import time
from huobi.exception.huobiapiexception import HuobiApiException
from huobi.impl.utils.etfresult import etf_result_check
from huobi.impl.utils import *

session = requests.Session()

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
    elif json_wrapper.contain_key("code"):
        code = json_wrapper.get_int("code")
        if code != 200:
            err_msg = json_wrapper.get_string_or_default("message", "")
            raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + str(code) + ": " + err_msg)
    else:
        raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Status cannot be found in response.")


def call_sync(request, is_checked=False):
    if request.method == "GET":
        # print("call_sync url : " , request.host + request.url)
        response = session.get(request.host + request.url, headers=request.header)
        # print("receive data : " + response.text)
        if is_checked is True:
            return response.text
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)
    elif request.method == "POST":
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        # print("receive data : " + response.text)
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)

def call_sync_perforence_test(request, is_checked=False):
    if request.method == "GET":
        inner_start_time = time.time()
        # print("call_sync_perforence_test url : ", request.host + request.url)
        response = session.get(request.host + request.url, headers=request.header)
        #print("call_sync_perforence_test data :", response.text)
        inner_end_time = time.time()
        cost_manual = round(inner_end_time - inner_start_time, 6)
        req_cost = response.elapsed.total_seconds()
        if is_checked is True:
            return response.text, req_cost, cost_manual
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper), req_cost, cost_manual
    elif request.method == "POST":
        inner_start_time = time.time()
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        inner_end_time = time.time()
        cost_manual = round(inner_end_time - inner_start_time, 6)
        req_cost = response.elapsed.total_seconds()
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper), req_cost, cost_manual

