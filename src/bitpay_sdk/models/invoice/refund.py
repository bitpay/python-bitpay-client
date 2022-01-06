from .refund_params import RefundParams


class Refund(object):

    __guid = None
    __refund_email = None
    __amount = None
    __currency = None
    __token = None
    __id = None
    __request_data = None
    __status = None
    __params = None

    def __init__(self, refund_email: str = "", amount: float = 0.0, currency: str = "", token: str = ""):
        self.__refund_email = refund_email
        self.__amount = amount
        self.__currency = currency
        self.__token = token
        self.__params = RefundParams()

    def get_guid(self):
        return self.__guid

    def set_guid(self, guid):
        self.__guid = guid

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount
