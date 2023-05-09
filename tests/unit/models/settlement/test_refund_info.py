import pytest

from bitpay.models.settlement.refund_info import RefundInfo


@pytest.mark.unit
def test_constructor():
    support_request = "someValue"
    currency = "USD"
    amounts = {"USD": 12.34}
    refund_info = RefundInfo(**{"supportRequest": support_request, "currency": currency, "amounts": amounts})

    assert support_request == refund_info.get_support_request()
    assert currency == refund_info.get_currency()
    assert amounts == refund_info.get_amounts()


@pytest.mark.unit
def test_modify_support_request():
    refund_info = RefundInfo()
    value = "someValue"
    refund_info.set_support_request(value)

    assert refund_info.get_support_request() == value


@pytest.mark.unit
def test_modify_currency():
    refund_info = RefundInfo()
    value = "someValue"
    refund_info.set_currency(value)

    assert refund_info.get_currency() == value


@pytest.mark.unit
def test_modify_amounts():
    refund_info = RefundInfo()
    value = {}
    refund_info.set_amounts(value)

    assert refund_info.get_amounts() == value

