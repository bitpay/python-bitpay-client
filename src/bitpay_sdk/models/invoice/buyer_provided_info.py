class BuyerProvidedInfo:

    __name = ""
    __phone_number = ""
    __selected_wallet = ""
    __email_address = ""
    __selected_transaction_currency = ""

    def __init__(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_selected_wallet(self):
        return self.__selected_wallet

    def set_selected_wallet(self, selected_wallet):
        self.__selected_wallet = selected_wallet

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_selected_transaction_currency(self):
        return self.__selected_transaction_currency

    def set_selected_transaction_currency(self, selected_transaction_currency):
        self.__selected_transaction_currency = selected_transaction_currency
