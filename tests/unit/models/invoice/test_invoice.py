from typing import List

import pytest

from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.buyer_provided_info import BuyerProvidedInfo
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.itemized_details import ItemizedDetails
from bitpay.models.invoice.miner_fees import MinerFees
from bitpay.models.invoice.refund_info import RefundInfo
from bitpay.models.invoice.shopper import Shopper
from bitpay.models.invoice.supported_transaction_currencies import (
    SupportedTransactionCurrencies,
)
from bitpay.models.invoice.universal_codes import UniversalCodes


@pytest.mark.unit
def test_constructor():
    price = 10.25
    currency = "BCH"
    shopper = Shopper()
    guid = "someGuid"
    buyer_name = "someName"
    itemized_details = [ItemizedDetails(), ItemizedDetails()]

    invoice = Invoice(
        price,
        currency,
        **{
            "shopper": shopper,
            "guid": guid,
            "buyer": {"name": buyer_name},
            "itemizedDetails": itemized_details,
        }
    )

    assert price == invoice.get_price()
    assert currency == invoice.get_currency()
    assert shopper == invoice.get_shopper()
    assert guid == invoice.get_guid()
    assert buyer_name == invoice.get_buyer().get_name()
    assert itemized_details == invoice.get_itemized_details()


@pytest.mark.unit
def test_modify_currency():
    invoice = Invoice()
    value = "someValue"
    invoice.set_currency(value)

    assert value == invoice.get_currency()


@pytest.mark.unit
def test_modify_guid():
    invoice = Invoice()
    value = "someValue"
    invoice.set_guid(value)

    assert value == invoice.get_guid()


@pytest.mark.unit
def test_modify_token():
    invoice = Invoice()
    value = "someValue"
    invoice.set_token(value)

    assert value == invoice.get_token()


@pytest.mark.unit
def test_modify_price():
    invoice = Invoice()
    value = 12
    invoice.set_price(value)

    assert value == invoice.get_price()


@pytest.mark.unit
def test_modify_pos_data():
    invoice = Invoice()
    value = "someValue"
    invoice.set_pos_data(value)

    assert value == invoice.get_pos_data()


@pytest.mark.unit
def test_modify_notification_url():
    invoice = Invoice()
    value = "someValue"
    invoice.set_notification_url(value)

    assert value == invoice.get_notification_url()


@pytest.mark.unit
def test_modify_transaction_speed():
    invoice = Invoice()
    value = "someValue"
    invoice.set_transaction_speed(value)

    assert value == invoice.get_transaction_speed()


@pytest.mark.unit
def test_modify_full_notifications():
    invoice = Invoice()
    value = True
    invoice.set_full_notifications(value)

    assert value == invoice.get_full_notifications()


@pytest.mark.unit
def test_modify_notification_email():
    invoice = Invoice()
    value = "someValue"
    invoice.set_notification_email(value)

    assert value == invoice.get_notification_email()


@pytest.mark.unit
def test_modify_redirect_url():
    invoice = Invoice()
    value = "someValue"
    invoice.set_redirect_u_r_l(value)

    assert value == invoice.get_redirect_u_r_l()


@pytest.mark.unit
def test_modify_close_url():
    invoice = Invoice()
    value = "someValue"
    invoice.set_close_url(value)

    assert value == invoice.get_close_url()


@pytest.mark.unit
def test_modify_order_id():
    invoice = Invoice()
    value = "someValue"
    invoice.set_order_id(value)

    assert value == invoice.get_order_id()


@pytest.mark.unit
def test_modify_item_desc():
    invoice = Invoice()
    value = "someValue"
    invoice.set_item_desc(value)

    assert value == invoice.get_item_desc()


@pytest.mark.unit
def test_modify_item_code():
    invoice = Invoice()
    value = "someValue"
    invoice.set_item_code(value)

    assert value == invoice.get_item_code()


@pytest.mark.unit
def test_modify_physical():
    invoice = Invoice()
    value = True
    invoice.set_physical(value)

    assert value == invoice.get_physical()


@pytest.mark.unit
def test_modify_payment_currencies():
    invoice = Invoice()
    value = []
    invoice.set_payment_currencies(value)

    assert value == invoice.get_payment_currencies()


@pytest.mark.unit
def test_modify_acceptance_window():
    invoice = Invoice()
    value = True
    invoice.set_acceptance_window(value)

    assert value == invoice.get_acceptance_window()


