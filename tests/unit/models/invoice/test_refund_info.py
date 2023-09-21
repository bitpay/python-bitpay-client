import pytest

from bitpay.models.invoice.refund_info import RefundInfo


@pytest.mark.unit
def test_construct():
    support_request = "someValue"
    currency = "USD"

    refund = RefundInfo(support_request=support_request, currency=currency)

    assert support_request == refund.support_request
    assert currency == refund.currency
