"""
SupportedTransactionCurrencies
"""
from .supported_transaction_currency import SupportedTransactionCurrency


class SupportedTransactionCurrencies:
    """
    currency selected for payment
    """

    __btc = SupportedTransactionCurrency()
    __bch = SupportedTransactionCurrency()
    __eth = SupportedTransactionCurrency()
    __usdc = SupportedTransactionCurrency()
    __gusd = SupportedTransactionCurrency()
    __busd = SupportedTransactionCurrency()
    __pax = SupportedTransactionCurrency()
    __xrp = SupportedTransactionCurrency()
    __doge = SupportedTransactionCurrency()
    __ltc = SupportedTransactionCurrency()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in [
                    "BTC",
                    "BCH",
                    "ETH",
                    "USDC",
                    "GUSD",
                    "BUSD",
                    "PAX",
                    "XRP",
                    "DOGE",
                    "LTC",
                ]:
                    value = SupportedTransactionCurrency(**value)
                getattr(self, "set_%s" % key.lower())(value)
            except AttributeError:
                pass

    def get_btc(self):
        """
        Get method for to btc
        :return: btc
        """
        return self.__btc

    def set_btc(self, btc: SupportedTransactionCurrency):
        """
        Set method for to btc
        :param btc: btc
        """
        self.__btc = btc

    def get_bch(self):
        """
        Get method for to bch
        :return: bch
        """
        return self.__bch

    def set_bch(self, bch: SupportedTransactionCurrency):
        """
        Set method for to bch
        :param bch: bch
        """
        self.__bch = bch

    def get_eth(self):
        """
        Get method for to eth
        :return: eth
        """
        return self.__eth

    def set_eth(self, eth: SupportedTransactionCurrency):
        """
        Set method for to eth
        :param eth: eth
        """
        self.__eth = eth

    def get_usdc(self):
        """
        Get method for to usdc
        :return: usdc
        """
        return self.__usdc

    def set_usdc(self, usdc: SupportedTransactionCurrency):
        """
        Set method for to usdc
        :param usdc: usdc
        """
        self.__usdc = usdc

    def get_gusd(self):
        """
        Get method for to gusd
        :return: gusd
        """
        return self.__gusd

    def set_gusd(self, gusd: SupportedTransactionCurrency):
        """
        Set method for to gusd
        :param gusd: gusd
        """
        self.__gusd = gusd

    def get_busd(self):
        """
        Get method for to busd
        :return: busd
        """
        return self.__busd

    def set_busd(self, busd: SupportedTransactionCurrency):
        """
        Set method for to busd
        :param user: busd
        """
        self.__busd = busd

    def get_pax(self):
        """
        Get method for to pax
        :return: pax
        """
        return self.__pax

    def set_pax(self, pax: SupportedTransactionCurrency):
        """
        Set method for to pax
        :param pax: pax
        """
        self.__pax = pax

    def get_xrp(self):
        """
        Get method for to xrp
        :return: xrp
        """
        return self.__xrp

    def set_xrp(self, xrp: SupportedTransactionCurrency):
        """
        Set method for to xrp
        :param xrp: xrp
        """
        self.__xrp = xrp

    def get_doge(self):
        """
        Get method for to doge
        :return: doge
        """
        return self.__doge

    def set_doge(self, doge: SupportedTransactionCurrency):
        """
        Set method for to doge
        :param doge: doge
        """
        self.__doge = doge

    def get_ltc(self):
        """
        Get method for to ltc
        :return: ltc
        """
        return self.__ltc

    def set_ltc(self, ltc: SupportedTransactionCurrency):
        """
        Set method for to ltc
        :param ltc: ltc
        """
        self.__ltc = ltc

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "btc": self.get_btc(),
            "bch": self.get_bch(),
            "eth": self.get_eth(),
            "usdc": self.get_usdc(),
            "gusd": self.get_gusd(),
            "busd": self.get_busd(),
            "pax": self.get_pax(),
            "xrp": self.get_xrp(),
            "doge": self.get_doge(),
            "ltc": self.get_ltc(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
