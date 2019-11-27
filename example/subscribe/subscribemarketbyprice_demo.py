#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.demo_service.mbp.mbp_data_process import MbpDataFormat
from huobi.demo_service.mbp.mbp_print import PrintMbp


logger = logging.getLogger("huobi-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)



"""
README: user can add data process in user_def_function function.
MbpDataFormat : get all 150 bids and 150 asks, and append increased subscribe data
                MbpDataFormat.format_subscribe format the request data and subscribe data, give user latest all 150 bids and 150 asks and seqNum
"""

def user_def_function(mbp_event:'MbpEvent'):
    """
    user defination function in callback
    :param mbp_event:
    :return:
    """
    if mbp_event is None:  # need check None
        return

    mbp = mbp_event.data
    print("Subscribe seqNum : ", mbp.seqNum, "prevSeqNum", mbp.prevSeqNum, "bids size", len(mbp.bids), "asks size", len(mbp.asks))
    PrintMbp.print_mbp_sub(mbp_event)
    """
    user add process code here!
    """
    return


def sub_callback(mbp_event: 'MbpEvent'):
    formated_mbp_event = MbpDataFormat.format_subscribe(mbp_event)
    user_def_function(formated_mbp_event)



def sub_error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)



if __name__ == '__main__':

    symbol = "btcusdt"
    level = MbpLevel.MBP150

    MbpDataFormat.set_request_symbol_level(symbol, level)
    sub_client = SubscriptionClient()
    sub_client.subscribe_mbp_event(symbol, level, sub_callback, sub_error)





