"""
Rate
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Rate:
    """
    Rate
    """

    __name = None
    __code = None
    __rate = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"rate": "float"}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_name(self) -> Optional[str]:
        """
        Get method for the name
        :return: name
        """
        return self.__name

    def set_name(self, name: Optional[str]) -> None:
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_code(self) -> Optional[str]:
        """
        Get method for the code
        :return: code
        """
        return self.__code

    def set_code(self, code: Optional[str]) -> None:
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_rate(self) -> Optional[float]:
        """
        Get method for the rate
        :return: rate
        """
        return self.__rate

    def set_rate(self, rate: Optional[float]) -> None:
        """
        Set method for to rate
        :param rate: rate
        """
        self.__rate = rate

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
