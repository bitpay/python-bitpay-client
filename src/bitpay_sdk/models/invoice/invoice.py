from .buyer import Buyer
from .shopper import Shopper
from .miner_fees import MinerFees
from .refund_info import RefundInfo
from .universal_codes import UniversalCodes
from .itemized_details import ItemizedDetails
from .buyer_provided_info import BuyerProvidedInfo
from ...utils.key_utils import change_camel_case_to_snake_case
from .supported_transaction_currencies import SupportedTransactionCurrencies


class Invoice(object):
    __currency = ""

    __guid = ""
    __token = ""

    __price = None
    __pos_data = None
    __notification_url = ""
    __transaction_speed = ""
    __full_notifications = False
    __notification_email = ""
    __redirect_url = ""
    __order_id = ""
    __item_desc = ""
    __item_code = ""
    __physical = False
    __payment_currencies = None
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
    __merchant_name = None
    __forced_buyer_selected_wallet = None
    __forced_buyer_selected_transaction_currency = None
    __itemized_details = ItemizedDetails()
    __universal_codes = UniversalCodes()
    __is_cancelled = None
    __bitpay_id_required = None
    __rate_refresh_time = None

    def __init__(self, price=None, currency=None, **kwargs):

        self.__price = kwargs.get('price', "") if not price else price
        self.__currency = kwargs.get('currency', "") if not currency else currency

        for key, value in kwargs.items():
            try:
                if key in ["buyer", "buyerProvidedInfo", "shopper", "supportedTransactionCurrencies", "minerFees",
                           "refundInfo", "universalCodes", "itemizedDetails"]:
                    klass = globals()[key[0].upper() + key[1:]]

                    if isinstance(value, list):
                        value = []
                        for obj in value:
                            value.append(klass(**obj))
                    else:
                        value = klass(**value)
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_guid(self):
        return self.__guid

    def set_guid(self, guid):
        self.__guid = guid

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_pos_data(self):
        return self.__pos_data

    def set_pos_data(self, pos_data):
        self.__pos_data = pos_data

    def get_notification_url(self):
        return self.__notification_url

    def set_notification_url(self, notification_url):
        self.__notification_url = notification_url

    def get_transaction_speed(self):
        return self.__transaction_speed

    def set_transaction_speed(self, transaction_speed):
        self.__transaction_speed = transaction_speed

    def get_full_notifications(self):
        return self.__full_notifications

    def set_full_notifications(self, full_notifications):
        self.__full_notifications = full_notifications

    def get_notification_email(self):
        return self.__notification_email

    def set_notification_email(self, notification_email):
        self.__notification_email = notification_email

    def get_redirect_url(self):
        return self.__redirect_url

    def set_redirect_url(self, redirect_url):
        self.__redirect_url = redirect_url

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_item_desc(self):
        return self.__item_desc

    def set_item_desc(self, item_desc):
        self.__item_desc = item_desc

    def get_item_code(self):
        return self.__item_code

    def set_item_code(self, item_code):
        self.__item_code = item_code

    def get_physical(self):
        return self.__physical

    def set_physical(self, physical):
        self.__physical = physical

    def get_payment_currencies(self):
        return self.__payment_currencies

    def set_payment_currencies(self, payment_currencies):
        self.__payment_currencies = payment_currencies

    def get_payment_subtotals(self):
        return self.__payment_subtotals

    def set_payment_subtotals(self, payment_subtotals):
        self.__payment_subtotals = payment_subtotals

    def get_payment_totals(self):
        return self.__payment_totals

    def set_payment_totals(self, payment_totals):
        self.__payment_totals = payment_totals

    def get_payment_display_totals(self):
        return self.__payment_display_totals

    def set_payment_display_totals(self, payment_display_totals):
        self.__payment_display_totals = payment_display_totals

    def get_payment_display_sub_totals(self):
        return self.__payment_display_subtotals

    def set_payment_display_sub_totals(self, payment_display_subtotals):
        self.__payment_display_subtotals = payment_display_subtotals

    def get_payment_codes(self):
        return self.__payment_codes

    def set_payment_codes(self, payment_codes):
        self.__payment_codes = payment_codes

    def get_acceptance_window(self):
        return self.__acceptance_window

    def set_acceptance_window(self, acceptance_window):
        self.__acceptance_window = acceptance_window

    def get_refund_addresses(self):
        return self.__refund_addresses

    def set_refund_addresses(self, refund_addresses):
        self.__refund_addresses = refund_addresses

    def get_close_url(self):
        return self.__close_url

    def set_close_url(self, close_url):
        self.__close_url = close_url

    def get_auto_redirect(self):
        return self.__auto_redirect

    def set_auto_redirect(self, auto_redirect):
        self.__auto_redirect = auto_redirect

    def get_json_pay_pro_required(self):
        return self.__json_paypro_required

    def set_json_pay_pro_required(self, json_paypro_required):
        self.__json_paypro_required = json_paypro_required

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_low_fee_detected(self):
        return self.__low_fee_detected

    def set_low_fee_detected(self, low_fee_detected):
        self.__low_fee_detected = low_fee_detected

    def get_invoice_time(self):
        return self.__invoice_time

    def set_invoice_time(self, invoice_time):
        self.__invoice_time = invoice_time

    def get_expiration_time(self):
        return self.__expiration_time

    def set_expiration_time(self, expiration_time):
        self.__expiration_time = expiration_time

    def get_current_time(self):
        return self.__current_time

    def set_current_time(self, current_time):
        self.__current_time = current_time

    def get_transactions(self):
        return self.__transactions

    def set_transactions(self, transactions):
        self.__transactions = transactions

    def get_exception_status(self):
        return self.__exception_status

    def set_exception_status(self, exception_status):
        self.__exception_status = exception_status

    def get_target_confirmations(self):
        return self.__target_confirmations

    def set_target_confirmations(self, target_confirmations):
        self.__target_confirmations = target_confirmations

    def get_refund_address_request_pending(self):
        return self.__refund_address_request_pending

    def set_refund_address_request_pending(self, refund_address_request_pending):
        self.__refund_address_request_pending = refund_address_request_pending

    def get_buyer_provided_email(self):
        return self.__buyer_provided_email

    def set_buyer_provided_email(self, buyer_provided_email):
        self.__buyer_provided_email = buyer_provided_email

    def get_buyer_provided_info(self):
        return self.__buyer_provided_info

    def set_buyer_provided_info(self, buyer_provided_info: BuyerProvidedInfo):
        self.__buyer_provided_info = buyer_provided_info

    def get_supported_transaction_currencies(self):
        return self.__supported_transaction_currencies

    def set_supported_transaction_currencies(self, supported_transaction_currencies: SupportedTransactionCurrencies):
        self.__supported_transaction_currencies = supported_transaction_currencies

    def get_miner_fees(self):
        return self.__miner_fees

    def set_miner_fees(self, miner_fees: MinerFees):
        self.__miner_fees = miner_fees

    def get_non_paypro_payment_received(self):
        return self.__non_paypro_payment_received

    def set_non_paypro_payment_received(self, non_paypro_payment_received):
        self.__non_paypro_payment_received = non_paypro_payment_received

    def get_shopper(self):
        return self.__shopper

    def set_shopper(self, shopper: Shopper):
        self.__shopper = shopper

    def get_bill_id(self):
        return self.__bill_id

    def set_bill_id(self, bill_id):
        self.__bill_id = bill_id

    def get_refund_info(self):
        return self.__refund_info

    def set_refund_info(self, refund_info: RefundInfo):
        self.__refund_info = refund_info

    def get_extended_notifications(self):
        return self.__extended_notifications

    def set_extended_notifications(self, extended_notifications):
        self.__extended_notifications = extended_notifications

    def get_transaction_currency(self):
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency):
        self.__transaction_currency = transaction_currency

    def get_underpaid_amount(self):
        return self.__underpaid_amount

    def set_underpaid_amount(self, underpaid_amount):
        self.__underpaid_amount = underpaid_amount

    def get_overpaid_amount(self):
        return self.__overpaid_amount

    def set_overpaid_amount(self, overpaid_amount):
        self.__overpaid_amount = overpaid_amount

    def get_amount_paid(self):
        return self.__amount_paid

    def set_amount_paid(self, amount_paid):
        self.__amount_paid = amount_paid

    def get_display_amount_paid(self):
        return self.__display_amount_paid

    def set_display_amount_paid(self, display_amount_paid):
        self.__display_amount_paid = display_amount_paid

    def get_exchange_rates(self):
        return self.__exchange_rates

    def set_exchange_rates(self, exchange_rates):
        self.__exchange_rates = exchange_rates

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_payment_string(self):
        return self.__payment_string

    def set_payment_string(self, payment_string):
        self.__payment_string = payment_string

    def get_verification_link(self):
        return self.__verification_link

    def set_verification_link(self, verification_link):
        self.__verification_link = verification_link

    def get_buyer_email(self):
        return self.__buyer_email

    def set_buyer_email(self, buyer_email):
        self.__buyer_email = buyer_email

    def get_merchant_name(self):
        return self.__merchant_name

    def set_merchant_name(self, merchant_name):
        self.__merchant_name = merchant_name

    def get_forced_buyer_selected_wallet(self):
        return self.__forced_buyer_selected_wallet

    def set_forced_buyer_selected_wallet(self, forced_buyer_selected_wallet):
        self.__forced_buyer_selected_wallet = forced_buyer_selected_wallet

    def get_forced_buyer_selected_transaction_currency(self):
        return self.__forced_buyer_selected_transaction_currency

    def set_forced_buyer_selected_transaction_currency(self, forced_buyer_selected_transaction_currency):
        self.__forced_buyer_selected_transaction_currency = forced_buyer_selected_transaction_currency

    def get_is_cancelled(self):
        return self.__is_cancelled

    def set_is_cancelled(self, is_cancelled):
        self.__is_cancelled = is_cancelled

    def get_bitpay_id_required(self):
        return self.__bitpay_id_required

    def set_bitpay_id_required(self, bitpay_id_required):
        self.__bitpay_id_required = bitpay_id_required

    def get_rate_refresh_time(self):
        return self.__rate_refresh_time

    def set_rate_refresh_time(self, rate_refresh_time):
        self.__rate_refresh_time = rate_refresh_time

    def get_universal_codes(self):
        return self.__universal_codes

    def set_universal_codes(self, universal_codes: UniversalCodes):
        self.__universal_codes = universal_codes

    def get_itemized_details(self):
        items = []
        for item in items:
            if isinstance(item, ItemizedDetails):
                items.append(item.to_json())
            else:
                items.append(item)
        return items

    def set_itemized_details(self, itemized_details: ItemizedDetails):
        items_array = []
        for item in itemized_details:
            if isinstance(item, ItemizedDetails):
                items_array.append(item.to_json())
            else:
                items_array.append(item)
        self.__itemized_details = items_array

    # Buyer Data

    def get_buyer(self):
        return self.__buyer

    def set_buyer(self, buyer: Buyer):
        self.__buyer = buyer

    def to_json(self):
        data = {
            # TODO: Add more data
            "currency": self.get_currency(),
            "price": self.get_price(),
            "token": self.get_token()
        }
        return data
