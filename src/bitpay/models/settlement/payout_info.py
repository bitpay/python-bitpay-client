"""
PayoutInfo: Object containing the settlement info provided by the Merchant
in his BitPay account settings
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutInfo:
    """
    PayoutInfo
    """

    __name = None
    __account = None
    __routing = None
    __merchant_ein = None
    __label = None
    __bank_country = None
    __bank = None
    __swift = None
    __address = None
    __city = None
    __postal = None
    __sort = None
    __wire = None
    __bank_name = None
    __bank_address = None
    __bank_address2 = None
    __iban = None
    __additional_information = None
    __account_holder_name = None
    __account_holder_address = None
    __account_holder_address2 = None
    __account_holder_postal_code = None
    __account_holder_city = None
    __account_holder_country = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key == "merchantEIN":
                    self.set_merchant_ein(value)
                else:
                    getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(
                        value
                    )
            except AttributeError:
                pass

    def get_name(self):
        """
        Get method for to name
        :return: name
        """
        return self.__name

    def set_name(self, name):
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_account(self):
        """
        Get method for to account
        :return: account
        """
        return self.__account

    def set_account(self, account):
        """
        Set method for to account
        :param account: account
        """
        self.__account = account

    def get_routing(self):
        """
        Get method for to routing
        :return: routing
        """
        return self.__routing

    def set_routing(self, routing):
        """
        Set method for to routing
        :param routing: routing
        """
        self.__routing = routing

    def get_merchant_ein(self):
        """
        Get method for to merchant_ein
        :return: merchant_ein
        """
        return self.__merchant_ein

    def set_merchant_ein(self, merchant_ein):
        """
        Set method for to merchant_ein
        :param merchant_ein: merchant_ein
        """
        self.__merchant_ein = merchant_ein

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

    def get_bank(self):
        """
        Get method for to bank
        :return: bank
        """
        return self.__bank

    def set_bank(self, bank):
        """
        Set method for to bank
        :param bank: bank
        """
        self.__bank = bank

    def get_swift(self):
        """
        Get method for to swift
        :return: swift
        """
        return self.__swift

    def set_swift(self, swift):
        """
        Set method for to swift
        :param swift: swift
        """
        self.__swift = swift

    def get_address(self):
        """
        Get method for to address
        :return: address
        """
        return self.__address

    def set_address(self, address):
        """
        Set method for to address
        :param address: address
        """
        self.__address = address

    def get_city(self):
        """
        Get method for to city
        :return: city
        """
        return self.__city

    def set_city(self, city):
        """
        Set method for to city
        :param city: city
        """
        self.__city = city

    def get_postal(self):
        """
        Get method for to postal
        :return: postal
        """
        return self.__postal

    def set_postal(self, postal):
        """
        Set method for to postal
        :param postal: postal
        """
        self.__postal = postal

    def get_sort(self):
        """
        Get method for to sort
        :return: sort
        """
        return self.__sort

    def set_sort(self, sort):
        """
        Set method for to sort
        :param sort: sort
        """
        self.__sort = sort

    def get_wire(self):
        """
        Get method for to wire
        :return: wire
        """
        return self.__wire

    def set_wire(self, wire):
        """
        Set method for to wire
        :param wire: wire
        """
        self.__wire = wire

    def get_bank_name(self):
        """
        Get method for to bank_name
        :return: bank_name
        """
        return self.__bank_name

    def set_bank_name(self, bank_name):
        """
        Set method for to bank_name
        :param bank_name: bank_name
        """
        self.__bank_name = bank_name

    def get_bank_address(self):
        """
        Get method for to bank_address
        :return: bank_address
        """
        return self.__bank_address

    def set_bank_address(self, bank_address):
        """
        Set method for to bank_address
        :param bank_address: bank_address
        """
        self.__bank_address = bank_address

    def get_bank_address2(self):
        """
        Get method for to bank_address2
        :return: bank_address2
        """
        return self.__bank_address2

    def set_bank_address2(self, bank_address2):
        """
        Set method for to bank_address2
        :param bank_address2: bank_address2
        """
        self.__bank_address2 = bank_address2

    def get_iban(self):
        """
        Get method for to iban
        :return: iban
        """
        return self.__iban

    def set_iban(self, iban):
        """
        Set method for to iban
        :param iban: iban
        """
        self.__iban = iban

    def get_additional_information(self):
        """
        Get method for to additional_information
        :return: additional_information
        """
        return self.__additional_information

    def set_additional_information(self, additional_information):
        """
        Set method for to additional_information
        :param additional_information: additional_information
        """
        self.__additional_information = additional_information

    def get_account_holder_name(self):
        """
        Get method for to account_holder_name
        :return: account_holder_name
        """
        return self.__account_holder_name

    def set_account_holder_name(self, account_holder_name):
        """
        Set method for to account_holder_name
        :param account_holder_name: account_holder_name
        """
        self.__account_holder_name = account_holder_name

    def get_account_holder_address(self):
        """
        Get method for to account_holder_address
        :return: account_holder_address
        """
        return self.__account_holder_address

    def set_account_holder_address(self, account_holder_address):
        """
        Set method for to account_holder_address
        :param account_holder_address: account_holder_address
        """
        self.__account_holder_address = account_holder_address

    def get_account_holder_address2(self):
        """
        Get method for to account_holder_address2
        :return: account_holder_address2
        """
        return self.__account_holder_address2

    def set_account_holder_address2(self, account_holder_address2):
        """
        Set method for to account_holder_address2
        :param account_holder_address2: account_holder_address2
        """
        self.__account_holder_address2 = account_holder_address2

    def get_account_holder_postal_code(self):
        """
        Get method for to account_holder_postal_code
        :return: account_holder_postal_code
        """
        return self.__account_holder_postal_code

    def set_account_holder_postal_code(self, account_holder_postal_code):
        """
        Set method for to account_holder_postal_code
        :param account_holder_postal_code: account_holder_postal_code
        """
        self.__account_holder_postal_code = account_holder_postal_code

    def get_account_holder_city(self):
        """
        Get method for to account_holder_city
        :return: account_holder_city
        """
        return self.__account_holder_city

    def set_account_holder_city(self, account_holder_city):
        """
        Set method for to account_holder_city
        :param account_holder_city: account_holder_city
        """
        self.__account_holder_city = account_holder_city

    def get_account_holder_country(self):
        """
        Get method for to account_holder_country
        :return: account_holder_country
        """
        return self.__account_holder_country

    def set_account_holder_country(self, account_holder_country):
        """
        Set method for to account_holder_country
        :param account_holder_country: account_holder_country
        """
        self.__account_holder_country = account_holder_country

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "label": self.get_label(),
            "bankCountry": self.get_bank_country(),
            "name": self.get_name(),
            "bank": self.get_bank(),
            "swift": self.get_swift(),
            "address": self.get_address(),
            "city": self.get_city(),
            "postal": self.get_postal(),
            "sort": self.get_sort(),
            "wire": self.get_wire(),
            "bankName": self.get_bank_name(),
            "bankAddress": self.get_bank_address(),
            "iban": self.get_iban(),
            "additionalInformation": self.get_additional_information(),
            "accountHolderName": self.get_account_holder_name(),
            "accountHolderAddress": self.get_account_holder_address(),
            "accountHolderAddress2": self.get_account_holder_address2(),
            "accountHolderPostalCode": self.get_account_holder_postal_code(),
            "accountHolderCity": self.get_account_holder_city(),
            "accountHolderCountry": self.get_account_holder_country(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
