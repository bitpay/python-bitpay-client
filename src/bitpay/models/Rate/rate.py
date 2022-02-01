"""
Rate
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Rate:
    """
    Rate
    """

    __name = None
    __code = None
    __rate = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_name(self):
        """
        Get method for the name
        :return: name
        """
        return self.__name

    def set_name(self, name):
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_code(self):
        """
        Get method for the code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_rate(self):
        """
        Get method for the rate
        :return: rate
        """
        return self.__rate

    def set_rate(self, rate):
        """
        Set method for to rate
        :param rate: rate
        """
        self.__rate = rate

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "name": self.get_name(),
            "code": self.get_code(),
            "rate": self.get_rate(),
        }
        return data
