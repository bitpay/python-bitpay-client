"""
Bill
"""
from typing import List, Optional

from .item import Item
from bitpay.models.currency import Currency
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Bill:
    """
    Bills are payment requests addressed to specific buyers.
    Bill line items have fixed prices, typically denominated
    in fiat currency.
    """

    __currency = None
    __token = None
    __email = None
    __items: Optional[List[Item]] = None
    __number = None
    __name = None
    __address1 = None
    __address2 = None
    __city = None
    __state = None
    __zip = None
    __country = None
    __cc: Optional[List[str]] = None
    __phone = None
    __due_date = None
    __pass_processing_fee = False
    __status = None
    __url = None
    __created_date = None
    __email_bill = None
    __id = None
    __merchant = None

    def __init__(
        self,
        number: Optional[str] = None,
        currency: Optional[str] = None,
        email: Optional[str] = None,
        **kwargs: dict
    ) -> None:
        self.set_number(number)
        self.set_email(email)
        if currency is not None:
            self.set_currency(currency)

        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {}, {"items": Item})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_currency(self) -> Optional[str]:
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: str) -> None:
        """
        Set method for to currency
        :param currency: currency
        """
        if not Currency.is_valid(currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__currency = currency

    def get_token(self) -> Optional[str]:
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def get_email(self) -> Optional[str]:
        """
        Get method for to email
        :return: email
        """
        return self.__email

    def set_email(self, email: Optional[str]) -> None:
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_number(self) -> Optional[str]:
        """
        Get method for to number
        :return: number
        """
        return self.__number

    def set_number(self, number: Optional[str]) -> None:
        """
        Set method for to number
        :param number: number
        """
        self.__number = number

    def get_name(self) -> Optional[str]:
        """
        Get method for to name
        :return: name
        """
        return self.__name

    def set_name(self, name: Optional[str]) -> None:
        """
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_address1(self) -> Optional[str]:
        """
        Get method for to address1
        :return: address1
        """
        return self.__address1

    def set_address1(self, address1: Optional[str]) -> None:
        """
        Set method for to address1
        :param address1: address1
        """
        self.__address1 = address1

    def get_address2(self) -> Optional[str]:
        """
        Get method for to address2
        :return: address2
        """
        return self.__address2

    def set_address2(self, address2: Optional[str]) -> None:
        """
        Set method for to address2
        :param address2: address2
        """
        self.__address2 = address2

    def get_city(self) -> Optional[str]:
        """
        Get method for to city
        :return: city
        """
        return self.__city

    def set_city(self, city: Optional[str]) -> None:
        """
        Set method for to city
        :param city: city
        """
        self.__city = city

    def get_state(self) -> Optional[str]:
        """
        Get method for to state
        :return: state
        """
        return self.__state

    def set_state(self, state: Optional[str]) -> None:
        """
        Set method for to state
        :param state: state
        """
        self.__state = state

    def get_zip(self) -> Optional[str]:
        """
        Get method for to zip
        :return: zip
        """
        return self.__zip

    def set_zip(self, zip: Optional[str]) -> None:
        """
        Set method for to zip
        :param zip: zip
        """
        self.__zip = zip

    def get_country(self) -> Optional[str]:
        """
        Get method for to country
        :return: country
        """
        return self.__country

    def set_country(self, country: Optional[str]) -> None:
        """
        Set method for to country
        :param country: country
        """
        self.__country = country

    def get_cc(self) -> Optional[List[str]]:
        """
        Get method for to cc
        :return: cc
        """
        return self.__cc

    def set_cc(self, cc: Optional[List[str]]) -> None:
        """
        Set method for to cc
        :param cc: cc
        """
        self.__cc = cc

    def get_phone(self) -> Optional[str]:
        """
        Get method for to phone
        :return: phone
        """
        return self.__phone

    def set_phone(self, phone: Optional[str]) -> None:
        """
        Set method for to phone
        :param phone: phone
        """
        self.__phone = phone

    def get_due_date(self) -> Optional[str]:
        """
        Get method for to due_date
        :return: due_date
        """
        return self.__due_date

    def set_due_date(self, due_date: Optional[str]) -> None:
        """
        Set method for to due_date
        :param due_date: due_date
        """
        self.__due_date = due_date

    def get_pass_processing_fee(self) -> bool:
        """
        Get method for to pass_processing_fee
        :return: pass_processing_fee
        """
        return self.__pass_processing_fee

    def set_pass_processing_fee(self, pass_processing_fee: bool) -> None:
        """
        Set method for to pass_processing_fee
        :param pass_processing_fee: pass_processing_fee
        """
        self.__pass_processing_fee = pass_processing_fee

    def get_status(self) -> Optional[str]:
        """
        Get method for to status
        :return: status
        """
        return self.__status

    def set_status(self, status: Optional[str]) -> None:
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_url(self) -> Optional[str]:
        """
        Get method for to url
        :return: url
        """
        return self.__url

    def set_url(self, url: Optional[str]) -> None:
        """
        Set method for to url
        :param url: url
        """
        self.__url = url

    def get_created_date(self) -> Optional[str]:
        """
        Get method for to created_date
        :return: created_date
        """
        return self.__created_date

    def set_created_date(self, created_date: Optional[str]) -> None:
        """
        Set method for to created_date
        :param created_date: created_date
        """
        self.__created_date = created_date

    def get_email_bill(self) -> Optional[str]:
        """
        Get method for to email_bill
        :return: email_bill
        """
        return self.__email_bill

    def set_email_bill(self, email_bill: Optional[str]) -> None:
        """
        Set method for to email_bill
        :param email_bill: email_bill
        """
        self.__email_bill = email_bill

    def get_id(self) -> Optional[str]:
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, value: Optional[str]) -> None:
        """
        Set method for to id
        :param value: id
        """
        self.__id = value

    def get_merchant(self) -> Optional[str]:
        """
        Get method for to merchant
        :return: merchant
        """
        return self.__merchant

    def set_merchant(self, merchant: Optional[str]) -> None:
        """
        Set method for to merchant
        :param merchant: merchant
        """
        self.__merchant = merchant

    def get_items(self) -> Optional[List[Item]]:
        """
        Get method for to item
        :return: item
        """
        return self.__items

    def set_items(self, item: Optional[List[Item]]) -> None:
        """
        Set method for to item
        :param item: item
        """
        self.__items = item

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
