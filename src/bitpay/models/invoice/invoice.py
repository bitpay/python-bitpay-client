"""
Invoice
"""
from .buyer import Buyer
from .shopper import Shopper
from .miner_fees import MinerFees
from .refund_info import RefundInfo
from .universal_codes import UniversalCodes
from .itemized_details import ItemizedDetails
from .buyer_provided_info import BuyerProvidedInfo
from ...utils.key_utils import change_camel_case_to_snake_case
from .supported_transaction_currencies import SupportedTransactionCurrencies


class Invoice:
    """
    Invoices are time-sensitive payment requests addressed to specific buyers.
    An invoice has a fixed price,typically denominated in fiat currency.
    It also has an equivalent price in the supported cryptocurrencies,
    calculated by BitPay, at a locked exchange rate with an expiration
    time of 15 minutes.
    """

    __currency = ""

    __guid = ""
    __token = ""

    __price = None
    __pos_data = None
    __notification_url = ""
    __transaction_speed = ""
    __full_notifications = False
    __notification_email = ""
    __redirect_URL = ""
    __order_id = ""
    __item_desc = ""
    __item_code = ""
    __physical = False
    __payment_currencies = []
    __payment_subtotals = None
    __payment_totals = None
    __payment_display_totals = None
    __payment_display_subtotals = None
    __payment_codes = None
    __acceptance_window = None
    __buyer = Buyer()
    __refund_addresses = None
    __close_url = ""
    __auto_redirect = False
    __json_paypro_required = None

    __id = None
    __url = None
    __status = None
    __low_fee_detected = None
    __invoice_time = None
    __expiration_time = None
    __current_time = None
    __transactions = None
    __exception_status = None
    __target_confirmations = None
    __refund_address_request_pending = None
    __buyer_provided_email = None
    __buyer_provided_info = BuyerProvidedInfo()
    __supported_transaction_currencies = SupportedTransactionCurrencies()
    __miner_fees = MinerFees()
    __non_paypro_payment_received = None
    __shopper = Shopper()
    __bill_id = None
    __refund_info = RefundInfo()
    __extended_notifications = False

    __transaction_currency = None
    __underpaid_amount = None
    __overpaid_amount = None
    __amount_paid = None
    __display_amount_paid = None
    __exchange_rates = None

    __payment_string = None
    __verification_link = None
    __buyer_email = None
    __declined_amount = None
    __merchant_name = None
    __forced_buyer_selected_wallet = None
    __forced_buyer_selected_transaction_currency = None
    __itemized_details = ItemizedDetails()
    __universal_codes = UniversalCodes()
    __is_cancelled = None
    __bitpay_id_required = None
    __rate_refresh_time = None

    def __init__(self, price=None, currency=None, **kwargs):
        self.set_price(price)
        self.set_currency(currency)

        for key, value in kwargs.items():
            try:
                if key in [
                    "buyer",
                    "buyerProvidedInfo",
                    "shopper",
                    "supportedTransactionCurrencies",
                    "minerFees",
                    "refundInfo",
                    "universalCodes",
                    "itemizedDetails",
                ]:
                    klass = globals()[key[0].upper() + key[1:]]

                    if isinstance(value, list):
                        objs = []
                        for obj in value:
                            objs.append(klass(**obj))
                        value = objs
                    else:
                        value = klass(**value)
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_guid(self):
        """
        Get method for the guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid):
        """
        Set method for the guid
        :param guid: guid
        """
        self.__guid = guid

    def get_token(self):
        """
        Get method for the token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for the token
        :param token: token
        """
        self.__token = token

    def get_declined_amount(self):
        """
        Get method for the declined_amount
        :return: declined_amount
        """
        return self.__declined_amount

    def set_declined_amount(self, declined_amount):
        """
        Set method for the declined_amount
        :param declined_amount: declined_amount
        """
        self.__declined_amount = declined_amount

    def get_pos_data(self):
        """
        Get method for the pos_data
        :return: pos_data
        """
        return self.__pos_data

    def set_pos_data(self, pos_data):
        """
        Set method for the pos_data
        :param pos_data: posData
        """
        self.__pos_data = pos_data

    def get_notification_url(self):
        """
        Get method for the notification_url
        :return: notification_url
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        Set method for the notification_url
        :param notification_url: notification_url
        """
        self.__notification_url = notification_url

    def get_transaction_speed(self):
        """
        Get method for the transaction_speed
        :return: transaction_speed
        """
        return self.__transaction_speed

    def set_transaction_speed(self, transaction_speed):
        """
        Set method for the transaction_speed
        :param transaction_speed: transaction_speed
        """
        self.__transaction_speed = transaction_speed

    def get_full_notifications(self):
        """
        Get method for the full_notifications
        :return: full_notifications
        """
        return self.__full_notifications

    def set_full_notifications(self, full_notifications):
        """
        Set method for the full_notifications
        :param full_notifications: full_notifications
        """
        self.__full_notifications = full_notifications

    def get_notification_email(self):
        """
        Get method for the notification_email
        :return: notification_email
        """
        return self.__notification_email

    def set_notification_email(self, notification_email):
        """
        Set method for the notification_email
        :param notification_email: notification_email
        """
        self.__notification_email = notification_email

    def get_redirect_u_r_l(self):
        """
        Get method for the redirect_URL
        :return: redirect_URL
        """
        return self.__redirect_URL

    def set_redirect_u_r_l(self, redirect_URL):
        """
        Set method for the redirect_URL
        :param redirect_URL: redirect_URL
        """
        self.__redirect_URL = redirect_URL

    def get_order_id(self):
        """
        Get method for the order_id
        :return: order_id
        """
        return self.__order_id

    def set_order_id(self, order_id):
        """
        Set method for the order_id
        :param order_id: order_id
        """
        self.__order_id = order_id

    def get_item_desc(self):
        """
        Get method for the item_desc
        :return: item_desc
        """
        return self.__item_desc

    def set_item_desc(self, item_desc):
        """
        Set method for the item_desc
        :param item_desc: item_desc
        """
        self.__item_desc = item_desc

    def get_item_code(self):
        """
        Get method for the item_code
        :return: item_code
        """
        return self.__item_code

    def set_item_code(self, item_code):
        """
        Set method for the item_code
        :param item_code: item_code
        """
        self.__item_code = item_code

    def get_physical(self):
        """
        Get method for the physical
        :return: physical
        """
        return self.__physical

    def set_physical(self, physical):
        """
        Set method for the physical
        :param physical: physical
        """
        self.__physical = physical

    def get_payment_currencies(self):
        """
        Get method for the payment_currencies
        :return: payment_currencies
        """
        return self.__payment_currencies

    def set_payment_currencies(self, payment_currencies):
        """
        Set method for the payment_currencies
        :param payment_currencies: payment_currencies
        """
        self.__payment_currencies = payment_currencies

    def get_payment_subtotals(self):
        """
        Get method for the payment_subtotals
        :return: payment_subtotals
        """
        return self.__payment_subtotals

    def set_payment_subtotals(self, payment_subtotals):
        """
        Set method for the payment_subtotals
        :param payment_subtotals: payment_subtotals
        """
        self.__payment_subtotals = payment_subtotals

    def get_payment_totals(self):
        """
        Get method for the payment_totals
        :return: payment_totals
        """
        return self.__payment_totals

    def set_payment_totals(self, payment_totals):
        """
        Set method for the payment_totals
        :param payment_totals: payment_totals
        """
        self.__payment_totals = payment_totals

    def get_payment_display_totals(self):
        """
        Get method for the payment_display_totals
        :return: payment_display_totals
        """
        return self.__payment_display_totals

    def set_payment_display_totals(self, payment_display_totals):
        """
        Set method for the payment_display_totals
        :param payment_display_totals: payment_display_totals
        """
        self.__payment_display_totals = payment_display_totals

    def get_payment_display_sub_totals(self):
        """
        Get method for the payment_display_subtotals
        :return: payment_display_subtotals
        """
        return self.__payment_display_subtotals

    def set_payment_display_sub_totals(self, payment_display_subtotals):
        """
        Set method for the payment_display_subtotals
        :param payment_display_subtotals: payment_display_subtotals
        """
        self.__payment_display_subtotals = payment_display_subtotals

    def get_payment_codes(self):
        """
        Get method for the payment_codes
        :return: payment_codes
        """
        return self.__payment_codes

    def set_payment_codes(self, payment_codes):
        """
        Set method for the payment_codes
        :param payment_codes: payment_codes
        """
        self.__payment_codes = payment_codes

    def get_acceptance_window(self):
        """
        Get method for the acceptance_window
        :return: acceptance_window
        """
        return self.__acceptance_window

    def set_acceptance_window(self, acceptance_window):
        """
        Set method for the acceptance_window
        :param acceptance_window: acceptance_window
        """
        self.__acceptance_window = acceptance_window

    def get_refund_addresses(self):
        """
        Get method for the refund_addresses
        :return: refund_addresses
        """
        return self.__refund_addresses

    def set_refund_addresses(self, refund_addresses):
        """
        Set method for the refund_addresses
        :param refund_addresses: refund_addresses
        """
        self.__refund_addresses = refund_addresses

    def get_close_url(self):
        """
        Get method for the close_url
        :return: close_url
        """
        return self.__close_url

    def set_close_url(self, close_url):
        """
        Set method for the close_url
        :param close_url: close_url
        """
        self.__close_url = close_url

    def get_auto_redirect(self):
        """
        Get method for the auto_redirect
        :return: auto_redirect
        """
        return self.__auto_redirect

    def set_auto_redirect(self, auto_redirect):
        """
        Set method for the auto_redirect
        :param auto_redirect: auto_redirect
        """
        self.__auto_redirect = auto_redirect

    def get_json_pay_pro_required(self):
        """
        Get method for the json_paypro_required
        :return: json_paypro_required
        """
        return self.__json_paypro_required

    def set_json_pay_pro_required(self, json_paypro_required):
        """
        Set method for the json_paypro_required
        :param json_paypro_required: json_paypro_required
        """
        self.__json_paypro_required = json_paypro_required

    def get_id(self):
        """
        Get method for the id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for the id
        :param id: id
        """
        self.__id = id

    def get_url(self):
        """
        Get method for the url
        :return: url
        """
        return self.__url

    def set_url(self, url):
        """
        Set method for the url
        :param url: url
        """
        self.__url = url

    def get_status(self):
        """
        Get method for the status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for the status
        :param status: status
        """
        self.__status = status

    def get_low_fee_detected(self):
        """
        Get method for the low_fee_detected
        :return: low_fee_detected
        """
        return self.__low_fee_detected

    def set_low_fee_detected(self, low_fee_detected):
        """
        Set method for the low_fee_detected
        :param low_fee_detected: low_fee_detected
        """
        self.__low_fee_detected = low_fee_detected

    def get_invoice_time(self):
        """
        Get method for the invoice_time
        :return: invoice_time
        """
        return self.__invoice_time

    def set_invoice_time(self, invoice_time):
        """
        Set method for the invoice_time
        :param invoice_time: invoice_time
        """
        self.__invoice_time = invoice_time

    def get_expiration_time(self):
        """
        Get method for the expiration_time
        :return: expiration_time
        """
        return self.__expiration_time

    def set_expiration_time(self, expiration_time):
        """
        Set method for the expiration_time
        :param expiration_time: expiration_time
        """
        self.__expiration_time = expiration_time

    def get_current_time(self):
        """
        Get method for the current_time
        :return: current_time
        """
        return self.__current_time

    def set_current_time(self, current_time):
        """
        Set method for the current_time
        :param current_time: current_time
        """
        self.__current_time = current_time

    def get_transactions(self):
        """
        Get method for the transactions
        :return: transactions
        """
        return self.__transactions

    def set_transactions(self, transactions):
        """
        Set method for the transactions
        :param transactions: transactions
        """
        self.__transactions = transactions

    def get_exception_status(self):
        """
        Get method for the exception_status
        :return: exception_status
        """
        return self.__exception_status

    def set_exception_status(self, exception_status):
        """
        Set method for the exception_status
        :param exception_status: exception_status
        """
        self.__exception_status = exception_status

    def get_target_confirmations(self):
        """
        Get method for the target_confirmations
        :return: target_confirmations
        """
        return self.__target_confirmations

    def set_target_confirmations(self, target_confirmations):
        """
        Set method for the target_confirmations
        :param target_confirmations: target_confirmations
        """
        self.__target_confirmations = target_confirmations

    def get_refund_address_request_pending(self):
        """
        Get method for the refund_address_request_pending
        :return: refund_address_request_pending
        """
        return self.__refund_address_request_pending

    def set_refund_address_request_pending(self, refund_address_request_pending):
        """
        Set method for the refund_address_request_pending
        :param refund_address_request_pending: refund_address_request_pending
        """
        self.__refund_address_request_pending = refund_address_request_pending

    def get_buyer_provided_email(self):
        """
        Get method for the buyer_provided_email
        :return: buyer_provided_email
        """
        return self.__buyer_provided_email

    def set_buyer_provided_email(self, buyer_provided_email):
        """
        Set method for the buyer_provided_email
        :param buyer_provided_email: buyer_provided_email
        """
        self.__buyer_provided_email = buyer_provided_email

    def get_buyer_provided_info(self):
        """
        Get method for the buyer_provided_info
        :return: buyer_provided_info
        """
        return self.__buyer_provided_info

    def set_buyer_provided_info(self, buyer_provided_info: BuyerProvidedInfo):
        """
        Set method for the buyer_provided_info
        :param buyer_provided_info: buyer_provided_info
        """
        self.__buyer_provided_info = buyer_provided_info

    def get_supported_transaction_currencies(self):
        """
        Get method for the supported_transaction_currencies
        :return: supported_transaction_currencies
        """
        return self.__supported_transaction_currencies

    def set_supported_transaction_currencies(
        self, supported_transaction_currencies: SupportedTransactionCurrencies
    ):
        """
        Set method for the supported_transaction_currencies
        :param supported_transaction_currencies: supported_transaction_currencies
        """
        self.__supported_transaction_currencies = supported_transaction_currencies

    def get_miner_fees(self):
        """
        Get method for the miner_fees
        :return: miner_fees
        """
        return self.__miner_fees

    def set_miner_fees(self, miner_fees: MinerFees):
        """
        Set method for the miner_fees
        :param miner_fees: miner_fees
        """
        self.__miner_fees = miner_fees

    def get_non_paypro_payment_received(self):
        """
        Get method for the non_paypro_payment_received
        :return: non_paypro_payment_received
        """
        return self.__non_paypro_payment_received

    def set_non_paypro_payment_received(self, non_paypro_payment_received):
        """
        Set method for the non_paypro_payment_received
        :param non_paypro_payment_received: non_paypro_payment_received
        """
        self.__non_paypro_payment_received = non_paypro_payment_received

    def get_shopper(self):
        """
        Get method for the shopper
        :return: shopper
        """
        return self.__shopper

    def set_shopper(self, shopper: Shopper):
        """
        Set method for the shopper
        :param shopper: shopper
        """
        self.__shopper = shopper

    def get_bill_id(self):
        """
        Get method for the bill_id
        :return: bill_id
        """
        return self.__bill_id

    def set_bill_id(self, bill_id):
        """
        Set method for the bill_id
        :param bill_id: bill_id
        """
        self.__bill_id = bill_id

    def get_refund_info(self):
        """
        Get method for the refund_info
        :return: refund_info
        """
        return self.__refund_info

    def set_refund_info(self, refund_info: RefundInfo):
        """
        Set method for the refund_info
        :param refund_info: refund_info
        """
        self.__refund_info = refund_info

    def get_extended_notifications(self):
        """
        Get method for the extended_notifications
        :return: extended_notifications
        """
        return self.__extended_notifications

    def set_extended_notifications(self, extended_notifications):
        """
        Set method for the extended_notifications
        :param extended_notifications: extended_notifications
        """
        self.__extended_notifications = extended_notifications

    def get_transaction_currency(self):
        """
        Get method for the transaction_currency
        :return: transaction_currency
        """
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency):
        """
        Set method for the transaction_currency
        :param transaction_currency: transaction_currency
        """
        self.__transaction_currency = transaction_currency

    def get_underpaid_amount(self):
        """
        Get method for the underpaid_amount
        :return: underpaid_amount
        """
        return self.__underpaid_amount

    def set_underpaid_amount(self, underpaid_amount):
        """
        Set method for the underpaid_amount
        :param underpaid_amount: underpaid_amount
        """
        self.__underpaid_amount = underpaid_amount

    def get_overpaid_amount(self):
        """
        Get method for the overpaid_amount
        :return: overpaid_amount
        """
        return self.__overpaid_amount

    def set_overpaid_amount(self, overpaid_amount):
        """
        Set method for the overpaid_amount
        :param overpaid_amount: overpaid_amount
        """
        self.__overpaid_amount = overpaid_amount

    def get_amount_paid(self):
        """
        Get method for the amount_paid
        :return: overpaid_amount
        """
        return self.__amount_paid

    def set_amount_paid(self, amount_paid):
        """
        Set method for the amount_paid
        :param amount_paid: amount_paid
        """
        self.__amount_paid = amount_paid

    def get_display_amount_paid(self):
        """
        Get method for the display_amount_paid
        :return: display_amount_paid
        """
        return self.__display_amount_paid

    def set_display_amount_paid(self, display_amount_paid):
        """
        Set method for the display_amount_paid
        :param display_amount_paid: display_amount_paid
        """
        self.__display_amount_paid = display_amount_paid

    def get_exchange_rates(self):
        """
        Get method for the exchange_rates
        :return: exchange_rates
        """
        return self.__exchange_rates

    def set_exchange_rates(self, exchange_rates):
        """
        Set method for the exchange_rates
        :param exchange_rates: exchange_rates
        """
        self.__exchange_rates = exchange_rates

    def get_price(self):
        """
        Get method for the price
        :return: price
        """
        return self.__price

    def set_price(self, price):
        """
        Set method for the price
        :param price: price
        """
        self.__price = price

    def get_currency(self):
        """
        Get method for the currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for the currency
        :param currency: currency
        """
        self.__currency = currency

    def get_payment_string(self):
        """
        Get method for the payment_string
        :return: payment_string
        """
        return self.__payment_string

    def set_payment_string(self, payment_string):
        """
        Set method for the payment_string
        :param payment_string: payment_string
        """
        self.__payment_string = payment_string

    def get_verification_link(self):
        """
        Get method for the verification_link
        :return: verification_link
        """
        return self.__verification_link

    def set_verification_link(self, verification_link):
        """
        Set method for the verification_link
        :param verification_link: verification_link
        """
        self.__verification_link = verification_link

    def get_buyer_email(self):
        """
        Get method for the buyer_email
        :return: buyer_email
        """
        return self.__buyer_email

    def set_buyer_email(self, buyer_email):
        """
        Set method for the buyer_email
        :param buyer_email: buyer_email
        """
        self.__buyer_email = buyer_email

    def get_merchant_name(self):
        """
        Get method for the merchant_name
        :return: merchant_name
        """
        return self.__merchant_name

    def set_merchant_name(self, merchant_name):
        """
        Set method for the merchant_name
        :param merchant_name: merchant_name
        """
        self.__merchant_name = merchant_name

    def get_forced_buyer_selected_wallet(self):
        """
        Get method for the forced_buyer_selected_wallet
        :return: forced_buyer_selected_wallet
        """
        return self.__forced_buyer_selected_wallet

    def set_forced_buyer_selected_wallet(self, forced_buyer_selected_wallet):
        """
        Set method for the forced_buyer_selected_wallet
        :param forced_buyer_selected_wallet: forced_buyer_selected_wallet
        """
        self.__forced_buyer_selected_wallet = forced_buyer_selected_wallet

    def get_forced_buyer_selected_transaction_currency(self):
        """
        Get method for the forced_buyer_selected_transaction_currency
        :return: forced_buyer_selected_transaction_currency
        """
        return self.__forced_buyer_selected_transaction_currency

    def set_forced_buyer_selected_transaction_currency(
        self, forced_buyer_selected_transaction_currency
    ):
        """
        Set method for the forced_buyer_selected_transaction_currency
        :param forced_buyer_selected_transaction_currency: forced_buyer_selected_transaction_currency
        """
        self.__forced_buyer_selected_transaction_currency = (
            forced_buyer_selected_transaction_currency
        )

    def get_is_cancelled(self):
        """
        Get method for the is_cancelled
        :return: is_cancelled
        """
        return self.__is_cancelled

    def set_is_cancelled(self, is_cancelled):
        """
        Set method for the is_cancelled
        :param is_cancelled: is_cancelled
        """
        self.__is_cancelled = is_cancelled

    def get_bitpay_id_required(self):
        """
        Get method for the bitpay_id_required
        :return: bitpay_id_required
        """
        return self.__bitpay_id_required

    def set_bitpay_id_required(self, bitpay_id_required):
        """
        Set method for the bitpay_id_required
        :param bitpay_id_required: bitpay_id_required
        """
        self.__bitpay_id_required = bitpay_id_required

    def get_rate_refresh_time(self):
        """
        Get method for the rate_refresh_time
        :return: rate_refresh_time
        """
        return self.__rate_refresh_time

    def set_rate_refresh_time(self, rate_refresh_time):
        """
        Set method for the rate_refresh_time
        :param rate_refresh_time: rate_refresh_time
        """
        self.__rate_refresh_time = rate_refresh_time

    def get_universal_codes(self):
        """
        Get method for the universal_codes
        :return: universal_codes
        """
        return self.__universal_codes

    def set_universal_codes(self, universal_codes: UniversalCodes):
        """
        Set method for the universal_codes
        :param universal_codes: universal_codes
        """
        self.__universal_codes = universal_codes

    def get_itemized_details(self):
        """
        Get method for the itemized_details
        :return: itemized_details
        """
        items = []
        for item in items:
            if isinstance(item, ItemizedDetails):
                items.append(item.to_json())
            else:
                items.append(item)
        return items

    def set_itemized_details(self, itemized_details: ItemizedDetails):
        """
        Set method for the itemized_details
        :param itemized_details: itemized_details
        """
        items_array = []
        for item in itemized_details:
            if isinstance(item, ItemizedDetails):
                items_array.append(item.to_json())
            else:
                items_array.append(item)
        self.__itemized_details = items_array

    # Buyer Data

    def get_buyer(self):
        """
        Get method for the buyer
        :return: buyer
        """
        return self.__buyer

    def set_buyer(self, buyer: Buyer):
        """
        Set method for the buyer
        :param buyer: buyer
        """
        self.__buyer = buyer

    def to_json(self):
        """
        :return: data in json
        """
        supported_transaction_currencies = {}
        for key, value in self.get_supported_transaction_currencies().to_json().items():
            supported_transaction_currencies[key] = value.to_json()

        miner_fees = {}
        for key, value in self.get_miner_fees().to_json().items():
            miner_fees[key] = value.to_json()

        data = {
            "currency": self.get_currency(),
            "price": self.get_price(),
            "token": self.get_token(),
            "posData": self.get_pos_data(),
            "notificationURL": self.get_notification_url(),
            "transactionSpeed": self.get_transaction_speed(),
            "fullNotifications": self.get_full_notifications(),
            "notificationEmail": self.get_notification_email(),
            "redirectURL": self.get_redirect_u_r_l(),
            "orderId": self.get_order_id(),
            "itemDesc": self.get_item_desc(),
            "itemCode": self.get_item_code(),
            "physical": self.get_physical(),
            "paymentCurrencies": self.get_payment_currencies(),
            "acceptanceWindow": self.get_acceptance_window(),
            "closeURL": self.get_close_url(),
            "buyer": self.get_buyer().to_json(),
            "refundAddresses": self.get_refund_addresses(),
            "id": self.get_id(),
            "url": self.get_url(),
            "status": self.get_status(),
            "lowFeeDetected": self.get_low_fee_detected(),
            "invoiceTime": self.get_invoice_time(),
            "expirationTime": self.get_expiration_time(),
            "transactions": self.get_transactions(),
            "exceptionStatus": self.get_exception_status(),
            "targetConfirmations": self.get_target_confirmations(),
            "refundAddressRequestPending": self.get_refund_address_request_pending(),
            "buyerProvidedEmail": self.get_buyer_provided_email(),
            "buyerProvidedInfo": self.get_buyer_provided_info().to_json(),
            "supportedTransactionCurrencies": supported_transaction_currencies,
            "minerFees": miner_fees,
            "billId": self.get_bill_id(),
            "refundInfo": self.get_refund_info().to_json(),
            "extendedNotifications": self.get_extended_notifications(),
            "transactionCurrency": self.get_transaction_currency(),
            "amountPaid": self.get_amount_paid(),
            "exchangeRates": self.get_exchange_rates(),
            "currentTime": self.get_current_time(),
            "declinedAmount": self.get_declined_amount(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
