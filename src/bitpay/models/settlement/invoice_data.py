"""
InvoiceData: Object containing relevant information from the paid invoice
"""
from typing import Optional, List

from bitpay.models.settlement.refund_info import RefundInfo
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class InvoiceData:
    """
    invoice data
    """

    __order_id = None
    __date = None
    __price = None
    __currency = None
    __transaction_currency = None
    __over_paid_amount = None
    __payout_percentage = None
    __buyer_email_address = None
    """
    RefundInfo
    """
    __refund_info = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "refundInfo": RefundInfo,
                        "date": "str",
                        "price": "float",
                        "overPaidAmount": "float",
                    },
                    {"payoutPercentage": "dict"},
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_order_id(self) -> Optional[str]:
        """
        Get method for to order_id
        :return: order_id
        """
        return self.__order_id

    def set_order_id(self, order_id: Optional[str]) -> None:
        """
        Set method for to order_id
        :param order_id: order_id
        """
        self.__order_id = order_id

    def get_buyer_email_address(self) -> Optional[str]:
        """
        Get method for to buyer_email_address
        :return: buyer_email_address
        """
        return self.__buyer_email_address

    def set_buyer_email_address(self, buyer_email_address: Optional[str]) -> None:
        """
        Set method for to buyer_email_address
        :param buyer_email_address: buyer_email_address
        """
        self.__buyer_email_address = buyer_email_address

    def get_date(self) -> Optional[str]:
        """
        Get method for to date
        :return: date
        """
        return self.__date

    def set_date(self, date: Optional[str]) -> None:
        """
        Set method for to date
        :param date: date
        """
        self.__date = date

    def get_price(self) -> Optional[float]:
        """
        Get method for to price
        :return: price
        """
        return self.__price

    def set_price(self, price: Optional[float]) -> None:
        """
        Set method for to price
        :param price: price
        """
        self.__price = price

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

    def get_over_paid_amount(self) -> Optional[float]:
        """
        Get method for to over_paid_amount
        :return: over_paid_amount
        """
        return self.__over_paid_amount

    def set_over_paid_amount(self, over_paid_amount: Optional[float]) -> None:
        """
        Set method for to over_paid_amount
        :param over_paid_amount: over_paid_amount
        """
        self.__over_paid_amount = over_paid_amount

    def get_payout_percentage(self) -> Optional[List[dict]]:
        """
        Get method for to payout_percentage
        :return: payout_percentage
        """
        return self.__payout_percentage

    def set_payout_percentage(self, payout_percentage: Optional[List[dict]]) -> None:
        """
        Set method for to payout_percentage
        :param payout_percentage: transaction_currency
        """
        self.__payout_percentage = payout_percentage

    def get_refund_info(self) -> Optional[RefundInfo]:
        """
        Get method for to refund_info
        :return: refund_info
        """
        return self.__refund_info

    def set_refund_info(self, refund_info: Optional[RefundInfo]) -> None:
        """
        Set method for to refund_info
        :param refund_info: refund_info
        """
        self.__refund_info = refund_info

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
