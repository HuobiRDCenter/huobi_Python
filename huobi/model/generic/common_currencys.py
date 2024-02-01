

class CommonCurrencys:

    def __init__(self):
        self.name = ""
        self.dn = ""
        self.vat = 0
        self.det = 0
        self.wet = 0
        self.wp = 0
        self.ct = ""
        self.cp = ""
        self.ss = []
        self.oe = 0
        self.dma = ""
        self.wma = ""
        self.sp = ""
        self.w = ""
        self.qc = None
        self.state = ""
        self.v = None
        self.whe = None
        self.cd = None
        self.de = None
        self.we = None
        self.cawt = None
        self.cao = None
        self.fc = 0
        self.sc = 0
        self.swd = ""
        self.wd = ""
        self.sdd = ""
        self.dd = ""
        self.svd = ""
        self.tags = ""
        self.fn = ""
        self.bc = None
        self.iqc = None


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.name, format_data + "name")
        PrintBasic.print_basic(self.dn, format_data + "dn")
        PrintBasic.print_basic(self.vat, format_data + "vat")
        PrintBasic.print_basic(self.det, format_data + "det")
        PrintBasic.print_basic(self.wet, format_data + "wet")
        PrintBasic.print_basic(self.wp, format_data + "wp")
        PrintBasic.print_basic(self.ct, format_data + "ct")
        PrintBasic.print_basic(self.cp, format_data + "cp")
        PrintBasic.print_basic(self.ss, format_data + "ss")
        PrintBasic.print_basic(self.oe, format_data + "oe")
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
        PrintBasic.print_basic(self.we, format_data + "we")
        PrintBasic.print_basic(self.cawt, format_data + "cawt")
        PrintBasic.print_basic(self.cao, format_data + "cao")
        PrintBasic.print_basic(self.fc, format_data + "fc")
        PrintBasic.print_basic(self.sc, format_data + "sc")
        PrintBasic.print_basic(self.swd, format_data + "swd")
        PrintBasic.print_basic(self.wd, format_data + "wd")
        PrintBasic.print_basic(self.sdd, format_data + "sdd")
        PrintBasic.print_basic(self.dd, format_data + "dd")
        PrintBasic.print_basic(self.svd, format_data + "svd")
        PrintBasic.print_basic(self.tags, format_data + "tags")
        PrintBasic.print_basic(self.fn, format_data + "fn")
        PrintBasic.print_basic(self.bc, format_data + "bc")
        PrintBasic.print_basic(self.iqc, format_data + "iqc")


