"""
ItemizedDetails
"""
from typing import Optional

from bitpay.utils import key_utils
from bitpay.utils.model_util import ModelUtil


class ItemizedDetails:
    """
    object containing line item details for display
    """

    __amount = None
    __description = None
    __is_fee = False

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {"amount": "float", "isFee": "bool"}, {}
                )
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_amount(self) -> Optional[float]:
        """
        Get method for the amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount: Optional[float]) -> None:
        """
        Set method for the amount
        :param amount: amount
        """
        self.__amount = amount

    def get_description(self) -> Optional[str]:
        """
        Get method for the description
        :return: description
        """
        return self.__description

    def set_description(self, description: Optional[str]) -> None:
        """
        Set method for the description
        :param description: description
        """
        self.__description = description

    def get_is_fee(self) -> bool:
        """
        Get method for the is_fee
        :return: is_fee
        """
        return self.__is_fee

    def set_is_fee(self, is_fee: bool) -> None:
        """
        Set method for the is_fee
        :param is_fee: is_fee
        """
        self.__is_fee = is_fee

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
