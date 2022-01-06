from src.bitpay_sdk.utils.key_utils import change_camel_case_to_snake_case


class SupportedTransactionCurrency(object):
    __enabled = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_enabled(self):
        return self.__enabled

    def set_enabled(self, enabled):
        self.__enabled = enabled

    def to_json(self):
        data = {
            "enabled": self.get_enabled(),
        }
        return data
