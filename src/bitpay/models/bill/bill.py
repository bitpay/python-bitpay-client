"""
Bill
"""
from .item import Item
from ..currency import Currency
from ...exceptions.bitpay_exception import BitPayException
from ...utils.key_utils import change_camel_case_to_snake_case


class Bill:
    """
    Bills are payment requests addressed to specific buyers.
    Bill line items have fixed prices, typically denominated
    in fiat currency.
    """

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
    __delivered = None
    __phone = None
    __due_date = None
    __pass_processing_fee = None
    __status = None
    __url = None
    __created_date = None
    __email_bill = None
    __id = None
    __merchant = None

    def __init__(self, number=None, currency=None, email=None, **kwargs):
        self.set_number(number)
        self.set_currency(currency)
        self.set_email(email)

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

    def get_currency(self):
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for to currency
        :param currency: currency
        """
        if not Currency.is_valid(currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__currency = currency

    def get_token(self):
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def get_delivered(self):
        """
        Get method for to delivered
        :return: delivered
        """
        return self.__delivered

    def set_delivered(self, delivered):
        """
        Set method for to delivered
        :param delivered: delivered
        """
        self.__delivered = delivered

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

    def get_number(self):
        """
        Get method for to number
        :return: number
        """
        return self.__number

    def set_number(self, number):
        """
        Set method for to number
        :param number: number
        """
        self.__number = number

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

    def get_cc(self):
        """
        Get method for to cc
        :return: cc
        """
        return self.__cc

    def set_cc(self, cc):
        """
        Set method for to cc
        :param cc: cc
        """
        self.__cc = cc

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

    def get_due_date(self):
        """
        Get method for to due_date
        :return: due_date
        """
        return self.__due_date

    def set_due_date(self, due_date):
        """
        Set method for to due_date
        :param due_date: due_date
        """
        self.__due_date = due_date

    def get_pass_processing_fee(self):
        """
        Get method for to pass_processing_fee
        :return: pass_processing_fee
        """
        return self.__pass_processing_fee

    def set_pass_processing_fee(self, pass_processing_fee):
        """
        Set method for to pass_processing_fee
        :param pass_processing_fee: pass_processing_fee
        """
        self.__pass_processing_fee = pass_processing_fee

    def get_status(self):
        """
        Get method for to status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_url(self):
        """
        Get method for to url
        :return: url
        """
        return self.__url

    def set_url(self, url):
        """
        Set method for to url
        :param url: url
        """
        self.__url = url

    def get_created_date(self):
        """
        Get method for to created_date
        :return: created_date
        """
        return self.__created_date

    def set_created_date(self, created_date):
        """
        Set method for to created_date
        :param created_date: created_date
        """
        self.__created_date = created_date

    def get_email_bill(self):
        """
        Get method for to email_bill
        :return: email_bill
        """
        return self.__email_bill

    def set_email_bill(self, email_bill):
        """
        Set method for to email_bill
        :param email_bill: email_bill
        """
        self.__email_bill = email_bill

    def get_id(self):
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_merchant(self):
        """
        Get method for to merchant
        :return: merchant
        """
        return self.__merchant

    def set_merchant(self, merchant):
        """
        Set method for to merchant
        :param merchant: merchant
        """
        self.__merchant = merchant

    def get_items(self):
        """
        Get method for to item
        :return: item
        """
        return self.__items

    def set_items(self, item: [Item]):
        """
        Set method for to item
        :param item: item
        """
        self.__items = item

    def to_json(self):
        """
        :return: data in json
        """
        items = []
        for item in self.get_items():
            items.append(item.to_json())
        data = {
            "currency": self.get_currency(),
            "token": self.get_token(),
            "email": self.get_email(),
            "items": items,
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
            "createdDate": self.get_created_date(),
            "delivered": self.get_delivered(),
            "emailBill": self.get_email_bill(),
            "id": self.get_id(),
            "merchant": self.get_merchant(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
