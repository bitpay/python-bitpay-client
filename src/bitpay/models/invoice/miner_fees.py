"""
MinerFees
"""
from .miner_fees_item import MinerFeesItem


class MinerFees:
    """
    The total amount of fees that the purchaser will pay to cover BitPay's
     UTXO sweep cost for an invoice. The key is the currency and the value
     is an amount in satoshis. This is referenced as "Network Cost" on an
     invoice,see this support article for more information
    """

    __btc = MinerFeesItem()
    __bch = MinerFeesItem()
    __eth = MinerFeesItem()
    __usdc = MinerFeesItem()
    __gusd = MinerFeesItem()
    __pax = MinerFeesItem()
    __doge = MinerFeesItem()
    __ltc = MinerFeesItem()
    __busd = MinerFeesItem()
    __xrp = MinerFeesItem()

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            try:
                if key in ["BTC", "BCH", "ETH", "USDC", "GUSD", "PAX", "BUSD", "XRP"]:
                    value = MinerFeesItem(**value)
                getattr(self, "set_%s" % key.lower())(value)
            except AttributeError:
                pass

    def get_btc(self):
        """
        Get method for the btc
        :return: btc
        """
        return self.__btc

    def set_btc(self, btc: MinerFeesItem):
        """
        Set method for the btc
        :param btc: btc
        """
        self.__btc = btc

    def get_bch(self):
        """
        Get method for the bch
        :return: bch
        """
        return self.__bch

    def set_bch(self, bch: MinerFeesItem):
        """
        Set method for the bch
        :param bch: bch
        """
        self.__bch = bch

    def get_eth(self):
        """
        Get method for the eth
        :return: eth
        """
        return self.__eth

    def set_eth(self, eth: MinerFeesItem):
        """
        Set method for the eth
        :param eth: eth
        """
        self.__eth = eth

    def get_usdc(self):
        """
        Get method for the usdc
        :return: usdc
        """
        return self.__usdc

    def set_usdc(self, usdc: MinerFeesItem):
        """
        Set method for the usdc
        :param usdc: usdc
        """
        self.__usdc = usdc

    def get_gusd(self):
        """
        Get method for the gusd
        :return: gusd
        """
        return self.__gusd

    def set_gusd(self, gusd: MinerFeesItem):
        """
        Set method for the gusd
        :param gusd: gusd
        """
        self.__gusd = gusd

    def get_doge(self):
        """
        Get method for the doge
        :return: doge
        """
        return self.__doge

    def set_doge(self, doge: MinerFeesItem):
        """
        Set method for the doge
        :param doge: doge
        """
        self.__doge = doge

    def get_ltc(self):
        """
        Get method for the ltc
        :return: ltc
        """
        return self.__ltc

    def set_ltc(self, ltc: MinerFeesItem):
        """
        Set method for the ltc
        :param ltc: ltc
        """
        self.__ltc = ltc

    def get_pax(self):
        """
        Get method for the pax
        :return: pax
        """
        return self.__pax

    def set_pax(self, pax: MinerFeesItem):
        """
        Set method for the pax
        :param pax: pax
        """
        self.__pax = pax

    def get_busd(self):
        """
        Get method for the busd
        :return: busd
        """
        return self.__busd

    def set_busd(self, busd: MinerFeesItem):
        """
        Set method for the busd
        :param busd: busd
        """
        self.__busd = busd

    def get_xrp(self):
        """
        Get method for the xrp
        :return: xrp
        """
        return self.__xrp

    def set_xrp(self, xrp: MinerFeesItem):
        """
        Set method for the xrp
        :param xrp: xrp
        """
        self.__xrp = xrp

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
            "pax": self.get_pax(),
            "doge": self.get_doge(),
            "ltc": self.get_ltc(),
            "xrp": self.get_xrp(),
            "busd": self.get_busd(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
