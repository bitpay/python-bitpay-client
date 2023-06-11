"""
SupportedTransactionCurrency
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class SupportedTransactionCurrency:
    """
    currency selected for payment is enabled
    """

    __enabled = False
    __reason = None

    def __init__(self, **kwargs: dict):
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"enabled": "bool"}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_enabled(self) -> bool:
        """
        Get method for to enabled
        :return: enabled
        """
        return self.__enabled

    def set_enabled(self, enabled: bool) -> None:
        """
        Set method for to enabled
        :param enabled: enabled
        """
        self.__enabled = enabled

    def get_reason(self) -> Optional[str]:
        """
        Get method for to reason
        :return: reason
        """
        return self.__reason

    def set_reason(self, reason: Optional[str]) -> None:
        """
        Set method for to reason
        :param reason: reason
        """
        self.__reason = reason

    def to_json(self) -> dict:
        """
        data in json
        :return:
        """
        return ModelUtil.to_json(self)
