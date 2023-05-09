import pytest

from bitpay.models.settlement.invoice_data import InvoiceData
from bitpay.models.settlement.settlement_ledger_entry import SettlementLedgerEntry


@pytest.mark.unit
def test_constructor():
    invoice_id = "1234"
    amount = 12.34
    description = "someDescription"
    invoice_data = InvoiceData()
    settlement_ledger_entry = SettlementLedgerEntry(**{"invoice_id": invoice_id, "amount": amount,
                                                       "description": description, "invoiceData": invoice_data})

    assert invoice_id == settlement_ledger_entry.get_invoice_id()
    assert amount == settlement_ledger_entry.get_amount()
    assert description == settlement_ledger_entry.get_description()
    assert invoice_data == settlement_ledger_entry.get_invoice_data()

    settlement_ledger_entry = SettlementLedgerEntry(**{"invoiceData": {"price": 12.34}})
    assert 12.34 == settlement_ledger_entry.get_invoice_data().get_price()


@pytest.mark.unit
def test_modify_code():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = 123
    settlement_ledger_entry.set_code(value)

    assert value == settlement_ledger_entry.get_code()


@pytest.mark.unit
def test_modify_invoice_id():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = "someValue"
    settlement_ledger_entry.set_invoice_id(value)

    assert value == settlement_ledger_entry.get_invoice_id()


@pytest.mark.unit
def test_modify_amount():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = 12
    settlement_ledger_entry.set_amount(value)

    assert value == settlement_ledger_entry.get_amount()


@pytest.mark.unit
def test_modify_timestamp():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = "someValue"
    settlement_ledger_entry.set_timestamp(value)

    assert value == settlement_ledger_entry.get_timestamp()


@pytest.mark.unit
def test_modify_description():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = "someValue"
    settlement_ledger_entry.set_description(value)

    assert value == settlement_ledger_entry.get_description()


@pytest.mark.unit
def test_modify_reference():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = "someValue"
    settlement_ledger_entry.set_reference(value)

    assert value == settlement_ledger_entry.get_reference()


@pytest.mark.unit
def test_modify_invoice_data():
    settlement_ledger_entry = SettlementLedgerEntry()
    value = InvoiceData()
    settlement_ledger_entry.set_invoice_data(value)

    assert value == settlement_ledger_entry.get_invoice_data()

