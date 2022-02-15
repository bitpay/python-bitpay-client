"""
Currency
"""
from ..utils.key_utils import change_camel_case_to_snake_case


class Currency:
    """
    Currency: Crypto and fiat
    """

    # Crypto
    BCH = "BCH"
    BTC = "BTC"
    ETH = "ETH"
    USDC = "USDC"
    GUSD = "GUSD"
    PAX = "PAX"
    XRP = "XRP"
    BUSD = "BUSD"
    DOGE = "DOGE"
    WBTC = "WBTC"
    DAI = "DAI"
    LTC = "LTC"
    SHIB = "SHIB"

    # Fiat
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPF = "XPF"
    XSU = "XSU"
    XUA = "XUA"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"

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
    __chain = None
    __tranche_decimals = None
    __max_supply = None

    @classmethod
    def is_valid(cls, value):
        try:
            return hasattr(Currency(), value)
        except Exception:
            return False

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_code(self):
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_symbol(self):
        """
        Get method for to symbol
        :return: symbol
        """
        return self.__symbol

    def set_symbol(self, symbol):
        """
        Set method for to symbol
        :param symbol: symbol
        """
        self.__symbol = symbol

    def get_chain(self):
        """
        Get method for to chain
        :return: chain
        """
        return self.__chain

    def set_chain(self, chain):
        """
        Set method for to chain
        :param chain: chain
        """
        self.__chain = chain

    def get_tranche_decimals(self):
        """
        Get method for to tranche_decimals
        :return: tranche_decimals
        """
        return self.__tranche_decimals

    def set_tranche_decimals(self, tranche_decimals):
        """
        Set method for to tranche_decimals
        :param tranche_decimals: tranche_decimals
        """
        self.__tranche_decimals = tranche_decimals

    def get_max_supply(self):
        """
        Get method for to max_supply
        :return: max_supply
        """
        return self.__max_supply

    def set_max_supply(self, max_supply):
        """
        Set method for to max_supply
        :param max_supply: max_supply
        """
        self.__max_supply = max_supply

    def get_precision(self):
        """
        Get method for to precision
        :return: precision
        """
        return self.__precision

    def set_precision(self, precision):
        """
        Set method for to precision
        :param precision: precision
        """
        self.__precision = precision

    def get_currently_settled(self):
        """
        Get method for to currently_settled
        :return: currently_settled
        """
        return self.__currently_settled

    def set_currently_settled(self, currently_settled):
        """
        Set method for to currently_settled
        :param currently_settled: currently_settled
        """
        self.__currently_settled = currently_settled

    def get_name(self):
        """
        Get method for to name
        :return: name
        """
        return self.__name

    def set_name(self, name):
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_plural(self):
        """
        Get method for to plural
        :return: plural
        """
        return self.__plural

    def set_plural(self, plural):
        """
        Set method for to plural
        :param plural: plural
        """
        self.__plural = plural

    def get_alts(self):
        """
        Get method for to alts
        :return: alts
        """
        return self.__alts

    def set_alts(self, alts):
        """
        Set method for to alts
        :param alts: alts
        """
        self.__alts = alts

    def get_minimum(self):
        """
        Get method for to minimum
        :return: minimum
        """
        return self.__minimum

    def set_minimum(self, minimum):
        """
        Set method for to minimum
        :param minimum: minimum
        """
        self.__minimum = minimum

    def get_sanctioned(self):
        """
        Get method for to sanctioned
        :return: sanctioned
        """
        return self.__sanctioned

    def set_sanctioned(self, sanctioned):
        """
        Set method for to sanctioned
        :param sanctioned: sanctioned
        """
        self.__sanctioned = sanctioned

    def get_decimals(self):
        """
        Get method for to decimals
        :return: decimals
        """
        return self.__decimals

    def set_decimals(self, decimals):
        """
        Set method for to decimals
        :param decimals: decimals
        """
        self.__decimals = decimals

    def get_payout_fields(self):
        """
        Get method for to payout_fields
        :return: payout_fields
        """
        return self.__payout_fields

    def set_payout_fields(self, payout_fields):
        """
        Set method for to payout_fields
        :param payout_fields: payout_fields
        """
        self.__payout_fields = payout_fields

    def get_settlement_minimum(self):
        """
        Get method for to settlement_minimum
        :return: settlement_minimum
        """
        return self.__settlement_minimum

    def set_settlement_minimum(self, settlement_minimum):
        """
        Set method for to code
        :param settlement_minimum: settlement_minimum
        """
        self.__settlement_minimum = settlement_minimum

    def to_json(self):
        """
        :return: data in json
        """
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
