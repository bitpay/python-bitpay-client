from .supported_transaction_currency import SupportedTransactionCurrency


class SupportedTransactionCurrencies(object):
    __btc = SupportedTransactionCurrency()
    __bch = SupportedTransactionCurrency()
    __eth = SupportedTransactionCurrency()
    __usdc = SupportedTransactionCurrency()
    __gusd = SupportedTransactionCurrency()
    __pax = SupportedTransactionCurrency()
    __xrp = SupportedTransactionCurrency()
    __doge = SupportedTransactionCurrency()
    __ltc = SupportedTransactionCurrency()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["BTC", "BCH", "ETH", "USDC", "GUSD", "PAX", "XRP", "DOGE", "LTC"]:
                    value = SupportedTransactionCurrency(**value)
                getattr(self, 'set_%s' % key.lower())(value)
            except AttributeError as e:
                print(e)

    def get_btc(self):
        return self.__btc

    def set_btc(self, btc: SupportedTransactionCurrency):
        self.__btc = btc

    def get_bch(self):
        return self.__bch

    def set_bch(self, bch: SupportedTransactionCurrency):
        self.__bch = bch

    def get_eth(self):
        return self.__eth

    def set_eth(self, eth: SupportedTransactionCurrency):
        self.__eth = eth

    def get_usdc(self):
        return self.__usdc

    def set_usdc(self, usdc: SupportedTransactionCurrency):
        self.__usdc = usdc

    def get_gusd(self):
        return self.__gusd

    def set_gusd(self, gusd: SupportedTransactionCurrency):
        self.__gusd = gusd

    def get_pax(self):
        return self.__pax

    def set_pax(self, pax: SupportedTransactionCurrency):
        self.__pax = pax

    def get_xrp(self):
        return self.__xrp

    def set_xrp(self, xrp: SupportedTransactionCurrency):
        self.__xrp = xrp

    def get_doge(self):
        return self.__doge

    def set_doge(self, doge: SupportedTransactionCurrency):
        self.__doge = doge

    def get_ltc(self):
        return self.__ltc

    def set_ltc(self, ltc: SupportedTransactionCurrency):
        self.__ltc = ltc

    def to_json(self):
        data = {
            "btc": self.get_btc(),
            "bch": self.get_bch(),
            "eth": self.get_eth(),
            "usdc": self.get_usdc(),
            "gusd": self.get_gusd(),
            "pax": self.get_pax(),
            "xrp": self.get_xrp(),
            "doge": self.get_doge(),
            "ltc": self.get_ltc()
        }
        return data
