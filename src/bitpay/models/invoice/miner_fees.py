"""
MinerFees
"""
from typing import Optional, Any

from .miner_fees_item import MinerFeesItem
from bitpay.utils.model_util import ModelUtil


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

    def __init__(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            try:
                if not isinstance(value, MinerFeesItem):
                    value = MinerFeesItem(**value)
                getattr(self, "set_%s" % key.lower())(value)
            except AttributeError:
                pass

    def get_btc(self) -> Optional[MinerFeesItem]:
        """
        Get method for the btc
        :return: btc
        """
        return self.__btc

    def set_btc(self, btc: MinerFeesItem) -> None:
        """
        Set method for the btc
        :param btc: btc
        """
        self.__btc = btc

    def get_bch(self) -> Optional[MinerFeesItem]:
        """
        Get method for the bch
        :return: bch
        """
        return self.__bch

    def set_bch(self, bch: MinerFeesItem) -> None:
        """
        Set method for the bch
        :param bch: bch
        """
        self.__bch = bch

    def get_eth(self) -> Optional[MinerFeesItem]:
        """
        Get method for the eth
        :return: eth
        """
        return self.__eth

    def set_eth(self, eth: MinerFeesItem) -> None:
        """
        Set method for the eth
        :param eth: eth
        """
        self.__eth = eth

    def get_usdc(self) -> Optional[MinerFeesItem]:
        """
        Get method for the usdc
        :return: usdc
        """
        return self.__usdc

    def set_usdc(self, usdc: MinerFeesItem) -> None:
        """
        Set method for the usdc
        :param usdc: usdc
        """
        self.__usdc = usdc

    def get_gusd(self) -> Optional[MinerFeesItem]:
        """
        Get method for the gusd
        :return: gusd
        """
        return self.__gusd

    def set_gusd(self, gusd: MinerFeesItem) -> None:
        """
        Set method for the gusd
        :param gusd: gusd
        """
        self.__gusd = gusd

    def get_doge(self) -> Optional[MinerFeesItem]:
        """
        Get method for the doge
        :return: doge
        """
        return self.__doge

    def set_doge(self, doge: MinerFeesItem) -> None:
        """
        Set method for the doge
        :param doge: doge
        """
        self.__doge = doge

    def get_ltc(self) -> Optional[MinerFeesItem]:
        """
        Get method for the ltc
        :return: ltc
        """
        return self.__ltc

    def set_ltc(self, ltc: MinerFeesItem) -> None:
        """
        Set method for the ltc
        :param ltc: ltc
        """
        self.__ltc = ltc

    def get_pax(self) -> Optional[MinerFeesItem]:
        """
        Get method for the pax
        :return: pax
        """
        return self.__pax

    def set_pax(self, pax: MinerFeesItem) -> None:
        """
        Set method for the pax
        :param pax: pax
        """
        self.__pax = pax

    def get_busd(self) -> Optional[MinerFeesItem]:
        """
        Get method for the busd
        :return: busd
        """
        return self.__busd

    def set_busd(self, busd: MinerFeesItem) -> None:
        """
        Set method for the busd
        :param busd: busd
        """
        self.__busd = busd

    def get_xrp(self) -> Optional[MinerFeesItem]:
        """
        Get method for the xrp
        :return: xrp
        """
        return self.__xrp

    def set_xrp(self, xrp: MinerFeesItem) -> None:
        """
        Set method for the xrp
        :param xrp: xrp
        """
        self.__xrp = xrp

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
