"""
Shopper
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Shopper:
    """
    shopper
    """

    __user = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_user(self) -> Optional[str]:
        """
        Get method for to user
        :return: user
        """
        return self.__user

    def set_user(self, user: Optional[str]) -> None:
        """
        Set method for to user
        :param user: user
        """
        self.__user = user

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
