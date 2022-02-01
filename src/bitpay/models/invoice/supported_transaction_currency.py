"""
SupportedTransactionCurrency
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class SupportedTransactionCurrency:
    """
    currency selected for payment is enabled
    """

    __enabled = None
    __reason = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_enabled(self):
        """
        Get method for to enabled
        :return: enabled
        """
        return self.__enabled

    def set_enabled(self, enabled):
        """
        Set method for to enabled
        :param enabled: enabled
        """
        self.__enabled = enabled

    def get_reason(self):
        """
        Get method for to reason
        :return: reason
        """
        return self.__reason

    def set_reason(self, reason):
        """
        Set method for to reason
        :param reason: reason
        """
        self.__reason = reason

    def to_json(self):
        """
        data in json
        :return:
        """
        data = {"enabled": self.get_enabled(), "reason": self.get_reason()}
        return data
