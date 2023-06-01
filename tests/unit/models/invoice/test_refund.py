import pytest

from bitpay.models.invoice.refund import Refund


@pytest.mark.unit
def test_construct():
    invoice_id = "123"
    amount = 12.34
    currency = "BCH"
    token = "someToken"
    refund_fee = 12.10

    refund = Refund(invoice_id, amount, currency, token, **{"refundFee": refund_fee})

    assert invoice_id == refund.get_invoice()
    assert amount == refund.get_amount()
    assert currency == refund.get_currency()
    assert token == refund.get_token()
    assert refund_fee == refund.get_refund_fee()


@pytest.mark.unit
def test_amount():
    refund = Refund()
    value = 16
    refund.set_amount(value)

    assert value == refund.get_amount()


@pytest.mark.unit
def test_buyer_pays_refund_fee():
    refund = Refund()
    value = True
    refund.set_buyer_pays_refund_fee(value)

    assert value == refund.get_buyer_pays_refund_fee()


@pytest.mark.unit
def test_currency():
    refund = Refund()
    value = "someValue"
    refund.set_currency(value)

    assert value == refund.get_currency()


@pytest.mark.unit
def test_guid():
    refund = Refund()
    value = "someValue"
    refund.set_guid(value)

    assert value == refund.get_guid()


@pytest.mark.unit
def test_id():
    refund = Refund()
    value = "someValue"
    refund.set_id(value)

    assert value == refund.get_id()


@pytest.mark.unit
def test_immediate():
    refund = Refund()
    value = True
    refund.set_immediate(value)

    assert value == refund.get_immediate()


@pytest.mark.unit
def test_invoice():
    refund = Refund()
    value = "someValue"
    refund.set_invoice(value)

    assert value == refund.get_invoice()


@pytest.mark.unit
def test_last_refund_notification():
    refund = Refund()
    value = "someValue"
    refund.set_last_refund_notification(value)

    assert value == refund.get_last_refund_notification()


@pytest.mark.unit
def test_notification_url():
    refund = Refund()
    value = "someValue"
    refund.set_notification_url(value)

    assert value == refund.get_notification_url()


@pytest.mark.unit
def test_preview():
    refund = Refund()
    value = True
    refund.set_preview(value)

    assert value == refund.get_preview()


@pytest.mark.unit
def test_reference():
    refund = Refund()
    value = "someValue"
    refund.set_reference(value)

    assert value == refund.get_reference()


@pytest.mark.unit
def test_refund_address():
    refund = Refund()
    value = "someValue"
    refund.set_refund_address(value)

    assert value == refund.get_refund_address()


@pytest.mark.unit
def test_refund_fee():
    refund = Refund()
    value = 123
    refund.set_refund_fee(value)

    assert value == refund.get_refund_fee()


@pytest.mark.unit
def test_request_date():
    refund = Refund()
    value = "someValue"
    refund.set_request_date(value)

    assert value == refund.get_request_date()


@pytest.mark.unit
def test_status():
    refund = Refund()
    value = "someValue"
    refund.set_status(value)

    assert value == refund.get_status()


@pytest.mark.unit
def test_support_request():
    refund = Refund()
    value = "someValue"
    refund.set_support_request(value)

    assert value == refund.get_support_request()


@pytest.mark.unit
def test_token():
    refund = Refund()
    value = "someValue"
    refund.set_token(value)

    assert value == refund.get_token()


@pytest.mark.unit
def test_transaction_amount():
    refund = Refund()
    value = 45
    refund.set_transaction_amount(value)

    assert value == refund.get_transaction_amount()


@pytest.mark.unit
def test_transaction_currency():
    refund = Refund()
    value = "someValue"
    refund.set_transaction_currency(value)

    assert value == refund.get_transaction_currency()


@pytest.mark.unit
def test_transaction_refund_fee():
    refund = Refund()
    value = 54
    refund.set_transaction_refund_fee(value)

    assert value == refund.get_transaction_refund_fee()
