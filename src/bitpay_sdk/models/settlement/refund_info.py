class RefundInfo:
    __support_request = None
    __currency = None
    __amounts = None

    def __init__(self):
        pass

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
            "amounts": self.get_amounts(),
            "currency": self.get_currency()
        }
        return data
