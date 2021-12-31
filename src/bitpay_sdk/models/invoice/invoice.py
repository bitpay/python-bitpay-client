from .buyer import Buyer


class Invoice:
    __currency = ""

    __guid = ""
    __token = ""

    __price = ""
    __id = ""
    __buyer = ""
    __buyer_provided_email = ""
    __buyer_provided_info = ""

    def __init__(self, price=None, currency=None):
        self.__price = price
        self.__currency = currency
        self.__buyer = Buyer()
        # TODO: Add buyer provided info

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    # Buyer Data
    def get_buyer(self):
        return self.__buyer

    def set_buyer(self, buyer: Buyer):
        self.__buyer = buyer

    def to_json(self):
        data = {
            "currency": self.get_currency(),
            "price": self.get_price(),
            "token": self.get_token()
        }
        return data
