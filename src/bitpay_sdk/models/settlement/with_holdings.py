class WithHoldings:
    __amount = None
    __code = None
    __description = None
    __notes = None
    __label = None
    __bank_country = None

    def __init__(self):
        pass

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

