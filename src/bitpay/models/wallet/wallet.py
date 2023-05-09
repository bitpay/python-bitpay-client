from typing import List, Optional

from .currencies import Currencies
from ...utils import key_utils
from ...utils.model_util import ModelUtil
from ...utils.model_util import ModelUtil


class Wallet(object):
    """
    supported wallets and supported currency details
    """

    __key = None
    __display_name = None
    __avatar = None
    __pay_pro = None
    __currencies = []
    __image = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"payPro": "bool"}, {"currencies": Currencies})
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_key(self) -> Optional[str]:
        """
        Get method for to key
        :return: key
        """
        return self.__key

    def set_key(self, key: Optional[str]):
        """
        Set method for to key
        :param key: key
        """
        self.__key = key

    def get_display_name(self) -> Optional[str]:
        """
        Get method for to display_name
        :return: display_name
        """
        return self.__display_name

    def set_display_name(self, display_name: Optional[str]):
        """
        Set method for to display_name
        :param display_name: display_name
        """
        self.__display_name = display_name

    def get_avatar(self) -> Optional[str]:
        """
        Get method for to avatar
        :return: avatar
        """
        return self.__avatar

    def set_avatar(self, avatar: Optional[str]):
        """
        Set method for to avatar
        :param avatar: avatar
        """
        self.__avatar = avatar

    def get_pay_pro(self) -> Optional[bool]:
        """
        Get method for to paypro
        :return: paypro
        """
        return self.__paypro

    def set_pay_pro(self, paypro: Optional[bool]):
        """
        Set method for to paypro
        :param paypro: paypro
        """
        self.__paypro = paypro

    def get_currencies(self) -> Optional[List[Currencies]]:
        """
        Get method for to currencies
        :return: List[Currencies]
        """
        return self.__currencies

    def set_currencies(self, currencies: Optional[List[Currencies]]):
        """
        Set method for to currencies
        :param currencies: currencies
        """
        self.__currencies = currencies

    def get_image(self) -> Optional[str]:
        """
        Get URL that displays wallet avatar image
        :return: image
        """
        return self.__image

    def set_image(self, value: Optional[str]):
        """
        Set URL that displays wallet avatar image
        :param value: image
        """
        self.__image = value

    def to_json(self):
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
