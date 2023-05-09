import pytest

from bitpay.models.invoice.refund_info import RefundInfo


@pytest.mark.unit
def test_modify_support_request():
    refund_info = RefundInfo()
    value = "someValue"
    refund_info.set_support_request(value)

    assert value == refund_info.get_support_request()


@pytest.mark.unit
def test_modify_currency():
    refund_info = RefundInfo()
    value = "someValue"
    refund_info.set_currency(value)

    assert value == refund_info.get_currency()


@pytest.mark.unit
def test_modify_amounts():
    refund_info = RefundInfo()
    value = []
    refund_info.set_amounts(value)

    assert value == refund_info.get_amounts()
