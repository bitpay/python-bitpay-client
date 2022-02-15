"""
UniversalCodes
"""
from ...utils import key_utils


class UniversalCodes:
    """
    object containing wallet-specific URLs for payment protocol
    """

    __payment_string = None
    __verification_link = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_payment_string(self):
        """
        Get method for to payment_string
        :return: payment_string
        """
        return self.__payment_string

    def set_payment_string(self, payment_string):
        """
        Set method for to payment_string
        :param payment_string: payment_string
        """
        self.__payment_string = payment_string

    def get_verification_link(self):
        """
        Get method for to enabled
        :return: enabled
        """
        return self.__verification_link

    def set_verification_link(self, verification_link):
        """
        Set method for to verification_link
        :param verification_link: verification_link
        """
        self.__verification_link = verification_link

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "paymentString": self.get_payment_string(),
            "verificationLink": self.get_verification_link(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
