"""
PayoutReceivedInfo
"""
from ...utils.key_utils import change_camel_case_to_snake_case
from .payout_received_info_address import PayoutReceivedInfoAddress


class PayoutReceivedInfo:
    """
    PayoutReceivedInfo
    """

    __name = None
    __email = None
    __address = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_name(self):
        """
        Get method for to name
        :return: name
        """
        return self.__name

    def set_name(self, name):
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_email(self):
        """
        Get method for to email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_address(self):
        """
        Get method for to address
        :return: address
        """
        return self.__address

    def set_address(self, address: PayoutReceivedInfoAddress):
        """
        Set method for to address
        :param address: address
        """
        self.__address = address

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "name": self.get_name(),
            "email": self.get_email(),
            "address": self.get_address(),
        }
        return data