@pytest.mark.unit
def test_modify_buyer():
    invoice = Invoice()
    value = Buyer()
    value.set_name("someName")
    invoice.set_buyer(value)

    assert value == invoice.get_buyer()


@pytest.mark.unit
def test_modify_buyer_sms():
    invoice = Invoice()
    value = "someValue"
    invoice.set_buyer_sms(value)

    assert value == invoice.get_buyer_sms()


@pytest.mark.unit
def test_modify_merchant_name():
    invoice = Invoice()
    value = "someValue"
    invoice.set_merchant_name(value)

    assert value == invoice.get_merchant_name()


@pytest.mark.unit
def test_modify_forced_buyer_selected_wallet():
    invoice = Invoice()
    value = "someValue"
    invoice.set_forced_buyer_selected_wallet(value)

    assert value == invoice.get_forced_buyer_selected_wallet()


@pytest.mark.unit
def test_modify_universal_codes():
    invoice = Invoice()
    value = UniversalCodes()
    invoice.set_universal_codes(value)

    assert value == invoice.get_universal_codes()


@pytest.mark.unit
def test_modify_itemized_details():
    invoice = Invoice()
    value = [ItemizedDetails()]
    invoice.set_itemized_details(value)

    assert value == invoice.get_itemized_details()


@pytest.mark.unit
def test_modify_auto_redirect():
    invoice = Invoice()
    value = True
    invoice.set_auto_redirect(value)

    assert value == invoice.get_auto_redirect()


@pytest.mark.unit
def test_modify_id():
    invoice = Invoice()
    value = "someValue"
    invoice.set_id(value)

    assert value == invoice.get_id()


@pytest.mark.unit
def test_modify_url():
    invoice = Invoice()
    value = "someValue"
    invoice.set_url(value)

    assert value == invoice.get_url()


@pytest.mark.unit
def test_modify_status():
    invoice = Invoice()
    value = "someValue"
    invoice.set_status(value)

    assert value == invoice.get_status()


@pytest.mark.unit
def test_modify_low_fee_detected():
    invoice = Invoice()
    value = True
    invoice.set_low_fee_detected(value)

    assert value == invoice.get_low_fee_detected()


@pytest.mark.unit
def test_modify_invoice_time():
    invoice = Invoice()
    value = 123456
    invoice.set_invoice_time(value)

    assert value == invoice.get_invoice_time()


@pytest.mark.unit
def test_modify_expiration_time():
    invoice = Invoice()
    value = 123456
    invoice.set_expiration_time(value)

    assert value == invoice.get_expiration_time()


@pytest.mark.unit
def test_modify_current_time():
    invoice = Invoice()
    value = 123456
    invoice.set_current_time(value)

    assert value == invoice.get_current_time()


@pytest.mark.unit
def test_modify_exception_status():
    invoice = Invoice()
    value = "someValue"
    invoice.set_exception_status(value)

    assert value == invoice.get_exception_status()


@pytest.mark.unit
def test_modify_target_confirmations():
    invoice = Invoice()
    value = True
    invoice.set_target_confirmations(value)

    assert value == invoice.get_target_confirmations()


@pytest.mark.unit
def test_modify_transactions():
    invoice = Invoice()
    value = []
    invoice.set_transactions(value)

    assert value == invoice.get_transactions()


@pytest.mark.unit
def test_modify_refund_addresses():
    invoice = Invoice()
    value = "someValue"
    invoice.set_refund_addresses(value)

    assert value == invoice.get_refund_addresses()


@pytest.mark.unit
def test_modify_refund_address_request_pending():
    invoice = Invoice()
    value = True
    invoice.set_refund_address_request_pending(value)

    assert value == invoice.get_refund_address_request_pending()


@pytest.mark.unit
def test_modify_buyer_provided_email():
    invoice = Invoice()
    value = "someValue"
    invoice.set_buyer_provided_email(value)

    assert value == invoice.get_buyer_provided_email()


@pytest.mark.unit
def test_modify_buyer_provided_info():
    invoice = Invoice()
    value = BuyerProvidedInfo()
    invoice.set_buyer_provided_info(value)

    assert value == invoice.get_buyer_provided_info()


@pytest.mark.unit
def test_modify_supported_transaction_currencies():
    invoice = Invoice()
    value = SupportedTransactionCurrencies()
    invoice.set_supported_transaction_currencies(value)

    assert value == invoice.get_supported_transaction_currencies()


