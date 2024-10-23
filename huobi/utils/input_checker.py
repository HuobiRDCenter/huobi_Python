import re
import time
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.constant.definition import *

reg_ex = "[ _`~!@#$%^&*()+=|{}':;',\\[\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？]|\n|\t"


def check_symbol(symbol):
    if not isinstance(symbol, str):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] symbol must be string")
    if re.match(reg_ex, symbol):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + symbol + "  is invalid symbol")


def check_time_in_force(time_in_force, order_type):
    if time_in_force is None:
        return

    if order_type in [OrderType.BUY_MARKET, OrderType.SELL_MARKET] \
            and time_in_force in [TimeInForceType.GTC, TimeInForceType.BOC, TimeInForceType.FOK]:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] timeInForce not supported for market order")


def check_symbol_list(symbols):
    if not isinstance(symbols, list):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] symbols in subscription is not a list")
    for symbol in symbols:
        check_symbol(symbol)


def check_currency(currency):
    if not isinstance(currency, str):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] currency must be string")
    if re.match(reg_ex, currency) is not None:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + currency + "  is invalid currency")


def check_range(value, min_value, max_value, name):
    if value is None:
        return
    if min_value > value or value > max_value:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR,
                                "[Input] " + name + " is out of bound. " + str(value) + " is not in [" + str(
                                    min_value) + "," + str(max_value) + "]")


def check_should_not_none(value, name):
    if value is None:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + name + " should not be null")


def check_should_none(value, name):
    if value is not None:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + name + " should be null")


def check_in_list(value, list_configed, name):
    if (value is not None) and (value not in list_configed):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR,
                                "[Input] " + name + " should be one in " + (",".join(list_configed)))


def check_list(list_value, min_value, max_value, name):
    if list_value is None:
        return
    if len(list_value) > max_value:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR,
                                "[Input] " + name + " is out of bound, the max size is " + str(max_value))
    if len(list_value) < min_value:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR,
                                "[Input] " + name + " should contain " + str(min_value) + " item(s) at least")


def greater_or_equal(value, base, name):
    if value is not None and value < base:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR,
                                "[Input] " + name + " should be greater than " + base)


def format_date(value, name):
    if value is None:
        return None
    if not isinstance(value, str):
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + name + " must be string")
    try:
        new_time = time.strptime(value, "%Y-%m-%d")
        return time.strftime("%Y-%m-%d", new_time)
    except:
        raise HuobiApiException(HuobiApiException.INPUT_ERROR, "[Input] " + name + " is not invalid date format")
