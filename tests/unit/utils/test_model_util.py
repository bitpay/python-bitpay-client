import json
import os

import pytest

from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.buyer_provided_info import BuyerProvidedInfo
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.itemized_details import ItemizedDetails
from bitpay.models.invoice.supported_transaction_currencies import SupportedTransactionCurrencies
from bitpay.models.invoice.supported_transaction_currency import SupportedTransactionCurrency
from bitpay.utils.model_util import ModelUtil


@pytest.mark.unit
def test_from_model():
    invoice = Invoice(2.16, "eur")
    invoice.set_order_id("98e572ea-910e-415d-b6de-65f5090680f6")
    invoice.set_redirect_u_r_l("https://url.com")

    buyer = Buyer()
    buyer.set_name("Bily Matthews")
    invoice.set_buyer(buyer)

    bch = SupportedTransactionCurrency()
    bch.set_reason("some reason")
    supported_transaction_currencies = SupportedTransactionCurrencies()
    supported_transaction_currencies.set_bch(bch)

    invoice.set_supported_transaction_currencies(supported_transaction_currencies)

    result = ModelUtil.to_json(invoice)
    with open(os.path.abspath(os.path.dirname(__file__)) + '/invoice_model.json', 'r') as file:
        expected_result = json.load(file)

    assert result == expected_result


@pytest.mark.unit
def test_get_field_value():
    float_value = 12.34
    to_convert_float = "12.67"
    int_value = 2
    to_convert_int = "3"
    bool_value = True
    to_convert_bool = "true"
    to_convert_list_strings = [1, "b"]
    to_convert_list_objects = [{"amount": 1}, {"amount": 2}]
    list_dict_values = {"BTC": 72000}
    dict_value = {"name": "Marcin"}
    object_value = BuyerProvidedInfo()

    args = {"underpaidAmount": float_value, "amountPaid": to_convert_float, "acceptanceWindow": int_value,
            "targetConfirmations": to_convert_int, "physical": bool_value, "isCancelled": to_convert_bool,
            "buyer": dict_value, "buyerProvidedInfo": object_value, "paymentCurrencies": to_convert_list_strings,
            "paymentSubtotals": list_dict_values, "itemizedDetails": to_convert_list_objects}

    invoice = Invoice(11.12, "USD", **args)

    assert invoice.get_underpaid_amount() == float_value
    assert invoice.get_amount_paid() == 12.67
    assert invoice.get_acceptance_window() == int_value
    assert invoice.get_target_confirmations() == 3
    assert invoice.get_physical() is True
    assert invoice.get_is_cancelled() is True
    assert invoice.get_buyer().get_name() == "Marcin"
    assert invoice.get_buyer_provided_info() == object_value
    assert invoice.get_payment_currencies()[0] == "1"
    assert invoice.get_payment_currencies()[1] == "b"
    assert invoice.get_payment_subtotals()["BTC"] == 72000
    assert isinstance(invoice.get_itemized_details()[0], ItemizedDetails)
