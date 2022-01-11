class Currency:

    # Crypto
    __bch = "BCH"
    __btc = "BTC"
    __eth = "ETH"
    __usdc = "USDC"
    __gusd = "GUSD"
    __pax = "PAX"
    __xrp = "XRP"
    __busd = "BUSD"
    __doge = "DOGE"
    __wbtc = "WBTC"
    __dai = "DAI"
    __ltc = "LTC"
    __shib = "SHIB"

    # Fiat
    __aed = "AED"
    __afn = "AFN"
    __all = "ALL"
    __amd = "AMD"
    __ang = "ANG"
    __aoa = "AOA"
    __ars = "ARS"
    __aud = "AUD"
    __awg = "AWG"
    __azn = "AZN"
    __bam = "BAM"
    __bbd = "BBD"
    __bdt = "BDT"
    __bgn = "BGN"
    __bhd = "BHD"
    __bif = "BIF"
    __bmd = "BMD"
    __bnd = "BND"
    __bob = "BOB"
    __bov = "BOV"
    __brl = "BRL"
    __bsd = "BSD"
    __btn = "BTN"
    __bwp = "BWP"
    __byr = "BYR"
    __bzd = "BZD"
    __cad = "CAD"
    __cdf = "CDF"
    __che = "CHE"
    __chf = "CHF"
    __chw = "CHW"
    __clf = "CLF"
    __clp = "CLP"
    __cny = "CNY"
    __cop = "COP"
    __cou = "COU"
    __crc = "CRC"
    __cuc = "CUC"
    __cup = "CUP"
    __cve = "CVE"
    __czk = "CZK"
    __djf = "DJF"
    __dkk = "DKK"
    __dop = "DOP"
    __dzd = "DZD"
    __egp = "EGP"
    __ern = "ERN"
    __etb = "ETB"
    __eur = "EUR"
    __fjd = "FJD"
    __fkp = "FKP"
    __gbp = "GBP"
    __gel = "GEL"
    __ghs = "GHS"
    __gip = "GIP"
    __gmd = "GMD"
    __gnf = "GNF"
    __gtq = "GTQ"
    __gyd = "GYD"
    __hkd = "HKD"
    __hnl = "HNL"
    __hrk = "HRK"
    __htg = "HTG"
    __huf = "HUF"
    __idr = "IDR"
    __ils = "ILS"
    __inr = "INR"
    __iqd = "IQD"
    __irr = "IRR"
    __isk = "ISK"
    __jmd = "JMD"
    __jod = "JOD"
    __jpy = "JPY"
    __kes = "KES"
    __kgs = "KGS"
    __khr = "KHR"
    __kmf = "KMF"
    __kpw = "KPW"
    __krw = "KRW"
    __kwd = "KWD"
    __kyd = "KYD"
    __kzt = "KZT"
    __lak = "LAK"
    __lbp = "LBP"
    __lkr = "LKR"
    __lrd = "LRD"
    __lsl = "LSL"
    __lyd = "LYD"
    __mad = "MAD"
    __mdl = "MDL"
    __mga = "MGA"
    __mkd = "MKD"
    __mmk = "MMK"
    __mnt = "MNT"
    __mop = "MOP"
    __mru = "MRU"
    __mur = "MUR"
    __mvr = "MVR"
    __mwk = "MWK"
    __mxn = "MXN"
    __mxv = "MXV"
    __myr = "MYR"
    __mzn = "MZN"
    __nad = "NAD"
    __ngn = "NGN"
    __nio = "NIO"
    __nok = "NOK"
    __npr = "NPR"
    __nzd = "NZD"
    __omr = "OMR"
    __pab = "PAB"
    __pen = "PEN"
    __pgk = "PGK"
    __php = "PHP"
    __pkr = "PKR"
    __pln = "PLN"
    __pyg = "PYG"
    __qar = "QAR"
    __ron = "RON"
    __rsd = "RSD"
    __rub = "RUB"
    __rwf = "RWF"
    __sar = "SAR"
    __sbd = "SBD"
    __scr = "SCR"
    __sdg = "SDG"
    __sek = "SEK"
    __sgd = "SGD"
    __shp = "SHP"
    __sll = "SLL"
    __sos = "SOS"
    __srd = "SRD"
    __ssp = "SSP"
    __stn = "STN"
    __svc = "SVC"
    __syp = "SYP"
    __szl = "SZL"
    __thb = "THB"
    __tjs = "TJS"
    __tmt = "TMT"
    __tnd = "TND"
    __top = "TOP"
    __try = "TRY"
    __ttd = "TTD"
    __twd = "TWD"
    __tzs = "TZS"
    __uah = "UAH"
    __ugx = "UGX"
    __usd = "USD"
    __usn = "USN"
    __uyi = "UYI"
    __uyu = "UYU"
    __uzs = "UZS"
    __vef = "VEF"
    __vnd = "VND"
    __vuv = "VUV"
    __wst = "WST"
    __xaf = "XAF"
    __xcd = "XCD"
    __xdr = "XDR"
    __xof = "XOF"
    __xpf = "XPF"
    __xsu = "XSU"
    __xua = "XUA"
    __yer = "YER"
    __zar = "ZAR"
    __zmw = "ZMW"
    __zwl = "ZWL"
    
    __code = None
    __symbol = None
    __precision = None
    __currently_settled = None
    __name = None
    __plural = None
    __alts = None
    __minimum = None
    __sanctioned = None
    __decimals = None
    __payout_fields = None
    __settlement_minimum = None

    def is_valid(self, value):
        try:
            obj = Currency()
            if hasattr(obj, value):
                return True
            return False
        except:
            return False

    def __init__(self):
        pass

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_symbol(self):
        return self.__symbol

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def get_precision(self):
        return self.__precision

    def set_precision(self, precision):
        self.__precision = precision

    def get_currently_settled(self):
        return self.__currently_settled

    def set_currently_settled(self, currently_settled):
        self.__currently_settled = currently_settled

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_plural(self):
        return self.__plural

    def set_plural(self, plural):
        self.__plural = plural

    def get_alts(self):
        return self.__alts

    def set_alts(self, alts):
        self.__alts = alts

    def get_minimum(self):
        return self.__minimum

    def set_minimum(self, minimum):
        self.__minimum = minimum

    def get_sanctioned(self):
        return self.__sanctioned

    def set_sanctioned(self, sanctioned):
        self.__sanctioned = sanctioned

    def get_decimals(self):
        return self.__decimals

    def set_decimals(self, decimals):
        self.__decimals = decimals

    def get_payout_fields(self):
        return self.__payout_fields

    def set_payout_fields(self, payout_fields):
        self.__payout_fields = payout_fields

    def get_settlement_minimum(self):
        return self.__settlement_minimum

    def set_settlement_minimum(self, settlement_minimum):
        self.__settlement_minimum = settlement_minimum

    def to_json(self):
        data = {
            "code": self.get_code(),
            "symbol": self.get_symbol(),
            "precision": self.get_precision(),
            "currentlySettled": self.get_currently_settled(),
            "name": self.get_name(),
            "plural": self.get_plural(),
            "alts": self.get_alts(),
            "minimum": self.get_minimum(),
            "sanctioned": self.get_sanctioned(),
            "decimals": self.get_decimals(),
            "payoutFields": self.get_payout_fields(),
            "settlementMinimum": self.get_settlement_minimum(),
        }
        return data
