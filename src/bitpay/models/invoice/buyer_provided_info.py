"""
BuyerProvidedInfo: Information collected from the buyer during the process of paying
an invoice. Initially this object is empty.
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class BuyerProvidedInfo:
    """
    Information collected from the buyer during the process of paying an invoice.
     Initially this object is empty.
    """

    __name = ""
    __phone_number = ""
    __selected_wallet = ""
    __email_address = ""
    __selected_transaction_currency = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_name(self):
        """
        Get method for the name
        :return: name
        """
        return self.__name

    def set_name(self, name):
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_phone_number(self):
        """
        Get method for the phone_number
        :return: phone_number
        """
        return self.__phone_number

    def set_phone_number(self, phone_number):
        """
        Set method for to phone_number
        :param phone_number: phone_number
        """
        self.__phone_number = phone_number

    def get_selected_wallet(self):
        """
        Get method for the selected_wallet
        :return: selected_wallet
        """
        return self.__selected_wallet

    def set_selected_wallet(self, selected_wallet):
        """
        Set method for to selected_wallet
        :param selected_wallet: selected_wallet
        """
        self.__selected_wallet = selected_wallet

    def get_email_address(self):
        """
        Get method for the email_address
        :return: email_address
        """
        return self.__email_address

    def set_email_address(self, email_address):
        """
        Set method for to email_address
        :param email_address: email_address
        """
        self.__email_address = email_address

    def get_selected_transaction_currency(self):
        """
        Get method for the selected_transaction_currency
        :return: selected_transaction_currency
        """
        return self.__selected_transaction_currency

    def set_selected_transaction_currency(self, selected_transaction_currency):
        """
        Set method for to selected_transaction_currency
        :param selected_transaction_currency: selected_transaction_currency
        """
        self.__selected_transaction_currency = selected_transaction_currency

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "name": self.get_name(),
            "phoneNumber": self.get_phone_number(),
            "selectedWallet": self.get_selected_wallet(),
            "emailAddress": self.get_email_address(),
            "selectedTransactionCurrency": self.get_selected_transaction_currency(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
