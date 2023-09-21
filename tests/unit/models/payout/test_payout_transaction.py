import pytest

from bitpay.models.payout.payout_transaction import PayoutTransaction


@pytest.mark.unit
def test_constructor():
    txid = "someValue"
    amount = 1234
    payout_transaction = PayoutTransaction(txid=txid, amount=amount)

    assert txid == payout_transaction.txid
    assert amount == payout_transaction.amount