@pytest.mark.unit
def test_modify_miner_fees():
    invoice = Invoice()
    value = MinerFees()
    invoice.set_miner_fees(value)

    assert value == invoice.get_miner_fees()


@pytest.mark.unit
def test_modify_shopper():
    invoice = Invoice()
    value = Shopper()
    invoice.set_shopper(value)

    assert value == invoice.get_shopper()


@pytest.mark.unit
def test_modify_bill_id():
    invoice = Invoice()
    value = "someValue"
    invoice.set_bill_id(value)

    assert value == invoice.get_bill_id()


@pytest.mark.unit
def test_modify_refund_info():
    invoice = Invoice()
    value = RefundInfo()
    invoice.set_refund_info(value)

    assert value == invoice.get_refund_info()


@pytest.mark.unit
def test_modify_extended_notifications():
    invoice = Invoice()
    value = True
    invoice.set_extended_notifications(value)

    assert value == invoice.get_extended_notifications()


@pytest.mark.unit
def test_modify_transaction_currency():
    invoice = Invoice()
    value = "someValue"
    invoice.set_transaction_currency(value)

    assert value == invoice.get_transaction_currency()


@pytest.mark.unit
def test_modify_forced_buyer_selected_transaction_currency():
    invoice = Invoice()
    value = "someValue"
    invoice.set_forced_buyer_selected_transaction_currency(value)

    assert value == invoice.get_forced_buyer_selected_transaction_currency()


@pytest.mark.unit
def test_modify_amount_paid():
    invoice = Invoice()
    value = 12
    invoice.set_amount_paid(value)

    assert value == invoice.get_amount_paid()


@pytest.mark.unit
def test_modify_display_amount_paid():
    invoice = Invoice()
    value = "someValue"
    invoice.set_display_amount_paid(value)

    assert value == invoice.get_display_amount_paid()


@pytest.mark.unit
def test_modify_exchange_rates():
    invoice = Invoice()
    value = {}
    invoice.set_exchange_rates(value)

    assert value == invoice.get_exchange_rates()


@pytest.mark.unit
def test_modify_is_cancelled():
    invoice = Invoice()
    value = True
    invoice.set_is_cancelled(value)

    assert value == invoice.get_is_cancelled()


@pytest.mark.unit
def test_modify_bitpay_id_required():
    invoice = Invoice()
    value = True
    invoice.set_bitpay_id_required(value)

    assert value == invoice.get_bitpay_id_required()


@pytest.mark.unit
def test_modify_payment_subtotals():
    invoice = Invoice()
    value = {}
    invoice.set_payment_subtotals(value)

    assert value == invoice.get_payment_subtotals()


@pytest.mark.unit
def test_modify_payment_totals():
    invoice = Invoice()
    value = {}
    invoice.set_payment_totals(value)

    assert value == invoice.get_payment_totals()


@pytest.mark.unit
def test_modify_payment_display_totals():
    invoice = Invoice()
    value = {}
    invoice.set_payment_display_totals(value)

    assert value == invoice.get_payment_display_totals()


@pytest.mark.unit
def test_modify_payment_display_sub_totals():
    invoice = Invoice()
    value = {}
    invoice.set_payment_display_sub_totals(value)

    assert value == invoice.get_payment_display_sub_totals()


@pytest.mark.unit
def test_modify_non_pay_pro_payment_received():
    invoice = Invoice()
    value = True
    invoice.set_non_pay_pro_payment_received(value)

    assert value == invoice.get_non_pay_pro_payment_received()


@pytest.mark.unit
def test_modify_json_pay_pro_required():
    invoice = Invoice()
    value = True
    invoice.set_json_pay_pro_required(value)

    assert value == invoice.get_json_pay_pro_required()


@pytest.mark.unit
def test_modify_underpaid_amount():
    invoice = Invoice()
    value = 12
    invoice.set_underpaid_amount(value)

    assert value == invoice.get_underpaid_amount()


@pytest.mark.unit
def test_modify_overpaid_amount():
    invoice = Invoice()
    value = 23
    invoice.set_overpaid_amount(value)

    assert value == invoice.get_overpaid_amount()


@pytest.mark.unit
def test_modify_payment_codes():
    invoice = Invoice()
    value = {}
    invoice.set_payment_codes(value)

    assert value == invoice.get_payment_codes()
