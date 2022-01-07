from src.bitpay_sdk.utils import key_utils


class UniversalCodes(object):

    __payment_string = None
    __verification_link = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % key_utils.change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_payment_string(self):
        return self.__payment_string

    def set_payment_string(self, payment_string):
        self.__payment_string = payment_string

    def get_verification_link(self):
        return self.__verification_link

    def set_verification_link(self, payment_string):
        self.__payment_string = payment_string

    def to_json(self):
        data = {
            "paymentString": self.get_payment_string(),
            "verificationLink": self.get_verification_link()
        }
        return data
