"""
PayoutTransaction
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutTransaction:
    """
    PayoutTransaction
    """

    __txid = None
    __amount = None
    __date = None
    __confirmations = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_txid(self):
        """
        Get method for txid
        :return: txid
        """
        return self.__txid

    def set_txid(self, txid):
        """
        Set method for to txid
        :param txid: txid
        """
        self.__txid = txid

    def get_amount(self):
        """
        Get method for amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount):
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_confirmations(self):
        """
        Get method for confirmations
        :return: confirmations
        """
        return self.__confirmations

    def set_confirmations(self, confirmations):
        """
        Set method for to confirmations
        :param confirmations: confirmations
        """
        self.__confirmations = confirmations

    def get_date(self):
        """
        Get method for date
        :return: date
        """
        return self.__date

    def set_date(self, date):
        """
        Set method for to date
        :param date: date
        """
        self.__date = date

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "txid": self.get_txid(),
            "amount": self.get_amount(),
            "date": self.get_date(),
            "confirmations": self.get_confirmations(),
        }
        return data
