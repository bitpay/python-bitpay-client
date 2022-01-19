class PayoutInstructionBtcSummary:
    __paid = None
    __unpaid = None

    def __init__(self, paid, unpaid):
        self.__paid = paid
        self.__unpaid = unpaid

    def get_paid(self):
        """
        Get method for to paid
        :return: paid
        """
        return self.__paid

    def set_paid(self, paid):
        """
        Set method for to paid
        :param paid: paid
        """
        self.__paid = paid

    def get_unpaid(self):
        """
        Get method for to unpaid
        :return: unpaid
        """
        return self.__unpaid

    def set_unpaid(self, unpaid):
        """
        Set method for to unpaid
        :param unpaid: unpaid
        """
        self.__unpaid = unpaid

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "paid": self.get_paid(),
            "unpaid": self.get_unpaid(),
        }
        return data
