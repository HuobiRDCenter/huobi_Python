

class CommonSymbolsV1:

    def __init__(self):
        self.symbol = ""
        self.sn = ""
        self.bc = ""
        self.qc = ""
        self.state = ""
        self.ve = None
        self.we = None
        self.dl = None
        self.cd = None
        self.te = None
        self.ce = None
        self.tet = 0
        self.toa = 0
        self.tca = 0
        self.voa = 0
        self.vca = 0
        self.sp = ""
        self.tm = ""
        self.w = 0
        self.ttp = 0.0
        self.tap = 0.0
        self.tpp = 0.0
        self.fp = 0.0
        self.tags = ""
        self.d = None
        self.bcdn = ""
        self.qcdn = ""
        self.elr = ""
        self.castate = ""
        self.ca1oa = 0
        self.ca1ca = 0
        self.ca2oa = 0
        self.ca2ca = 0


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "symbol")
        PrintBasic.print_basic(self.sn, format_data + "sn")
        PrintBasic.print_basic(self.bc, format_data + "bc")
        PrintBasic.print_basic(self.qc, format_data + "qc")
        PrintBasic.print_basic(self.state, format_data + "state")
        PrintBasic.print_basic(self.ve, format_data + "ve")
        PrintBasic.print_basic(self.we, format_data + "we")
        PrintBasic.print_basic(self.dl, format_data + "dl")
        PrintBasic.print_basic(self.cd, format_data + "cd")
        PrintBasic.print_basic(self.te, format_data + "te")
        PrintBasic.print_basic(self.ce, format_data + "ce")
        PrintBasic.print_basic(self.tet, format_data + "tet")
        PrintBasic.print_basic(self.toa, format_data + "toa")
        PrintBasic.print_basic(self.tca, format_data + "tca")
        PrintBasic.print_basic(self.voa, format_data + "voa")
        PrintBasic.print_basic(self.vca, format_data + "vca")
        PrintBasic.print_basic(self.sp, format_data + "sp")
        PrintBasic.print_basic(self.tm, format_data + "tm")
        PrintBasic.print_basic(self.w, format_data + "w")
        PrintBasic.print_basic(self.ttp, format_data + "ttp")
        PrintBasic.print_basic(self.tap, format_data + "tap")
        PrintBasic.print_basic(self.tpp, format_data + "tpp")
        PrintBasic.print_basic(self.fp, format_data + "fp")
        PrintBasic.print_basic(self.tags, format_data + "tags")
        PrintBasic.print_basic(self.d, format_data + "d")
        PrintBasic.print_basic(self.bcdn, format_data + "bcdn")
        PrintBasic.print_basic(self.qcdn, format_data + "qcdn")
        PrintBasic.print_basic(self.elr, format_data + "elr")
        PrintBasic.print_basic(self.castate, format_data + "castate")
        PrintBasic.print_basic(self.ca1oa, format_data + "ca1oa")
        PrintBasic.print_basic(self.ca1ca, format_data + "ca1ca")
        PrintBasic.print_basic(self.ca2oa, format_data + "ca2oa")
        PrintBasic.print_basic(self.ca2ca, format_data + "ca2ca")


