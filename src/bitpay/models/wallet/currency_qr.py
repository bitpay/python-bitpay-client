"""
Currency Qr
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class CurrencyQr:
    """
    Currency Qr
    """

    __type = None
    __collapsed = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"collapsed": "bool"}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_type(self) -> Optional[str]:
        """
        Get method for to type
        :return: type
        """
        return self.__type

    def set_type(self, type: Optional[str]) -> None:
        """
        Set method for to type
        :param type: type
        """
        self.__type = type

    def get_collapsed(self) -> Optional[bool]:
        """
        Get method for to collapsed
        :return: collapsed
        """
        return self.__collapsed

    def set_collapsed(self, collapsed: Optional[bool]) -> None:
        """
        Set method for to collapsed
        :param collapsed: collapsed
        """
        self.__collapsed = collapsed

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
