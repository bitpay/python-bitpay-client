from .miner_fees_item import MinerFeesItem


def change_camel_case_to_snake_case(string):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in string]).lstrip('_')


class MinerFees:
    __btc = None
    __bch = None
    __eth = None
    __usdc = None
    __gusd = None
    __pax = None

    def __init__(self, **kwargs):
        self.__btc = MinerFeesItem()
        self.__bch = MinerFeesItem()
        self.__eth = MinerFeesItem()
        self.__usdc = MinerFeesItem()
        self.__gusd = MinerFeesItem()
        self.__pax = MinerFeesItem()
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                pass

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

    def get_pax(self):
        return self.__pax

    def set_pax(self, pax: MinerFeesItem):
        self.__pax = pax

    def to_json(self):
        data = {
            "btc": self.get_btc(),
            "bch": self.get_bch(),
            "eth": self.get_eth(),
            "usdc": self.get_usdc(),
            "gusd": self.get_gusd(),
            "pax": self.get_pax()
        }
        return data
