class Buyer:
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

    def __init__(self):
        pass

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

    def get_locality(self):
        return self.__locality

    def set_locality(self, locality):
        self.__locality = locality

    def get_region(self):
        return self.__region

    def set_region(self, region):
        self.__region = region

    def get_postal_code(self):
        return self.__postal_code

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

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
