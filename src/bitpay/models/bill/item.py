"""
Item
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Item:
    """
    List of line items
    """

    __id = None
    __description = None
    __price = None
    __quantity = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {"price": "float", "quantity": "int"}, {}
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_id(self) -> Optional[str]:
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id: Optional[str]) -> None:
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_description(self) -> Optional[str]:
        """
        Get method for to description
        :return: description
        """
        return self.__description

    def set_description(self, description: Optional[str]) -> None:
        """
        Set method for to description
        :param description: description
        """
        self.__description = description

    def get_price(self) -> Optional[float]:
        """
        Get method for to price
        :return: price
        """
        return self.__price

    def set_price(self, price: Optional[float]) -> None:
        """
        Set method for to price
        :param price: price
        """
        self.__price = price

    def get_quantity(self) -> Optional[int]:
        """
        Get method for to quantity
        :return: quantity
        """
        return self.__quantity

    def set_quantity(self, quantity: Optional[int]) -> None:
        """
        Set method for to quantity
        :param quantity: quantity
        """
        self.__quantity = quantity

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
