

class MarketSymbols:

    def __init__(self):
        self.symbol = ""
        self.bc = ""
        self.qc = ""
        self.state = ""
        self.sp = ""
        self.tags = ""
        self.lr = 0.0
        self.smlr = 0.0
        self.pp = 0
        self.ap = 0
        self.vp = 0
        self.minoa = 0.0
        self.maxoa = 0.0
        self.minov = 0.0
        self.lominoa = 0.0
        self.lomaxoa = 0.0
        self.lomaxba = 0.0
        self.lomaxsa = 0.0
        self.smminoa = 0.0
        self.smmaxoa = 0.0
        self.bmmaxov = 0.0
        self.blmlt = 0.0
        self.slmgt = 0.0
        self.msormlt = 0.0
        self.mbormlt = 0.0
        self.at = ""
        self.u = ""
        self.mfr = 0.0
        self.ct = ""
        self.rt = ""
        self.rthr = 0.0
        self.in_ = 0.0
        self.maxov = 0.0
        self.flr = 0.0
        self.castate = ""


    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "symbol")
        PrintBasic.print_basic(self.bc, format_data + "bc")
        PrintBasic.print_basic(self.qc, format_data + "qc")
        PrintBasic.print_basic(self.state, format_data + "state")
        PrintBasic.print_basic(self.sp, format_data + "sp")
        PrintBasic.print_basic(self.tags, format_data + "tags")
        PrintBasic.print_basic(self.lr, format_data + "lr")
        PrintBasic.print_basic(self.smlr, format_data + "smlr")
        PrintBasic.print_basic(self.pp, format_data + "pp")
        PrintBasic.print_basic(self.ap, format_data + "ap")
        PrintBasic.print_basic(self.vp, format_data + "vp")
        PrintBasic.print_basic(self.minoa, format_data + "minoa")
        PrintBasic.print_basic(self.maxoa, format_data + "maxoa")
        PrintBasic.print_basic(self.minov, format_data + "minov")
        PrintBasic.print_basic(self.lominoa, format_data + "lominoa")
        PrintBasic.print_basic(self.lomaxoa, format_data + "lomaxoa")
        PrintBasic.print_basic(self.lomaxba, format_data + "lomaxba")
        PrintBasic.print_basic(self.lomaxsa, format_data + "lomaxsa")
        PrintBasic.print_basic(self.smminoa, format_data + "smminoa")
        PrintBasic.print_basic(self.smmaxoa, format_data + "smmaxoa")
        PrintBasic.print_basic(self.bmmaxov, format_data + "bmmaxov")
        PrintBasic.print_basic(self.blmlt, format_data + "blmlt")
        PrintBasic.print_basic(self.slmgt, format_data + "slmgt")
        PrintBasic.print_basic(self.msormlt, format_data + "msormlt")
        PrintBasic.print_basic(self.mbormlt, format_data + "mbormlt")
        PrintBasic.print_basic(self.at, format_data + "at")
        PrintBasic.print_basic(self.u, format_data + "u")
        PrintBasic.print_basic(self.mfr, format_data + "mfr")
        PrintBasic.print_basic(self.ct, format_data + "ct")
        PrintBasic.print_basic(self.rt, format_data + "rt")
        PrintBasic.print_basic(self.rthr, format_data + "rthr")
        PrintBasic.print_basic(self.in_, format_data + "in_")
        PrintBasic.print_basic(self.maxov, format_data + "maxov")
        PrintBasic.print_basic(self.flr, format_data + "flr")
        PrintBasic.print_basic(self.castate, format_data + "castate")




