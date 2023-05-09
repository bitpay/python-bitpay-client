import pytest

from bitpay.models.ledger.buyer import Buyer
from bitpay.models.ledger.ledger_entry import LedgerEntry


@pytest.mark.unit
def test_constructor():
    type = "invoice"
    currency = "USD"
    buyer_city = "Rzeszow"
    buyer_fields = Buyer(**{"city": buyer_city})
    ledger_entry = LedgerEntry(**{"type": type, "currency": currency, "buyerFields": buyer_fields})

    assert type == ledger_entry.get_type()
    assert currency == ledger_entry.get_currency()
    assert buyer_city == ledger_entry.get_buyer_fields().get_city()


@pytest.mark.unit
def test_modify_type():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_type(value)

    assert value == ledger_entry.get_type()


@pytest.mark.unit
def test_modify_amount():
    ledger_entry = LedgerEntry()
    value = 231
    ledger_entry.set_amount(value)

    assert value == ledger_entry.get_amount()


@pytest.mark.unit
def test_modify_code():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_code(value)

    assert value == ledger_entry.get_code()


@pytest.mark.unit
def test_modify_timestamp():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_timestamp(value)

    assert value == ledger_entry.get_timestamp()


@pytest.mark.unit
def test_modify_currency():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_currency(value)

    assert value == ledger_entry.get_currency()


@pytest.mark.unit
def test_modify_tx_type():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_tx_type(value)

    assert value == ledger_entry.get_tx_type()


@pytest.mark.unit
def test_modify_scale():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_scale(value)

    assert value == ledger_entry.get_scale()


@pytest.mark.unit
def test_modify_id():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_id(value)

    assert value == ledger_entry.get_id()


@pytest.mark.unit
def test_modify_support_request():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_support_request(value)

    assert value == ledger_entry.get_support_request()


@pytest.mark.unit
def test_modify_description():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_description(value)

    assert value == ledger_entry.get_description()


@pytest.mark.unit
def test_modify_invoice_id():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_invoice_id(value)

    assert value == ledger_entry.get_invoice_id()


@pytest.mark.unit
def test_modify_buyer_fields():
    ledger_entry = LedgerEntry()
    value = Buyer()
    ledger_entry.set_buyer_fields(value)

    assert value == ledger_entry.get_buyer_fields()


@pytest.mark.unit
def test_modify_invoice_amount():
    ledger_entry = LedgerEntry()
    value = 23
    ledger_entry.set_invoice_amount(value)

    assert value == ledger_entry.get_invoice_amount()


@pytest.mark.unit
def test_modify_invoice_currency():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_invoice_currency(value)

    assert value == ledger_entry.get_invoice_currency()


@pytest.mark.unit
def test_modify_transaction_currency():
    ledger_entry = LedgerEntry()
    value = "someValue"
    ledger_entry.set_transaction_currency(value)

    assert value == ledger_entry.get_transaction_currency()


