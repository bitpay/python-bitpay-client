"""
Buyer
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class Buyer:
    """
    Allows merchant to pass buyer related information in the invoice object
    """

    __name = ""
    __address1 = ""
    __address2 = ""
    __locality = ""
    __region = ""
    __postal_code = ""
    __country = ""
    __email = ""
    __phone = ""
    __notify = ""
    __buyer_email = ""

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
        Set method for the name
        :param name: name
        """
        self.__name = name

    def get_buyer_email(self):
        """
        Get method for the buyer_email
        :return: buyer_email
        """
        return self.__buyer_email

    def set_buyer_email(self, buyer_email):
        """
        Set method for the buyer_email
        :param buyer_email: buyer_email
        """
        self.__buyer_email = buyer_email

    def get_address1(self):
        """
        Get method for the address1
        :return: address1
        """
        return self.__address1

    def set_address1(self, address1):
        """
        Set method for the address1
        :param address1: address1
        """
        self.__address1 = address1

    def get_address2(self):
        """
        Get method for the address2
        :return: address2
        """
        return self.__address2

    def set_address2(self, address2):
        """
        Set method for the address2
        :param address2: address2
        """
        self.__address2 = address2

    def get_locality(self):
        """
        Get method for the locality
        :return: locality
        """
        return self.__locality

    def set_locality(self, locality):
        """
        Set method for the locality
        :param locality: locality
        """
        self.__locality = locality

    def get_region(self):
        """
        Get method for the region
        :return: region
        """
        return self.__region

    def set_region(self, region):
        """
        Set method for the region
        :param region: region
        """
        self.__region = region

    def get_postal_code(self):
        """
        Get method for the postal_code
        :return: postal_code
        """
        return self.__postal_code

    def set_postal_code(self, postal_code):
        """
        Set method for the postal_code
        :param postal_code: postal_code
        """
        self.__postal_code = postal_code

    def get_country(self):
        """
        Get method for the country
        :return: country
        """
        return self.__country

    def set_country(self, country):
        """
        Set method for the country
        :param country: country
        """
        self.__country = country

    def get_email(self):
        """
        Get method for the email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for the email
        :param email: email
        """
        self.__email = email

    def get_phone(self):
        """
        Get method for the phone
        :return: phone
        """
        return self.__phone

    def set_phone(self, phone):
        """
        Set method for the phone
        :param phone: phone
        """
        self.__phone = phone

    def get_notify(self):
        """
        Get method for to notify
        :return: notify
        """
        return self.__notify

    def set_notify(self, notify):
        """
        Set method for to notify
        :param notify: notify
        """
        self.__notify = notify

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "name": self.get_name(),
            "address1": self.get_address1(),
            "address2": self.get_address2(),
            "locality": self.get_locality(),
            "region": self.get_region(),
            "postalCode": self.get_postal_code(),
            "country": self.get_country(),
            "email": self.get_email(),
            "phone": self.get_phone(),
            "notify": self.get_notify(),
            "buyerEmail": self.get_buyer_email(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
