"""
Invoice
"""
from typing import Union, List, Optional, Dict

from .buyer import Buyer
from .shopper import Shopper
from .miner_fees import MinerFees
from .refund_info import RefundInfo
from .transaction import Transaction
from .universal_codes import UniversalCodes
from .itemized_details import ItemizedDetails
from .buyer_provided_info import BuyerProvidedInfo
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from .supported_transaction_currencies import SupportedTransactionCurrencies
from bitpay.utils.model_util import ModelUtil


class Invoice:
    """
    Invoices are time-sensitive payment requests addressed to specific buyers.
    An invoice has a fixed price,typically denominated in fiat currency.
    It also has an equivalent price in the supported cryptocurrencies,
    calculated by BitPay, at a locked exchange rate with an expiration
    time of 15 minutes.
    """

    __currency = None

    __guid = None
    __token = None

    __price = None
    __pos_data = None
    __notification_url = None
    __transaction_speed = None
    __full_notifications = False
    __notification_email = None
    __redirect_URL = None
    __order_id = None
    __item_desc = None
    __item_code = None
    __physical = False
    __payment_currencies: Optional[List[str]] = None
    __payment_subtotals: Optional[dict] = None
    __payment_totals: Optional[dict] = None
    __payment_display_totals: Optional[dict] = None
    __payment_display_subtotals: Optional[dict] = None
    __payment_codes: Optional[dict] = None
    __acceptance_window = None
    __buyer = None
    __refund_addresses: Optional[List[str]]
    __close_url = None
    __auto_redirect = False
    __json_paypro_required = False

    __id = None
    __url = None
    __status = None
    __low_fee_detected = False
    __invoice_time = None
    __expiration_time = None
    __current_time = None
    __transactions: Optional[List[Transaction]] = None
    __exception_status = None
    __target_confirmations = None
    __refund_address_request_pending = False
    __buyer_provided_email = None
    __buyer_provided_info = None
    __buyer_sms = None
    __supported_transaction_currencies = None
    __miner_fees = None
    __non_pay_pro_payment_received = False
    __shopper = None
    __bill_id = None
    __refund_info: Optional[List[RefundInfo]] = None
    __extended_notifications = False
    __invoice_buyer_provided_info = None

    __transaction_currency = None
    __underpaid_amount = None
    __overpaid_amount = None
    __amount_paid = None
    __display_amount_paid = None
    __exchange_rates: Optional[dict] = None

    __payment_string = None
    __verification_link = None
    __buyer_email = None
    __merchant_name = None
    __forced_buyer_selected_wallet = None
    __forced_buyer_selected_transaction_currency = None
    __itemized_details: Optional[List[ItemizedDetails]] = None
    __universal_codes = None
    __is_cancelled = False
    __bitpay_id_required = False

    def __init__(
        self,
        price: Optional[float] = None,
        currency: Optional[str] = None,
        **kwargs: dict
    ) -> None:
        self.set_price(price)
        self.set_currency(currency)

        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "price": "float",
                        "amountPaid": "float",
                        "underpaidAmount": "float",
                        "overpaidAmount": "float",
                        "physical": "bool",
                        "autoRedirect": "bool",
                        "acceptanceWindow": "int",
                        "lowFeeDetected": "bool",
                        "refundAddressRequestPending": "bool",
                        "extendedNotifications": "bool",
                        "isCancelled": "bool",
                        "bitpayIdRequired": "bool",
                        "nonPayProPaymentReceived": "bool",
                        "jsonPayProRequired": "bool",
                        "invoiceTime": "int",
                        "expirationTime": "int",
                        "currentTime": "int",
                        "targetConfirmations": "int",
                        "buyer": Buyer,
                        "buyerProvidedInfo": BuyerProvidedInfo,
                        "shopper": Shopper,
                        "supportedTransactionCurrencies": SupportedTransactionCurrencies,
                        "minerFees": MinerFees,
                        "universalCodes": UniversalCodes,
                        "fullNotifications": "bool",
                    },
                    {
                        "paymentCurrencies": "str",
                        "paymentSubtotals": "dict",
                        "paymentTotals": "dict",
                        "paymentDisplayTotals": "dict",
                        "paymentDisplaySubTotals": "dict",
                        "refundAddresses": "str",
                        "itemizedDetails": ItemizedDetails,
                        "refundInfo": RefundInfo,
                        "paymentCodes": "dict",
                        "transactions": Transaction,
                        "exchangeRates": "dict",
                    },
                )

                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
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

    def get_pos_data(self) -> Optional[str]:
        """
        Get method for the pos_data
        :return: pos_data
        """
        return self.__pos_data

    def set_pos_data(self, pos_data: Optional[str]) -> None:
        """
        Set method for the pos_data
        :param pos_data: posData
        """
        self.__pos_data = pos_data

    def get_notification_url(self) -> Optional[str]:
        """
        Get method for the notification_url
        :return: notification_url
        """
        return self.__notification_url

    def set_notification_url(self, notification_url: Optional[str]) -> None:
        """
        Set method for the notification_url
        :param notification_url: notification_url
        """
        self.__notification_url = notification_url

    def get_transaction_speed(self) -> Optional[str]:
        """
        Get method for the transaction_speed
        :return: transaction_speed
        """
        return self.__transaction_speed

    def set_transaction_speed(self, transaction_speed: Optional[str]) -> None:
        """
        Set method for the transaction_speed
        :param transaction_speed: transaction_speed
        """
        self.__transaction_speed = transaction_speed

    def get_full_notifications(self) -> bool:
        """
        Get method for the full_notifications
        :return: full_notifications
        """
        return self.__full_notifications

    def set_full_notifications(self, full_notifications: bool) -> None:
        """
        Set method for the full_notifications
        :param full_notifications: full_notifications
        """
        self.__full_notifications = full_notifications

    def get_notification_email(self) -> Optional[str]:
        """
        Get method for the notification_email
        :return: notification_email
        """
        return self.__notification_email

    def set_notification_email(self, notification_email: Optional[str]) -> None:
        """
        Set method for the notification_email
        :param notification_email: notification_email
        """
        self.__notification_email = notification_email

    def get_redirect_u_r_l(self) -> Optional[str]:
        """
        Get method for the redirect_URL
        :return: redirect_URL
        """
        return self.__redirect_URL

    def set_redirect_u_r_l(self, redirect_url: Optional[str]) -> None:
        """
        Set method for the redirect_URL
        :param redirect_url: redirect_URL
        """
        self.__redirect_URL = redirect_url

    def get_order_id(self) -> Optional[str]:
        """
        Get method for the order_id
        :return: order_id
        """
        return self.__order_id

    def set_order_id(self, order_id: Optional[str]) -> None:
        """
        Set method for the order_id
        :param order_id: order_id
        """
        self.__order_id = order_id

    def get_item_desc(self) -> Optional[str]:
        """
        Get method for the item_desc
        :return: item_desc
        """
        return self.__item_desc

    def set_item_desc(self, item_desc: Optional[str]) -> None:
        """
        Set method for the item_desc
        :param item_desc: item_desc
        """
        self.__item_desc = item_desc

    def get_item_code(self) -> Optional[str]:
        """
        Get method for the item_code
        :return: item_code
        """
        return self.__item_code

    def set_item_code(self, item_code: Optional[str]) -> None:
        """
        Set method for the item_code
        :param item_code: item_code
        """
        self.__item_code = item_code

    def get_physical(self) -> bool:
        """
        Get method for the physical
        :return: physical
        """
        return self.__physical

    def set_physical(self, physical: bool) -> None:
        """
        Set method for the physical
        :param physical: physical
        """
        self.__physical = physical

    def get_payment_currencies(self) -> Optional[List[str]]:
        """
        Get method for the payment_currencies
        :return: payment_currencies
        """
        return self.__payment_currencies

    def set_payment_currencies(self, payment_currencies: List[str]) -> None:
        """
        Set method for the payment_currencies
        :param payment_currencies: payment_currencies
        """
        self.__payment_currencies = payment_currencies

    def get_payment_subtotals(self) -> Optional[dict]:
        """
        Get method for the payment_subtotals
        :return: payment_subtotals
        """
        return self.__payment_subtotals

    def set_payment_subtotals(self, payment_subtotals: Optional[dict]) -> None:
        """
        Set method for the payment_subtotals
        :param payment_subtotals: payment_subtotals
        """
        self.__payment_subtotals = payment_subtotals

    def get_payment_totals(self) -> Optional[dict]:
        """
        Get method for the payment_totals
        :return: payment_totals
        """
        return self.__payment_totals

    def set_payment_totals(self, payment_totals: Optional[dict]) -> None:
        """
        Set method for the payment_totals
        :param payment_totals: payment_totals
        """
        self.__payment_totals = payment_totals

    def get_payment_display_totals(self) -> Optional[dict]:
        """
        Get method for the payment_display_totals
        :return: payment_display_totals
        """
        return self.__payment_display_totals

    def set_payment_display_totals(
        self, payment_display_totals: Optional[dict]
    ) -> None:
        """
        Set method for the payment_display_totals
        :param payment_display_totals: payment_display_totals
        """
        self.__payment_display_totals = payment_display_totals

    def get_payment_display_sub_totals(self) -> Optional[dict]:
        """
        Get method for the payment_display_subtotals
        :return: payment_display_subtotals
        """
        return self.__payment_display_subtotals

    def set_payment_display_sub_totals(
        self, payment_display_subtotals: Optional[dict]
    ) -> None:
        """
        Set method for the payment_display_subtotals
        :param payment_display_subtotals: payment_display_subtotals
        """
        self.__payment_display_subtotals = payment_display_subtotals

    def get_payment_codes(self) -> Optional[dict]:
        """
        Get method for the payment_codes
        :return: payment_codes
        """
        return self.__payment_codes

    def set_payment_codes(self, payment_codes: Optional[dict]) -> None:
        """
        Set method for the payment_codes
        :param payment_codes: payment_codes
        """
        self.__payment_codes = payment_codes

    def get_acceptance_window(self) -> Optional[int]:
        """
        Get method for the acceptance_window
        :return: acceptance_window
        """
        return self.__acceptance_window

    def set_acceptance_window(self, acceptance_window: Optional[int]) -> None:
        """
        Set method for the acceptance_window
        :param acceptance_window: acceptance_window
        """
        self.__acceptance_window = acceptance_window

    def get_refund_addresses(self) -> Optional[List[str]]:
        """
        Get method for the refund_addresses
        :return: refund_addresses
        """
        return self.__refund_addresses

    def set_refund_addresses(self, refund_addresses: Optional[List[str]]) -> None:
        """
        Set method for the refund_addresses
        :param refund_addresses: refund_addresses
        """
        self.__refund_addresses = refund_addresses

    def get_close_url(self) -> Optional[str]:
        """
        Get method for the close_url
        :return: close_url
        """
        return self.__close_url

    def set_close_url(self, close_url: Optional[str]) -> None:
        """
        Set method for the close_url
        :param close_url: close_url
        """
        self.__close_url = close_url

    def get_auto_redirect(self) -> bool:
        """
        Get method for the auto_redirect
        :return: auto_redirect
        """
        return self.__auto_redirect

    def set_auto_redirect(self, auto_redirect: bool) -> None:
        """
        Set method for the auto_redirect
        :param auto_redirect: auto_redirect
        """
        self.__auto_redirect = auto_redirect

    def get_json_pay_pro_required(self) -> bool:
        """
        Get method for the json_paypro_required
        :return: json_paypro_required
        """
        return self.__json_paypro_required

    def set_json_pay_pro_required(self, json_paypro_required: bool) -> None:
        """
        Set method for the json_paypro_required
        :param json_paypro_required: json_paypro_required
        """
        self.__json_paypro_required = json_paypro_required

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

    def get_url(self) -> Optional[str]:
        """
        Get method for the url
        :return: url
        """
        return self.__url

    def set_url(self, url: Optional[str]) -> None:
        """
        Set method for the url
        :param url: url
        """
        self.__url = url

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

    def get_low_fee_detected(self) -> bool:
        """
        Get method for the low_fee_detected
        :return: low_fee_detected
        """
        return self.__low_fee_detected

    def set_low_fee_detected(self, low_fee_detected: bool) -> None:
        """
        Set method for the low_fee_detected
        :param low_fee_detected: low_fee_detected
        """
        self.__low_fee_detected = low_fee_detected

    def get_invoice_time(self) -> Optional[int]:
        """
        Get method for the invoice_time
        :return: invoice_time
        """
        return self.__invoice_time

    def set_invoice_time(self, invoice_time: Optional[int]) -> None:
        """
        Set method for the invoice_time
        :param invoice_time: invoice_time
        """
        self.__invoice_time = invoice_time

    def get_expiration_time(self) -> Optional[int]:
        """
        Get method for the expiration_time
        :return: expiration_time
        """
        return self.__expiration_time

    def set_expiration_time(self, expiration_time: Optional[int]) -> None:
        """
        Set method for the expiration_time
        :param expiration_time: expiration_time
        """
        self.__expiration_time = expiration_time

    def get_current_time(self) -> Optional[int]:
        """
        Get method for the current_time
        :return: current_time
        """
        return self.__current_time

    def set_current_time(self, current_time: Optional[int]) -> None:
        """
        Set method for the current_time
        :param current_time: current_time
        """
        self.__current_time = current_time

    def get_transactions(self) -> Optional[List[Transaction]]:
        """
        Get method for the transactions
        :return: transactions
        """
        return self.__transactions

    def set_transactions(self, transactions: List[Transaction]) -> None:
        """
        Set method for the transactions
        :param transactions: transactions
        """
        self.__transactions = transactions

    def get_exception_status(self) -> Optional[str]:
        """
        Get method for the exception_status
        :return: exception_status
        """
        return self.__exception_status

    def set_exception_status(self, exception_status: Optional[str]) -> None:
        """
        Set method for the exception_status
        :param exception_status: exception_status
        """
        self.__exception_status = exception_status

    def get_target_confirmations(self) -> Optional[int]:
        """
        Get method for the target_confirmations
        :return: target_confirmations
        """
        return self.__target_confirmations

    def set_target_confirmations(self, target_confirmations: Optional[int]) -> None:
        """
        Set method for the target_confirmations
        :param target_confirmations: target_confirmations
        """
        self.__target_confirmations = target_confirmations

    def get_refund_address_request_pending(self) -> bool:
        """
        Get method for the refund_address_request_pending
        :return: refund_address_request_pending
        """
        return self.__refund_address_request_pending

    def set_refund_address_request_pending(
        self, refund_address_request_pending: bool
    ) -> None:
        """
        Set method for the refund_address_request_pending
        :param refund_address_request_pending: refund_address_request_pending
        """
        self.__refund_address_request_pending = refund_address_request_pending

    def get_buyer_provided_email(self) -> Optional[str]:
        """
        Get method for the buyer_provided_email
        :return: buyer_provided_email
        """
        return self.__buyer_provided_email

    def set_buyer_provided_email(self, buyer_provided_email: Optional[str]) -> None:
        """
        Set method for the buyer_provided_email
        :param buyer_provided_email: buyer_provided_email
        """
        self.__buyer_provided_email = buyer_provided_email

    def get_buyer_provided_info(self) -> Optional[BuyerProvidedInfo]:
        """
        Get method for the buyer_provided_info
        :return: buyer_provided_info
        """
        return self.__buyer_provided_info

    def set_buyer_provided_info(self, buyer_provided_info: BuyerProvidedInfo) -> None:
        """
        Set method for the buyer_provided_info
        :param buyer_provided_info: buyer_provided_info
        """
        self.__buyer_provided_info = buyer_provided_info

    def get_supported_transaction_currencies(
        self,
    ) -> Optional[SupportedTransactionCurrencies]:
        """
        Get method for the supported_transaction_currencies
        :return: supported_transaction_currencies
        """
        return self.__supported_transaction_currencies

    def set_supported_transaction_currencies(
        self, supported_transaction_currencies: SupportedTransactionCurrencies
    ) -> None:
        """
        Set method for the supported_transaction_currencies
        :param supported_transaction_currencies: supported_transaction_currencies
        """
        self.__supported_transaction_currencies = supported_transaction_currencies

    def get_miner_fees(self) -> Optional[MinerFees]:
        """
        Get method for the miner_fees
        :return: miner_fees
        """
        return self.__miner_fees

    def set_miner_fees(self, miner_fees: Optional[MinerFees]) -> None:
        """
        Set method for the miner_fees
        :param miner_fees: miner_fees
        """
        self.__miner_fees = miner_fees

    def get_non_pay_pro_payment_received(self) -> bool:
        """
        Get method for the non_paypro_payment_received
        :return: non_paypro_payment_received
        """
        return self.__non_pay_pro_payment_received

    def set_non_pay_pro_payment_received(
        self, non_pay_pro_payment_received: bool
    ) -> None:
        """
        Set method for the non_paypro_payment_received
        :param non_pay_pro_payment_received: non_paypro_payment_received
        """
        self.__non_pay_pro_payment_received = non_pay_pro_payment_received

    def get_shopper(self) -> Optional[Shopper]:
        """
        Get method for the shopper
        :return: shopper
        """
        return self.__shopper

    def set_shopper(self, shopper: Optional[Shopper]) -> None:
        """
        Set method for the shopper
        :param shopper: shopper
        """
        self.__shopper = shopper

    def get_bill_id(self) -> Optional[str]:
        """
        Get method for the bill_id
        :return: bill_id
        """
        return self.__bill_id

    def set_bill_id(self, bill_id: Optional[str]) -> None:
        """
        Set method for the bill_id
        :param bill_id: bill_id
        """
        self.__bill_id = bill_id

    def get_refund_info(self) -> Optional[List[RefundInfo]]:
        """
        Get method for the refund_info
        :return: refund_info
        """
        return self.__refund_info

    def set_refund_info(self, refund_info: Optional[List[RefundInfo]]) -> None:
        """
        Set method for the refund_info
        :param refund_info: refund_info
        """
        self.__refund_info = refund_info

    def get_extended_notifications(self) -> bool:
        """
        Get method for the extended_notifications
        :return: extended_notifications
        """
        return self.__extended_notifications

    def set_extended_notifications(self, extended_notifications: bool) -> None:
        """
        Set method for the extended_notifications
        :param extended_notifications: extended_notifications
        """
        self.__extended_notifications = extended_notifications

    def get_transaction_currency(self) -> Optional[str]:
        """
        Get method for the transaction_currency
        :return: transaction_currency
        """
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency: Optional[str]) -> None:
        """
        Set method for the transaction_currency
        :param transaction_currency: transaction_currency
        """
        self.__transaction_currency = transaction_currency

    def get_underpaid_amount(self) -> Optional[str]:
        """
        Get method for the underpaid_amount
        :return: underpaid_amount
        """
        return self.__underpaid_amount

    def set_underpaid_amount(self, underpaid_amount: Optional[float]) -> None:
        """
        Set method for the underpaid_amount
        :param underpaid_amount: underpaid_amount
        """
        self.__underpaid_amount = underpaid_amount

    def get_overpaid_amount(self) -> Optional[float]:
        """
        Get method for the overpaid_amount
        :return: overpaid_amount
        """
        return self.__overpaid_amount

    def set_overpaid_amount(self, overpaid_amount: Optional[float]) -> None:
        """
        Set method for the overpaid_amount
        :param overpaid_amount: overpaid_amount
        """
        self.__overpaid_amount = overpaid_amount

    def get_amount_paid(self) -> Optional[float]:
        """
        Get method for the amount_paid
        :return: overpaid_amount
        """
        return self.__amount_paid

    def set_amount_paid(self, amount_paid: Optional[float]) -> None:
        """
        Set method for the amount_paid
        :param amount_paid: amount_paid
        """
        self.__amount_paid = amount_paid

    def get_display_amount_paid(self) -> Optional[str]:
        """
        Get method for the display_amount_paid
        :return: display_amount_paid
        """
        return self.__display_amount_paid

    def set_display_amount_paid(self, display_amount_paid: Optional[str]) -> None:
        """
        Set method for the display_amount_paid
        :param display_amount_paid: display_amount_paid
        """
        self.__display_amount_paid = display_amount_paid

    def get_exchange_rates(self) -> Optional[dict]:
        """
        Get method for the exchange_rates
        :return: exchange_rates
        """
        return self.__exchange_rates

    def set_exchange_rates(self, exchange_rates: Optional[dict]) -> None:
        """
        Set method for the exchange_rates
        :param exchange_rates: exchange_rates
        """
        self.__exchange_rates = exchange_rates

    def get_price(self) -> Optional[float]:
        """
        Get method for the price
        :return: price
        """
        return self.__price

    def set_price(self, price: Optional[float]) -> None:
        """
        Set method for the price
        :param price: price
        """
        self.__price = price

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

    def get_payment_string(self) -> Optional[str]:
        """
        Get method for the payment_string
        :return: payment_string
        """
        return self.__payment_string

    def set_payment_string(self, payment_string: Optional[str]) -> None:
        """
        Set method for the payment_string
        :param payment_string: payment_string
        """
        self.__payment_string = payment_string

    def get_verification_link(self) -> Optional[str]:
        """
        Get method for the verification_link
        :return: verification_link
        """
        return self.__verification_link

    def set_verification_link(self, verification_link: Optional[str]) -> None:
        """
        Set method for the verification_link
        :param verification_link: verification_link
        """
        self.__verification_link = verification_link

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

    def get_merchant_name(self) -> Optional[str]:
        """
        Get method for the merchant_name
        :return: merchant_name
        """
        return self.__merchant_name

    def set_merchant_name(self, merchant_name: Optional[str]) -> None:
        """
        Set method for the merchant_name
        :param merchant_name: merchant_name
        """
        self.__merchant_name = merchant_name

    def get_forced_buyer_selected_wallet(self) -> Optional[str]:
        """
        Get method for the forced_buyer_selected_wallet
        :return: forced_buyer_selected_wallet
        """
        return self.__forced_buyer_selected_wallet

    def set_forced_buyer_selected_wallet(
        self, forced_buyer_selected_wallet: Optional[str]
    ) -> None:
        """
        Set method for the forced_buyer_selected_wallet
        :param forced_buyer_selected_wallet: forced_buyer_selected_wallet
        """
        self.__forced_buyer_selected_wallet = forced_buyer_selected_wallet

    def get_forced_buyer_selected_transaction_currency(self) -> Optional[str]:
        """
        Get method for the forced_buyer_selected_transaction_currency
        :return: forced_buyer_selected_transaction_currency
        """
        return self.__forced_buyer_selected_transaction_currency

    def set_forced_buyer_selected_transaction_currency(
        self, forced_buyer_selected_transaction_currency: Optional[str]
    ) -> None:
        """
        Set method for the forced_buyer_selected_transaction_currency
        :param forced_buyer_selected_transaction_currency: forced_buyer_selected_transaction_currency
        """
        self.__forced_buyer_selected_transaction_currency = (
            forced_buyer_selected_transaction_currency
        )

    def get_is_cancelled(self) -> bool:
        """
        Get method for the is_cancelled
        :return: is_cancelled
        """
        return self.__is_cancelled

    def set_is_cancelled(self, is_cancelled: bool) -> None:
        """
        Set method for the is_cancelled
        :param is_cancelled: is_cancelled
        """
        self.__is_cancelled = is_cancelled

    def get_bitpay_id_required(self) -> bool:
        """
        Get method for the bitpay_id_required
        :return: bitpay_id_required
        """
        return self.__bitpay_id_required

    def set_bitpay_id_required(self, bitpay_id_required: bool) -> None:
        """
        Set method for the bitpay_id_required
        :param bitpay_id_required: bitpay_id_required
        """
        self.__bitpay_id_required = bitpay_id_required

    def get_universal_codes(self) -> Optional[UniversalCodes]:
        """
        Get method for the universal_codes
        :return: universal_codes
        """
        return self.__universal_codes

    def set_universal_codes(self, universal_codes: Optional[UniversalCodes]) -> None:
        """
        Set method for the universal_codes
        :param universal_codes: universal_codes
        """
        self.__universal_codes = universal_codes

    def get_itemized_details(self) -> Optional[List[ItemizedDetails]]:
        """
        Get method for the itemized_details
        :return: ItemizedDetails[]
        """
        return self.__itemized_details

    def set_itemized_details(self, itemized_details: List[ItemizedDetails]) -> None:
        """
        Set method for the itemized_details
        :param itemized_details: itemized_details
        """
        self.__itemized_details = itemized_details

    # Buyer Data

    def get_buyer(self) -> Optional[Buyer]:
        """
        Get method for the buyer
        :return: buyer
        """
        return self.__buyer

    def set_buyer(self, buyer: Optional[Buyer]) -> None:
        """
        Set method for the buyer
        :param buyer: buyer
        """
        self.__buyer = buyer

    def get_buyer_sms(self) -> Optional[str]:
        """
        Get buyer sms
        :return: Optional[str]
        """
        return self.__buyer_sms

    def set_buyer_sms(self, sms: Optional[str]) -> None:
        """
        Set method for the buyer
        :param sms: str
        """
        self.__buyer_sms = sms

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
