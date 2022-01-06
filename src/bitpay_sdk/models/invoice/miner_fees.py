from .miner_fees_item import MinerFeesItem


class MinerFees(object):
    __btc = MinerFeesItem()
    __bch = MinerFeesItem()
    __eth = MinerFeesItem()
    __usdc = MinerFeesItem()
    __gusd = MinerFeesItem()
    __pax = MinerFeesItem()
    __doge = MinerFeesItem()
    __ltc = MinerFeesItem()

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            try:
                if key in ["BTC", "BCH", "ETH", "USDC", "GUSD", "PAX"]:
                    value = MinerFeesItem(**value)
                getattr(self, 'set_%s' % key.lower())(value)
            except AttributeError as e:
                print(e)

    def get_btc(self):
        return self.__btc

    def set_btc(self, btc: MinerFeesItem):
        self.__btc = btc

    def get_bch(self):
        return self.__bch

    def set_bch(self, bch: MinerFeesItem):
        self.__bch = bch

    def get_eth(self):
        return self.__eth

    def set_eth(self, eth: MinerFeesItem):
        self.__eth = eth

    def get_usdc(self):
        return self.__usdc

    def set_usdc(self, usdc: MinerFeesItem):
        self.__usdc = usdc

    def get_gusd(self):
        return self.__gusd

    def set_gusd(self, gusd: MinerFeesItem):
        self.__gusd = gusd

    def get_doge(self):
        return self.__doge

    def set_doge(self, doge: MinerFeesItem):
        self.__doge = doge

    def get_ltc(self):
        return self.__ltc

    def set_pax(self, ltc: MinerFeesItem):
        self.__ltc = ltc

    def to_json(self):
        data = {
            "btc": self.get_btc(),
            "bch": self.get_bch(),
            "eth": self.get_eth(),
            "usdc": self.get_usdc(),
            "gusd": self.get_gusd(),
            "pax": self.get_pax(),
            "doge": self.get_doge(),
            "ltc": self.get_ltc()
        }
        return data
