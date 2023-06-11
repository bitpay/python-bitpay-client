"""
Ledger
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Ledger:
    """
    Ledgers are records of money movement.
    """

    __currency = None
    __balance = None

    def __init__(self, **kwargs: dict):
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"balance": "float"}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_currency(self) -> Optional[str]:
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: Optional[str]) -> None:
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_balance(self) -> Optional[float]:
        """
        Get method for to balance
        :return: balance
        """
        return self.__balance

    def set_balance(self, balance: Optional[float]) -> None:
        """
        Set method for to balance
        :param balance: balance
        """
        self.__balance = balance

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
