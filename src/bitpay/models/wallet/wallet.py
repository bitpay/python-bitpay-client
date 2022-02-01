from .currencies import Currencies
from ...utils import key_utils


class Wallet(object):
    """
    supported wallets and supported currency details
    """

    __key = None
    __display_name = None
    __avatar = None
    __pay_pro = None
    __currencies = Currencies()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["currencies"]:

                    klass = globals()[key[0].upper() + key[1:]]

                    if isinstance(value, list):
                        objs = []
                        for obj in value:
                            objs.append(klass(**obj))
                        value = objs
                    else:
                        value = klass(**value)
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_key(self):
        """
        Get method for to key
        :return: key
        """
        return self.__key

    def set_key(self, key):
        """
        Set method for to key
        :param key: key
        """
        self.__key = key

    def get_display_name(self):
        """
        Get method for to display_name
        :return: display_name
        """
        return self.__display_name

    def set_display_name(self, display_name):
        """
        Set method for to display_name
        :param display_name: display_name
        """
        self.__display_name = display_name

    def get_avatar(self):
        """
        Get method for to avatar
        :return: avatar
        """
        return self.__avatar

    def set_avatar(self, avatar):
        """
        Set method for to avatar
        :param avatar: avatar
        """
        self.__avatar = avatar

    def get_pay_pro(self):
        """
        Get method for to paypro
        :return: paypro
        """
        return self.__paypro

    def set_pay_pro(self, paypro):
        """
        Set method for to paypro
        :param paypro: paypro
        """
        self.__paypro = paypro

    def get_currencies(self):
        """
        Get method for to currencies
        :return: currencies
        """
        return self.__currencies

    def set_currencies(self, currencies: Currencies):
        """
        Set method for to currencies
        :param currencies: currencies
        """
        self.__currencies = currencies

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "key": self.get_key(),
            "displayName": self.get_display_name(),
            "avatar": self.get_avatar(),
            "payPro": self.get_pay_pro(),
            "currencies": self.get_currencies(),
        }
        return data
