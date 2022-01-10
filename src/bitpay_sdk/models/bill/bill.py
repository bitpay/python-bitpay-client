from .item import Item


class Bill:
    __currency = None
    __token = ""
    __email = None
    __items = None
    __number = None
    __name = None
    __address1 = None
    __address2 = None
    __city = None
    __state = None
    __zip = None
    __country = None
    __cc = None
    __phone = None
    __due_date = None
    __pass_processing_fee = None
    __status = None
    __url = None
    __create_date = None
    __id = None
    __merchant = None

    def __init__(self, number=None, currency=None, email=None, items: Item = None):
        self.__number = number
        self.__currency = currency
        self.__email = email
        self.__items = items

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        # TODO : Reflection Class problem
        pass

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

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

    def get_cc(self):
        return self.__cc

    def set_cc(self, cc):
        self.__cc = cc

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_due_date(self):
        return self.__due_date

    def set_due_date(self, due_date):
        self.__due_date = due_date

    def get_pass_processing_fee(self):
        return self.__pass_processing_fee

    def set_pass_processing_fee(self, pass_processing_fee):
        self.__pass_processing_fee = pass_processing_fee

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_create_date(self):
        return self.__create_date

    def set_create_date(self, create_date):
        self.__create_date = create_date

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_merchant(self):
        return self.__merchant

    def set_merchant(self, merchant):
        self.__merchant = merchant

    def get_items(self):
        return self.__items

    def set_items(self, item:Item):
        self.__items = item

    def to_json(self):
        data = {
            "currency": self.get_currency(),
            "token": self.get_token(),
            "email": self.get_email(),
            "items": self.get_items(),
            "number": self.get_number(),
            "name": self.get_name(),
            "address1": self.get_address1(),
            "address2": self.get_address2(),
            "city": self.get_city(),
            "state": self.get_state(),
            "zip": self.get_zip(),
            "country": self.get_country(),
            "cc": self.get_cc(),
            "phone": self.get_phone(),
            "dueDate": self.get_due_date(),
            "passProcessingFee": self.get_pass_processing_fee(),
            "status": self.get_status(),
            "url": self.get_url(),
            "createDate": self.get_create_date(),
            "id": self.get_id(),
            "merchant": self.get_merchant()
        }
        return data
