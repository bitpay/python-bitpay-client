import json
import os
import pytest

from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.supported_transaction_currencies import (
    SupportedTransactionCurrencies,
)
from bitpay.models.invoice.supported_transaction_currency import (
    SupportedTransactionCurrency,
)


@pytest.mark.unit
def test_from_to_json():
    bch = SupportedTransactionCurrency(reason="some reason")
    supported_transaction_currencies = SupportedTransactionCurrencies(bch=bch)
    buyer = Buyer(name="Bily Matthews")
    invoice = Invoice(price=2.16, currency="eur", buyer=buyer,
                      supported_transaction_currencies=supported_transaction_currencies)
    invoice.order_id = "98e572ea-910e-415d-b6de-65f5090680f6"
    invoice.redirect_url = "https://url.com"

    result = Invoice.to_json(invoice)
    with open(
            os.path.abspath(os.path.dirname(__file__)) + "/invoice_model.json", "r"
    ) as file:
        expected_result = json.load(file)

    assert result == expected_result


@pytest.mark.unit
def test_currency_validation():
    valid_invoice = Invoice(currency="USD")

    with pytest.raises(BitPayException) as exception:
        invalid_invoice = Invoice(currency="INVALID")

    assert (
        exception.value.args[0]
        == ""'BITPAY-GENERIC: Unexpected Bitpay exception.:currency code must be a type of Model.Currency'""
    )
