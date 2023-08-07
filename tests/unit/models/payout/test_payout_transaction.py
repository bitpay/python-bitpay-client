import pytest

from bitpay.models.payout.payout_transaction import PayoutTransaction


@pytest.mark.unit
def test_constructor():
    txid = "someValue"
    amount = 1234
    payout_transaction = PayoutTransaction(**{"txid": txid, "amount": amount})

    assert txid == payout_transaction.get_txid()
    assert amount == payout_transaction.get_amount()


@pytest.mark.unit
def test_modify_txid():
    payout_transaction = PayoutTransaction()
    value = "someValue"
    payout_transaction.set_txid(value)

    assert value == payout_transaction.get_txid()


@pytest.mark.unit
def test_modify_amount():
    payout_transaction = PayoutTransaction()
    value = 12.34
    payout_transaction.set_amount(value)

    assert value == payout_transaction.get_amount()


@pytest.mark.unit
def test_modify_date():
    payout_transaction = PayoutTransaction()
    value = "someValue"
    payout_transaction.set_date(value)

    assert value == payout_transaction.get_date()


@pytest.mark.unit
def test_modify_confirmations():
    payout_transaction = PayoutTransaction()
    value = "someValue"
    payout_transaction.set_confirmations(value)

    assert value == payout_transaction.get_confirmations()
