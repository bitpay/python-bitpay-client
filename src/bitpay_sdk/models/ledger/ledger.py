class Ledger:

    __currency = None
    __balance = None

    def __init__(self):
        pass

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def to_json(self):
        data = {
            "currency": self.get_currency(),
            "balance": self.get_balance(),
        }
        return data
