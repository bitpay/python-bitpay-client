"""
Payout
"""
from typing import Optional, List, Any, Dict

from bitpay.models.currency import Currency
from .payout_transaction import PayoutTransaction
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Payout:
    """
    Payout
    """

    __token = None

    __amount = 0.0
    __currency = None
    __effective_date = None

    __reference = None
    __notification_email = None
    __notification_url = None
    __redirect_url = None
    __ledger_currency = None

    __id = None
    __shopper_id = None
    __recipient_id = None
    __exchange_rates = None
    __account = None
    __email = None
    __label = None
    __support_phone = None
    __status = None
    __message = None
    __request_date = None
    __date_executed = None
    __transactions: Optional[List[PayoutTransaction]]
    __account_id = None
    __group_id: Optional[str] = None

    def __init__(
        self,
        amount: float = 0.0,
        currency: Optional[str] = None,
        ledger_currency: Optional[str] = None,
        **kwargs: Dict[str, Any]
    ) -> None:
        self.set_amount(amount)
        if currency:
            self.set_currency(currency)
        if ledger_currency:
            self.set_ledger_currency(ledger_currency)

        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "amount": "float",
                        "effectiveDate": "str",
                        "requestDate": "str",
                        "dateExecuted": "str",
                        "code": "int",
                    },
                    {"exchangeRates": "dict", "transactions": PayoutTransaction},
                )
                if key in ["notificationURL"]:
                    self.set_notification_url(str(value))
                    continue
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_token(self) -> Optional[str]:
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def get_amount(self) -> float:
        """
        Get method for to amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount: float) -> None:
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_account_id(self) -> Optional[str]:
        """
        Get method for to account_id
        :return: account_id
        """
        return self.__account_id

    def set_account_id(self, account_id: Optional[str]) -> None:
        """
        Set method for to account_id
        :param account_id: account_id
        """
        self.__account_id = account_id

    def get_currency(self) -> Optional[str]:
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: str) -> None:
        """
        Set method for to currency
        :param currency: currency
        """
        if not Currency.is_valid(currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__currency = currency

    def get_effective_date(self) -> Optional[str]:
        """
        Get method for to effective_date
        :return: effective_date
        """
        return self.__effective_date

    def set_effective_date(self, effective_date: Optional[str]) -> None:
        """
        Set method for to effective_date
        :param effective_date: effective_date
        """
        self.__effective_date = effective_date

    def get_reference(self) -> Optional[str]:
        """
        Get method for to reference
        :return: reference
        """
        return self.__reference

    def set_reference(self, reference: Optional[str]) -> None:
        """
        Set method for to reference
        :param reference: reference
        """
        self.__reference = reference

    def get_notification_email(self) -> Optional[str]:
        """
        Get method for to notification_email
        :return: notification_email
        """
        return self.__notification_email

    def set_notification_email(self, notification_email: Optional[str]) -> None:
        """
        Set method for to notification_email
        :param notification_email: notification_email
        """
        self.__notification_email = notification_email

    def get_notification_url(self) -> Optional[str]:
        """
        Get method for to notification_url
        :return: notification_url
        """
        return self.__notification_url

    def set_notification_url(self, notification_url: Optional[str]) -> None:
        """
        Set method for to notification_url
        :param notification_url: notification_url
        """
        self.__notification_url = notification_url

    def get_redirect_url(self) -> Optional[str]:
        """
        Get method for to redirect_url
        :return: redirect_url
        """
        return self.__redirect_url

    def set_redirect_url(self, redirect_url: Optional[str]) -> None:
        """
        Set method for to redirect_url
        :param redirect_url: redirect_url
        """
        self.__redirect_url = redirect_url

    def get_ledger_currency(self) -> Optional[str]:
        """
        Get method for to ledger_currency
        :return: ledger_currency
        """
        return self.__ledger_currency

    def set_ledger_currency(self, ledger_currency: str) -> None:
        """
        Set method for to ledger_currency
        :param ledger_currency: ledger_currency
        """
        if not Currency.is_valid(ledger_currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__ledger_currency = ledger_currency

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

    def get_shopper_id(self) -> Optional[str]:
        """
        Get method for to shopper_id
        :return: shopper_id
        """
        return self.__shopper_id

    def set_shopper_id(self, shopper_id: Optional[str]) -> None:
        """
        Set method for to shopper_id
        :param shopper_id: shopper_id
        """
        self.__shopper_id = shopper_id

    def get_recipient_id(self) -> Optional[str]:
        """
        Get method for to recipient_id
        :return: recipient_id
        """
        return self.__recipient_id

    def set_recipient_id(self, recipient_id: Optional[str]) -> None:
        """
        Set method for to recipient_id
        :param recipient_id: recipient_id
        """
        self.__recipient_id = recipient_id

    def get_exchange_rates(self) -> Optional[List[dict]]:
        """
        Get method for to exchange_rates
        :return: exchange_rates
        """
        return self.__exchange_rates

    def set_exchange_rates(self, exchange_rates: Optional[List[dict]]) -> None:
        """
        Set method for to exchange_rates
        :param exchange_rates: exchange_rates
        """
        self.__exchange_rates = exchange_rates

    def get_account(self) -> Optional[str]:
        """
        Get method for to account
        :return: account
        """
        return self.__account

    def set_account(self, account: Optional[str]) -> None:
        """
        Set method for to account
        :param account: account
        """
        self.__account = account

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

    def get_support_phone(self) -> Optional[str]:
        """
        Get method for to support_phone
        :return: support_phone
        """
        return self.__support_phone

    def set_support_phone(self, support_phone: Optional[str]) -> None:
        """
        Set method for to support_phone
        :param support_phone: support_phone
        """
        self.__support_phone = support_phone

    def get_status(self) -> Optional[str]:
        """
        Get method for to status
        :return: status
        """
        return self.__status

    def set_status(self, status: Optional[str]) -> None:
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_message(self) -> Optional[str]:
        """
        Get method for to message
        :return: message
        """
        return self.__message

    def set_message(self, message: Optional[str]) -> None:
        """
        Set method for to message
        :param message: message
        """
        self.__message = message

    def get_request_date(self) -> Optional[str]:
        """
        Get method for to code
        :return: code
        """
        return self.__request_date

    def set_request_date(self, request_date: Optional[str]) -> None:
        """
        Set method for to request_date
        :param request_date: request_date
        """
        self.__request_date = request_date

    def get_date_executed(self) -> Optional[str]:
        """
        Get method for to date_executed
        :return: date_executed
        """
        return self.__date_executed

    def set_date_executed(self, date_executed: Optional[str]) -> None:
        """
        Set method for to date_executed
        :param date_executed: date_executed
        """
        self.__date_executed = date_executed

    def get_transactions(self) -> Optional[List[PayoutTransaction]]:
        """
        Get method for to transactions
        :return: transactions
        """
        return self.__transactions

    def set_transactions(self, transactions: Optional[List[PayoutTransaction]]) -> None:
        """
        Set method for to transactions
        :param transactions: transactions
        """
        self.__transactions = transactions

    def get_group_id(self) -> Optional[str]:
        """
        Added to the payouts made at the same time through the `Create Payout Group` request.
        Can be used for querying or deleting.
        """
        return self.__group_id

    def set_group_id(self, value: str) -> None:
        """
        Added to the payouts made at the same time through the `Create Payout Group` request.
        Can be used for querying or deleting.
        """
        self.__group_id = value

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        data = ModelUtil.to_json(self)
        if "notificationUrl" in data:
            data["notificationURL"] = data.pop("notificationUrl")

        return data
