"""
ItemizedDetails
"""
from ...utils import key_utils


class ItemizedDetails:
    """
    object containing line item details for display
    """

    __amount = None
    __description = None
    __is_fee = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_amount(self):
        """
        Get method for the amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount):
        """
        Set method for the amount
        :param amount: amount
        """
        self.__amount = amount

    def get_description(self):
        """
        Get method for the description
        :return: description
        """
        return self.__description

    def set_description(self, description):
        """
        Set method for the description
        :param description: description
        """
        self.__description = description

    def get_is_fee(self):
        """
        Get method for the is_fee
        :return: is_fee
        """
        return self.__is_fee

    def set_is_fee(self, is_fee):
        """
        Set method for the is_fee
        :param is_fee: is_fee
        """
        self.__is_fee = is_fee

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "amount": self.get_amount(),
            "description": self.get_description(),
            "is_fee": self.get_is_fee(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
