import pytest

from bitpay.models.invoice.refund import Refund


@pytest.mark.unit
def test_construct():
    invoice_id = "123"
    amount = 12.34
    currency = "BCH"
    token = "someToken"
    refund_fee = 12.10

    refund = Refund(invoice=invoice_id, amount=amount, currency=currency, token=token, refund_fee=refund_fee)

    assert invoice_id == refund.invoice
    assert amount == refund.amount
    assert currency == refund.currency
    assert token == refund.token
    assert refund_fee == refund.refund_fee
