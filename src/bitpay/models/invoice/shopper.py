"""
Shopper
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Shopper:
    """
    shopper
    """

    __user = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_user(self):
        """
        Get method for to user
        :return: user
        """
        return self.__user

    def set_user(self, user):
        """
        Set method for to user
        :param user: user
        """
        self.__user = user

    def to_json(self):
        """
        :return: data in json
        """
        data = {"user": self.get_user()}
        return data
