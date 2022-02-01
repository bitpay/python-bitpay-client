"""
BIll Data
"""
from .item import Item
from ..currency import Currency
from ...exceptions.bitpay_exception import BitPayException
from ...utils.key_utils import change_camel_case_to_snake_case


class BillData:
    """
    Bill Data
    """

    __email_bill = None
    __cc = None
    __number = None
    __currency = None
    __name = None
    __address1 = None
    __address2 = None
    __city = None
    __state = None
    __zip = None
    __country = None
    __email = None
    __phone = None
    __due_date = None
    __pass_processing_fee = None
    __items = None
    __merchant = None

    def __init__(self, currency, email, due_date=None, **kwargs):
        if currency:
            self.set_currency(currency)
        self.set_email(email)
        self.set_due_date(due_date)

        for key, value in kwargs.items():
            try:
                if key in ["items"]:
                    klass = (
                        Item if key == "items" else globals()[key[0].upper() + key[1:]]
                    )

                    if isinstance(value, list):
                        objs = []
                        for obj in value:
                            objs.append(klass(**obj))
                        value = objs
                    else:
                        value = klass(**value)
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_email_bill(self):
        """
        Get method for the email_bill
        :return: email_bill
        """
        return self.__email_bill

    def set_email_bill(self, email_bill):
        """
        Set method for the email_bill
        :param email_bill: email_bill
        """
        self.__email_bill = email_bill

    def get_cc(self):
        """
        Get method for the cc
        :return: cc
        """
        return self.__cc

    def set_cc(self, cc):
        """
        Set method for the cc
        :param cc: cc
        """
        self.__cc = cc

    def get_number(self):
        """
        Get method for the number
        :return: number
        """
        return self.__number

    def set_number(self, number):
        """
        Set method for the number
        :param number: number
        """
        self.__number = number

    def get_currency(self):
        """
        Get method for the currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for the currency
        :param currency: currency
        """
        if not Currency.is_valid(currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__currency = currency

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

    def get_city(self):
        """
        Get method for the city
        :return: city
        """
        return self.__city

    def set_city(self, city):
        """
        Set method for the city
        :param city: city
        """
        self.__city = city

    def get_state(self):
        """
        Get method for the state
        :return: state
        """
        return self.__state

    def set_state(self, state):
        """
        Set method for the state
        :param state: state
        """
        self.__state = state

    def get_zip(self):
        """
        Get method for the zip
        :return: zip
        """
        return self.__zip

    def set_zip(self, zip):
        """
        Set method for the zip
        :param zip: zip
        """
        self.__zip = zip

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

    def get_due_date(self):
        """
        Get method for the due_date
        :return: due_date
        """
        return self.__due_date

    def set_due_date(self, due_date):
        """
        Set method for the due_date
        :param due_date: due_date
        """
        self.__due_date = due_date

    def get_pass_processing_fee(self):
        """
        Get method for the pass_processing_fee
        :return: pass_processing_fee
        """
        return self.__pass_processing_fee

    def set_pass_processing_fee(self, pass_processing_fee):
        """
        Set method for the pass_processing_fee
        :param pass_processing_fee: pass_processing_fee
        """
        self.__pass_processing_fee = pass_processing_fee

    def get_items(self):
        """
        Get method for the items
        :return: items
        """
        return self.__items

    def set_items(self, items: [Item]):
        """
        Set method for the items
        :param items: items
        """
        self.__items = items

    def get_merchant(self):
        """
        Get method for the merchant
        :return: merchant
        """
        return self.__merchant

    def set_merchant(self, merchant):
        """
        Set method for the merchant
        :param merchant: merchant
        """
        self.__merchant = merchant

    def to_json(self):
        """
        :return: data in json
        """
        items = []
        for item in self.get_items():
            items.append(item.to_json())
        data = {
            "emailBill": self.get_email_bill(),
            "cc": self.get_cc(),
            "number": self.get_number(),
            "currency": self.get_currency(),
            "name": self.get_name(),
            "address1": self.get_address1(),
            "address2": self.get_address2(),
            "city": self.get_city(),
            "state": self.get_state(),
            "zip": self.get_zip(),
            "country": self.get_country(),
            "email": self.get_email(),
            "phone": self.get_phone(),
            "dueDate": self.get_due_date(),
            "passProcessingFee": self.get_pass_processing_fee(),
            "items": items,
            "merchant": self.get_merchant(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
