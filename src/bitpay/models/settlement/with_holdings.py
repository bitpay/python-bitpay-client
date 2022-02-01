from ...utils.key_utils import change_camel_case_to_snake_case


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

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
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

    def get_description(self):
        """
        Get method for to description
        :return: description
        """
        return self.__description

    def set_description(self, description):
        """
        Set method for to description
        :param description: description
        """
        self.__description = description

    def get_notes(self):
        """
        Get method for to notes
        :return: notes
        """
        return self.__notes

    def set_notes(self, notes):
        """
        Set method for to notes
        :param notes: notes
        """
        self.__notes = notes

    def get_label(self):
        """
        Get method for to label
        :return: label
        """
        return self.__label

    def set_label(self, label):
        """
        Set method for to label
        :param label: label
        """
        self.__label = label

    def get_bank_country(self):
        """
        Get method for to bank_country
        :return: bank_country
        """
        return self.__bank_country

    def set_bank_country(self, bank_country):
        """
        Set method for to bank_country
        :param bank_country: bank_country
        """
        self.__bank_country = bank_country

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "amount": self.get_amount(),
            "code": self.get_code(),
            "description": self.get_description(),
            "notes": self.get_notes(),
            "label": self.get_label(),
            "bankCountry": self.get_bank_country(),
        }
        return data
