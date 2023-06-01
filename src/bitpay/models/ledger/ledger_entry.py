"""
LedgerEntry
"""
from typing import Optional

from bitpay.models.ledger.buyer import Buyer
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class LedgerEntry:
    """
    Ledger entry
    """

    __type = None
    __amount = None
    __code = None
    __timestamp = None
    __currency = None
    __tx_type = None
    __scale = None
    __id = None
    __support_request = None
    __description = None
    __invoice_id = None

    # Buyer
    __buyer_fields = Buyer()

    __invoice_amount = None
    __invoice_currency = None
    __transaction_currency = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {"amount": "float", "invoiceAmount": "float", "buyerFields": Buyer},
                    {},
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_type(self) -> Optional[str]:
        """
        Get method for to type
        :return: type
        """
        return self.__type

    def set_type(self, type: Optional[str]) -> None:
        """
        Set method for to type
        :param type: type
        """
        self.__type = type

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

    def get_timestamp(self) -> Optional[str]:
        """
        Get method for to timestamp
        :return: timestamp
        """
        return self.__timestamp

    def set_timestamp(self, timestamp: Optional[str]) -> None:
        """
        Set method for to timestamp
        :param timestamp: timestamp
        """
        self.__timestamp = timestamp

    def get_currency(self) -> Optional[str]:
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: Optional[str]) -> None:
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_tx_type(self) -> Optional[str]:
        """
        Get method for to tx_type
        :return: tx_type
        """
        return self.__tx_type

    def set_tx_type(self, tx_type: Optional[str]) -> None:
        """
        Set method for to tx_type
        :param tx_type: tx_type
        """
        self.__tx_type = tx_type

    def get_scale(self) -> Optional[str]:
        """
        Get method for to scale
        :return: scale
        """
        return self.__scale

    def set_scale(self, scale: Optional[str]) -> None:
        """
        Set method for to scale
        :param scale: scale
        """
        self.__scale = scale

    def get_id(self) -> Optional[str]:
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id: Optional[str]) -> None:
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_support_request(self) -> Optional[str]:
        """
        Get method for to support_request
        :return: support_request
        """
        return self.__support_request

    def set_support_request(self, support_request: Optional[str]) -> None:
        """
        Set method for to support_request
        :param support_request: support_request
        """
        self.__support_request = support_request

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

    def get_invoice_id(self) -> Optional[str]:
        """
        Get method for to invoice_id
        :return: invoice_id
        """
        return self.__invoice_id

    def set_invoice_id(self, invoice_id: Optional[str]) -> None:
        """
        Set method for to invoice_id
        :param invoice_id: invoice_id
        """
        self.__invoice_id = invoice_id

    def get_buyer_fields(self) -> Optional[Buyer]:
        """
        Get method for to buyer_fields
        :return: buyer_fields
        """
        return self.__buyer_fields

    def set_buyer_fields(self, buyer_fields: Buyer) -> None:
        """
        Set method for to buyer_fields
        :param buyer_fields: buyer_fields
        """
        self.__buyer_fields = buyer_fields

    def get_invoice_amount(self) -> Optional[float]:
        """
        Get method for to invoice_amount
        :return: invoice_amount
        """
        return self.__invoice_amount

    def set_invoice_amount(self, invoice_amount: Optional[float]) -> None:
        """
        Set method for to invoice_amount
        :param invoice_amount: invoice_amount
        """
        self.__invoice_amount = invoice_amount

    def get_invoice_currency(self) -> Optional[str]:
        """
        Get method for to invoice_currency
        :return: invoice_currency
        """
        return self.__invoice_currency

    def set_invoice_currency(self, invoice_currency: Optional[str]) -> None:
        """
        Set method for to invoice_currency
        :param invoice_currency: invoice_currency
        """
        self.__invoice_currency = invoice_currency

    def get_transaction_currency(self) -> Optional[str]:
        """
        Get method for to transaction_currency
        :return: transaction_currency
        """
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency: Optional[str]) -> None:
        """
        Set method for to transaction_currency
        :param transaction_currency: transaction_currency
        """
        self.__transaction_currency = transaction_currency

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
