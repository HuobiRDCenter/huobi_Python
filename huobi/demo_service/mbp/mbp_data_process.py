#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
from huobi import SubscriptionClient
from huobi.model import *


class MbpDataFormat:
    symbol = ""
    level = 0
    sub_mbp_obj_list = []
    sub_mbp_pre_seq_list = []
    flag_enter_req = False  # need call request to get the first batch data
    flag_done = False   # the request data match with subscribe data, after matched, this flag can't be changed again
    req_mbp_base_obj = None  # one request data cache at the match point
    sub_mbp_cache_pre = None # base on req_mbp_base_obj and update by sub_mbp_event by each receive


    @staticmethod
    def set_request_symbol_level(symbol, level):
        """
        for input params
        """
        MbpDataFormat.symbol = symbol
        MbpDataFormat.level = level

    @staticmethod
    def reset_variables():
        MbpDataFormat.sub_mbp_obj_list = []
        MbpDataFormat.sub_mbp_pre_seq_list = []
        MbpDataFormat.flag_enter_req = False
        MbpDataFormat.flag_done = False
        MbpDataFormat.req_mbp_base_obj = None
        MbpDataFormat.sub_mbp_cache_pre = None


    @staticmethod
    def transfer_req_to_sub(req: 'MbpRequest'):
        """
        transfter MbpRequest to MbpEvent
        """
        sub = MbpEvent()
        sub.symbol = req.symbol
        sub.data = req.data
        return sub

    @staticmethod
    def format_as_price_amount(list_data):
        """
        transfer list<DepthEntry> as list<{price:amount}> for data search and merge
        :param list_data:
        :return:
        """
        price_amount_dict = {}
        if list_data and len(list_data):
            for row in list_data:  # row type is DepthEntry
                price_amount_dict[row.price] = row.amount
        return price_amount_dict

    @staticmethod
    def update_depth(old_list, new_list):
        """
        merge bids or asks data
        1. update amount when price exist in old_list
        2. add amount when price not exist in old_list
        3. delete price when amount is 0
        :param old_list: list<DepthEntry> can be asks or bids
        :param new_list: list<DepthEntry> can be asks or bids
        :return:
        """
        if len(old_list) == 0:
            return new_list

        if len(new_list) == 0:
            return old_list

        new_price_amount_dict = MbpDataFormat.format_as_price_amount(new_list)
        merged_list = []

        if len(old_list):
            for old_row in old_list:  # old_row type is DepthEntry
                old_price_tmp = old_row.price
                if (old_price_tmp in new_price_amount_dict):
                    if (new_price_amount_dict[old_price_tmp]):  # modify price&amount
                        tmp = DepthEntry()
                        tmp.price = old_price_tmp
                        tmp.amount = new_price_amount_dict[old_price_tmp]
                        merged_list.append(tmp)
                    else:
                        pass  # delete price&amount
                    del new_price_amount_dict[old_price_tmp]
                else:
                    merged_list.append(old_row)

        if len(new_price_amount_dict):
            for idx_price, idx_amount in new_price_amount_dict.items():
                if idx_amount:
                    tmp = DepthEntry()
                    tmp.price = idx_price
                    tmp.amount = idx_amount
                    merged_list.append(tmp)  # add price&amount

        return merged_list

    @staticmethod
    def update_depth_remove_amount_zero(old_list, new_list):
        """
        remove the DepthEntry.amount = 0 from merge_list
        :param old_list:
        :param new_list:
        :return:
        """
        merge_list = MbpDataFormat.update_depth(old_list, new_list)
        new_list = []
        if len(merge_list):
            for idx, row in enumerate(merge_list):
                if row.amount:
                    new_list.append(row)

        return new_list

    @staticmethod
    def data_merge(base: 'MbpEvent', sub: 'MbpEvent'):
        """
        merge asks and bids from sub(MbpEvent) to base(MbpEvent)
        merge rule see function update_depth
        :param base:
        :param sub:
        :return:
        """
        merged = MbpEvent()
        merged.data.seqNum = sub.data.seqNum
        merged.data.prevSeqNum = sub.data.prevSeqNum
        bids = MbpDataFormat.update_depth_remove_amount_zero(base.data.bids, sub.data.bids)
        asks = MbpDataFormat.update_depth_remove_amount_zero(base.data.asks, sub.data.asks)
        if len(bids):
            merged.data.bids = sorted(bids, key=lambda e: getattr(e, "price"), reverse=True)

        if len(asks):
            merged.data.asks = sorted(asks, key=lambda e: getattr(e, "price"), reverse=False)

        return merged

    @staticmethod
    def format_subscribe(mbp_event:'MbpEvent'):
        """
        call function for subscribe_mbp_event callback
        :param mbp_event:
        :return:
        """
        MbpDataFormat.start_request_mbp()
        formated_data = MbpDataFormat.full_subscribe_data(mbp_event)
        if MbpDataFormat.flag_done == False:
            #print(len(MbpDataFormat.sub_mbp_pre_seq_list), len(MbpDataFormat.sub_mbp_obj_list), MbpDataFormat.sub_mbp_pre_seq_list)
            pass

        return formated_data

    @staticmethod
    def full_subscribe_data(mbp_event: 'MbpEvent'):
        """
        only process MbpEvent data, need more process, see format_subscribe
        :param mbp_event:
        :return:
        """
        if MbpDataFormat.flag_done == False: # only false to cache the data
            MbpDataFormat.sub_mbp_obj_list.append(mbp_event)
            MbpDataFormat.sub_mbp_pre_seq_list.append(mbp_event.data.prevSeqNum)

            if MbpDataFormat.req_mbp_base_obj is not None:
                req_seq_num_tmp = MbpDataFormat.req_mbp_base_obj.data.seqNum
                MbpDataFormat.flag_done = (req_seq_num_tmp in MbpDataFormat.sub_mbp_pre_seq_list)
                if MbpDataFormat.flag_done:
                    #print("****************** Match Request seqNum : ", req_seq_num_tmp)
                    match_index_tmp = MbpDataFormat.sub_mbp_pre_seq_list.index(req_seq_num_tmp)
                    tmp_sub_mbp_pre_seq_list = MbpDataFormat.sub_mbp_pre_seq_list[match_index_tmp:]
                    tmp_sub_mbp_obj_list = MbpDataFormat.sub_mbp_obj_list[match_index_tmp:]
                    MbpDataFormat.sub_mbp_cache_pre = MbpDataFormat.transfer_req_to_sub(MbpDataFormat.req_mbp_base_obj)
                    #PrintMbp.print_mbp_sub(MbpDataFormat.sub_mbp_cache_pre)
                    if len(tmp_sub_mbp_obj_list):  # add by seq to sub_mbp_cache_pre
                        for row_mbp_event in tmp_sub_mbp_obj_list:
                            MbpDataFormat.sub_mbp_cache_pre = MbpDataFormat.data_merge(MbpDataFormat.sub_mbp_cache_pre, row_mbp_event)

                    MbpDataFormat.sub_mbp_pre_seq_list = []  # clear the queue
                    MbpDataFormat.sub_mbp_obj_list = []      # clear the queue

                    return MbpDataFormat.sub_mbp_cache_pre
                else:
                    #print("******************", len(MbpDataFormat.sub_mbp_pre_seq_list), req_seq_num_tmp, MbpDataFormat.sub_mbp_pre_seq_list[-1])
                    if req_seq_num_tmp < MbpDataFormat.sub_mbp_pre_seq_list[-1]:
                        #print("<first>Error happened for missmatch data : ", req_seq_num_tmp)
                        MbpDataFormat.reset_variables()
                    else:
                        #print("****************** continue wait")
                        pass

                return None  # invalid data, discard

        else:
            if MbpDataFormat.sub_mbp_cache_pre.data.seqNum != mbp_event.data.prevSeqNum:  # the seq number mismatch and request again
                print("<second>Error happened for missmatch data : ", MbpDataFormat.sub_mbp_cache_pre.data.seqNum, mbp_event.data.prevSeqNum)
                MbpDataFormat.reset_variables()
                return None

            MbpDataFormat.sub_mbp_cache_pre = MbpDataFormat.data_merge(MbpDataFormat.sub_mbp_cache_pre, mbp_event)
            return MbpDataFormat.sub_mbp_cache_pre

    @staticmethod
    def start_request_mbp():
        """
        need request_mbp_event request to get bids 150 and asks 150 data information
        :return:
        """
        if (MbpDataFormat.flag_enter_req == False):
            MbpDataFormat.flag_enter_req = True

            def request_callback(mbp_req: 'MbpRequest'):
                mbp = mbp_req.data
                print("===== Request seqNum : ", mbp.seqNum, "prevSeqNum", mbp.prevSeqNum)

                MbpDataFormat.req_mbp_base_obj = mbp_req

            def request_error(e: 'HuobiApiException'):
                print(e.error_code + e.error_message)

            sub_client_local = SubscriptionClient()
            sub_client_local.request_mbp_event(MbpDataFormat.symbol, MbpDataFormat.level, request_callback, request_error)





