from .models.facade import Facade


class Tokens:
    __merchant = ""
    __payout = ""

    def __init__(self, merchant=None, payout = None):
        self.__merchant = merchant
        self.__payout = payout

    def get_token_by_facade(self, facade):

        token = None

        if Facade.Merchant == "Merchant":
            token = self.__merchant
        elif Facade.Payout == "Payout":
            token = self.__payout

        if token:
            return token

        raise Exception("given facade does not exist or no token defined for the given facade")

    def get_merchant_token(self):
        return self.__merchant

    def set_merchant_token(self, merchant):
        self.__merchant = merchant

    def get_payout_token(self):
        return self.__payout

    def set_payout_token(self, payout):
        self.__payout = payout
