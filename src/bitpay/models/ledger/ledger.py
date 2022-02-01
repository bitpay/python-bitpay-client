"""
Ledger
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Ledger:
    """
    Ledgers are records of money movement.
    """

    __currency = None
    __balance = None
    __parent = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_currency(self):
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_balance(self):
        """
        Get method for to balance
        :return: balance
        """
        return self.__balance

    def set_balance(self, balance):
        """
        Set method for to balance
        :param balance: balance
        """
        self.__balance = balance

    def get_parent(self):
        """
        Get method for to parent
        :return: parent
        """
        return self.__parent

    def set_parent(self, parent):
        """
        Set method for to parent
        :param parent: parent
        """
        self.__parent = parent

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "currency": self.get_currency(),
            "balance": self.get_balance(),
        }
        return data
