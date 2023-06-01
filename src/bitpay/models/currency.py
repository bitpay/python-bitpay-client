"""
Currency
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


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
    __name = None
    __plural = None
    __alts = None
    __minimum = None
    __sanctioned = False
    __decimals = None
    __chain = None

    @classmethod
    def is_valid(cls, value: str) -> bool:
        try:
            return hasattr(Currency(), value)
        except Exception:
            return False

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "precision": "int",
                        "minimum": "float",
                        "sanctioned": "bool",
                        "decimals": "int",
                    },
                    {},
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_code(self) -> Optional[str]:
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code: Optional[str]) -> None:
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_symbol(self) -> Optional[str]:
        """
        Get method for to symbol
        :return: symbol
        """
        return self.__symbol

    def set_symbol(self, symbol: Optional[str]) -> None:
        """
        Set method for to symbol
        :param symbol: symbol
        """
        self.__symbol = symbol

    def get_chain(self) -> Optional[str]:
        """
        Get method for to chain
        :return: chain
        """
        return self.__chain

    def set_chain(self, chain: Optional[str]) -> None:
        """
        Set method for to chain
        :param chain: chain
        """
        self.__chain = chain

    def get_precision(self) -> Optional[int]:
        """
        Get method for to precision
        :return: precision
        """
        return self.__precision

    def set_precision(self, precision: Optional[int]) -> None:
        """
        Set method for to precision
        :param precision: precision
        """
        self.__precision = precision

    def get_name(self) -> Optional[str]:
        """
        Get method for to name
        :return: name
        """
        return self.__name

    def set_name(self, name: Optional[str]) -> None:
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_plural(self) -> Optional[str]:
        """
        Get method for to plural
        :return: plural
        """
        return self.__plural

    def set_plural(self, plural: Optional[str]) -> None:
        """
        Set method for to plural
        :param plural: plural
        """
        self.__plural = plural

    def get_alts(self) -> Optional[str]:
        """
        Get method for to alts
        :return: alts
        """
        return self.__alts

    def set_alts(self, alts: Optional[str]) -> None:
        """
        Set method for to alts
        :param alts: alts
        """
        self.__alts = alts

    def get_minimum(self) -> Optional[float]:
        """
        Get method for to minimum
        :return: minimum
        """
        return self.__minimum

    def set_minimum(self, minimum: Optional[float]) -> None:
        """
        Set method for to minimum
        :param minimum: minimum
        """
        self.__minimum = minimum

    def get_sanctioned(self) -> bool:
        """
        Get method for to sanctioned
        :return: sanctioned
        """
        return self.__sanctioned

    def set_sanctioned(self, sanctioned: bool) -> None:
        """
        Set method for to sanctioned
        :param sanctioned: sanctioned
        """
        self.__sanctioned = sanctioned

    def get_decimals(self) -> Optional[int]:
        """
        Get method for to decimals
        :return: decimals
        """
        return self.__decimals

    def set_decimals(self, decimals: Optional[int]) -> None:
        """
        Set method for to decimals
        :param decimals: decimals
        """
        self.__decimals = decimals

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
