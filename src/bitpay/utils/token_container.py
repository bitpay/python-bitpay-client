from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.models.facade import Facade


class TokenContainer:
    __data__ = None

    def __init__(self):
        self.__data__ = {}

    def get_access_token(self, facade):
        if not isinstance(facade, Facade):
            raise BitPayException("Wrong facade")

        try:
            return self.__data__[facade]
        except Exception as exe:
            raise BitPayException("There is no token for the specified key: ", str(exe))

    def put(self, key, value):
        self.__data__[key] = value

    def add_pos(self, token):
        self.__data__[Facade.POS] = token

    def add_merchant(self, token):
        self.__data__[Facade.MERCHANT] = token

    def add_payout(self, token):
        self.__data__[Facade.PAYOUT] = token
