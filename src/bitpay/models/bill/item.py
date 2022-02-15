"""
Item
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Item:
    """
    List of line items
    """

    __id = None
    __description = None
    __price = None
    __quantity = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_id(self):
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_description(self):
        """
        Get method for to description
        :return: description
        """
        return self.__description

    def set_description(self, description):
        """
        Set method for to description
        :param description: description
        """
        self.__description = description

    def get_price(self):
        """
        Get method for to price
        :return: price
        """
        return self.__price

    def set_price(self, price):
        """
        Set method for to price
        :param price: price
        """
        self.__price = price

    def get_quantity(self):
        """
        Get method for to quantity
        :return: quantity
        """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        Set method for to quantity
        :param quantity: quantity
        """
        self.__quantity = quantity

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "id": self.get_id(),
            "description": self.get_description(),
            "price": self.get_price(),
            "quantity": self.get_quantity(),
        }
        return data
