#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
from huobi import SubscriptionClient
from huobi.model import *
from huobi.base.printobject import *


class PrintMbp:
    @staticmethod
    def print_mbp(mbp: 'Mbp'):
        print("seqNum: ", mbp.seqNum)
        print("prevSeqNum : ", mbp.prevSeqNum)
        print("Bid number :", len(mbp.bids))
        print("Asks number :", len(mbp.asks))
        for entry in mbp.bids:
            print("Bids: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

        for entry in mbp.asks:
            print("Asks: " + " price: " + str(entry.price) + ", amount: " + str(entry.amount))

        print()

    @staticmethod
    def print_mbp_req(mbp_req_obj: 'MbpRequest'):
        print("---- req:  ----")
        PrintBasic.print_basic(mbp_req_obj.symbol, "Symbol")
        PrintBasic.print_basic(mbp_req_obj.rep, "Timestamp")
        PrintBasic.print_basic(mbp_req_obj.id, "Client Req ID")
        PrintMbp.print_mbp(mbp_req_obj.data)
        print()

    @staticmethod
    def print_mbp_sub(mbp_sub_obj: 'MbpEvent'):
        print("---- sub:  ----")
        PrintBasic.print_basic(mbp_sub_obj.symbol, "Symbol")
        PrintBasic.print_basic(mbp_sub_obj.ch, "Channel")
        PrintBasic.print_basic(mbp_sub_obj.ts, "Time")
        PrintMbp.print_mbp(mbp_sub_obj.data)
        print()






