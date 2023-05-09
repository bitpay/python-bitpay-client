import pytest

from bitpay.models.ledger.ledger import Ledger


@pytest.mark.unit
def test_constructor():
    currency = "USD"
    balance = 12.34
    ledger = Ledger(**{"currency": currency, "balance": balance})

    assert currency == ledger.get_currency()
    assert balance == ledger.get_balance()


@pytest.mark.unit
def test_modify_currency():
    ledger = Ledger()
    value = "someValue"
    ledger.set_currency(value)

    assert value == ledger.get_currency()


@pytest.mark.unit
def test_modify_balance():
    ledger = Ledger()
    value = 12.23
    ledger.set_balance(value)

    assert value == ledger.get_balance()

