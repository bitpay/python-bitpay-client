from src.bitpay_sdk.utils import key_utils
from .currencies import Currencies


class Wallet(object):
    __key = None
    __display_name = None
    __avatar = None
    __paypro = None
    __currencies = Currencies()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["currencies"]:
                    klass = globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(self, 'set_%s' % key_utils.change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_display_name(self):
        return self.__display_name

    def set_display_name(self, display_name):
        self.__display_name = display_name

    def get_avatar(self):
        return self.__avatar

    def set_avatar(self, avatar):
        self.__avatar = avatar

    def get_paypro(self):
        return self.__paypro

    def set_paypro(self, paypro):
        self.__paypro = paypro

    def get_currencies(self):
        return self.__currencies

    def set_currencies(self, currencies: Currencies):
        self.__currencies = currencies

    def to_json(self):
        data = {
            'key': self.get_key(),
            'displayName': self.get_display_name(),
            'avatar': self.get_avatar(),
            'paypro': self.get_paypro(),
            'currencies': self.get_currencies()
        }
        return data

