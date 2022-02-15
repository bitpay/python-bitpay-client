"""
Currency Qr
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class CurrencyQr:
    """
    Currency Qr
    """

    __type = None
    __collapsed = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_type(self):
        """
        Get method for to type
        :return: type
        """
        return self.__type

    def set_type(self, type):
        """
        Set method for to type
        :param type: type
        """
        self.__type = type

    def get_collapsed(self):
        """
        Get method for to collapsed
        :return: collapsed
        """
        return self.__collapsed

    def set_collapsed(self, collapsed):
        """
        Set method for to collapsed
        :param collapsed: collapsed
        """
        self.__collapsed = collapsed

    def to_json(self):
        """
        :return: data in json
        """
        data = {"type": self.get_type(), "collapsed": self.get_collapsed()}
        return data
