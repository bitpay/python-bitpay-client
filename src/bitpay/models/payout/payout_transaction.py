"""
PayoutTransaction
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class PayoutTransaction:
    """
    PayoutTransaction
    """

    __txid = None
    __amount = None
    __date = None
    __confirmations = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {"amount": "float", "date": "str"}, {}
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_txid(self) -> Optional[str]:
        """
        Get method for txid
        :return: txid
        """
        return self.__txid

    def set_txid(self, txid: Optional[str]) -> None:
        """
        Set method for to txid
        :param txid: txid
        """
        self.__txid = txid

    def get_amount(self) -> Optional[float]:
        """
        Get method for amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount: Optional[float]) -> None:
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_confirmations(self) -> Optional[str]:
        """
        Get method for confirmations
        :return: confirmations
        """
        return self.__confirmations

    def set_confirmations(self, confirmations: Optional[str]) -> None:
        """
        Set method for to confirmations
        :param confirmations: confirmations
        """
        self.__confirmations = confirmations

    def get_date(self) -> Optional[str]:
        """
        Get method for date
        :return: date
        """
        return self.__date

    def set_date(self, date: Optional[str]) -> None:
        """
        Set method for to date
        :param date: date
        """
        self.__date = date

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
