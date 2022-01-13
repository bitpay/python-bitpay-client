from ...utils.key_utils import change_camel_case_to_snake_case


class SupportedTransactionCurrency:
    """
    currency selected for payment is enabled
    """
    __enabled = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

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

    def to_json(self):
        """
        data in json
        :return:
        """
        data = {
            "enabled": self.get_enabled(),
        }
        return data
