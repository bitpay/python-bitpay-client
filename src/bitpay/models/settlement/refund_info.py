"""
RefundInfo: Object containing information about the refund executed for the invoice
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class RefundInfo:
    """
    Information about refund
    """

    __support_request = None
    __currency = None
    __amounts = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_support_request(self):
        """
        Get method for to support_request
        :return: support_request
        """
        return self.__support_request

    def set_support_request(self, support_request):
        """
        Set method for to support_request
        :param support_request: support_request
        """
        self.__support_request = support_request

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

    def get_amounts(self):
        """
        Get method for to amounts
        :return: amounts
        """
        return self.__amounts

    def set_amounts(self, amounts):
        """
        Set method for to amounts
        :param amounts: amounts
        """
        self.__amounts = amounts

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "supportRequest": self.get_support_request(),
            "amounts": self.get_amounts(),
            "currency": self.get_currency(),
        }
        return data
