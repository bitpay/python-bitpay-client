"""
RefundInfo
"""
from typing import Optional, List

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class RefundInfo:
    """
    Information about refund
    """

    __support_request = None
    __currency = None
    __amounts: Optional[List[dict]] = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {}, {"amounts": "dict"})

                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_support_request(self) -> Optional[str]:
        """
        Get method for the support_request
        :return: support_request
        """
        return self.__support_request

    def set_support_request(self, support_request: Optional[str]) -> None:
        """
        Set method for the support_request
        :param support_request: support_request
        """
        self.__support_request = support_request

    def get_currency(self) -> Optional[str]:
        """
        Get method for the currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: Optional[str]) -> None:
        """
        Set method for the currency
        :param currency: currency
        """
        self.__currency = currency

    def get_amounts(self) -> Optional[List[dict]]:
        """
        Get method for the amounts
        :return: amounts
        """
        return self.__amounts

    def set_amounts(self, amounts: Optional[List[dict]]) -> None:
        """
        Set method for the amounts
        :param amounts: amounts
        """
        self.__amounts = amounts

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
