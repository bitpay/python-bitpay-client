class Ledger:
    """
    Ledgers are records of money movement.
    """
    __currency = None
    __balance = None

    def __init__(self):
        pass

    def get_currency(self):
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_balance(self):
        """
        Get method for to balance
        :return: balance
        """
        return self.__balance

    def set_balance(self, balance):
        """
        Set method for to balance
        :param balance: balance
        """
        self.__balance = balance

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "currency": self.get_currency(),
            "balance": self.get_balance(),
        }
        return data
