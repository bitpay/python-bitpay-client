class WithHoldings:
    """
    Holdings
    """
    __amount = None
    __code = None
    __description = None
    __notes = None
    __label = None
    __bank_country = None

    def __init__(self):
        pass

    def get_amount(self):
        """
        Get method for to amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount):
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_code(self):
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for to code
        :param code: code
        """
        self.__code = code
