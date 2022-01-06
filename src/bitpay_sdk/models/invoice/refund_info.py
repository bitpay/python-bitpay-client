from src.bitpay_sdk.utils.key_utils import change_camel_case_to_snake_case


class RefundInfo(object):
    __support_request = None
    __currency = None
    __amounts = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_support_request(self):
        return self.__support_request

    def set_support_request(self, support_request):
        self.__support_request = support_request

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_amounts(self):
        return self.__amounts

    def set_amounts(self, amounts):
        self.__amounts = amounts

    def to_json(self):
        data = {
            "supportRequest": self.get_support_request(),
            "currency": self.get_currency(),
            "amounts": self.get_amounts()
        }
        return data
