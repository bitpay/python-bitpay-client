import pytest

from bitpay.models.ledger.buyer import Buyer
from bitpay.models.ledger.ledger_entry import LedgerEntry


@pytest.mark.unit
def test_constructor():
    type = "invoice"
    currency = "USD"
    buyer_city = "Rzeszow"
    buyer_fields = Buyer(city=buyer_city)
    ledger_entry = LedgerEntry(
        type=type, currency=currency, buyerFields=buyer_fields
    )

    assert type == ledger_entry.type
    assert currency == ledger_entry.currency
    assert buyer_city == ledger_entry.buyer_fields.city
