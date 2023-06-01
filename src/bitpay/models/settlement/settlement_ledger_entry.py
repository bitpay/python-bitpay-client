"""
SettlementLedgerEntry: ledger entries in the settlement,
"""
from typing import Optional

from .invoice_data import InvoiceData
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class SettlementLedgerEntry:
    """
    SettlementLedgerEntry
    """

    __code = None
    __invoice_id = None
    __amount = None
    __timestamp = None
    __description = None
    __reference = None
    __invoice_data: Optional[InvoiceData] = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "invoiceData": InvoiceData,
                        "code": "int",
                        "amount": "float",
                        "timestamp": "str",
                    },
                    {},
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_code(self) -> Optional[int]:
        """
        Get method for the code
        :return: code
        """
        return self.__code

    def set_code(self, code: Optional[int]) -> None:
        """
        Set method for the code
        :param code: code
        """
        self.__code = code

    def get_invoice_id(self) -> Optional[str]:
        """
        Get method for the invoice_id
        :return: invoice_id
        """
        return self.__invoice_id

    def set_invoice_id(self, invoice_id: Optional[str]) -> None:
        """
        Set method for the invoice_id
        :param invoice_id: invoice_id
        """
        self.__invoice_id = invoice_id

    def get_amount(self) -> Optional[float]:
        """
        Get method for the amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount: Optional[float]) -> None:
        """
        Set method for the amount
        :param amount: amount
        """
        self.__amount = amount

    def get_timestamp(self) -> Optional[str]:
        """
        Get method for the timestamp
        :return: timestamp
        """
        return self.__timestamp

    def set_timestamp(self, timestamp: Optional[str]) -> None:
        """
        Set method for the timestamp
        :param timestamp: timestamp
        """
        self.__timestamp = timestamp

    def get_description(self) -> Optional[str]:
        """
        Get method for the description
        :return: description
        """
        return self.__description

    def set_description(self, description: Optional[str]) -> None:
        """
        Set method for the description
        :param description: description
        """
        self.__description = description

    def get_reference(self) -> Optional[str]:
        """
        Get method for the reference
        :return: reference
        """
        return self.__reference

    def set_reference(self, reference: Optional[str]) -> None:
        """
        Set method for the reference
        :param reference: reference
        """
        self.__reference = reference

    def get_invoice_data(self) -> Optional[InvoiceData]:
        """
        Get method for the invoice_data
        :return: invoice_data
        """
        return self.__invoice_data

    def set_invoice_data(self, invoice_data: Optional[InvoiceData]) -> None:
        """
        Set method for the invoice_data
        :param invoice_data: invoice_data
        """
        self.__invoice_data = invoice_data

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
