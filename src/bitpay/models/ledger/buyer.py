"""
Buyer
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Buyer:
    """
    Allows merchant to pass buyer related information in the invoice object
    """

    __name = None
    __address1 = None
    __address2 = None
    __city = None
    __state = None
    __zip = None
    __country = None
    __email = None
    __phone = None
    __notify = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

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

    def get_notify(self) -> Optional[str]:
        """
        Get method for to notify
        :return: notify
        """
        return self.__notify

    def set_notify(self, notify: Optional[str]) -> None:
        """
        Set method for to notify
        :param notify: notify
        """
        self.__notify = notify

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
