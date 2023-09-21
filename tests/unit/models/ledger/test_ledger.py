import pytest

from bitpay.models.ledger.ledger import Ledger


@pytest.mark.unit
def test_constructor():
    currency = "USD"
    balance = 12.34
    ledger = Ledger(currency=currency, balance=balance)

    assert currency == ledger.currency
    assert balance == ledger.balance
