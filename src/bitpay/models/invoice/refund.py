"""
Refund
"""
from typing import Optional

from bitpay.utils import key_utils
from bitpay.utils.model_util import ModelUtil


class Refund:
    """
    Refund an invoice
    """

    __guid = None
    __amount = None
    __currency = None
    __token = None
    __id = None
    __request_date = None
    __status = None

    __preview = False
    __immediate = False
    __reference = None
    __buyer_pays_refund_fee = False
    __refund_fee = None
    __last_refund_notification = None
    __invoice = None
    __notification_url = None
    __refund_address = None
    __support_request = None
    __transaction_currency = None
    __transaction_amount = None
    __transaction_refund_fee = None

    def __init__(
        self,
        invoice_id: str = "",
        amount: float = 0.0,
        currency: str = "",
        token: str = "",
        **kwargs: dict
    ) -> None:
        self.set_invoice(invoice_id)
        self.set_amount(amount)
        self.set_currency(currency)
        self.set_token(token)

        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "amount": "float",
                        "preview": "bool",
                        "immediate": "bool",
                        "buyerPaysRefundFee": "bool",
                        "refundFee": "float",
                        "transactionAmount": "float",
                        "transactionRefundFee": "float",
                    },
                    {},
                )
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_guid(self) -> Optional[str]:
        """
        Get method for the guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid: Optional[str]) -> None:
        """
        Set method for the guid
        :param guid: guid
        """
        self.__guid = guid

    def get_preview(self) -> bool:
        """
        Get method for the preview
        :return: preview
        """
        return self.__preview

    def set_preview(self, preview: bool) -> None:
        """
        Set method for the preview
        :param preview: preview
        """
        self.__preview = preview

    def get_immediate(self) -> bool:
        """
        Get method for the immediate
        :return: immediate
        """
        return self.__immediate

    def set_immediate(self, immediate: bool) -> None:
        """
        Set method for the immediate
        :param immediate: immediate
        """
        self.__immediate = immediate

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

    def get_buyer_pays_refund_fee(self) -> bool:
        """
        Get method for the buyer_pays_refund_fee
        :return: buyer_pays_refund_fee
        """
        return self.__buyer_pays_refund_fee

    def set_buyer_pays_refund_fee(self, buyer_pays_refund_fee: bool) -> None:
        """
        Set method for the buyer_pays_refund_fee
        :param buyer_pays_refund_fee: buyer_pays_refund_fee
        """
        self.__buyer_pays_refund_fee = buyer_pays_refund_fee

    def get_refund_fee(self) -> Optional[float]:
        """
        Get method for the refund_fee
        :return: refund_fee
        """
        return self.__refund_fee

    def set_refund_fee(self, refund_fee: Optional[float]) -> None:
        """
        Set method for the refund_fee
        :param refund_fee: refund_fee
        """
        self.__refund_fee = refund_fee

    def get_last_refund_notification(self) -> Optional[str]:
        """
        Get method for the last_refund_notification
        :return: last_refund_notification
        """
        return self.__last_refund_notification

    def set_last_refund_notification(
        self, last_refund_notification: Optional[str]
    ) -> None:
        """
        Set method for the last_refund_notification
        :param last_refund_notification: last_refund_notification
        """
        self.__last_refund_notification = last_refund_notification

    def get_invoice(self) -> Optional[str]:
        """
        Get method for the invoice
        :return: invoice
        """
        return self.__invoice

    def set_invoice(self, invoice: Optional[str]) -> None:
        """
        Set method for the invoice
        :param invoice: invoice
        """
        self.__invoice = invoice

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

    def get_token(self) -> Optional[str]:
        """
        Get method for the token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for the token
        :param token: token
        """
        self.__token = token

    def get_id(self) -> Optional[str]:
        """
        Get method for the id
        :return: id
        """
        return self.__id

    def set_id(self, id: Optional[str]) -> None:
        """
        Set method for the id
        :param id: id
        """
        self.__id = id

    def get_request_date(self) -> Optional[str]:
        """
        Get method for the request_date
        :return: request_date
        """
        return self.__request_date

    def set_request_date(self, request_date: Optional[str]) -> None:
        """
        Set method for the request_date
        :param request_date: request_date
        """
        self.__request_date = request_date

    def get_status(self) -> Optional[str]:
        """
        Get method for the status
        :return: status
        """
        return self.__status

    def set_status(self, status: Optional[str]) -> None:
        """
        Set method for the status
        :param status: status
        """
        self.__status = status

    def get_notification_url(self) -> Optional[str]:
        """
        Gets URL to which BitPay sends webhook notifications. HTTPS is mandatory.
        :return: notification url
        """
        return self.__notification_url

    def set_notification_url(self, value: Optional[str]) -> None:
        """
        Sets URL to which BitPay sends webhook notifications. HTTPS is mandatory.
        :param value: notification url
        """
        self.__notification_url = value

    def get_refund_address(self) -> Optional[str]:
        """
        Gets the wallet address that the refund will return the funds to, added by the customer.
        :return: refund address
        """
        return self.__refund_address

    def set_refund_address(self, value: Optional[str]) -> None:
        """
        Sets the wallet address that the refund will return the funds to, added by the customer.
        :param value: refund address
        """
        self.__refund_address = value

    def get_support_request(self) -> Optional[str]:
        """
        Gets the ID of the associated support request for the refund.
        :return: support request
        """
        return self.__support_request

    def set_support_request(self, value: Optional[str]) -> None:
        """
        Sets the ID of the associated support request for the refund.
        :param value: support request
        """
        self.__support_request = value

    def get_transaction_currency(self) -> Optional[str]:
        """
        Gets the currency used for the invoice transaction.
        :return: the transaction currency of the Refund
        """
        return self.__transaction_currency

    def set_transaction_currency(self, value: Optional[str]) -> None:
        """
        Sets the currency used for the invoice transaction.
        :param value: the transaction currency of the Refund
        """
        self.__transaction_currency = value

    def get_transaction_amount(self) -> Optional[float]:
        """
        Gets amount to be refunded in terms of the transaction currency.
        :return: the transaction amount of the Refund
        """
        return self.__transaction_amount

    def set_transaction_amount(self, value: Optional[float]) -> None:
        """
        Sets amount to be refunded in terms of the transaction currency.
        :param value: the transaction amount of the Refund
        """
        self.__transaction_amount = value

    def get_transaction_refund_fee(self) -> Optional[float]:
        """
        Gets the refund fee expressed in terms of transaction currency.
        :return: the transaction refund fee of the Refund
        """
        return self.__transaction_refund_fee

    def set_transaction_refund_fee(self, value: Optional[float]) -> None:
        """
        Sets the refund fee expressed in terms of transaction currency.
        :param value: the transaction amount of the Refund
        """
        self.__transaction_refund_fee = value

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
