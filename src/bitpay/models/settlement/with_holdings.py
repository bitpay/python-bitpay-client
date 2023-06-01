from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class WithHoldings:
    """
    Holdings
    """

    __amount = None
    __code = None
    __description = None
    __notes = None
    __label = None
    __bank_country = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            value = ModelUtil.get_field_value(key, value, {"amount": "float"}, {})
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_amount(self) -> Optional[float]:
        """
        Get method for to amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount: Optional[float]) -> None:
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_code(self) -> Optional[str]:
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code: Optional[str]) -> None:
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_description(self) -> Optional[str]:
        """
        Get method for to description
        :return: description
        """
        return self.__description

    def set_description(self, description: Optional[str]) -> None:
        """
        Set method for to description
        :param description: description
        """
        self.__description = description

    def get_notes(self) -> Optional[str]:
        """
        Get method for to notes
        :return: notes
        """
        return self.__notes

    def set_notes(self, notes: Optional[str]) -> None:
        """
        Set method for to notes
        :param notes: notes
        """
        self.__notes = notes

    def get_label(self) -> Optional[str]:
        """
        Get method for to label
        :return: label
        """
        return self.__label

    def set_label(self, label: Optional[str]) -> None:
        """
        Set method for to label
        :param label: label
        """
        self.__label = label

    def get_bank_country(self) -> Optional[str]:
        """
        Get method for to bank_country
        :return: bank_country
        """
        return self.__bank_country

    def set_bank_country(self, bank_country: Optional[str]) -> None:
        """
        Set method for to bank_country
        :param bank_country: bank_country
        """
        self.__bank_country = bank_country

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
