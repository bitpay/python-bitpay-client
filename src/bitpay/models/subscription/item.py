"""
Item
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Item:
    """
    Item
    """

    __description = None
    __price = None
    __quantity = None

    def __init__(self, price=0.0, quantity=0, description="", **kwargs):
        self.set_price(price)
        self.set_quantity(quantity)
        self.set_description(description)

        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_description(self):
        """
        Get method for the description
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
        Get method for the price
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
        Get method for the quantity
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
            "price": self.get_price(),
            "description": self.get_description(),
            "quantity": self.get_quantity(),
        }
        return data
