"""
Currencies
"""
from typing import Optional

from bitpay.utils import key_utils
from bitpay.models.wallet.currency_qr import CurrencyQr
from bitpay.utils.model_util import ModelUtil
from bitpay.utils.model_util import ModelUtil


class Currencies(object):
    """
    details of what currencies support payments for this wallet
    """

    __code = None
    __p2p = False
    __dapp_browser = False
    __pay_pro = False
    __qr = None
    __image = None
    __withdrawal_fee = None
    __wallet_connect = False

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "p2p": "bool",
                        "dappBrowser": "bool",
                        "payPro": "bool",
                        "qr": CurrencyQr,
                        "walletConnect": "bool",
                    },
                    {},
                )
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
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

    def get_p2p(self) -> bool:
        """
        Get method for to p2p
        :return: p2p
        """
        return self.__p2p

    def set_p2p(self, p2p: bool) -> None:
        """
        Set method for to p2p
        :param p2p: p2p
        """
        self.__p2p = p2p

    def get_dapp_browser(self) -> bool:
        """
        Get method for to dapp_browser
        :return: dapp_browser
        """
        return self.__dapp_browser

    def set_dapp_browser(self, dapp_browser: bool) -> None:
        """
        Set method for to dapp_browser
        :param dapp_browser: dapp_browser
        """
        self.__dapp_browser = dapp_browser

    def get_pay_pro(self) -> bool:
        """
        Get method for to pay_pro
        :return: pay_pro
        """
        return self.__pay_pro

    def set_pay_pro(self, pay_pro: bool) -> None:
        """
        Set method for to pay_pro
        :param pay_pro: pay_pro
        """
        self.__pay_pro = pay_pro

    def get_qr(self) -> Optional[CurrencyQr]:
        """
        Get method for to qr
        :return: qr
        """
        return self.__qr

    def set_qr(self, qr: Optional[CurrencyQr]) -> None:
        """
        Set method for to qr
        :param qr: qr
        """
        self.__qr = qr

    def get_withdrawal_fee(self) -> Optional[str]:
        """
        Get method for to withdrawal_fee
        :return: withdrawal_fee
        """
        return self.__withdrawal_fee

    def set_withdrawal_fee(self, withdrawal_fee: Optional[str]) -> None:
        """
        Set method for to withdrawal_fee
        :param withdrawal_fee: withdrawal_fee
        """
        self.__withdrawal_fee = withdrawal_fee

    def get_wallet_connect(self) -> Optional[bool]:
        """
        Get method for to wallet_connect
        :return: wallet_connect
        """
        return self.__wallet_connect

    def set_wallet_connect(self, wallet_connect: bool) -> None:
        """
        Set method for to wallet_connect
        :param wallet_connect: wallet_connect
        """
        self.__wallet_connect = wallet_connect

    def get_image(self) -> Optional[str]:
        """
        Get URL that displays currency image
        :return: image
        """
        return self.__image

    def set_image(self, value: Optional[str]) -> None:
        """
        Set URL that displays currency image
        :param value: image
        """
        self.__image = value

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
