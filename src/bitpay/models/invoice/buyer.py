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
    __locality = None
    __region = None
    __postal_code = None
    __country = None
    __email = None
    __phone = None
    __notify = False
    __buyer_email = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {"notify": "bool"}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_name(self) -> Optional[str]:
        """
        Get method for the name
        :return: name
        """
        return self.__name

    def set_name(self, name: Optional[str]) -> None:
        """
        Set method for the name
        :param name: name
        """
        self.__name = name

    def get_buyer_email(self) -> Optional[str]:
        """
        Get method for the buyer_email
        :return: buyer_email
        """
        return self.__buyer_email

    def set_buyer_email(self, buyer_email: Optional[str]) -> None:
        """
        Set method for the buyer_email
        :param buyer_email: buyer_email
        """
        self.__buyer_email = buyer_email

    def get_address1(self) -> Optional[str]:
        """
        Get method for the address1
        :return: address1
        """
        return self.__address1

    def set_address1(self, address1: Optional[str]) -> None:
        """
        Set method for the address1
        :param address1: address1
        """
        self.__address1 = address1

    def get_address2(self) -> Optional[str]:
        """
        Get method for the address2
        :return: address2
        """
        return self.__address2

    def set_address2(self, address2: Optional[str]) -> None:
        """
        Set method for the address2
        :param address2: address2
        """
        self.__address2 = address2

    def get_locality(self) -> Optional[str]:
        """
        Get method for the locality
        :return: locality
        """
        return self.__locality

    def set_locality(self, locality: Optional[str]) -> None:
        """
        Set method for the locality
        :param locality: locality
        """
        self.__locality = locality

    def get_region(self) -> Optional[str]:
        """
        Get method for the region
        :return: region
        """
        return self.__region

    def set_region(self, region: Optional[str]) -> None:
        """
        Set method for the region
        :param region: region
        """
        self.__region = region

    def get_postal_code(self) -> Optional[str]:
        """
        Get method for the postal_code
        :return: postal_code
        """
        return self.__postal_code

    def set_postal_code(self, postal_code: Optional[str]) -> None:
        """
        Set method for the postal_code
        :param postal_code: postal_code
        """
        self.__postal_code = postal_code

    def get_country(self) -> Optional[str]:
        """
        Get method for the country
        :return: country
        """
        return self.__country

    def set_country(self, country: Optional[str]) -> None:
        """
        Set method for the country
        :param country: country
        """
        self.__country = country

    def get_email(self) -> Optional[str]:
        """
        Get method for the email
        :return: email
        """
        return self.__email

    def set_email(self, email: Optional[str]) -> None:
        """
        Set method for the email
        :param email: email
        """
        self.__email = email

    def get_phone(self) -> Optional[str]:
        """
        Get method for the phone
        :return: phone
        """
        return self.__phone

    def set_phone(self, phone: Optional[str]) -> None:
        """
        Set method for the phone
        :param phone: phone
        """
        self.__phone = phone

    def get_notify(self) -> bool:
        """
        Get method for to notify
        :return: notify
        """
        return self.__notify

    def set_notify(self, notify: bool = False) -> None:
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
