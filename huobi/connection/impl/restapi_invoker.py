import requests
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.utils.etf_result import etf_result_check
from huobi.utils import *
import time

from huobi.utils.print_mix_object import TypeCheck

session = requests.Session()

def check_response(dict_data):
    status = dict_data.get("status", None)
    code = dict_data.get("code", None)
    success = dict_data.get("success", None)
    if status and len(status):
        if TypeCheck.is_basic(status): # for normal case
            if status == "error":
                err_code = dict_data.get("err-code", 0)
                err_msg = dict_data.get("err-msg", "")
                raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                        "[Executing] " + str(err_code) + ": " + err_msg)
            elif status != "ok":
                raise HuobiApiException(HuobiApiException.RUNTIME_ERROR,
                                        "[Invoking] Response is not expected: " + status)
        elif TypeCheck.is_dict(status): # for https://status.huobigroup.com/api/v2/summary.json in example example/generic/get_system_status.py
            if dict_data.get("page") and dict_data.get("components"):
                pass
            else:
                raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                        "[Executing] System is in maintenances")
    elif code:
        code_int = int(code)
        if code_int != 200:
            err_code = dict_data.get("code", 0)
            err_msg = dict_data.get("message", "")
            raise HuobiApiException(HuobiApiException.EXEC_ERROR,
                                    "[Executing] " + str(err_code) + ": " + err_msg)
    elif success is not None:
        if bool(success) is False:
            err_code = etf_result_check(dict_data.get("code"))
            err_msg = dict_data.get("message", "")
            if err_code == "":
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + err_msg)
            else:
                raise HuobiApiException(HuobiApiException.EXEC_ERROR, "[Executing] " + str(err_code) + ": " + err_msg)
    else:
        raise HuobiApiException(HuobiApiException.RUNTIME_ERROR, "[Invoking] Status cannot be found in response.")


def call_sync(request, is_checked=False):
    if request.method == "GET":
        # print("call_sync url : " , request.host + request.url)
        response = session.get(request.host + request.url, headers=request.header)
        if is_checked is True:
            return response.text
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        check_response(dict_data)
        return request.json_parser(dict_data)

    elif request.method == "POST":
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        check_response(dict_data)
        return request.json_parser(dict_data)

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
            return response.text
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        check_response(dict_data)
        return request.json_parser(dict_data), req_cost, cost_manual

    elif request.method == "POST":
        inner_start_time = time.time()
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        inner_end_time = time.time()
        cost_manual = round(inner_end_time - inner_start_time, 6)
        req_cost = response.elapsed.total_seconds()
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        check_response(dict_data)
        return request.json_parser(dict_data), req_cost, cost_manual
