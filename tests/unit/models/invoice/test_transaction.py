import pytest

from bitpay.models.invoice.transaction import Transaction


@pytest.mark.unit
def test_constructor():
    amount = 12.45
    confirmations = 4
    transaction = Transaction(amount=amount, confirmations=confirmations)

    assert transaction.amount == amount
    assert transaction.confirmations == confirmations
