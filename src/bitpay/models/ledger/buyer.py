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
    __city = ""
    __state = ""
    __zip = ""
    __country = ""
    __email = ""
    __phone = ""
    __notify = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
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

    def get_address1(self):
        """
        Get method for to address1
        :return: address1
        """
        return self.__address1

    def set_address1(self, address1):
        """
        Set method for to address1
        :param address1: address1
        """
        self.__address1 = address1

    def get_address2(self):
        """
        Get method for to address2
        :return: address2
        """
        return self.__address2

    def set_address2(self, address2):
        """
        Set method for to address2
        :param address2: address2
        """
        self.__address2 = address2

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

    def get_state(self):
        """
        Get method for to state
        :return: state
        """
        return self.__state

    def set_state(self, state):
        """
        Set method for to state
        :param state: state
        """
        self.__state = state

    def get_zip(self):
        """
        Get method for to zip
        :return: zip
        """
        return self.__zip

    def set_zip(self, zip):
        """
        Set method for to zip
        :param zip: zip
        """
        self.__zip = zip

    def get_country(self):
        """
        Get method for to country
        :return: country
        """
        return self.__country

    def set_country(self, country):
        """
        Set method for to country
        :param country: country
        """
        self.__country = country

    def get_email(self):
        """
        Get method for to email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_phone(self):
        """
        Get method for to phone
        :return: phone
        """
        return self.__phone

    def set_phone(self, phone):
        """
        Set method for to phone
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
            "city": self.get_city(),
            "state": self.get_state(),
            "zip": self.get_zip(),
            "country": self.get_country(),
            "email": self.get_email(),
            "phone": self.get_phone(),
            "notify": self.get_notify(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
