from src.bitpay_sdk.utils.key_utils import change_camel_case_to_snake_case


class Buyer(object):
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
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address1(self):
        return self.__address1

    def set_address1(self, address1):
        self.__address1 = address1

    def get_address2(self):
        return self.__address2

    def set_address2(self, address2):
        self.__address2 = address2

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_zip(self):
        return self.__zip

    def set_zip(self, zip):
        self.__zip = zip

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_notify(self):
        return self.__notify

    def set_notify(self, notify):
        self.__notify = notify

    def to_json(self):
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
        return data
