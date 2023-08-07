"""
BuyerProvidedInfo: Information collected from the buyer during the process of paying
an invoice. Initially this object is empty.
"""
from typing import Union, Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class BuyerProvidedInfo:
    """
    Information collected from the buyer during the process of paying an invoice.
     Initially this object is empty.
    """

    __name = None
    __phone_number = None
    __selected_wallet = None
    __email_address = None
    __selected_transaction_currency = None
    __sms = None
    __sms_verified = False

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {"smsVerified": "bool"}, {}
                )
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
        Set method for to name
        :param name: name
        """
        self.__name = name

    def get_phone_number(self) -> Optional[str]:
        """
        Get method for the phone_number
        :return: phone_number
        """
        return self.__phone_number

    def set_phone_number(self, phone_number: Optional[str]) -> None:
        """
        Set method for to phone_number
        :param phone_number: phone_number
        """
        self.__phone_number = phone_number

    def get_selected_wallet(self) -> Optional[str]:
        """
        Get method for the selected_wallet
        :return: selected_wallet
        """
        return self.__selected_wallet

    def set_selected_wallet(self, selected_wallet: Optional[str]) -> None:
        """
        Set method for to selected_wallet
        :param selected_wallet: selected_wallet
        """
        self.__selected_wallet = selected_wallet

    def get_email_address(self) -> Optional[str]:
        """
        Get method for the email_address
        :return: email_address
        """
        return self.__email_address

    def set_email_address(self, email_address: Optional[str]) -> None:
        """
        Set method for to email_address
        :param email_address: email_address
        """
        self.__email_address = email_address

    def get_selected_transaction_currency(self) -> Optional[str]:
        """
        Get method for the selected_transaction_currency
        :return: selected_transaction_currency
        """
        return self.__selected_transaction_currency

    def set_selected_transaction_currency(
        self, selected_transaction_currency: Optional[str]
    ) -> None:
        """
        Set method for to selected_transaction_currency
        :param selected_transaction_currency: selected_transaction_currency
        """
        self.__selected_transaction_currency = selected_transaction_currency

    def get_sms(self) -> Optional[str]:
        """
        Get sms
        :return: Union[str, None]
        """
        return self.__sms

    def get_sms_verified(self) -> bool:
        """
        Get sms verified
        :return: bool
        """
        return self.__sms_verified

    def set_sms(self, value: Optional[str]) -> None:
        """
        Set sms
        :param value: str
        """
        self.__sms = value

    def set_sms_verified(self, value: bool) -> None:
        """
        Set sms verified
        :param value: bool
        """
        self.__sms_verified = value

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
