

class CommonCurrencies:

    def __init__(self):
        self.cc = ""
        self.dn = ""
        self.fn = ""
        self.at = 0
        self.wp = 0
        self.ft = ""
        self.dma = ""
        self.wma = ""
        self.sp = ""
        self.w = 0
        self.qc = None
        self.state = ""
        self.v = None
        self.whe = None
        self.cd = None
        self.de = None
        self.wed = None
        self.cawt = None
        self.fc = 0
        self.sc = 0
        self.swd = ""
        self.wd = ""
        self.sdd = ""
        self.dd = ""
        self.svd = ""
        self.tags = ""


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.cc, format_data + "cc")
        PrintBasic.print_basic(self.dn, format_data + "dn")
        PrintBasic.print_basic(self.fn, format_data + "fn")
        PrintBasic.print_basic(self.at, format_data + "at")
        PrintBasic.print_basic(self.wp, format_data + "wp")
        PrintBasic.print_basic(self.ft, format_data + "ft")
        PrintBasic.print_basic(self.dma, format_data + "dma")
        PrintBasic.print_basic(self.wma, format_data + "wma")
        PrintBasic.print_basic(self.sp, format_data + "sp")
        PrintBasic.print_basic(self.w, format_data + "w")
        PrintBasic.print_basic(self.qc, format_data + "qc")
        PrintBasic.print_basic(self.state, format_data + "state")
        PrintBasic.print_basic(self.v, format_data + "v")
        PrintBasic.print_basic(self.whe, format_data + "whe")
        PrintBasic.print_basic(self.cd, format_data + "cd")
        PrintBasic.print_basic(self.de, format_data + "de")
        PrintBasic.print_basic(self.wed, format_data + "wed")
        PrintBasic.print_basic(self.cawt, format_data + "cawt")
        PrintBasic.print_basic(self.fc, format_data + "fc")
        PrintBasic.print_basic(self.sc, format_data + "sc")
        PrintBasic.print_basic(self.swd, format_data + "swd")
        PrintBasic.print_basic(self.wd, format_data + "wd")
        PrintBasic.print_basic(self.sdd, format_data + "sdd")
        PrintBasic.print_basic(self.dd, format_data + "dd")
        PrintBasic.print_basic(self.svd, format_data + "svd")
        PrintBasic.print_basic(self.tags, format_data + "tags")


