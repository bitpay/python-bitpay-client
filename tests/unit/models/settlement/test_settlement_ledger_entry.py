import pytest

from bitpay.models.settlement.invoice_data import InvoiceData
from bitpay.models.settlement.settlement_ledger_entry import SettlementLedgerEntry


@pytest.mark.unit
def test_constructor():
    invoice_id = "1234"
    amount = 12.34
    description = "someDescription"
    invoice_data = InvoiceData()
    settlement_ledger_entry = SettlementLedgerEntry(
        invoice_id=invoice_id,
        amount=amount,
        description=description,
        invoice_data=invoice_data
    )

    assert invoice_id == settlement_ledger_entry.invoice_id
    assert amount == settlement_ledger_entry.amount
    assert description == settlement_ledger_entry.description
    assert invoice_data == settlement_ledger_entry.invoice_data

    settlement_ledger_entry = SettlementLedgerEntry(invoice_data=InvoiceData(price=12.34))
    assert 12.34 == settlement_ledger_entry.invoice_data.price
